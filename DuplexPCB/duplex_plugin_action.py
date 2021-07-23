import pdb
import pcbnew
import re

__version__ = "0.0.1"

# the internal coorinate space of pcbnew is 10E-6 mm. (a millionth of a mm)
# the coordinate 121550000 corresponds to 121.550000 
#SCALE = 1000000

# types of transformation
TRANSFORM_TYPE_SHIFT = 0
TRANSFORM_TYPE_MIRROR = 1
TRANSFORM_TYPE_FLIP = 2

def __ModifyPoint(mirror_type, point, center):
    new_x = point.x
    new_y = point.y
    if mirror_type == TRANSFORM_TYPE_SHIFT:
        new_x = point.x + center[0]
        new_y = point.y + center[1]
    elif mirror_type in [TRANSFORM_TYPE_MIRROR, TRANSFORM_TYPE_FLIP]:
        new_x = 2 * center[0] - point.x
        new_y = 2 * center[1] - point.y
    return pcbnew.wxPoint(new_x, new_y)
    
def __GetElements(mapfile):
    elements = {}
    with open(mapfile, "r") as f:
        lines = f.readlines()
        for line in lines:
            e1, e2 = line.strip().split(":")
            if e1 is not None and e2 is not None:
                elements[e1] = e2
    return elements

def MakeDuplex(board=None, center_x=0.0, center_y=0.0, mirror_type=TRANSFORM_TYPE_SHIFT, do_footprints=True, do_tracks=True,
                 do_vias=True, do_polygons=False, mapfile=None, do_multi=True, sheet_orig="", sheet_copy=""):
    """Do second part"""
    if board is None:
        board = GetBoard()    
    coord_x = pcbnew.FromMM(center_x)
    coord_y = pcbnew.FromMM(center_y)
    elements = __GetElements(mapfile)
    count_footprints = 0
    count_vias = 0
    count_tracks = 0
    if do_footprints:
        # Process footprints
        for element in elements:
            # Find the footprint
            e_orig = board.FindModuleByReference(element)
            if e_orig is None:
                continue
            # Find the copy
            e_copy = board.FindModuleByReference(elements[element])
            if e_copy is None:
                continue
            # Place it
            pos = e_orig.GetPosition()
            new_pos = __ModifyPoint(mirror_type, pos, [coord_x, coord_y])
            e_copy.SetPosition(new_pos)        
            # flip footprint if necessary
            flip = e_orig.IsFlipped()
            if flip and not e_copy.IsFlipped():
                e_copy.Flip(new_pos)
            # get original angle
            angle = e_orig.GetOrientation()
            if mirror_type == TRANSFORM_TYPE_MIRROR:
                # Rotate it (angle in 1/10 degreee)
                new_angle = int((angle + 180*10) % (360*10))
            else:
                new_angle = angle
            e_copy.SetOrientation(new_angle)
            count_footprints = count_footprints + 1
    if do_vias:
        tracks = board.GetTracks()
        vias = []
        for track in tracks:
            if track.GetClass() == "VIA":
                old_name = track.GetNetname()
                match = re.search(r"Net-\(([a-zA-Z]+\d+)-(Pad\d+)\)", old_name)
                if do_multi:
                    match2 = re.search(r"\/{}\/([a-zA-Z0-9_+]+)".format(sheet_orig), old_name)
                    #name_spl = old_name.split('/')
                    #if (len(name_spl) == 3 and name_spl[1] == sheet_orig)
                else:
                    match2 = re.search(r"{}".format(sheet_orig), old_name)
                if old_name == "GND" or match2 or match:
                    pos = track.GetPosition()
                    new_pos = __ModifyPoint(mirror_type, pos, [coord_x, coord_y])
                    if match:
                        if match.group(1) in elements:
                            new_name = "Net-(" + elements[match.group(1)] + "-" + match.group(2) +")"
                        else:
                            continue
                    elif old_name == "GND":
                        new_name = "GND"
                        #new_code = track.GetNetCode()
                    else:
                        #new_name = "/{}/{}".format(sheet_copy, name_spl[-1])
                        #new_name = old_name[:-1] + "2"
                        if do_multi:
                            new_name = "/{}/{}".format(sheet_copy, match2.group(1))
                        else:
                            new_name = "{}2".format(match2.group(1))
                    print(old_name + ":" + new_name)
                    if new_name not in board.GetNetsByName():
                        continue
                    new_code = board.GetNetcodeFromNetname(new_name)
                    via_copy = track.Duplicate()
                    via_copy.SetPosition(new_pos)
                    via_copy.SetNetCode(new_code)
                    vias.append(via_copy)
                    count_vias = count_vias + 1
                    #print(old_name, new_name, track.GetNetCode(), new_code)
        for via in vias:
            tracks.Append(via)
    if do_tracks:
        new_tracks = []
        tracks = board.GetTracks()
        for track in tracks:
            if track.GetClass() == "TRACK":
                old_name = track.GetNetname()
                match = re.search(r"Net-\(([a-zA-Z]+\d+)-(Pad\d+)\)", old_name)
                name_spl = old_name.split('/')
                if (len(name_spl) == 3 and name_spl[1] == sheet_orig) or old_name == "GND" or match:
                    pos = track.GetPosition()
                    start = track.GetStart()
                    end = track.GetEnd()
                    if match:
                        if match.group(1) in elements:
                            new_name = "Net-(" + elements[match.group(1)] + "-" + match.group(2) +")"
                        else:
                            continue        
                    elif old_name == "GND":
                        new_name = "GND";
                        #new_code = track.GetNetCode()
                    else:
                        new_name = "/{}/{}".format(sheet_copy, name_spl[-1])
                        #new_name = old_name[:-1] + "2"
                    if new_name not in board.GetNetsByName():
                        continue
                    new_code = board.GetNetcodeFromNetname(new_name)
                    track_copy = track.Duplicate()
                    track_copy.SetPosition(__ModifyPoint(mirror_type, pos, [coord_x, coord_y]))
                    track_copy.SetStart(__ModifyPoint(mirror_type, start, [coord_x, coord_y]))
                    track_copy.SetEnd(__ModifyPoint(mirror_type, end, [coord_x, coord_y]))
                    track_copy.SetNetCode(new_code)
                    new_tracks.append(track_copy)
                    count_tracks = count_tracks + 1
                    #print(track.GetNetname(), new_name, [pos.x, pos.y], track.GetNetCode(), new_code)
        for track in new_tracks:
            tracks.Append(track)
    if do_polygons:
        pass
    result = {}
    result["footprints"] = count_footprints
    result["vias"] = count_vias
    result["tracks"] = count_tracks
    return result
    

'''class DuplexAction:
    def __init__(self, board, params, mapfile):
        self.board = board
        self.params = params
        self.mapfile = mapfile
        self.elements = {}
        
    def process():
        # read mapping file and create dictionary
        with open(self.mapfile, "r") as f:
            lines = f.readlines()
            for line in lines:
                e1, e2 = line.strip().split(":")
                if e1 is not None and e2 is not None:
                    self.elements[e1] = e2
        result = {}
        result["footprints"] = 10;
        result["vias"] = 15;
        result["tracks"] = 20;
        return result'''