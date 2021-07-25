import pcbnew

board = pcbnew.GetBoard()

diameters = set()

for track in board.GetTracks():
    if track.GetClass() == "VIA":
        diameters.add((pcbnew.ToMM(track.GetWidth()), pcbnew.ToMM(track.GetDrillValue())))

for d in diameters:
    print("{}:{}".format(d[0], d[1]))
    
for track in board.GetTracks():
    if track.GetClass() == "VIA":
        if pcbnew.ToMM(track.GetWidth()) == 0.8 and pcbnew.ToMM(track.GetDrillValue()) == 0.5:
            track.SetSelected()
            print(track.GetNetname())
        else:
            track.ClearSelected()
            
pcbnew.UpdateUserInterface()
    
'''if trk.IsSelected():
  trk.ClearSelected()
else:
  trk.SetSelected()'''