# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
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
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"DuplexPCB", pos = wx.DefaultPosition, size = wx.Size( 400,310 ), style = wx.DEFAULT_DIALOG_STYLE )

		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"PCB center: " ), wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"X", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.sp_center_x = wx.SpinCtrlDouble( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 0, 250, 0, 0.1 )
		self.sp_center_x.SetDigits( 1 )
		bSizer2.Add( self.sp_center_x, 0, wx.ALL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Y", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.sp_center_y = wx.SpinCtrlDouble( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 0, 250, 0, 0.1 )
		self.sp_center_y.SetDigits( 1 )
		bSizer2.Add( self.sp_center_y, 0, wx.ALL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		sbSizer1.Add( bSizer2, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Mirror: " ), wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_radioBtn1 = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"X only", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_radioBtn1, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_radioBtn2 = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Y only", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_radioBtn2, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_radioBtn3 = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Both", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_radioBtn3, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		sbSizer4.Add( bSizer4, 1, wx.EXPAND, 5 )


		bSizer1.Add( sbSizer4, 1, wx.EXPAND, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Copy: " ), wx.VERTICAL )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_checkBox1 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Footprints", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.SetValue(True)
		gSizer1.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Vias", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.SetValue(True)
		gSizer1.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		self.m_checkBox3 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Tracks", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox3.SetValue(True)
		gSizer1.Add( self.m_checkBox3, 0, wx.ALL, 5 )

		self.m_checkBox4 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Polygons", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_checkBox4, 0, wx.ALL, 5 )


		sbSizer3.Add( gSizer1, 1, wx.EXPAND, 5 )


		bSizer1.Add( sbSizer3, 1, wx.EXPAND, 5 )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Mapping file: " ), wx.VERTICAL )

		self.fp_mapfile = wx.FilePickerCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a mapping file", u"*.txt", wx.DefaultPosition, wx.Size( 370,-1 ), wx.FLP_DEFAULT_STYLE )
		sbSizer5.Add( self.fp_mapfile, 0, wx.ALL, 5 )


		bSizer1.Add( sbSizer5, 1, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.but_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.but_ok, 0, wx.ALL, 5 )

		self.but_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.but_cancel, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer6, 1, wx.ALIGN_RIGHT|wx.EXPAND|wx.RIGHT, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


