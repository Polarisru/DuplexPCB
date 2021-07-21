#cd PATH_TO_WORK
#execfile("mirror_modules.py")

import pdb
import pcbnew
import re

__version__ = "0.0.1"

# the internal coorinate space of pcbnew is 10E-6 mm. (a millionth of a mm)
# the coordinate 121550000 corresponds to 121.550000 
SCALE = 1000000

# middle of the PCB
COOR_X = 0
COOR_Y = 0

# types of mirroring
MIRROR_TYPE_X = 0
MIRROR_TYPE_Y = 1
MIRROR_TYPE_BOTH = 2

def __ModifyPoint(mirror_type, point):
    if mirror_type in [MIRROR_TYPE_X, MIRROR_TYPE_BOTH]:
        new_x = 2 * COOR_X - point.x
    if mirror_type in [MIRROR_TYPE_Y, MIRROR_TYPE_BOTH]:
        new_y = 2 * COOR_Y - point.y
    return pcbnew.wxPoint(new_x, new_y)

def MakeDuplex(center_x=0, center_y=0, mirror_type=0, do_footprints=True, do_tracks=True,
                 do_vias=True, do_polygons=False, mapfile=None, board=None):
    """Do second part"""
    if board is None:
        board = GetBoard()    
    COOR_X = int(center_x * SCALE)
    COOR_Y = int(center_y * SCALE)
    elements = {}
    with open(mapfile, "r") as f:
        lines = f.readlines()
        for line in lines:
            e1, e2 = line.strip().split(":")
            if e1 is not None and e2 is not None:
                elements[e1] = e2
    count_footprints = 0
    count_vias = 0
    count_tracks = 0
    for element in elements:
        # Find the footprint
        e_orig = board.FindModuleByReference(element)
        # Find the copy
        e_copy = board.FindModuleByReference(elements[element])
        # Place it
        pos = e_orig.GetPosition()
        e_copy.SetPosition(__ModifyPoint(mirror_type, pos))        
        # flip footprint if necessary
        flip = e_orig.IsFlipped()
        if flip and not e_copy.IsFlipped():
            e_copy.Flip(pos)
        # get original angle
        angle = e_orig.GetOrientation()
        # Rotate it (angle in 1/10 degreee)
        new_angle = int((angle + 180*10) % (360*10))
        e_copy.SetOrientation(new_angle)
        count_footprints = count_footprints + 1
    
    result = {}
    result["footprints"] = count_footprints;
    result["vias"] = count_vias;
    result["tracks"] = count_tracks;
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

'''        
# Footprints
print("Moving footprints...")

for element in elements:
  # Find the component
  e_orig = board.FindModuleByReference(element)
  # Find the copy
  e_copy = board.FindModuleByReference(elements[element])

  # Place it
  pos = e_orig.GetPosition()
  new_x = COOR_X - pos.x + COOR_X
  new_y = COOR_Y - pos.y
  e_copy.SetPosition(pcbnew.wxPoint(new_x, new_y))
  
  flip = e_orig.IsFlipped()
  if flip and not e_copy.IsFlipped():
    e_copy.Flip(pcbnew.wxPoint(new_x, new_y))

  # get original angle
  angle = e_orig.GetOrientation()
  # Rotate it (angle in 1/10 degreee)
  new_angle = int((angle + 180*10) % (360*10))
  e_copy.SetOrientation(new_angle)
  
  print("{} placed at: ({:.3}, {:.3}) with {}deg".format(e2, float(new_x) / SCALE, float(new_y) / SCALE, new_angle // 10))

print("Footprints: Ready!")

# Vias
print("Creating vias...")

tracks = board.GetTracks()
vias = []
for track in tracks:
  if track.GetClass() == "VIA":
    old_name = track.GetNetname()
    match = re.search(r"Net-\(([a-zA-Z]+\d+)-(Pad\d+)\)", old_name)
    if old_name == "GND" or old_name.endswith("1") or match:
      pos = track.GetPosition()
      new_x = COOR_X - pos.x + COOR_X
      new_y = COOR_Y - pos.y
      if match:
        if match.group(1) in elems:
          new_name = "Net-(" + elems[match.group(1)] + "-" + match.group(2) +")"
          if new_name in board.GetNetsByName():
            new_code = board.GetNetcodeFromNetname(new_name)
          else:
            continue
        else:
          continue
      elif old_name == "GND":
        new_name = "GND"
        new_code = track.GetNetCode()
      else:
        name_spl = old_name.split('/')
        if len(name_spl) == 3:
            new_name = "/ACE2/" + name_spl[-1][:-1] + "2"
        else:
            new_name = old_name[:-1] + "2"
        new_code = board.GetNetcodeFromNetname(new_name)
      via_copy = track.Duplicate()
      via_copy.SetPosition(pcbnew.wxPoint(new_x, new_y))
      via_copy.SetNetCode(new_code)
      vias.append(via_copy)
      print(old_name, new_name, track.GetNetCode(), new_code)

for via in vias:
  tracks.Append(via)

print("Vias: Ready!")  

# Tracks
print("Creating tracks...")
  
track_except = []
new_tracks = []
tracks = board.GetTracks()
for track in tracks:
  if track.GetClass() == "TRACK":
    old_name = track.GetNetname()
    match = re.search(r"Net-\(([a-zA-Z]+\d+)-(Pad\d+)\)", old_name)
    if (old_name.endswith("1") and not old_name in track_except) or old_name == "GND" or match:
      pos = track.GetPosition()
      start = track.GetStart()
      end = track.GetEnd()
      #print(track.GetNetname(), [pos.x, pos.y], [start.x, start.y], [end.y, end.y])
      if match:
        if match.group(1) in elems:
          new_name = "Net-(" + elems[match.group(1)] + "-" + match.group(2) +")"
          if new_name in board.GetNetsByName():
            new_code = board.GetNetcodeFromNetname(new_name)
          else:
            continue
        else:
          continue        
      elif old_name == "GND":
        new_name = "GND";
        new_code = track.GetNetCode()
      else:
        name_spl = old_name.split('/')
        if len(name_spl) == 3:
          new_name = "/ACE2/" + name_spl[-1][:-1] + "2"
        else:
          new_name = old_name[:-1] + "2"
        new_code = board.GetNetcodeFromNetname(new_name)
      #print(new_name, [pos_new.x, pos_new.y], [start_new.x, start_new.y], [end_new.y, end_new.y])
      track_copy = track.Duplicate()
      track_copy.SetPosition(modify_point(pos))
      track_copy.SetStart(modify_point(start))
      track_copy.SetEnd(modify_point(end))
      track_copy.SetNetCode(new_code)
      new_tracks.append(track_copy)
      print(track.GetNetname(), new_name, [pos.x, pos.y], track.GetNetCode(), new_code)      
      
for track in new_tracks:
  tracks.Append(track)
  
print("Tracks: Ready!")

pcbnew.Refresh()
'''