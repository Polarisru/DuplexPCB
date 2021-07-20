#cd PATH_TO_WORK
#execfile("mirror_modules.py")

import pdb
import pcbnew
import re

# the internal coorinate space of pcbnew is 10E-6 mm. (a millionth of a mm)
# the coordinate 121550000 corresponds to 121.550000 

SCALE = 1000000

COOR_X = int(148.5 * SCALE)
COOR_Y = int((70 + 50) * SCALE)

board = pcbnew.GetBoard()

def modify_point(point):
  new_x = COOR_X - point.x + COOR_X
  new_y = COOR_Y - point.y
  return pcbnew.wxPoint(new_x, new_y)

# Footprints
print("Moving footprints...")

with open("table_pcb.txt", "r") as f:
  elements = f.readlines()

elems = {}

for element in elements:
  e1, e2 = element.strip().split(":")
  elems[e1] = e2
  # Find the component
  e_orig = board.FindModuleByReference(e1)
  # Find the copy
  e_copy = board.FindModuleByReference(e2)

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