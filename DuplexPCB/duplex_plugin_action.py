import pcbnew
import re

__version__ = "0.0.2"

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
    
def __MovePoint(mirror_type, point, center):
    new_x = point.x
    new_y = point.y    
    if mirror_type == TRANSFORM_TYPE_SHIFT:
        new_x = point.x + center[0]
        new_y = point.y + center[1]    
    elif mirror_type == TRANSFORM_TYPE_MIRROR:
        new_x = 2 * (center[0] - point.x)
        new_y = 2 * (center[1] - point.y)
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
    
def __GetNewName(old_name, do_multi, sheet_orig, sheet_copy, elements):
    match = re.search(r"Net-\(([a-zA-Z]+\d+)-(Pad\d+)\)", old_name)
    match2 = False
    if do_multi:
        name_spl = old_name.split('/')
        if len(name_spl) == 3 and name_spl[1] == sheet_orig:
            match2 = True
    else:
        name_spl = old_name.rpartition(sheet_orig)
        if name_spl[1] == sheet_orig and len(name_spl[2]) == 0:
            match2 = True
    if old_name == "GND" or match2 or match:
        if match:
            if match.group(1) in elements:
                return "Net-({}-{})".format(elements[match.group(1)], match.group(2))
        elif old_name == "GND":
            return "GND"
        else:
            if do_multi:
                return "/{}/{}".format(sheet_copy, name_spl[-1])
            else:
                return "{}{}".format(name_spl[0], sheet_copy)
    return None

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
    count_polys = 0
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
            # process reference
            ref = e_orig.Reference()
            ref_copy = e_copy.Reference()
            pos_ref = ref.GetPosition()
            #new_pos_ref = __ModifyPoint(mirror_type, pos_ref, [coord_x, coord_y])
            new_pos_ref = __ModifyPoint(mirror_type, pos, [coord_x, coord_y])
            ref_diff = pos - pos_ref
            new_pos_ref = new_pos_ref + ref_diff
            ref_copy.SetPosition(new_pos_ref)
            angle_ref = ref.GetTextAngle()
            #if mirror_type == TRANSFORM_TYPE_MIRROR:
            #    # Rotate it (angle in 1/10 degreee)
            #    new_angle_ref = int((angle_ref + 180*10) % (360*10))
            #else:
            #    new_angle_ref = angle_ref
            #ref_copy.Move(ref_diff)
            ref_copy.SetTextAngle(angle_ref)
            if angle % (180*10) == 0:
                ref_copy.Rotate(new_pos_ref, 180*10)
            just = ref.GetHorizJustify()
            ref_copy.SetHorizJustify(just)
            ref_copy.SetKeepUpright(not ref.IsKeepUpright())
            if not ref.IsVisible():
                ref_copy.SetVisible(False)
    if do_tracks or do_vias:
        tracks = board.GetTracks()
        new_tracks = []
        for track in tracks:
            if track.GetClass() in ["VIA", "TRACK"]:
                old_name = track.GetNetname()
                new_name = __GetNewName(old_name, do_multi, sheet_orig, sheet_copy, elements)
                if new_name is None:
                    continue
                if new_name not in board.GetNetsByName():
                    continue
                new_code = board.GetNetcodeFromNetname(new_name)
                pos = track.GetPosition()
                if do_vias and track.GetClass() == "VIA":
                    new_pos = __ModifyPoint(mirror_type, pos, [coord_x, coord_y])
                    via_copy = track.Duplicate()
                    via_copy.SetPosition(new_pos)
                    via_copy.SetNetCode(new_code)
                    new_tracks.append(via_copy)
                    count_vias = count_vias + 1
                if do_tracks and track.GetClass() == "TRACK":
                    start = track.GetStart()
                    end = track.GetEnd()
                    track_copy = track.Duplicate()
                    track_copy.SetPosition(__ModifyPoint(mirror_type, pos, [coord_x, coord_y]))
                    track_copy.SetStart(__ModifyPoint(mirror_type, start, [coord_x, coord_y]))
                    track_copy.SetEnd(__ModifyPoint(mirror_type, end, [coord_x, coord_y]))
                    track_copy.SetNetCode(new_code)
                    new_tracks.append(track_copy)
                    count_tracks = count_tracks + 1
        for track in new_tracks:
            tracks.Append(track)
    if do_polygons:
        zones = board.Zones()
        for zone in zones:
            pos = zone.GetPosition()
            zone_copy = zone.Duplicate()
            # move and rotate new zone
            new_pos = __MovePoint(mirror_type, pos, [coord_x, coord_y])
            if mirror_type == TRANSFORM_TYPE_MIRROR:
                zone_copy.Rotate(pos, 180*10)
            zone_copy.Move(new_pos)
            layer = zone.GetLayer()
            zone_copy.SetLayer(layer)
            old_name = zone.GetNetname()
            new_name = __GetNewName(old_name, do_multi, sheet_orig, sheet_copy, elements)
            new_code = board.GetNetcodeFromNetname(new_name)
            #new_net = board.FindNet(new_code)
            zone_copy.SetNetCode(new_code)
            #new_zone.SetNet(new_net)            
            board.Add(zone_copy)
            count_polys = count_polys + 1
    result = {}
    result["footprints"] = count_footprints
    result["vias"] = count_vias
    result["tracks"] = count_tracks
    result["polygons"] = count_polys
    return result
