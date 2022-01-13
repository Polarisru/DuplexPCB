# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class duplex_gui
###########################################################################

class duplex_gui ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"DuplexPCB", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sizer_main = wx.BoxSizer( wx.VERTICAL )

		sb_transform = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Transformation: " ), wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.radio_shift = wx.RadioButton( sb_transform.GetStaticBox(), wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.radio_shift.SetValue( True )
		bSizer4.Add( self.radio_shift, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.radio_mirror = wx.RadioButton( sb_transform.GetStaticBox(), wx.ID_ANY, u"Mirror", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.radio_mirror, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.radio_flip = wx.RadioButton( sb_transform.GetStaticBox(), wx.ID_ANY, u"Flip", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.radio_flip, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		sb_transform.Add( bSizer4, 1, wx.EXPAND, 5 )


		sizer_main.Add( sb_transform, 1, wx.EXPAND, 5 )

		sb_center = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Transformation point: " ), wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( sb_center.GetStaticBox(), wx.ID_ANY, u"X", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.sp_center_x = wx.SpinCtrlDouble( sb_center.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 0, 250, 0.100000, 0.1 )
		self.sp_center_x.SetDigits( 1 )
		bSizer2.Add( self.sp_center_x, 0, wx.ALL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( sb_center.GetStaticBox(), wx.ID_ANY, u"Y", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer2.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.sp_center_y = wx.SpinCtrlDouble( sb_center.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 0, 250, 0, 0.1 )
		self.sp_center_y.SetDigits( 1 )
		bSizer2.Add( self.sp_center_y, 0, wx.ALL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		sb_center.Add( bSizer2, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		sizer_main.Add( sb_center, 1, wx.EXPAND, 5 )

		sb_structure = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Project structure: " ), wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.radio_single = wx.RadioButton( sb_structure.GetStaticBox(), wx.ID_ANY, u"Single sheet", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.radio_single.SetValue( True )
		bSizer6.Add( self.radio_single, 0, wx.ALL, 5 )


		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.radio_multi = wx.RadioButton( sb_structure.GetStaticBox(), wx.ID_ANY, u"Multiple sheets", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.radio_multi, 0, wx.ALL, 5 )


		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		sb_structure.Add( bSizer6, 1, wx.EXPAND, 5 )


		sizer_main.Add( sb_structure, 1, wx.EXPAND, 5 )

		sb_mapping = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Nets mapping: " ), wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.st_orig = wx.StaticText( sb_mapping.GetStaticBox(), wx.ID_ANY, u"Original", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_orig.Wrap( -1 )

		bSizer7.Add( self.st_orig, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.text_orig = wx.TextCtrl( sb_mapping.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.text_orig, 0, wx.ALL, 5 )


		bSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.st_copy = wx.StaticText( sb_mapping.GetStaticBox(), wx.ID_ANY, u"Copy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_copy.Wrap( -1 )

		bSizer7.Add( self.st_copy, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.text_copy = wx.TextCtrl( sb_mapping.GetStaticBox(), wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.text_copy, 0, wx.ALL, 5 )


		sb_mapping.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer71 = wx.BoxSizer( wx.VERTICAL )


		bSizer71.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.st_map_hint = wx.StaticText( sb_mapping.GetStaticBox(), wx.ID_ANY, u"Enter suffixes for duplicated nets (e.g., 1 and 2 for NET1 and NET2)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_map_hint.Wrap( -1 )

		bSizer71.Add( self.st_map_hint, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer71.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		sb_mapping.Add( bSizer71, 1, wx.EXPAND, 5 )


		sizer_main.Add( sb_mapping, 1, wx.EXPAND, 5 )

		sb_copy = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Copy: " ), wx.VERTICAL )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.cb_footprints = wx.CheckBox( sb_copy.GetStaticBox(), wx.ID_ANY, u"Footprints", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_footprints.SetValue(True)
		gSizer1.Add( self.cb_footprints, 0, wx.ALL, 5 )

		self.cb_vias = wx.CheckBox( sb_copy.GetStaticBox(), wx.ID_ANY, u"Vias", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_vias.SetValue(True)
		gSizer1.Add( self.cb_vias, 0, wx.ALL, 5 )

		self.cb_tracks = wx.CheckBox( sb_copy.GetStaticBox(), wx.ID_ANY, u"Tracks", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_tracks.SetValue(True)
		gSizer1.Add( self.cb_tracks, 0, wx.ALL, 5 )

		self.cb_polygons = wx.CheckBox( sb_copy.GetStaticBox(), wx.ID_ANY, u"Polygons", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.cb_polygons, 0, wx.ALL, 5 )


		sb_copy.Add( gSizer1, 1, wx.EXPAND, 5 )


		sizer_main.Add( sb_copy, 1, wx.EXPAND, 5 )

		sb_file = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Components mapping file: " ), wx.VERTICAL )

		self.fp_mapfile = wx.FilePickerCtrl( sb_file.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a mapping file", u"*.txt", wx.DefaultPosition, wx.Size( 370,-1 ), wx.FLP_DEFAULT_STYLE )
		sb_file.Add( self.fp_mapfile, 0, wx.ALL, 5 )


		sizer_main.Add( sb_file, 1, wx.EXPAND, 5 )

		sb_buttons = wx.BoxSizer( wx.HORIZONTAL )


		sb_buttons.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.but_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		sb_buttons.Add( self.but_ok, 0, wx.ALL, 5 )

		self.but_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		sb_buttons.Add( self.but_cancel, 0, wx.ALL, 5 )


		sizer_main.Add( sb_buttons, 1, wx.ALIGN_RIGHT|wx.EXPAND|wx.RIGHT, 5 )


		self.SetSizer( sizer_main )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


