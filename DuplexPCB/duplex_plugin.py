#!/usr/bin/env python

import wx
import os
from pcbnew import ActionPlugin, GetBoard

from .duplex_dialog import InitDuplexDialog

class DuplexPlugin(ActionPlugin):
    """Class that gathers the actionplugin stuff"""
    def defaults(self):
        self.name = "DuplexPCB"
        self.category = "Modify PCB"
        self.description = "Traces the second part of the board with the option of mirroring"
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'DuplexPCB.png')
        self.show_toolbar_button = True

    def Run(self):
        InitDuplexDialog(GetBoard())
