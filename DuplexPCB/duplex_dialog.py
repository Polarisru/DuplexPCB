#!/usr/bin/env python

import wx
import pcbnew
import os
import time

from duplex_plugin_gui import duplex_gui
from duplex_plugin_action import MakeDuplex, __version__

class DuplexDialog(duplex_gui):
    """Class that gathers all the Gui control"""

    def __init__(self, board):
        """Init the brand new instance"""
        super(DuplexDialog, self).__init__(None)
        self.board = board
        self.SetTitle("DuplexPCB (ver.{})".format(__version__))
        self.Bind(wx.EVT_CLOSE, self.onCloseWindow)
        self.but_cancel.Bind(wx.EVT_BUTTON, self.onCloseWindow)
        self.but_ok.Bind(wx.EVT_BUTTON, self.onProcessAction)
        self.Bind(wx.EVT_RADIOBUTTON, self.onProcessMirror)
        #self.m_bitmap_help.SetBitmap(wx.Bitmap( os.path.join(os.path.dirname(os.path.realpath(__file__)), "rcs", "teardrops-help.png") ) )
        self.SetMinSize(self.GetSize())
        self.mirror_type = 0

    def onAction(self, e):
        """Enables or disables the parameters/options elements"""
        els = [self.st_hpercent, self.sp_hpercent, self.st_vpercent,
               self.sp_vpercent, self.st_nbseg, self.sp_nbseg,
               self.cb_include_smd_pads, self.cb_discard_in_same_zone,
               self.cb_follow_tracks, self.cb_no_bulge]
        for i, el in enumerate(els):
            if self.rbx_action.GetSelection() == 0:
                el.Enable()
            else:
                el.Disable()
                
    def onProcessMirror(self, event):
        rb = event.GetEventObject() 
        if rb == self.radio_shift:
            self.mirror_type = 0
        elif rb == self.radio_mirror:
            self.mirror_type = 1
        else:
            self.mirror_type = 2
        #print("Value: " + str(self.mirror_type))

    def onProcessAction(self, event):
        # Executes the requested action
        result = MakeDuplex(board=self.board, 
                            center_x=self.sp_center_x.GetValue(), 
                            center_y=self.sp_center_y.GetValue(),
                            mirror_type=self.mirror_type,
                            do_footprints=self.cb_footprints.IsChecked(),
                            do_vias=self.cb_vias.IsChecked(),
                            do_tracks=self.cb_tracks.IsChecked(),
                            do_polygons=self.cb_polygons.IsChecked(),
                            sheet_orig=self.text_orig.GetValue(), 
                            sheet_copy=self.text_copy.GetValue(),
                            mapfile=self.fp_mapfile.GetPath())
        # Show up updated PCB
        pcbnew.Refresh() 
        msg = ""
        for x in result:
            msg += "{}: {}\n".format(x, str(result[x]))
        wx.MessageBox("Ready!\n\nProcessed:\n" + msg)
        self.EndModal(wx.ID_OK)

    def onCloseWindow(self, event):
        self.EndModal(wx.ID_OK)


def InitDuplexDialog(board):
    # Launch the dialog
    tg = DuplexDialog(board)
    tg.ShowModal()
    return tg
    
if __name__ == '__main__':
    InitDuplexDialog(pcbnew.GetBoard())
