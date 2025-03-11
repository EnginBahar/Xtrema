# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 05:32:59 2015

@author: TheLichWing
"""

import Main_Window as XM
from PyQt5.QtWidgets import QLabel
import Calculations as cl
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets as Qt
import numpy as np
from plotpy.builder import make
import os


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = Qt.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return Qt.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return Qt.QApplication.translate(context, text, disambig)


#################################################################
"Min/Max Window Start"
#################################################################
class MinMax_Window(object):
    def setupUi(self, MinMax_Window):
        MinMax_Window.setObjectName(_fromUtf8("MinMax_Window"))
        MinMax_Window.resize(900, 650)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/MM.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MinMax_Window.setWindowIcon(icon)
        
        self.centralwidget = Qt.QWidget(MinMax_Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.Main_HLayout = Qt.QHBoxLayout(self.centralwidget)
        self.Main_HLayout.setContentsMargins(2, 2, 2, 2)
        self.Main_HLayout.setSpacing(2)
        self.Main_HLayout.setObjectName(_fromUtf8("Main_HLayout"))
        
        self.Graph_Splitter = Qt.QSplitter(self.centralwidget)
        self.Graph_Splitter.setOrientation(QtCore.Qt.Horizontal)
        self.Graph_Splitter.setHandleWidth(5)
        self.Graph_Splitter.setObjectName(_fromUtf8("Graph_Splitter"))

        self.LFrame = Qt.QFrame(self.Graph_Splitter)
        self.LFrame.setObjectName(_fromUtf8("LFrame"))
        
        self.LFrame_VLayout = Qt.QVBoxLayout(self.LFrame)
        self.LFrame_VLayout.setSpacing(2)
        self.LFrame_VLayout.setContentsMargins(0, 0, 0, 0)
        self.LFrame_VLayout.setObjectName(_fromUtf8("LFrame_VLayout"))
        
        self.Graph_Frame = Qt.QFrame(self.LFrame)
        self.Graph_Frame.setFrameShape(Qt.QFrame.StyledPanel)
        self.Graph_Frame.setFrameShadow(Qt.QFrame.Raised)
        self.Graph_Frame.setObjectName(_fromUtf8("Graph_Frame"))
        
        self.LFrame_VLayout.addWidget(self.Graph_Frame)
        
        self.LBFrame = Qt.QFrame(self.LFrame)
        self.LBFrame.setMaximumHeight(50)
        self.LBFrame.setFrameShape(Qt.QFrame.StyledPanel)
        self.LBFrame.setFrameShadow(Qt.QFrame.Raised)
        self.LBFrame.setObjectName(_fromUtf8("LBFrame"))
        
        self.LBFrame_HLayout = Qt.QHBoxLayout(self.LBFrame)
        self.LBFrame_HLayout.setObjectName(_fromUtf8("LBFrame_HLayout"))
        spacerItem = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.LBFrame_HLayout.addItem(spacerItem)
        
        self.Light_Curve_Button = Qt.QPushButton(self.LBFrame)
        self.Light_Curve_Button.setObjectName(_fromUtf8("Light_Curve_Button"))
        
        self.LBFrame_HLayout.addWidget(self.Light_Curve_Button)
        
        self.Min_Max_Region_Button = Qt.QPushButton(self.LBFrame)
        self.Min_Max_Region_Button.setObjectName(_fromUtf8("Min_Max_Region_Button"))
        
        self.LBFrame_HLayout.addWidget(self.Min_Max_Region_Button)
        spacerItem1 = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.LBFrame_HLayout.addItem(spacerItem1)
        
        self.LFrame_VLayout.addWidget(self.LBFrame)
        
        self.RFrame = Qt.QFrame(self.Graph_Splitter)
        self.RFrame.setFixedWidth(410)
        self.RFrame.setObjectName(_fromUtf8("RFrame"))
        
        self.RFrame_HLayout = Qt.QHBoxLayout(self.RFrame)
        self.RFrame_HLayout.setSpacing(0)
        self.RFrame_HLayout.setContentsMargins(0, 0, 0, 0)
        self.RFrame_HLayout.setObjectName(_fromUtf8("RFrame_HLayout"))
        
        self.Table_Splitter = Qt.QSplitter(self.RFrame)
        self.Table_Splitter.setOrientation(QtCore.Qt.Horizontal)
        self.Table_Splitter.setHandleWidth(5)
        self.Table_Splitter.setObjectName(_fromUtf8("Table_Splitter"))
        
        self.RLFrame = Qt.QFrame(self.Table_Splitter)
        self.RLFrame.setFixedWidth(201)
        self.RLFrame.setFrameShape(Qt.QFrame.StyledPanel)
        self.RLFrame.setFrameShadow(Qt.QFrame.Raised)
        self.RLFrame.setObjectName(_fromUtf8("RLFrame"))
        
        self.RLFrame_VLayout = Qt.QVBoxLayout(self.RLFrame)
        self.RLFrame_VLayout.setContentsMargins(0, 0, 0, 0)
        self.RLFrame_VLayout.setSpacing(0)
        self.RLFrame_VLayout.setObjectName(_fromUtf8("RLFrame_VLayout"))


        Select_Min_Max_Region_Hlayout = Qt.QHBoxLayout()
        Select_Min_Max_Region_Hlayout.setContentsMargins(0, 0, 0, 0)
        Select_Min_Max_Region_Hlayout.setSpacing(5)
        self.Select_Min_Max_Region_Label = QLabel(self.RLFrame)
        self.Select_Min_Max_Region_CheckBox = Qt.QCheckBox(self.RLFrame)
        self.Select_Min_Max_Region_CheckBox.setObjectName(_fromUtf8("Select_Min_Max_Region_CheckBox"))
        Select_Min_Max_Region_Spacer = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        Select_Min_Max_Region_Hlayout.addWidget(self.Select_Min_Max_Region_CheckBox)
        Select_Min_Max_Region_Hlayout.addWidget(self.Select_Min_Max_Region_Label)
        Select_Min_Max_Region_Hlayout.addItem(Select_Min_Max_Region_Spacer)

        self.RLFrame_VLayout.addLayout(Select_Min_Max_Region_Hlayout)

        Show_Min_Max_PointorCurve_Hlayout = Qt.QHBoxLayout()
        Show_Min_Max_PointorCurve_Hlayout.setContentsMargins(0, 0, 0, 0)
        Show_Min_Max_PointorCurve_Hlayout.setSpacing(5)
        self.Show_Min_Max_PointorCurve_Label = QLabel(self.RLFrame)
        self.Show_Min_Max_PointorCurve_CheckButton = Qt.QCheckBox(self.RLFrame)
        self.Show_Min_Max_PointorCurve_CheckButton.setObjectName(_fromUtf8("Show_Min_Max_PointorCurve_CheckButton"))
        Show_Min_Max_PointorCurve_Spacer = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        Show_Min_Max_PointorCurve_Hlayout.addWidget(self.Show_Min_Max_PointorCurve_CheckButton)
        Show_Min_Max_PointorCurve_Hlayout.addWidget(self.Show_Min_Max_PointorCurve_Label)
        Show_Min_Max_PointorCurve_Hlayout.addItem(Show_Min_Max_PointorCurve_Spacer)
        
        self.RLFrame_VLayout.addLayout(Show_Min_Max_PointorCurve_Hlayout)
        
        self.Extremum_GroupBox = Qt.QGroupBox(self.RLFrame)
        self.Extremum_GroupBox.setStyleSheet(XM.groupBoxStyle)
        self.Extremum_GroupBox.setObjectName(_fromUtf8("Extremum_GroupBox"))
        
        self.Extremum_GroupBox_VLayout = Qt.QVBoxLayout(self.Extremum_GroupBox)
        self.Extremum_GroupBox_VLayout.setObjectName(_fromUtf8("Extremum_GroupBox_VLayout"))
        
        self.Extremum_ComboBox = Qt.QComboBox(self.Extremum_GroupBox)
        self.Extremum_ComboBox.setObjectName(_fromUtf8("Extremum_ComboBox"))
        self.Extremum_ComboBox.addItem(_fromUtf8(""))
        self.Extremum_ComboBox.addItem(_fromUtf8(""))
        self.Extremum_ComboBox.addItem(_fromUtf8(""))
        
        self.Extremum_GroupBox_VLayout.addWidget(self.Extremum_ComboBox)
        
        self.RLFrame_VLayout.addWidget(self.Extremum_GroupBox)
        
        self.Min_Max_Setting_GroupBox = Qt.QGroupBox(self.RLFrame)
        self.Min_Max_Setting_GroupBox.setStyleSheet(XM.groupBoxStyle)
        self.Min_Max_Setting_GroupBox.setObjectName(_fromUtf8("Min_Max_Setting_GroupBox"))
        
        self.Min_Max_Setting_GroupBox_VLayout = Qt.QVBoxLayout(self.Min_Max_Setting_GroupBox)
        self.Min_Max_Setting_GroupBox_VLayout.setContentsMargins(2, -1, 2, -1)
        self.Min_Max_Setting_GroupBox_VLayout.setObjectName(_fromUtf8("Min_Max_Setting_GroupBox_VLayout"))
        self.Min_Max_Setting_GroupBox_VLayout.setSpacing(1)
        
        """ Start of Setting Widgets for Maximum Brightness of Eclipsing Binary"""
        
        self.WoRP_of_1Maxs_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_1Maxs_Frame.setObjectName(_fromUtf8("WoRP_of_1Maxs_Frame"))
     
        self.WoLP_of_1Maxs_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_1Maxs_Frame.setObjectName(_fromUtf8("WoLP_of_1Maxs_Frame"))
                
        self.WoRP_of_2Maxs_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_2Maxs_Frame.setObjectName(_fromUtf8("WoRP_of_2Maxs_Frame"))
                
        self.WoLP_of_2Maxs_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_2Maxs_Frame.setObjectName(_fromUtf8("WoLP_of_2Maxs_Frame"))
        
        self.Points_1Maxs_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.Points_1Maxs_Frame.setObjectName(_fromUtf8("Points_1Maxs_Frame"))
        
        self.Points_2Maxs_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.Points_2Maxs_Frame.setObjectName(_fromUtf8("Points_2Maxs_Frame"))
                
        self.Level_of_1Maxs_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.Level_of_1Maxs_Frame.setObjectName(_fromUtf8("Level_of_1Maxs_Frame"))
                
        self.Level_of_2Maxs_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.Level_of_2Maxs_Frame.setObjectName(_fromUtf8("Level_of_2Maxs_Frame"))
        
        
        
        self.Points_1Maxs_HLayout = Qt.QHBoxLayout(self.Points_1Maxs_Frame)
        self.Points_1Maxs_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Points_1Maxs_HLayout.setSpacing(2)
        self.Points_1Maxs_HLayout.setObjectName(_fromUtf8("Points_1Maxs_HLayout"))
        
        self.Points_1Maxs_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.Points_1Maxs_CheckBox.setMinimumWidth(130)
        self.Points_1Maxs_CheckBox.setObjectName(_fromUtf8("Points_1Maxs_CheckBox"))
        
        self.Points_1Maxs_HLayout.addWidget(self.Points_1Maxs_CheckBox)
        
        self.Points_1Maxs_Colon_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.Points_1Maxs_Colon_Label.setObjectName(_fromUtf8("Points_1Maxs_Colon_Label"))
        
        self.Points_1Maxs_HLayout.addWidget(self.Points_1Maxs_Colon_Label)
        
        self.Points_1Maxs_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.Points_1Maxs_LineEdit.setMaximumWidth(54)
        self.Points_1Maxs_LineEdit.setObjectName(_fromUtf8("Points_1Maxs_LineEdit"))
        
        self.Points_1Maxs_HLayout.addWidget(self.Points_1Maxs_LineEdit)
        
        
        self.Points_2Maxs_HLayout = Qt.QHBoxLayout(self.Points_2Maxs_Frame)
        self.Points_2Maxs_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Points_2Maxs_HLayout.setSpacing(2)
        self.Points_2Maxs_HLayout.setObjectName(_fromUtf8("Points_1Maxs_HLayout"))
        
        self.Points_2Maxs_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.Points_2Maxs_CheckBox.setMinimumWidth(130)
        self.Points_2Maxs_CheckBox.setObjectName(_fromUtf8("Points_1Maxs_CheckBox"))
        
        self.Points_2Maxs_HLayout.addWidget(self.Points_2Maxs_CheckBox)
        
        self.Points_2Maxs_Colon_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.Points_2Maxs_Colon_Label.setObjectName(_fromUtf8("Points_1Maxs_Colon_Label"))
        
        self.Points_2Maxs_HLayout.addWidget(self.Points_2Maxs_Colon_Label)
        
        self.Points_2Maxs_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.Points_2Maxs_LineEdit.setMaximumWidth(54)
        self.Points_2Maxs_LineEdit.setObjectName(_fromUtf8("Points_1Maxs_LineEdit"))
        
        self.Points_2Maxs_HLayout.addWidget(self.Points_2Maxs_LineEdit)
        
        self.WoRP_of_1Maxs_HLayout = Qt.QHBoxLayout(self.WoRP_of_1Maxs_Frame)
        self.WoRP_of_1Maxs_HLayout.setContentsMargins(0, 0, 0, 0)
        self.WoRP_of_1Maxs_HLayout.setSpacing(2)
        self.WoRP_of_1Maxs_HLayout.setObjectName(_fromUtf8("WoRP_of_1Maxs_HLayout"))
        
        self.WoRP_of_1Maxs_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_1Maxs_CheckBox.setMinimumWidth(130)
        self.WoRP_of_1Maxs_CheckBox.setObjectName(_fromUtf8("WoRP_of_1Maxs_CheckBox"))
        
        self.WoRP_of_1Maxs_HLayout.addWidget(self.WoRP_of_1Maxs_CheckBox)
        
        self.WoRP_of_1Maxs_Colon_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_1Maxs_Colon_Label.setObjectName(_fromUtf8("WoRP_of_1Maxs_Colon_Label"))
        
        self.WoRP_of_1Maxs_HLayout.addWidget(self.WoRP_of_1Maxs_Colon_Label)
        
        self.WoRP_of_1Maxs_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_1Maxs_LineEdit.setMaximumWidth(54)
        self.WoRP_of_1Maxs_LineEdit.setObjectName(_fromUtf8("WoRP_of_1Maxs_LineEdit"))
        
        self.WoRP_of_1Maxs_HLayout.addWidget(self.WoRP_of_1Maxs_LineEdit)

        self.WoLP_of_1Maxs_HLayout = Qt.QHBoxLayout(self.WoLP_of_1Maxs_Frame)
        self.WoLP_of_1Maxs_HLayout.setContentsMargins(0, 0, 0, 0)
        self.WoLP_of_1Maxs_HLayout.setSpacing(2)
        self.WoLP_of_1Maxs_HLayout.setObjectName(_fromUtf8("WoLP_of_1Maxs_HLayout"))
        
        self.WoLP_of_1Maxs_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_1Maxs_CheckBox.setMinimumWidth(130)
        self.WoLP_of_1Maxs_CheckBox.setObjectName(_fromUtf8("WoLP_of_1Maxs_CheckBox"))
        
        self.WoLP_of_1Maxs_HLayout.addWidget(self.WoLP_of_1Maxs_CheckBox)
        
        self.WoLP_of_1Maxs_Colon_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_1Maxs_Colon_Label.setObjectName(_fromUtf8("WoLP_of_1Maxs_Colon_Label"))
        
        self.WoLP_of_1Maxs_HLayout.addWidget(self.WoLP_of_1Maxs_Colon_Label)
        
        self.WoLP_of_1Maxs_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_1Maxs_LineEdit.setMaximumWidth(54)
        self.WoLP_of_1Maxs_LineEdit.setObjectName(_fromUtf8("WoLP_of_1Maxs_LineEdit"))
        
        self.WoLP_of_1Maxs_HLayout.addWidget(self.WoLP_of_1Maxs_LineEdit)

        self.WoRP_of_2Maxs_HLayout = Qt.QHBoxLayout(self.WoRP_of_2Maxs_Frame)
        self.WoRP_of_2Maxs_HLayout.setContentsMargins(0, 0, 0, 0)
        self.WoRP_of_2Maxs_HLayout.setSpacing(2)
        self.WoRP_of_2Maxs_HLayout.setObjectName(_fromUtf8("WoRP_of_2Maxs_HLayout"))
        
        self.WoRP_of_2Maxs_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_2Maxs_CheckBox.setMinimumWidth(130)
        self.WoRP_of_2Maxs_CheckBox.setObjectName(_fromUtf8("WoRP_of_2Maxs_CheckBox"))
        
        self.WoRP_of_2Maxs_HLayout.addWidget(self.WoRP_of_2Maxs_CheckBox)
        
        self.WoRP_of_2Maxs_Colon_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_2Maxs_Colon_Label.setObjectName(_fromUtf8("WoRP_of_2Maxs_Colon_Label"))
        
        self.WoRP_of_2Maxs_HLayout.addWidget(self.WoRP_of_2Maxs_Colon_Label)
        
        self.WoRP_of_2Maxs_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_2Maxs_LineEdit.setMaximumWidth(54)
        self.WoRP_of_2Maxs_LineEdit.setObjectName(_fromUtf8("WoRP_of_2Maxs_LineEdit"))
        
        self.WoRP_of_2Maxs_HLayout.addWidget(self.WoRP_of_2Maxs_LineEdit)
        
        self.WoLP_of_2Maxs_HLayout = Qt.QHBoxLayout(self.WoLP_of_2Maxs_Frame)
        self.WoLP_of_2Maxs_HLayout.setContentsMargins(0, 0, 0, 0)
        self.WoLP_of_2Maxs_HLayout.setSpacing(2)
        self.WoLP_of_2Maxs_HLayout.setObjectName(_fromUtf8("WoLP_of_2Maxs_HLayout"))
        
        self.WoLP_of_2Maxs_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_2Maxs_CheckBox.setMinimumWidth(130)
        self.WoLP_of_2Maxs_CheckBox.setObjectName(_fromUtf8("WoLP_of_2Maxs_CheckBox"))
        
        self.WoLP_of_2Maxs_HLayout.addWidget(self.WoLP_of_2Maxs_CheckBox)
        
        self.WoLP_of_2Maxs_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_2Maxs_Label.setObjectName(_fromUtf8("WoLP_of_2Maxs_Label"))
        
        self.WoLP_of_2Maxs_HLayout.addWidget(self.WoLP_of_2Maxs_Label)
        
        self.WoLP_of_2Maxs_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_2Maxs_LineEdit.setMaximumWidth(54)
        self.WoLP_of_2Maxs_LineEdit.setObjectName(_fromUtf8("WoLP_of_2Maxs_LineEdit"))
        
        self.WoLP_of_2Maxs_HLayout.addWidget(self.WoLP_of_2Maxs_LineEdit)

        self.Level_of_1Maxs_HLayout = Qt.QHBoxLayout(self.Level_of_1Maxs_Frame)
        self.Level_of_1Maxs_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Level_of_1Maxs_HLayout.setSpacing(2)
        self.Level_of_1Maxs_HLayout.setObjectName(_fromUtf8("Level_of_1Maxs_HLayout"))
        
        self.Level_of_1Maxs_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.Level_of_1Maxs_CheckBox.setMinimumWidth(130)
        self.Level_of_1Maxs_CheckBox.setObjectName(_fromUtf8("Level_of_1Maxs_CheckBox"))
        
        self.Level_of_1Maxs_HLayout.addWidget(self.Level_of_1Maxs_CheckBox)
        
        self.Level_of_1Maxs_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.Level_of_1Maxs_Label.setObjectName(_fromUtf8("Level_of_1Maxs_Label"))
        
        self.Level_of_1Maxs_HLayout.addWidget(self.Level_of_1Maxs_Label)
        
        self.Level_of_1Maxs_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.Level_of_1Maxs_LineEdit.setMaximumWidth(54)
        self.Level_of_1Maxs_LineEdit.setObjectName(_fromUtf8("Level_of_1Maxs_LineEdit"))
        
        self.Level_of_1Maxs_HLayout.addWidget(self.Level_of_1Maxs_LineEdit)
        
        self.Level_of_2Maxs_HLayout = Qt.QHBoxLayout(self.Level_of_2Maxs_Frame)
        self.Level_of_2Maxs_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Level_of_2Maxs_HLayout.setSpacing(2)
        self.Level_of_2Maxs_HLayout.setObjectName(_fromUtf8("Level_of_2Maxs_HLayout"))
        
        self.Level_of_2Maxs_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.Level_of_2Maxs_CheckBox.setMinimumWidth(130)
        self.Level_of_2Maxs_CheckBox.setObjectName(_fromUtf8("Level_of_2Maxs_CheckBox"))
        
        self.Level_of_2Maxs_HLayout.addWidget(self.Level_of_2Maxs_CheckBox)
        
        self.Level_of_2Maxs_Colon_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.Level_of_2Maxs_Colon_Label.setObjectName(_fromUtf8("Level_of_2Maxs_Colon_Label"))
        
        self.Level_of_2Maxs_HLayout.addWidget(self.Level_of_2Maxs_Colon_Label)
        
        self.Level_of_2Maxs_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.Level_of_2Maxs_LineEdit.setMaximumWidth(54)
        self.Level_of_2Maxs_LineEdit.setObjectName(_fromUtf8("Level_of_2Maxs_LineEdit"))
        
        self.Level_of_2Maxs_HLayout.addWidget(self.Level_of_2Maxs_LineEdit)
        
        """ End of Setting Widgets for Maximum Brightness of Eclipsing Binary"""
        
        """ Start of Setting Widgets for Minima of Eclipsing Binary"""
        
        self.Stack_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.Stack_Frame.setObjectName(_fromUtf8("Stack_Frame"))
        
        self.Points_1Mins_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.Points_1Mins_Frame.setObjectName(_fromUtf8("Points_1Mins_Frame"))
        
        self.Points_2Mins_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.Points_2Mins_Frame.setObjectName(_fromUtf8("Points_2Mins_Frame"))
                
        self.WoRP_of_1Mins_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_1Mins_Frame.setObjectName(_fromUtf8("WoRP_of_1Mins_Frame"))
     
        self.WoLP_of_1Mins_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_1Mins_Frame.setObjectName(_fromUtf8("WoLP_of_1Mins_Frame"))
                
        self.WoRP_of_2Mins_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_2Mins_Frame.setObjectName(_fromUtf8("WoRP_of_2Mins_Frame"))
                
        self.WoLP_of_2Mins_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_2Mins_Frame.setObjectName(_fromUtf8("WoLP_of_2Mins_Frame"))
                
        self.Level_of_1Mins_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.Level_of_1Mins_Frame.setObjectName(_fromUtf8("Level_of_1Mins_Frame"))
                
        self.Level_of_2Mins_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.Level_of_2Mins_Frame.setObjectName(_fromUtf8("Level_of_2Mins_Frame"))
                
        self.Stack_HLayout = Qt.QHBoxLayout(self.Stack_Frame)
        self.Stack_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Stack_HLayout.setSpacing(2)
        self.Stack_HLayout.setObjectName(_fromUtf8("Stack_HLayout"))
        
        self.Stack_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.Stack_CheckBox.setMinimumWidth(130)
        self.Stack_CheckBox.setObjectName(_fromUtf8("Stack_CheckBox"))
        
        self.Stack_HLayout.addWidget(self.Stack_CheckBox)
        
        self.Stack_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.Stack_Label.setObjectName(_fromUtf8("Stack_Label"))
        
        self.Stack_HLayout.addWidget(self.Stack_Label)
        
        self.Stack_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.Stack_LineEdit.setMaximumWidth(54)
        self.Stack_LineEdit.setObjectName(_fromUtf8("Stack_LineEdit"))
        
        self.Stack_HLayout.addWidget(self.Stack_LineEdit)
        
        self.Points_1Mins_HLayout = Qt.QHBoxLayout(self.Points_1Mins_Frame)
        self.Points_1Mins_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Points_1Mins_HLayout.setSpacing(2)
        self.Points_1Mins_HLayout.setObjectName(_fromUtf8("Points_1Mins_HLayout"))
        
        self.Points_1Mins_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.Points_1Mins_CheckBox.setMinimumWidth(130)
        self.Points_1Mins_CheckBox.setObjectName(_fromUtf8("Points_1Mins_CheckBox"))
        
        self.Points_1Mins_HLayout.addWidget(self.Points_1Mins_CheckBox)
        
        self.Points_1Mins_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.Points_1Mins_Label.setObjectName(_fromUtf8("Points_1Mins_Label"))
        
        self.Points_1Mins_HLayout.addWidget(self.Points_1Mins_Label)
        
        self.Points_1Mins_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.Points_1Mins_LineEdit.setMaximumWidth(54)
        
        self.Points_1Mins_HLayout.addWidget(self.Points_1Mins_LineEdit)
        
        self.Points_2Mins_HLayout = Qt.QHBoxLayout(self.Points_2Mins_Frame)
        self.Points_2Mins_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Points_2Mins_HLayout.setSpacing(2)
        self.Points_2Mins_HLayout.setObjectName(_fromUtf8("Points_2Mins_HLayout"))
        
        self.Points_2Mins_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.Points_2Mins_CheckBox.setMinimumWidth(130)
        self.Points_2Mins_CheckBox.setObjectName(_fromUtf8("Points_2Mins_CheckBox"))
        
        self.Points_2Mins_HLayout.addWidget(self.Points_2Mins_CheckBox)
        
        self.Points_2Mins_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.Points_2Mins_Label.setObjectName(_fromUtf8("Points_2Mins_Label"))
        
        self.Points_2Mins_HLayout.addWidget(self.Points_2Mins_Label)
        
        self.Points_2Mins_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.Points_2Mins_LineEdit.setMaximumWidth(54)
        
        self.Points_2Mins_HLayout.addWidget(self.Points_2Mins_LineEdit)     
        
        self.WoRP_of_1Mins_HLayout = Qt.QHBoxLayout(self.WoRP_of_1Mins_Frame)
        self.WoRP_of_1Mins_HLayout.setContentsMargins(0, 0, 0, 0)
        self.WoRP_of_1Mins_HLayout.setSpacing(2)
        self.WoRP_of_1Mins_HLayout.setObjectName(_fromUtf8("WoRP_of_1Mins_HLayout"))
        
        self.WoRP_of_1Mins_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_1Mins_CheckBox.setMinimumWidth(130)
        self.WoRP_of_1Mins_CheckBox.setObjectName(_fromUtf8("WoRP_of_1Mins_CheckBox"))
        
        self.WoRP_of_1Mins_HLayout.addWidget(self.WoRP_of_1Mins_CheckBox)
        
        self.WoRP_of_1Mins_Colon_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_1Mins_Colon_Label.setObjectName(_fromUtf8("WoRP_of_1Mins_Colon_Label"))
        
        self.WoRP_of_1Mins_HLayout.addWidget(self.WoRP_of_1Mins_Colon_Label)
        
        self.WoRP_of_1Mins_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_1Mins_LineEdit.setMaximumWidth(54)
        self.WoRP_of_1Mins_LineEdit.setObjectName(_fromUtf8("WoRP_of_1Mins_LineEdit"))
        
        self.WoRP_of_1Mins_HLayout.addWidget(self.WoRP_of_1Mins_LineEdit)

        self.WoLP_of_1Mins_HLayout = Qt.QHBoxLayout(self.WoLP_of_1Mins_Frame)
        self.WoLP_of_1Mins_HLayout.setContentsMargins(0, 0, 0, 0)
        self.WoLP_of_1Mins_HLayout.setSpacing(2)
        self.WoLP_of_1Mins_HLayout.setObjectName(_fromUtf8("WoLP_of_1Mins_HLayout"))
        
        self.WoLP_of_1Mins_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_1Mins_CheckBox.setMinimumWidth(130)
        self.WoLP_of_1Mins_CheckBox.setObjectName(_fromUtf8("WoLP_of_1Mins_CheckBox"))
        
        self.WoLP_of_1Mins_HLayout.addWidget(self.WoLP_of_1Mins_CheckBox)
        
        self.WoLP_of_1Mins_Colon_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_1Mins_Colon_Label.setObjectName(_fromUtf8("WoLP_of_1Mins_Colon_Label"))
        
        self.WoLP_of_1Mins_HLayout.addWidget(self.WoLP_of_1Mins_Colon_Label)
        
        self.WoLP_of_1Mins_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_1Mins_LineEdit.setMaximumWidth(54)
        self.WoLP_of_1Mins_LineEdit.setObjectName(_fromUtf8("WoLP_of_1Mins_LineEdit"))
        
        self.WoLP_of_1Mins_HLayout.addWidget(self.WoLP_of_1Mins_LineEdit)

        self.WoRP_of_2Mins_HLayout = Qt.QHBoxLayout(self.WoRP_of_2Mins_Frame)
        self.WoRP_of_2Mins_HLayout.setContentsMargins(0, 0, 0, 0)
        self.WoRP_of_2Mins_HLayout.setSpacing(2)
        self.WoRP_of_2Mins_HLayout.setObjectName(_fromUtf8("WoRP_of_2Mins_HLayout"))
        
        self.WoRP_of_2Mins_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_2Mins_CheckBox.setMinimumWidth(130)
        self.WoRP_of_2Mins_CheckBox.setObjectName(_fromUtf8("WoRP_of_2Mins_CheckBox"))
        
        self.WoRP_of_2Mins_HLayout.addWidget(self.WoRP_of_2Mins_CheckBox)
        
        self.WoRP_of_2Mins_Colon_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_2Mins_Colon_Label.setObjectName(_fromUtf8("WoRP_of_2Mins_Colon_Label"))
        
        self.WoRP_of_2Mins_HLayout.addWidget(self.WoRP_of_2Mins_Colon_Label)
        
        self.WoRP_of_2Mins_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_2Mins_LineEdit.setMaximumWidth(54)
        self.WoRP_of_2Mins_LineEdit.setObjectName(_fromUtf8("WoRP_of_2Mins_LineEdit"))
        
        self.WoRP_of_2Mins_HLayout.addWidget(self.WoRP_of_2Mins_LineEdit)
        
        self.WoLP_of_2Mins_HLayout = Qt.QHBoxLayout(self.WoLP_of_2Mins_Frame)
        self.WoLP_of_2Mins_HLayout.setContentsMargins(0, 0, 0, 0)
        self.WoLP_of_2Mins_HLayout.setSpacing(2)
        self.WoLP_of_2Mins_HLayout.setObjectName(_fromUtf8("WoLP_of_2Mins_HLayout"))
        
        self.WoLP_of_2Mins_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_2Mins_CheckBox.setMinimumWidth(130)
        self.WoLP_of_2Mins_CheckBox.setObjectName(_fromUtf8("WoLP_of_2Mins_CheckBox"))
        
        self.WoLP_of_2Mins_HLayout.addWidget(self.WoLP_of_2Mins_CheckBox)
        
        self.WoLP_of_2Mins_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_2Mins_Label.setObjectName(_fromUtf8("WoLP_of_2Mins_Label"))
        
        self.WoLP_of_2Mins_HLayout.addWidget(self.WoLP_of_2Mins_Label)
        
        self.WoLP_of_2Mins_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_2Mins_LineEdit.setMaximumWidth(54)
        self.WoLP_of_2Mins_LineEdit.setObjectName(_fromUtf8("WoLP_of_2Mins_LineEdit"))
        
        self.WoLP_of_2Mins_HLayout.addWidget(self.WoLP_of_2Mins_LineEdit)

        self.Level_of_1Mins_HLayout = Qt.QHBoxLayout(self.Level_of_1Mins_Frame)
        self.Level_of_1Mins_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Level_of_1Mins_HLayout.setSpacing(2)
        self.Level_of_1Mins_HLayout.setObjectName(_fromUtf8("Level_of_1Mins_HLayout"))
        
        self.Level_of_1Mins_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.Level_of_1Mins_CheckBox.setMinimumWidth(130)
        self.Level_of_1Mins_CheckBox.setObjectName(_fromUtf8("Level_of_1Mins_CheckBox"))
        
        self.Level_of_1Mins_HLayout.addWidget(self.Level_of_1Mins_CheckBox)
        
        self.Level_of_1Mins_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.Level_of_1Mins_Label.setObjectName(_fromUtf8("Level_of_1Mins_Label"))
        
        self.Level_of_1Mins_HLayout.addWidget(self.Level_of_1Mins_Label)
        
        self.Level_of_1Mins_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.Level_of_1Mins_LineEdit.setMaximumWidth(54)
        self.Level_of_1Mins_LineEdit.setObjectName(_fromUtf8("Level_of_1Mins_LineEdit"))
        
        self.Level_of_1Mins_HLayout.addWidget(self.Level_of_1Mins_LineEdit)
        
        self.Level_of_2Mins_HLayout = Qt.QHBoxLayout(self.Level_of_2Mins_Frame)
        self.Level_of_2Mins_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Level_of_2Mins_HLayout.setSpacing(2)
        self.Level_of_2Mins_HLayout.setObjectName(_fromUtf8("Level_of_2Mins_HLayout"))
        
        self.Level_of_2Mins_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.Level_of_2Mins_CheckBox.setMinimumWidth(130)
        self.Level_of_2Mins_CheckBox.setObjectName(_fromUtf8("Level_of_2Mins_CheckBox"))
        
        self.Level_of_2Mins_HLayout.addWidget(self.Level_of_2Mins_CheckBox)
        
        self.Level_of_2Mins_Colon_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.Level_of_2Mins_Colon_Label.setObjectName(_fromUtf8("Level_of_2Mins_Colon_Label"))
        
        self.Level_of_2Mins_HLayout.addWidget(self.Level_of_2Mins_Colon_Label)
        
        self.Level_of_2Mins_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.Level_of_2Mins_LineEdit.setMaximumWidth(54)
        self.Level_of_2Mins_LineEdit.setObjectName(_fromUtf8("Level_of_2Mins_LineEdit"))
        
        self.Level_of_2Mins_HLayout.addWidget(self.Level_of_2Mins_LineEdit)
        """ End of Setting Widgets for Minima of Eclipsing Binary"""
        
        """ Start of Setting Widgets for Maxima of Pulsating Star"""
        self.Stack_PS_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.Stack_PS_Frame.setObjectName(_fromUtf8("Stack_PS_Frame"))
        
        self.Points_PS_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.Points_PS_Frame.setObjectName(_fromUtf8("Points_PS_Frame"))
                
        self.WoRP_of_Maxs_PS_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_Maxs_PS_Frame.setObjectName(_fromUtf8("WoRP_of_Maxs_PS_Frame"))
     
        self.WoLP_of_Maxs_PS_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_Maxs_PS_Frame.setObjectName(_fromUtf8("WoLP_of_Maxs_PS_Frame"))
                
        self.Level_of_Maxs_PS_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.Level_of_Maxs_PS_Frame.setObjectName(_fromUtf8("Level_of_Maxs_PS_Frame"))
        
        self.Stack_PS_HLayout = Qt.QHBoxLayout(self.Stack_PS_Frame)
        self.Stack_PS_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Stack_PS_HLayout.setSpacing(2)
        self.Stack_PS_HLayout.setObjectName(_fromUtf8("Stack_PS_HLayout"))
        
        self.Stack_PS_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.Stack_PS_CheckBox.setMinimumWidth(130)
        self.Stack_PS_CheckBox.setObjectName(_fromUtf8("Stack_PS_CheckBox"))
        
        self.Stack_PS_HLayout.addWidget(self.Stack_PS_CheckBox)
        
        self.Stack_PS_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.Stack_PS_Label.setObjectName(_fromUtf8("Stack_PS_Label"))
        
        self.Stack_PS_HLayout.addWidget(self.Stack_PS_Label)
        
        self.Stack_PS_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.Stack_PS_LineEdit.setMaximumWidth(54)
        self.Stack_PS_LineEdit.setObjectName(_fromUtf8("Stack_PS_LineEdit"))
        
        self.Stack_PS_HLayout.addWidget(self.Stack_PS_LineEdit)
        
        
        self.Points_PS_HLayout = Qt.QHBoxLayout(self.Points_PS_Frame)
        self.Points_PS_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Points_PS_HLayout.setSpacing(2)
        self.Points_PS_HLayout.setObjectName(_fromUtf8("Points_PS_HLayout"))
        
        self.Points_PS_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.Points_PS_CheckBox.setMinimumWidth(130)
        self.Points_PS_CheckBox.setObjectName(_fromUtf8("Points_PS_CheckBox"))
        
        self.Points_PS_HLayout.addWidget(self.Points_PS_CheckBox)
        
        self.Points_PS_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.Points_PS_Label.setObjectName(_fromUtf8("Points_PS_Label"))
        
        self.Points_PS_HLayout.addWidget(self.Points_PS_Label)
        
        self.Points_PS_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.Points_PS_LineEdit.setMaximumWidth(54)
        self.Points_PS_LineEdit.setObjectName(_fromUtf8("Points_PS_LineEdit"))
        
        self.Points_PS_HLayout.addWidget(self.Points_PS_LineEdit)
        
        self.WoRP_of_Maxs_PS_HLayout = Qt.QHBoxLayout(self.WoRP_of_Maxs_PS_Frame)
        self.WoRP_of_Maxs_PS_HLayout.setContentsMargins(0, 0, 0, 0)
        self.WoRP_of_Maxs_PS_HLayout.setSpacing(2)
        self.WoRP_of_Maxs_PS_HLayout.setObjectName(_fromUtf8("WoRP_of_Maxs_PS_HLayout"))
        
        self.WoRP_of_Maxs_PS_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_Maxs_PS_CheckBox.setMinimumWidth(130)
        self.WoRP_of_Maxs_PS_CheckBox.setObjectName(_fromUtf8("WoRP_of_Maxs_PS_CheckBox"))
        
        self.WoRP_of_Maxs_PS_HLayout.addWidget(self.WoRP_of_Maxs_PS_CheckBox)
        
        self.WoRP_of_Maxs_Colon_PS_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_Maxs_Colon_PS_Label.setObjectName(_fromUtf8("WoRP_of_Maxs_Colon_PS_Label"))
        
        self.WoRP_of_Maxs_PS_HLayout.addWidget(self.WoRP_of_Maxs_Colon_PS_Label)
        
        self.WoRP_of_Maxs_PS_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_Maxs_PS_LineEdit.setMaximumWidth(54)
        self.WoRP_of_Maxs_PS_LineEdit.setObjectName(_fromUtf8("WoRP_of_Maxs_PS_LineEdit"))
        
        self.WoRP_of_Maxs_PS_HLayout.addWidget(self.WoRP_of_Maxs_PS_LineEdit)

        self.WoLP_of_Maxs_PS_HLayout = Qt.QHBoxLayout(self.WoLP_of_Maxs_PS_Frame)
        self.WoLP_of_Maxs_PS_HLayout.setContentsMargins(0, 0, 0, 0)
        self.WoLP_of_Maxs_PS_HLayout.setSpacing(2)
        self.WoLP_of_Maxs_PS_HLayout.setObjectName(_fromUtf8("WoLP_of_Maxs_PS_HLayout"))
        
        self.WoLP_of_Maxs_PS_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_Maxs_PS_CheckBox.setMinimumWidth(130)
        self.WoLP_of_Maxs_PS_CheckBox.setObjectName(_fromUtf8("WoLP_of_Maxs_PS_CheckBox"))
        
        self.WoLP_of_Maxs_PS_HLayout.addWidget(self.WoLP_of_Maxs_PS_CheckBox)
        
        self.WoLP_of_Maxs_Colon_PS_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_Maxs_Colon_PS_Label.setObjectName(_fromUtf8("WoLP_of_Maxs_Colon_PS_Label"))
        
        self.WoLP_of_Maxs_PS_HLayout.addWidget(self.WoLP_of_Maxs_Colon_PS_Label)
        
        self.WoLP_of_Maxs_PS_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_Maxs_PS_LineEdit.setMaximumWidth(54)
        self.WoLP_of_Maxs_PS_LineEdit.setObjectName(_fromUtf8("WoLP_of_Maxs_PS_LineEdit"))
        
        self.WoLP_of_Maxs_PS_HLayout.addWidget(self.WoLP_of_Maxs_PS_LineEdit)

        self.Level_of_Maxs_PS_HLayout = Qt.QHBoxLayout(self.Level_of_Maxs_PS_Frame)
        self.Level_of_Maxs_PS_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Level_of_Maxs_PS_HLayout.setSpacing(2)
        self.Level_of_Maxs_PS_HLayout.setObjectName(_fromUtf8("Level_of_Maxs_PS_HLayout"))
        
        self.Level_of_Maxs_PS_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.Level_of_Maxs_PS_CheckBox.setMinimumWidth(130)
        self.Level_of_Maxs_PS_CheckBox.setObjectName(_fromUtf8("Level_of_Maxs_PS_CheckBox"))
        
        self.Level_of_Maxs_PS_HLayout.addWidget(self.Level_of_Maxs_PS_CheckBox)
        
        self.Level_of_Maxs_Colon_PS_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.Level_of_Maxs_Colon_PS_Label.setObjectName(_fromUtf8("Level_of_Maxs_Colon_PS_Label"))
        
        self.Level_of_Maxs_PS_HLayout.addWidget(self.Level_of_Maxs_Colon_PS_Label)
        
        self.Level_of_Maxs_PS_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.Level_of_Maxs_PS_LineEdit.setMaximumWidth(54)
        self.Level_of_Maxs_PS_LineEdit.setObjectName(_fromUtf8("Level_of_Maxs_PS_LineEdit"))
        
        self.Level_of_Maxs_PS_HLayout.addWidget(self.Level_of_Maxs_PS_LineEdit)
        
        """ End of Setting Widgets for Maxima of Pulsating Star"""
        
        """ Start of Setting Widgets for Maximum Brightness of Pulsating Star"""
        self.WoRP_of_MaxsBR_PS_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_MaxsBR_PS_Frame.setObjectName(_fromUtf8("WoRP_of_MaxsBR_PS_Frame"))
     
        self.PointsBR_PS_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.PointsBR_PS_Frame.setObjectName(_fromUtf8("PointsBR_PS_Frame"))
     
        self.WoLP_of_MaxsBR_PS_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_MaxsBR_PS_Frame.setObjectName(_fromUtf8("WoLP_of_MaxsBR_PS_Frame"))
                
        self.Level_of_MaxsBR_PS_Frame = Qt.QFrame(self.Min_Max_Setting_GroupBox)
        self.Level_of_MaxsBR_PS_Frame.setObjectName(_fromUtf8("Level_of_MaxsBR_PS_Frame"))

        self.PointsBR_PS_HLayout = Qt.QHBoxLayout(self.PointsBR_PS_Frame)
        self.PointsBR_PS_HLayout.setContentsMargins(0, 0, 0, 0)
        self.PointsBR_PS_HLayout.setSpacing(2)
        self.PointsBR_PS_HLayout.setObjectName(_fromUtf8("PointsBR_PS_HLayout"))
        
        self.PointsBR_PS_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.PointsBR_PS_CheckBox.setMinimumWidth(130)
        self.PointsBR_PS_CheckBox.setObjectName(_fromUtf8("PointsBR_PS_CheckBox"))
        
        self.PointsBR_PS_HLayout.addWidget(self.PointsBR_PS_CheckBox)
        
        self.PointsBR_Colon_PS_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.PointsBR_Colon_PS_Label.setObjectName(_fromUtf8("PointsBR_Colon_PS_Label"))
        
        self.PointsBR_PS_HLayout.addWidget(self.PointsBR_Colon_PS_Label)
        
        self.PointsBR_PS_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.PointsBR_PS_LineEdit.setMaximumWidth(54)
        self.PointsBR_PS_LineEdit.setObjectName(_fromUtf8("PointsBR_PS_LineEdit"))
        
        self.PointsBR_PS_HLayout.addWidget(self.PointsBR_PS_LineEdit)
        self.WoRP_of_MaxsBR_PS_HLayout = Qt.QHBoxLayout(self.WoRP_of_MaxsBR_PS_Frame)
        self.WoRP_of_MaxsBR_PS_HLayout.setContentsMargins(0, 0, 0, 0)
        self.WoRP_of_MaxsBR_PS_HLayout.setSpacing(2)
        self.WoRP_of_MaxsBR_PS_HLayout.setObjectName(_fromUtf8("WoRP_of_MaxsBR_PS_HLayout"))
        
        self.WoRP_of_MaxsBR_PS_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_MaxsBR_PS_CheckBox.setMinimumWidth(130)
        self.WoRP_of_MaxsBR_PS_CheckBox.setObjectName(_fromUtf8("WoRP_of_MaxsBR_PS_CheckBox"))
        
        self.WoRP_of_MaxsBR_PS_HLayout.addWidget(self.WoRP_of_MaxsBR_PS_CheckBox)
        
        self.WoRP_of_MaxsBR_Colon_PS_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_MaxsBR_Colon_PS_Label.setObjectName(_fromUtf8("WoRP_of_MaxsBR_Colon_PS_Label"))
        
        self.WoRP_of_MaxsBR_PS_HLayout.addWidget(self.WoRP_of_MaxsBR_Colon_PS_Label)
        
        self.WoRP_of_MaxsBR_PS_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.WoRP_of_MaxsBR_PS_LineEdit.setMaximumWidth(54)
        self.WoRP_of_MaxsBR_PS_LineEdit.setObjectName(_fromUtf8("WoRP_of_MaxsBR_PS_LineEdit"))
        
        self.WoRP_of_MaxsBR_PS_HLayout.addWidget(self.WoRP_of_MaxsBR_PS_LineEdit)

        self.WoLP_of_MaxsBR_PS_HLayout = Qt.QHBoxLayout(self.WoLP_of_MaxsBR_PS_Frame)
        self.WoLP_of_MaxsBR_PS_HLayout.setContentsMargins(0, 0, 0, 0)
        self.WoLP_of_MaxsBR_PS_HLayout.setSpacing(2)
        self.WoLP_of_MaxsBR_PS_HLayout.setObjectName(_fromUtf8("WoLP_of_MaxsBR_PS_HLayout"))
        
        self.WoLP_of_MaxsBR_PS_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_MaxsBR_PS_CheckBox.setMinimumWidth(130)
        self.WoLP_of_MaxsBR_PS_CheckBox.setObjectName(_fromUtf8("WoLP_of_MaxsBR_PS_CheckBox"))
        
        self.WoLP_of_MaxsBR_PS_HLayout.addWidget(self.WoLP_of_MaxsBR_PS_CheckBox)
        
        self.WoLP_of_MaxsBR_Colon_PS_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_MaxsBR_Colon_PS_Label.setObjectName(_fromUtf8("WoLP_of_MaxsBR_Colon_PS_Label"))
        
        self.WoLP_of_MaxsBR_PS_HLayout.addWidget(self.WoLP_of_MaxsBR_Colon_PS_Label)
        
        self.WoLP_of_MaxsBR_PS_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.WoLP_of_MaxsBR_PS_LineEdit.setMaximumWidth(54)
        self.WoLP_of_MaxsBR_PS_LineEdit.setObjectName(_fromUtf8("WoLP_of_MaxsBR_PS_LineEdit"))
        
        self.WoLP_of_MaxsBR_PS_HLayout.addWidget(self.WoLP_of_MaxsBR_PS_LineEdit)

        self.Level_of_MaxsBR_PS_HLayout = Qt.QHBoxLayout(self.Level_of_MaxsBR_PS_Frame)
        self.Level_of_MaxsBR_PS_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Level_of_MaxsBR_PS_HLayout.setSpacing(2)
        self.Level_of_MaxsBR_PS_HLayout.setObjectName(_fromUtf8("Level_of_MaxsBR_PS_HLayout"))
        
        self.Level_of_MaxsBR_PS_CheckBox = Qt.QCheckBox(self.Min_Max_Setting_GroupBox)
        self.Level_of_MaxsBR_PS_CheckBox.setMinimumWidth(130)
        self.Level_of_MaxsBR_PS_CheckBox.setObjectName(_fromUtf8("Level_of_MaxsBR_PS_CheckBox"))
        
        self.Level_of_MaxsBR_PS_HLayout.addWidget(self.Level_of_MaxsBR_PS_CheckBox)
        
        self.Level_of_MaxsBR_Colon_PS_Label = Qt.QLabel(self.Min_Max_Setting_GroupBox)
        self.Level_of_MaxsBR_Colon_PS_Label.setObjectName(_fromUtf8("Level_of_MaxsBR_Colon_PS_Label"))
        
        self.Level_of_MaxsBR_PS_HLayout.addWidget(self.Level_of_MaxsBR_Colon_PS_Label)
        
        self.Level_of_MaxsBR_PS_LineEdit = Qt.QLineEdit(self.Min_Max_Setting_GroupBox)
        self.Level_of_MaxsBR_PS_LineEdit.setMaximumWidth(54)
        self.Level_of_MaxsBR_PS_LineEdit.setObjectName(_fromUtf8("Level_of_MaxsBR_PS_LineEdit"))
        
        self.Level_of_MaxsBR_PS_HLayout.addWidget(self.Level_of_MaxsBR_PS_LineEdit)
        """ End of Setting Widgets for Maximum Brightness of Pulsating Star"""
        
        self.Find_Region_Button = Qt.QPushButton(self.Min_Max_Setting_GroupBox)
        self.Find_Region_Button.setObjectName(_fromUtf8("Find_Region_Button"))
        
        self.RLFrame_VLayout.addWidget(self.Min_Max_Setting_GroupBox)
        
        self.Methods_GroupBox = Qt.QGroupBox(self.RLFrame)
        self.Methods_GroupBox.setStyleSheet(XM.groupBoxStyle)
        self.Methods_GroupBox.setObjectName(_fromUtf8("Methods_GroupBox"))
        
        self.Methods_GroupBox_VLayout = Qt.QVBoxLayout(self.Methods_GroupBox)
        self.Methods_GroupBox_VLayout.setObjectName(_fromUtf8("Methods_GroupBox_VLayout"))
        
        self.Methods_1Min_HLLine = Qt.QFrame(self.Methods_GroupBox)
        self.Methods_1Min_HLLine.setObjectName(_fromUtf8("Methods_1Min_HLLine"))
        self.Methods_1Min_HLLine.setFrameShape(Qt.QFrame.HLine)
        
        self.Methods_1Min_HLayout = Qt.QHBoxLayout()
        self.Methods_1Min_HLayout.setObjectName(_fromUtf8("Methods_1Min_HLayout"))
        self.Methods_1Min_HLayout.addWidget(self.Methods_1Min_HLLine)
        
        self.Methods_1Min_Label = Qt.QLabel(self.Methods_GroupBox)
        self.Methods_1Min_Label.setObjectName(_fromUtf8("Methods_1Min_Label"))
        self.Methods_1Min_Label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.Methods_1Min_HLayout.addWidget(self.Methods_1Min_Label) 
        
        self.Methods_1Min_HRLine = Qt.QFrame(self.Methods_GroupBox)
        self.Methods_1Min_HRLine.setObjectName(_fromUtf8("Methods_1Min_HRLine"))
        self.Methods_1Min_HRLine.setFrameShape(Qt.QFrame.HLine)

        self.Methods_1Min_HLayout.addWidget(self.Methods_1Min_HRLine)
        
        self.Methods_GroupBox_VLayout.addLayout(self.Methods_1Min_HLayout)
        
        self.Methods_ComboBox1 = Qt.QComboBox(self.Methods_GroupBox)
        self.Methods_ComboBox1.setObjectName(_fromUtf8("Methods_ComboBox1"))
        self.Methods_ComboBox1.addItem(_fromUtf8(""))
        self.Methods_ComboBox1.addItem(_fromUtf8(""))
        self.Methods_ComboBox1.addItem(_fromUtf8(""))
        self.Methods_ComboBox1.addItem(_fromUtf8(""))
        self.Methods_ComboBox1.addItem(_fromUtf8(""))
        #self.Methods_ComboBox1.model().item(3).setEnabled(False)
        #self.Methods_ComboBox1.model().item(4).setEnabled(False)
        
        self.Methods_GroupBox_VLayout.addWidget(self.Methods_ComboBox1)
        
        self.Degree_of_Polynom_Label1 = Qt.QLabel(self.Methods_GroupBox)
        self.Degree_of_Polynom_Label1.setObjectName(_fromUtf8("Degree_of_Polynom_Label1"))
        
        self.Degree_of_Polynom_LineEdit1 = Qt.QLineEdit(self.Methods_GroupBox)
        self.Degree_of_Polynom_LineEdit1.setText('2')
        self.Degree_of_Polynom_LineEdit1.setObjectName(_fromUtf8("Degree_of_Polynom_LineEdit1"))
        self.Degree_of_Polynom_LineEdit1.setFixedSize(QtCore.QSize(27,23))
        
        self.Degree_of_Polynom_Frame1 = Qt.QFrame(self.Methods_GroupBox)
        self.Degree_of_Polynom_Frame1.setObjectName(_fromUtf8("Degree_of_Polynom_Frame1"))
        self.Degree_of_Polynom_Frame1.setFrameShape(Qt.QFrame.NoFrame)
        self.Degree_of_Polynom_Frame1.setMaximumHeight(23)
        self.Degree_of_Polynom_Frame1.hide()
        
        self.Degree_of_Polynom_HLayout1 = Qt.QHBoxLayout(self.Degree_of_Polynom_Frame1)
        self.Degree_of_Polynom_HLayout1.setObjectName(_fromUtf8("Degree_of_Polynom_HLayout1"))
        self.Degree_of_Polynom_HLayout1.setContentsMargins(0, 0, 0, 0)
        
        self.Degree_of_Polynom_LSpacer1 = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum) 
        self.Degree_of_Polynom_HLayout1.addItem(self.Degree_of_Polynom_LSpacer1)
        
        self.Degree_of_Polynom_HLayout1.addWidget(self.Degree_of_Polynom_Label1)
        
        self.Degree_of_Polynom_MSpacer1 = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum) 
        self.Degree_of_Polynom_HLayout1.addItem(self.Degree_of_Polynom_MSpacer1)
        
        self.Degree_of_Polynom_HLayout1.addWidget(self.Degree_of_Polynom_LineEdit1)
        
        self.Degree_of_Polynom_RSpacer1 = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum) 
        self.Degree_of_Polynom_HLayout1.addItem(self.Degree_of_Polynom_RSpacer1)
        
        self.Methods_GroupBox_VLayout.addWidget(self.Degree_of_Polynom_Frame1)
        
        self.Methods_HLine = Qt.QFrame(self.Methods_GroupBox)
        self.Methods_HLine.setObjectName(_fromUtf8("Methods_HLine"))
        self.Methods_HLine.setFrameShape(Qt.QFrame.HLine)

        self.Methods_GroupBox_VLayout.addWidget(self.Methods_HLine)
        
        self.Methods_2Min_HLLine = Qt.QFrame(self.Methods_GroupBox)
        self.Methods_2Min_HLLine.setObjectName(_fromUtf8("Methods_2Min_HLLine"))
        self.Methods_2Min_HLLine.setFrameShape(Qt.QFrame.HLine)

        self.Methods_2Min_HLayout = Qt.QHBoxLayout()
        self.Methods_2Min_HLayout.setObjectName(_fromUtf8("Methods_2Min_HLayout"))
        self.Methods_2Min_HLayout.addWidget(self.Methods_2Min_HLLine)
        
        self.Methods_2Min_Label = Qt.QLabel(self.Methods_GroupBox)
        self.Methods_2Min_Label.setObjectName(_fromUtf8("Methods_2Min_Label"))
        self.Methods_2Min_Label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.Methods_2Min_HLayout.addWidget(self.Methods_2Min_Label) 
        
        self.Methods_2Min_HRLine = Qt.QFrame(self.Methods_GroupBox)
        self.Methods_2Min_HRLine.setObjectName(_fromUtf8("Methods_2Min_HRLine"))
        self.Methods_2Min_HRLine.setFrameShape(Qt.QFrame.HLine)
        
        self.Methods_2Min_HLayout.addWidget(self.Methods_2Min_HRLine)
        
        self.Methods_GroupBox_VLayout.addLayout(self.Methods_2Min_HLayout)
        
        self.Methods_ComboBox2 = Qt.QComboBox(self.Methods_GroupBox)
        self.Methods_ComboBox2.setObjectName(_fromUtf8("Methods_ComboBox2"))
        self.Methods_ComboBox2.addItem(_fromUtf8(""))
        self.Methods_ComboBox2.addItem(_fromUtf8(""))
        self.Methods_ComboBox2.addItem(_fromUtf8(""))
        self.Methods_ComboBox2.addItem(_fromUtf8(""))
        self.Methods_ComboBox2.addItem(_fromUtf8(""))
        #self.Methods_ComboBox2.model().item(3).setEnabled(False)
        #self.Methods_ComboBox2.model().item(4).setEnabled(False)
        
        self.Methods_GroupBox_VLayout.addWidget(self.Methods_ComboBox2)
        
        self.Degree_of_Polynom_Label2 = Qt.QLabel(self.Methods_GroupBox)
        self.Degree_of_Polynom_Label2.setObjectName(_fromUtf8("Degree_of_Polynom_Label1"))
        
        self.Degree_of_Polynom_LineEdit2 = Qt.QLineEdit(self.Methods_GroupBox)
        self.Degree_of_Polynom_LineEdit2.setText('2')
        self.Degree_of_Polynom_LineEdit2.setObjectName(_fromUtf8("Degree_of_Polynom_LineEdit2"))
        self.Degree_of_Polynom_LineEdit2.setFixedSize(QtCore.QSize(27,23))
        
        self.Degree_of_Polynom_Frame2 = Qt.QFrame(self.Methods_GroupBox)
        self.Degree_of_Polynom_Frame2.setObjectName(_fromUtf8("Degree_of_Polynom_Frame2"))
        self.Degree_of_Polynom_Frame2.setMaximumHeight(23)
        self.Degree_of_Polynom_Frame2.setFrameShape(Qt.QFrame.NoFrame)
        self.Degree_of_Polynom_Frame2.hide()
        
        self.Degree_of_Polynom_HLayout2 = Qt.QHBoxLayout(self.Degree_of_Polynom_Frame2)
        self.Degree_of_Polynom_HLayout2.setObjectName(_fromUtf8("Degree_of_Polynom_HLayout2"))
        self.Degree_of_Polynom_HLayout2.setContentsMargins(0, 0, 0, 0)
        
        self.Degree_of_Polynom_LSpacer2 = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum) 
        self.Degree_of_Polynom_HLayout2.addItem(self.Degree_of_Polynom_LSpacer2)
        
        self.Degree_of_Polynom_HLayout2.addWidget(self.Degree_of_Polynom_Label2)
        
        self.Degree_of_Polynom_MSpacer2 = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum) 
        self.Degree_of_Polynom_HLayout2.addItem(self.Degree_of_Polynom_MSpacer2)
        
        self.Degree_of_Polynom_HLayout2.addWidget(self.Degree_of_Polynom_LineEdit2)
        
        self.Degree_of_Polynom_RSpacer2 = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum) 
        self.Degree_of_Polynom_HLayout2.addItem(self.Degree_of_Polynom_RSpacer2)
        
        self.Methods_GroupBox_VLayout.addWidget(self.Degree_of_Polynom_Frame2)
        
        self.RLFrame_VLayout.addWidget(self.Methods_GroupBox)
        
        self.Calculate_Min_Max_Button = Qt.QPushButton(self.RLFrame)
        self.Calculate_Min_Max_Button.setObjectName(_fromUtf8("Calculate_Min_Max_Button"))
        
        self.RLFrame_VLayout.addWidget(self.Calculate_Min_Max_Button)
        
        self.WoRP_of_1Maxs_Frame.hide()
        self.WoLP_of_1Maxs_Frame.hide()
        self.WoRP_of_2Maxs_Frame.hide()
        self.WoLP_of_2Maxs_Frame.hide()
        self.Points_1Maxs_Frame.hide()
        self.Points_2Maxs_Frame.hide()
        self.Level_of_1Maxs_Frame.hide()
        self.Level_of_2Maxs_Frame.hide()
        
        self.WoRP_of_MaxsBR_PS_Frame.hide()
        self.PointsBR_PS_Frame.hide()
        self.WoLP_of_MaxsBR_PS_Frame.hide()
        self.Level_of_MaxsBR_PS_Frame.hide()
        
        self.ToVS = XM.ui.OD.ToVS_ComboBox.currentIndex()
        if self.ToVS == 0:
            self.Extremum_ComboBox.model().item(1).setEnabled(False)
            
            self.Stack_PS_Frame.hide()
            self.Points_PS_Frame.hide()
            self.WoRP_of_Maxs_PS_Frame.hide()
            self.WoLP_of_Maxs_PS_Frame.hide()
            self.Level_of_Maxs_PS_Frame.hide()
            
            
            self.Methods_1Min_HLLine.show()
            self.Methods_1Min_Label.show()
            self.Methods_1Min_HRLine.show()
            self.Methods_HLine.show()
            self.Methods_2Min_HLLine.show()
            self.Methods_2Min_Label.show()
            self.Methods_2Min_HRLine.show()
            self.Methods_ComboBox2.show()
            
            self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Stack_Frame)
            self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Points_1Mins_Frame)
            self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Points_2Mins_Frame)
            self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoRP_of_1Mins_Frame)
            self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoLP_of_1Mins_Frame)
            self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoRP_of_2Mins_Frame)
            self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoLP_of_2Mins_Frame)
            self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Level_of_1Mins_Frame)
            self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Level_of_2Mins_Frame)
            self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Find_Region_Button)
        
        else:
            self.Extremum_ComboBox.model().item(0).setEnabled(False)
            
            self.Stack_Frame.hide()
            self.Points_1Mins_Frame.hide()
            self.Points_2Mins_Frame.hide()
            self.WoRP_of_1Mins_Frame.hide()
            self.WoLP_of_1Mins_Frame.hide()
            self.WoRP_of_2Mins_Frame.hide()
            self.WoLP_of_2Mins_Frame.hide()
            self.Level_of_1Mins_Frame.hide()
            self.Level_of_2Mins_Frame.hide()
            #self.Find_Region_Button.hide()
            
            self.Methods_1Min_HLLine.hide()
            self.Methods_1Min_Label.hide()
            self.Methods_1Min_HRLine.hide()
            self.Methods_HLine.hide()
            self.Methods_2Min_HLLine.hide()
            self.Methods_2Min_Label.hide()
            self.Methods_2Min_HRLine.hide()
            self.Methods_ComboBox2.hide()
            
            self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Stack_PS_Frame)
            self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Points_PS_Frame)
            self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoRP_of_Maxs_PS_Frame)
            self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoLP_of_Maxs_PS_Frame)
            self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Level_of_Maxs_PS_Frame)
            self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Find_Region_Button)
            
            self.Degree_of_Polynom_Frame2.hide()
            self.Extremum_ComboBox.setCurrentIndex(1)
        
        
        self.ProgressBar = Qt.QProgressBar(self.RLFrame)
        self.ProgressBar.setMinimumHeight(40)
        self.ProgressBar.setObjectName(_fromUtf8("ProgressBar"))
        self.ProgressBar.setVisible(False)
        self.ProgressBar.setTextVisible(False)
        
        self.ProgressBar_Label = Qt.QLabel()
        self.ProgressBar_Label.setWordWrap(True)
        self.ProgressBar_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.ProgressBar_Label.setObjectName(_fromUtf8("ProgressBar_Label"))
        
        self.ProgressBar_GLayout = Qt.QGridLayout()
        self.ProgressBar_GLayout.setObjectName(_fromUtf8("ProgressBar_GLayout"))
        
        self.ProgressBar_GLayout.addWidget(self.ProgressBar,0,0)
        self.ProgressBar_GLayout.addWidget(self.ProgressBar_Label,0,0)
        
        self.RLFrame_SpacerItem = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Minimum, Qt.QSizePolicy.Expanding) 
        self.RLFrame_VLayout.addItem(self.RLFrame_SpacerItem)
        
        self.RLFrame_VLayout.addLayout(self.ProgressBar_GLayout)
        
        self.RRFrame = Qt.QFrame(self.Table_Splitter)
        self.RRFrame.setObjectName(_fromUtf8("RRFrame"))
        
        self.RRFrame_VLayout = Qt.QVBoxLayout(self.RRFrame)
        self.RRFrame_VLayout.setContentsMargins(0, 0, 0, 0)
        self.RRFrame_VLayout.setObjectName(_fromUtf8("RRFrame_VLayout"))
        
        self.Min_Max_Table = Qt.QTableWidget(self.RRFrame)
        self.Min_Max_Table.setSortingEnabled(True)
        self.Min_Max_Table.setObjectName(_fromUtf8("Min_Max_Table"))
        self.Min_Max_Table.setColumnCount(3)
        self.Min_Max_Table.setRowCount(0)
        item = Qt.QTableWidgetItem()
        self.Min_Max_Table.setHorizontalHeaderItem(0, item)
        item = Qt.QTableWidgetItem()
        self.Min_Max_Table.setHorizontalHeaderItem(1, item)
        item = Qt.QTableWidgetItem()
        self.Min_Max_Table.setHorizontalHeaderItem(2, item)
        self.Min_Max_Table.setColumnWidth(0,85)
        self.Min_Max_Table.setColumnWidth(1,33)
        self.Min_Max_Table.horizontalHeader().setStretchLastSection(True)
        
        self.RRFrame_VLayout.addWidget(self.Min_Max_Table)
        
        self.RRFrame_Button_HLayout = Qt.QHBoxLayout()
        self.RRFrame_Button_HLayout.setObjectName(_fromUtf8("RRFrame_Button_HLayout"))
        
        self.Save_Min_Max_Time_Button = Qt.QPushButton(self.RRFrame)
        self.Save_Min_Max_Time_Button.setObjectName(_fromUtf8("Save_Min_Max_Time_Button"))
        
        self.RRFrame_Button_HLayout.addWidget(self.Save_Min_Max_Time_Button)
        
        self.Show_O_C_Button = Qt.QPushButton(self.RRFrame)
        self.Show_O_C_Button.setObjectName(_fromUtf8("Show_O_C_Button"))
        
        self.RRFrame_Button_HLayout.addWidget(self.Show_O_C_Button)
        
        self.RRFrame_VLayout.addLayout(self.RRFrame_Button_HLayout)
        
        self.RFrame_HLayout.addWidget(self.Table_Splitter)
        
        self.Main_HLayout.addWidget(self.Graph_Splitter)
        
        MinMax_Window.setCentralWidget(self.centralwidget)
        
        self.Calculate_Min_Max_Button.setEnabled(False)
        self.Save_Min_Max_Time_Button.setEnabled(False)
        self.Show_O_C_Button.setEnabled(False)
        self.Min_Max_Region_Button.setEnabled(False)
        
        self.statusbar = Qt.QStatusBar(MinMax_Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MinMax_Window.setStatusBar(self.statusbar)
        from plotpy.plot import PlotDialog
        self.Graph_Win = PlotDialog(edit=False, toolbar=True)
        from plotpy.tools import HCursorTool
        self.Graph_Win.manager.add_tool(HCursorTool)
        self.Graph_Plot = self.Graph_Win.get_plot()
        self.Graph_Toolbar = self.Graph_Win.get_toolbar()        
        self.Graph_Icons  = self.Graph_Toolbar.actions()
        self.Graph_Icons[7].setVisible(False)
        self.Graph_Icons[8].setVisible(False)
        self.Graph_HLayout  = Qt.QHBoxLayout(self.Graph_Frame)
        self.Graph_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Graph_HLayout.addWidget(self.Graph_Win)
        
        self.Table_Splitter.splitterMoved.connect(self.TableHeader_Resize)
        self.Select_Min_Max_Region_CheckBox.clicked.connect(self.Manuel_Selection)
        self.Methods_ComboBox1.currentIndexChanged.connect(self.DoP_Widget1)
        self.Methods_ComboBox2.currentIndexChanged.connect(self.DoP_Widget2)
        self.Methods_ComboBox1.currentIndexChanged.connect(self.SpecialFunc)
        self.Methods_ComboBox2.currentIndexChanged.connect(self.SpecialFunc)
        self.Extremum_ComboBox.currentIndexChanged.connect(self.Update_Settings)
        #self.Extremum_ComboBox.currentIndexChanged.connect(self.LCurve)
        
        self.Calculate_Min_Max_Button.clicked.connect(self.Calculate)
        self.Min_Max_Region_Button.clicked.connect(self.Show_Region)
        self.Find_Region_Button.clicked.connect(self.Find_Region)
        self.Light_Curve_Button.clicked.connect(self.LCurve)
        self.Show_O_C_Button.clicked.connect(self.Show_OC)
        self.Save_Min_Max_Time_Button.clicked.connect(self.Save)
        self.Graph_Plot.mouseReleaseEvent = self.Graph_Event
        
        
        self.Stack_CheckBox.setChecked(True)
        self.Points_1Mins_CheckBox.setChecked(True)
        self.Points_2Mins_CheckBox.setChecked(True)
        self.WoRP_of_1Mins_CheckBox.setChecked(True)
        self.WoLP_of_1Mins_CheckBox.setChecked(True)
        self.WoRP_of_2Mins_CheckBox.setChecked(True)
        self.WoLP_of_2Mins_CheckBox.setChecked(True)
        self.Level_of_1Mins_CheckBox.setChecked(True)
        self.Level_of_2Mins_CheckBox.setChecked(True)
        
        self.Points_1Maxs_CheckBox.setChecked(True)
        self.Points_2Maxs_CheckBox.setChecked(True)
        self.WoRP_of_1Maxs_CheckBox.setChecked(True)
        self.WoLP_of_1Maxs_CheckBox.setChecked(True)
        self.WoRP_of_2Maxs_CheckBox.setChecked(True)
        self.WoLP_of_2Maxs_CheckBox.setChecked(True)
        self.Level_of_1Maxs_CheckBox.setChecked(True)
        self.Level_of_2Maxs_CheckBox.setChecked(True)
        
        self.Stack_PS_CheckBox.setChecked(True)
        self.Points_PS_CheckBox.setChecked(True)
        self.WoRP_of_Maxs_PS_CheckBox.setChecked(True)
        self.WoLP_of_Maxs_PS_CheckBox.setChecked(True)
        self.Level_of_Maxs_PS_CheckBox.setChecked(True)
        
        self.PointsBR_PS_CheckBox.setChecked(True)
        self.WoRP_of_MaxsBR_PS_CheckBox.setChecked(True)
        self.WoLP_of_MaxsBR_PS_CheckBox.setChecked(True)
        self.Level_of_MaxsBR_PS_CheckBox.setChecked(True)
        
        
        self.Stack_CheckBox.clicked.connect(lambda x: self.Stack_LineEdit.setEnabled(True) 
                    if self.Stack_CheckBox.isChecked() == True \
                    else (self.Stack_LineEdit.setEnabled(False), self.Stack_LineEdit.setText('1')))
        self.WoRP_of_1Mins_CheckBox.clicked.connect(lambda x: self.WoRP_of_1Mins_LineEdit.setEnabled(True) 
                    if self.WoRP_of_1Mins_CheckBox.isChecked() == True \
                    else (self.WoRP_of_1Mins_LineEdit.setEnabled(False), self.WoRP_of_1Mins_LineEdit.setText('4')))
        self.WoLP_of_1Mins_CheckBox.clicked.connect(lambda x: self.WoLP_of_1Mins_LineEdit.setEnabled(True) 
                    if self.WoLP_of_1Mins_CheckBox.isChecked() == True \
                    else (self.WoLP_of_1Mins_LineEdit.setEnabled(False), self.WoLP_of_1Mins_LineEdit.setText('4')))
        self.WoRP_of_2Mins_CheckBox.clicked.connect(lambda x: self.WoRP_of_2Mins_LineEdit.setEnabled(True) 
                    if self.WoRP_of_2Mins_CheckBox.isChecked() == True \
                    else (self.WoRP_of_2Mins_LineEdit.setEnabled(False), self.WoRP_of_2Mins_LineEdit.setText('4')))
        self.WoLP_of_2Mins_CheckBox.clicked.connect(lambda x: self.WoLP_of_2Mins_LineEdit.setEnabled(True) 
                    if self.WoLP_of_2Mins_CheckBox.isChecked() == True \
                    else (self.WoLP_of_2Mins_LineEdit.setEnabled(False), self.WoLP_of_2Mins_LineEdit.setText('4')))
        self.Level_of_1Mins_CheckBox.clicked.connect(lambda x: self.Level_of_1Mins_LineEdit.setEnabled(True) 
                    if self.Level_of_1Mins_CheckBox.isChecked() == True \
                    else self.Level_of_1Mins_LineEdit.setEnabled(False))
        self.Level_of_2Mins_CheckBox.clicked.connect(lambda x: self.Level_of_2Mins_LineEdit.setEnabled(True) 
                    if self.Level_of_2Mins_CheckBox.isChecked() == True \
                    else self.Level_of_2Mins_LineEdit.setEnabled(False))
        

        self.WoRP_of_1Maxs_CheckBox.clicked.connect(lambda x: self.WoRP_of_1Maxs_LineEdit.setEnabled(True) 
                    if self.WoRP_of_1Maxs_CheckBox.isChecked() == True \
                    else (self.WoRP_of_1Maxs_LineEdit.setEnabled(False), self.WoRP_of_1Maxs_LineEdit.setText('4')))
        self.WoLP_of_1Maxs_CheckBox.clicked.connect(lambda x: self.WoLP_of_1Maxs_LineEdit.setEnabled(True) 
                    if self.WoLP_of_1Maxs_CheckBox.isChecked() == True \
                    else (self.WoLP_of_1Maxs_LineEdit.setEnabled(False), self.WoLP_of_1Maxs_LineEdit.setText('4')))
        self.WoRP_of_2Maxs_CheckBox.clicked.connect(lambda x: self.WoRP_of_2Maxs_LineEdit.setEnabled(True) 
                    if self.WoRP_of_2Maxs_CheckBox.isChecked() == True \
                    else (self.WoRP_of_2Maxs_LineEdit.setEnabled(False), self.WoRP_of_2Maxs_LineEdit.setText('4')))
        self.WoLP_of_2Maxs_CheckBox.clicked.connect(lambda x: self.WoLP_of_2Maxs_LineEdit.setEnabled(True) 
                    if self.WoLP_of_2Maxs_CheckBox.isChecked() == True \
                    else (self.WoLP_of_2Maxs_LineEdit.setEnabled(False), self.WoLP_of_2Maxs_LineEdit.setText('4')))
        self.Level_of_1Maxs_CheckBox.clicked.connect(lambda x: self.Level_of_1Maxs_LineEdit.setEnabled(True) 
                    if self.Level_of_1Maxs_CheckBox.isChecked() == True \
                    else self.Level_of_1Maxs_LineEdit.setEnabled(False))
        self.Level_of_2Maxs_CheckBox.clicked.connect(lambda x: self.Level_of_2Maxs_LineEdit.setEnabled(True) 
                    if self.Level_of_2Maxs_CheckBox.isChecked() == True \
                    else self.Level_of_2Maxs_LineEdit.setEnabled(False))
                    
        
        self.Stack_PS_CheckBox.clicked.connect(lambda x: self.Stack_PS_LineEdit.setEnabled(True) 
                    if self.Stack_PS_CheckBox.isChecked() == True \
                    else (self.Stack_PS_LineEdit.setEnabled(False), self.Stack_PS_LineEdit.setText('1')))
        self.WoRP_of_Maxs_PS_CheckBox.clicked.connect(lambda x: self.WoRP_of_Maxs_PS_LineEdit.setEnabled(True) 
                    if self.WoRP_of_Maxs_PS_CheckBox.isChecked() == True \
                    else (self.WoRP_of_Maxs_PS_LineEdit.setEnabled(False), self.WoRP_of_Maxs_PS_LineEdit.setText('2')))
        self.WoLP_of_Maxs_PS_CheckBox.clicked.connect(lambda x: self.WoLP_of_Maxs_PS_LineEdit.setEnabled(True) 
                    if self.WoLP_of_Maxs_PS_CheckBox.isChecked() == True \
                    else (self.WoLP_of_Maxs_PS_LineEdit.setEnabled(False), self.WoLP_of_Maxs_PS_LineEdit.setText('2')))
        self.Level_of_Maxs_PS_CheckBox.clicked.connect(lambda x: self.Level_of_Maxs_PS_LineEdit.setEnabled(True) 
                    if self.Level_of_Maxs_PS_CheckBox.isChecked() == True \
                    else self.Level_of_Maxs_PS_LineEdit.setEnabled(False))
        
        self.WoRP_of_MaxsBR_PS_CheckBox.clicked.connect(lambda x: self.WoRP_of_MaxsBR_PS_LineEdit.setEnabled(True) 
                    if self.WoRP_of_MaxsBR_PS_CheckBox.isChecked() == True \
                    else (self.WoRP_of_MaxsBR_PS_LineEdit.setEnabled(False), self.WoRP_of_MaxsBR_PS_LineEdit.setText('2')))
        self.WoLP_of_MaxsBR_PS_CheckBox.clicked.connect(lambda x: self.WoLP_of_MaxsBR_PS_LineEdit.setEnabled(True) 
                    if self.WoLP_of_MaxsBR_PS_CheckBox.isChecked() == True \
                    else (self.WoLP_of_MaxsBR_PS_LineEdit.setEnabled(False), self.WoLP_of_MaxsBR_PS_LineEdit.setText('2')))
        self.Level_of_MaxsBR_PS_CheckBox.clicked.connect(lambda x: self.Level_of_MaxsBR_PS_LineEdit.setEnabled(True) 
                    if self.Level_of_MaxsBR_PS_CheckBox.isChecked() == True \
                    else self.Level_of_MaxsBR_PS_LineEdit.setEnabled(False))
        
        self.retranslateUi(MinMax_Window)
        QtCore.QMetaObject.connectSlotsByName(MinMax_Window)

    def retranslateUi(self, MinMax_Window):
        MinMax_Window.setWindowTitle(_translate("MinMax_Window", "Extrema Window", None))
        self.Light_Curve_Button.setText(_translate("MinMax_Window", "Light Curve(s)", None))
        self.Min_Max_Region_Button.setText(_translate("MinMax_Window", "Extremum Region(s)", None))
        self.Select_Min_Max_Region_Label.setText(_translate("MinMax_Window", "Select Extremum Region(s) Manually on the Plot", None))
        self.Select_Min_Max_Region_Label.setWordWrap(True)
        self.Show_Min_Max_PointorCurve_Label.setText(_translate("MinMax_Window", "Display Extremum Point(s) and/or Model(s) on the Plot", None))
        self.Show_Min_Max_PointorCurve_Label.setWordWrap(True)
        self.Extremum_GroupBox.setTitle(_translate("MinMax_Window", "Extremum Type", None))
        self.Extremum_ComboBox.setItemText(0, _translate("MinMax_Window", "Minimum Time", None))
        self.Extremum_ComboBox.setItemText(1, _translate("MinMax_Window", "Maximum Time", None))
        self.Extremum_ComboBox.setItemText(2, _translate("MinMax_Window", "Maximum Brightness", None))
        self.Min_Max_Setting_GroupBox.setTitle(_translate("MinMax_Window", "Extremum Region(s) Settings", None))
        self.Stack_CheckBox.setText(_translate("MinMax_Window", "Stack", None))
        self.Stack_Label.setText(_translate("MinMax_Window", ":", None))
        
        self.Points_1Mins_CheckBox.setText(_translate("MinMax_Window", "Points 1. Mins", None))
        self.Points_1Mins_Label.setText(_translate("MinMax_Window", ":", None))
        self.Points_1Maxs_CheckBox.setText(_translate("MinMax_Window", "Points 1. Maxs", None))
        self.Points_1Maxs_Colon_Label.setText(_translate("MinMax_Window", ":", None))
        self.Points_2Mins_CheckBox.setText(_translate("MinMax_Window", "Points 2. Mins", None))
        self.Points_2Mins_Label.setText(_translate("MinMax_Window", ":", None))
        self.Points_2Maxs_CheckBox.setText(_translate("MinMax_Window", "Points 2. Maxs", None))
        self.Points_2Maxs_Colon_Label.setText(_translate("MinMax_Window", ":", None))
        
        self.PointsBR_PS_CheckBox.setText(_translate("MinMax_Window", "Points", None))
        self.PointsBR_Colon_PS_Label.setText(_translate("MinMax_Window", ":", None))
        
        self.Stack_CheckBox.setText(_translate("MinMax_Window", "Stack", None))
        self.Stack_Label.setText(_translate("MinMax_Window", ":", None))
        
        self.WoRP_of_1Mins_CheckBox.setText(_translate("MinMax_Window", "Width of RP of 1. Mins", None))
        self.WoRP_of_1Mins_Colon_Label.setText(_translate("MinMax_Window", ":", None))
        self.WoLP_of_1Mins_CheckBox.setText(_translate("MinMax_Window", "Width of LP of 1. Mins", None))
        self.WoLP_of_1Mins_Colon_Label.setText(_translate("MinMax_Window", ":", None))
        self.WoRP_of_2Mins_CheckBox.setText(_translate("MinMax_Window", "Width of RP of 2. Mins", None))
        self.WoRP_of_2Mins_Colon_Label.setText(_translate("MinMax_Window", ":", None))
        self.WoLP_of_2Mins_CheckBox.setText(_translate("MinMax_Window", "Width of LP of 2. Mins", None))
        self.WoLP_of_2Mins_Label.setText(_translate("MinMax_Window", ":", None))
        self.Level_of_1Mins_CheckBox.setText(_translate("MinMax_Window", "Level of 1. Mins", None))
        self.Level_of_1Mins_Label.setText(_translate("MinMax_Window", ":", None))
        self.Level_of_2Mins_CheckBox.setText(_translate("MinMax_Window", "Level of 2. Mins", None))
        self.Level_of_2Mins_Colon_Label.setText(_translate("MinMax_Window", ":", None))
        
        
        
        self.WoRP_of_1Maxs_CheckBox.setText(_translate("MinMax_Window", "Width of RP of 1. Maxs", None))
        self.WoRP_of_1Maxs_Colon_Label.setText(_translate("MinMax_Window", ":", None))
        self.WoLP_of_1Maxs_CheckBox.setText(_translate("MinMax_Window", "Width of LP of 1. Maxs", None))
        self.WoLP_of_1Maxs_Colon_Label.setText(_translate("MinMax_Window", ":", None))
        self.WoRP_of_2Maxs_CheckBox.setText(_translate("MinMax_Window", "Width of RP of 2. Maxs", None))
        self.WoRP_of_2Maxs_Colon_Label.setText(_translate("MinMax_Window", ":", None))
        self.WoLP_of_2Maxs_CheckBox.setText(_translate("MinMax_Window", "Width of LP of 2. Maxs", None))
        self.WoLP_of_2Maxs_Label.setText(_translate("MinMax_Window", ":", None))
        self.Level_of_1Maxs_CheckBox.setText(_translate("MinMax_Window", "Level of 1. Maxs", None))
        self.Level_of_1Maxs_Label.setText(_translate("MinMax_Window", ":", None))
        self.Level_of_2Maxs_CheckBox.setText(_translate("MinMax_Window", "Level of 2. Maxs", None))
        self.Level_of_2Maxs_Colon_Label.setText(_translate("MinMax_Window", ":", None))
        
        self.Stack_PS_CheckBox.setText(_translate("MinMax_Window", "Stack", None))
        self.Stack_PS_Label.setText(_translate("MinMax_Window", ":", None))
        self.Points_PS_CheckBox.setText(_translate("MinMax_Window", "Points", None))
        self.Points_PS_Label.setText(_translate("MinMax_Window", ":", None))
        self.WoRP_of_Maxs_PS_CheckBox.setText(_translate("MinMax_Window", "Width of RP of Maxs", None))
        self.WoRP_of_Maxs_Colon_PS_Label.setText(_translate("MinMax_Window", ":", None))
        self.WoLP_of_Maxs_PS_CheckBox.setText(_translate("MinMax_Window", "Width of LP of Maxs", None))
        self.WoLP_of_Maxs_Colon_PS_Label.setText(_translate("MinMax_Window", ":", None))
        self.Level_of_Maxs_PS_CheckBox.setText(_translate("MinMax_Window", "Level of Maxs", None))
        self.Level_of_Maxs_Colon_PS_Label.setText(_translate("MinMax_Window", ":", None))
        
        self.WoRP_of_MaxsBR_PS_CheckBox.setText(_translate("MinMax_Window", "Width of RP of Maxs", None))
        self.WoRP_of_MaxsBR_Colon_PS_Label.setText(_translate("MinMax_Window", ":", None))
        self.WoLP_of_MaxsBR_PS_CheckBox.setText(_translate("MinMax_Window", "Width of LP of Maxs", None))
        self.WoLP_of_MaxsBR_Colon_PS_Label.setText(_translate("MinMax_Window", ":", None))
        self.Level_of_MaxsBR_PS_CheckBox.setText(_translate("MinMax_Window", "Level of Maxs", None))
        self.Level_of_MaxsBR_Colon_PS_Label.setText(_translate("MinMax_Window", ":", None))
        
        self.Stack_LineEdit.setText(_translate("MinMax_Window", "1", None))
        self.Points_1Mins_LineEdit.setText(_translate("MinMax_Window", "1", None))
        self.Points_2Mins_LineEdit.setText(_translate("MinMax_Window", "1", None))
        self.WoRP_of_1Mins_LineEdit.setText(_translate("MinMax_Window", "4", None))
        self.WoLP_of_1Mins_LineEdit.setText(_translate("MinMax_Window", "4", None))
        self.WoRP_of_2Mins_LineEdit.setText(_translate("MinMax_Window", "4", None))
        self.WoLP_of_2Mins_LineEdit.setText(_translate("MinMax_Window", "4", None))
        #self.Level_of_1Mins_LineEdit.setText()
        #self.Level_of_2Mins_LineEdit.setText()
        self.Points_1Maxs_LineEdit.setText(_translate("MinMax_Window", "1", None))
        self.Points_2Maxs_LineEdit.setText(_translate("MinMax_Window", "1", None))
        self.WoRP_of_1Maxs_LineEdit.setText(_translate("MinMax_Window", "4", None))
        self.WoLP_of_1Maxs_LineEdit.setText(_translate("MinMax_Window", "4", None))
        self.WoRP_of_2Maxs_LineEdit.setText(_translate("MinMax_Window", "4", None))
        self.WoLP_of_2Maxs_LineEdit.setText(_translate("MinMax_Window", "4", None))
        #self.Level_of_1Maxs_LineEdit.setText()
        #self.Level_of_2Maxs_LineEdit.setText()
        
        self.Stack_PS_LineEdit.setText(_translate("MinMax_Window", "1", None))
        self.Points_PS_LineEdit.setText(_translate("MinMax_Window", "1", None))
        self.WoRP_of_Maxs_PS_LineEdit.setText(_translate("MinMax_Window", "2", None))
        self.WoLP_of_Maxs_PS_LineEdit.setText(_translate("MinMax_Window", "2", None))
        #self.Level_of_Maxs_PS_LineEdit.setText()
        
        self.PointsBR_PS_LineEdit.setText(_translate("MinMax_Window", "1", None))
        self.WoRP_of_MaxsBR_PS_LineEdit.setText(_translate("MinMax_Window", "2", None))
        self.WoLP_of_MaxsBR_PS_LineEdit.setText(_translate("MinMax_Window", "2", None))
        #self.Level_of_MaxsBR_PS_LineEdit.setText()
        
        self.Find_Region_Button.setText(_translate("MinMax_Window", "Find Region(s)", None))
        self.Methods_GroupBox.setTitle(_translate("MinMax_Window", "Methods", None))
        self.Methods_ComboBox1.setItemText(0, _translate("MinMax_Window", "Kwee - Van Woerden", None))
        self.Methods_ComboBox1.setItemText(1, _translate("MinMax_Window", "Bisection of Chord", None))
        self.Methods_ComboBox1.setItemText(2, _translate("MinMax_Window", "Polynomial Fit", None))
        self.Methods_ComboBox1.setItemText(3, _translate("MinMax_Window", "Fourier Fit", None))
        self.Methods_ComboBox1.setItemText(4, _translate("MinMax_Window", "Add Function", None))
        self.Methods_1Min_Label.setText(_translate("MinMax_Window", "1. Min", None))
        self.Methods_ComboBox2.setItemText(0, _translate("MinMax_Window", "Kwee - Van Woerden", None))
        self.Methods_ComboBox2.setItemText(1, _translate("MinMax_Window", "Bisection of Chord", None))
        self.Methods_ComboBox2.setItemText(2, _translate("MinMax_Window", "Polynomial Fit", None))
        self.Methods_ComboBox2.setItemText(3, _translate("MinMax_Window", "Fourier Fit", None))
        self.Methods_ComboBox2.setItemText(4, _translate("MinMax_Window", "Add Function", None))
        self.Methods_2Min_Label.setText(_translate("MinMax_Window", "2. Min", None))
        self.Degree_of_Polynom_Label1.setText(_translate("MinMax_Window", "Degree of Polynom :", None))
        self.Degree_of_Polynom_Label2.setText(_translate("MinMax_Window", "Degree of Polynom :", None))
        self.Calculate_Min_Max_Button.setText(_translate("MinMax_Window", "Calculate Min/Max Time(s)", None))
        item = self.Min_Max_Table.horizontalHeaderItem(0)
        item.setText(_translate("MinMax_Window", "Min/Max Time", None))
        item = self.Min_Max_Table.horizontalHeaderItem(1)
        item.setText(_translate("MinMax_Window", "Type", None))
        item = self.Min_Max_Table.horizontalHeaderItem(2)
        item.setText(_translate("MinMax_Window", "Error", None))
        self.Save_Min_Max_Time_Button.setText(_translate("MinMax_Window", "Save", None))
        self.Show_O_C_Button.setText(_translate("MinMax_Window", "Show O-C", None))
        self.ProgressBar.setValue(0)
     
    def SpecialFunc(self):
        signal = XM.ui.MinMax_Window.sender()
        if signal.objectName() == 'Methods_ComboBox1':
            combobox = self.Methods_ComboBox1
        elif signal.objectName() == 'Methods_ComboBox2':
            combobox = self.Methods_ComboBox2
        
        if combobox.currentText() == 'Add Function':
            combobox.setCurrentIndex(3)
            
            SF_Win = Qt.QDialog(XM.window)
            #SF_Win.setMinimumSize(300,150)
            SF_Win.setWindowTitle('User-Defined Function')
            SF_Main_VLayout = Qt.QVBoxLayout(SF_Win)
            
            AddNew_Button = Qt.QPushButton()
            AddNew_Button.setText('Add New Function')
            AddNew_Button.setObjectName('AddNew')
            Edit_Button = Qt.QPushButton()
            Edit_Button.setText('Edit Function')
            Edit_Button.setObjectName('Edit')
            
            FuncBox = Qt.QComboBox()
            FuncBox.addItem('Select Function')
            funcs = [[],[]]
            # try:
            print(os.path.dirname(os.path.abspath(__file__)))
            func_file = open(os.path.dirname(os.path.abspath(__file__)) + '/functions','r')
            lines = func_file.readlines()
            for item in lines:
                funcs[0].append(item.split(',')[0])
                funcs[1].append(item.split(',')[1])
                FuncBox.addItem(item.split(',')[0])
            # except:
            #     pass
            #
            #
            Finish_Button = Qt.QPushButton()
            Finish_Button.setText('Finish')
            
            def AddNew():    
                AF_Win = Qt.QDialog(XM.window)
                AF_Win.setWindowTitle('Add Function')
                AF_Main_VLayout = Qt.QVBoxLayout(AF_Win)
                
                
                Label = Qt.QLabel()
                Label.setText(('Addition        : +      Subtraction  : -\n'
                               'Multiplication : *      Division       : /\n'
                               'Exponent      : ^      Square root : sqrt()\n'
                               'Cosine          :      cos() Sine       : sin()\n'
                               'Note: You can use other all operators or functions in the numpy module '))
            
                TextEdit = Qt.QTextEdit()
                Add_Button = Qt.QPushButton()

                signal = SF_Win.sender()
                if signal.objectName() == 'Edit' and FuncBox.currentIndex() != 0:
                    SF_Win.hide()
                    AF_Win.show()
                    Add_Button.setText('Edit')
                    for i in range(len(funcs[0])):
                        if FuncBox.currentText() == funcs[0][i]:
                            TextEdit.setText(funcs[1][i])
                            
                elif signal.objectName() == 'Edit' and FuncBox.currentIndex() == 0:
                     Qt.QMessageBox.question(XM.window, 'Message',
                        'Please choose a function', Qt.QMessageBox.Ok)
                
                else:
                    SF_Win.hide()
                    AF_Win.show()
                    Add_Button.setText('Add')
                    
                TextEdit.setMinimumSize(300,150)
                font = QtGui.QFont()
                font.setFamily(_fromUtf8("Times New Roman"))
                font.setPointSize(20)
                font.setWeight(50)
                TextEdit.setFont(font)
                
                
                
                AF_Main_VLayout.addWidget(Label)
                AF_Main_VLayout.addWidget(TextEdit)
                AF_Main_VLayout.addWidget(Add_Button)
                
                
                def Add():
                    if signal.objectName() == 'AddNew':
                        text = '' 
                    else:
                        text = FuncBox.currentText()
                        
                    name, ok = Qt.QInputDialog.getText(XM.window,'Fuction Name',
                                               'Please enter a name for the function',
                                               text = text)
                                               
                    if ok == True:
                        AF_Win.close()
                        
                        order = -1
                        for i in range(len(funcs[0])):
                            if funcs[0][i] == name:
                                order = i
                                break
                        
                        if order != -1:
                            funcs[1][order] = TextEdit.toPlainText()
                            
                        else:    
                            FuncBox.addItem(name)
                            funcs[0].append(name)
                            funcs[1].append(TextEdit.toPlainText())
                        
                        func_file = open('functions','w')
                        for i in range(len(funcs[0])):
                            func_file.write(str(funcs[0][i]).replace('\n','')+','+
                                            str(funcs[1][i]).replace('\n','')+'\n')
                        
                        if signal.objectName() == 'AddNew':
                            FuncBox.setCurrentIndex(FuncBox.count()-1)
                        
                        
                        SF_Win.show()
                    #else:
                    
                Add_Button.clicked.connect(Add)
                
            def finish():
                for i in range(len(funcs[0])): 
                    if FuncBox.currentText() == funcs[0][i]:
                        combobox.model().item(4).setText(funcs[0][i])
                        try:
                            combobox.model().item(5).setText('Add Function')
                        except:
                            combobox.addItem('Add Function')
                        combobox.blockSignals(True)
                        combobox.setCurrentIndex(4)
                        combobox.blockSignals(False)
                        if signal.objectName() == 'Methods_ComboBox1':
                            self.func1 = funcs[1][i]
                        elif signal.objectName() == 'Methods_ComboBox2':
                            self.func2 = funcs[1][i] 
                        
                        break                
                
                SF_Win.close()
            
            
            Finish_Button.clicked.connect(finish)
            AddNew_Button.clicked.connect(AddNew)
            Edit_Button.clicked.connect(AddNew)
            
            SF_Main_VLayout.addWidget(FuncBox)
            SF_Main_VLayout.addWidget(AddNew_Button)
            SF_Main_VLayout.addWidget(Edit_Button)
            SF_Main_VLayout.addWidget(Finish_Button)
        
            SF_Win.exec_()
    

    def Graph_Event(self, event):
        if self.Select_Min_Max_Region_CheckBox.isChecked() == True:
            item_list = self.Graph_Plot.get_items()
            from plotpy.items import XRangeSelection
            for item in item_list:
                if type(item) == XRangeSelection:
                    self.Calculate_Min_Max_Button.setEnabled(True)
                    break
                else:
                    self.Calculate_Min_Max_Button.setEnabled(False)
    
    def TableHeader_Resize(self):        
        """Not: Splitter sola kaydırıldığında Min_Max_Table
           da 'Type' başlığının genişliği 35 birim kalmak kaydıyla
           diğer iki başlık otomatik olarak boyutlandırılmalı.
           Mevcut algoritma sağlıklı değil. Daha iyisini yaz"""
        
        
        Table_Size = self.Min_Max_Table.size()
        if Table_Size.width() == 405:
            self.Min_Max_Table.setColumnWidth(0,200)
            self.Min_Max_Table.setColumnWidth(2,150)
        else:
            self.Min_Max_Table.setColumnWidth(0,100)
            self.Min_Max_Table.setColumnWidth(2,50)
        
    def Update_Settings(self):
        if self.ToVS == 0:
            if self.Extremum_ComboBox.currentText() == "Minimum Time":
                
                self.Methods_1Min_Label.setText(_translate("MainWindow", "1. Mins", None))
                self.Methods_2Min_Label.setText(_translate("MainWindow", "2. Mins", None))
                
                while self.Min_Max_Setting_GroupBox_VLayout.count() > 0: 
                    self.Min_Max_Setting_GroupBox_VLayout.itemAt(0).widget().setParent(None)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Stack_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Points_1Mins_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Points_2Mins_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoRP_of_1Mins_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoLP_of_1Mins_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoRP_of_2Mins_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoLP_of_2Mins_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Level_of_1Mins_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Level_of_2Mins_Frame)    
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Find_Region_Button)
                
                self.Methods_ComboBox1.model().item(0).setEnabled(True)
                self.Methods_ComboBox1.model().item(1).setEnabled(True)
                self.Methods_ComboBox2.model().item(0).setEnabled(True)
                self.Methods_ComboBox2.model().item(1).setEnabled(True)
                
                item = self.Min_Max_Table.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "Min/Max Time", None))
                item = self.Min_Max_Table.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Type", None))
                item = self.Min_Max_Table.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Error", None))
                self.Show_O_C_Button.setText("Show O-C")
                
                if self.Select_Min_Max_Region_CheckBox.isChecked() == True:
                    self.Degree_of_Polynom_Frame2.hide()
                else:
                    self.Degree_of_Polynom_Frame2.show()
             
            elif self.Extremum_ComboBox.currentText() == "Maximum Brightness":

                self.Methods_1Min_Label.setText(_translate("MainWindow", "1. Maxs", None))
                self.Methods_2Min_Label.setText(_translate("MainWindow", "2. Maxs", None))
                
                while self.Min_Max_Setting_GroupBox_VLayout.count() > 0: 
                    self.Min_Max_Setting_GroupBox_VLayout.itemAt(0).widget().setParent(None)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoRP_of_1Maxs_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoLP_of_1Maxs_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoRP_of_2Maxs_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoLP_of_2Maxs_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Points_1Maxs_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Points_2Maxs_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Level_of_1Maxs_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Level_of_2Maxs_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Find_Region_Button)
                
                self.WoRP_of_1Maxs_Frame.show()
                self.WoLP_of_1Maxs_Frame.show()
                self.WoRP_of_2Maxs_Frame.show()
                self.WoLP_of_2Maxs_Frame.show()
                self.Points_1Maxs_Frame.show()
                self.Points_2Maxs_Frame.show()
                self.Level_of_1Maxs_Frame.show()
                self.Level_of_2Maxs_Frame.show()
                
                self.Methods_ComboBox1.model().item(0).setEnabled(False)
                self.Methods_ComboBox1.model().item(1).setEnabled(False)
                self.Methods_ComboBox2.model().item(0).setEnabled(False)
                self.Methods_ComboBox2.model().item(1).setEnabled(False)
                if self.Methods_ComboBox1.currentIndex() in [0,1]:
                    self.Methods_ComboBox1.setCurrentIndex(2)
                if self.Methods_ComboBox2.currentIndex() in [0,1]:
                    self.Methods_ComboBox2.setCurrentIndex(2)
                
                if self.Select_Min_Max_Region_CheckBox.isChecked() == True:
                    self.Degree_of_Polynom_Frame2.hide()
                else:
                    self.Degree_of_Polynom_Frame2.show()
                
                item = self.Min_Max_Table.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "Time", None))
                item = self.Min_Max_Table.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Type", None))
                item = self.Min_Max_Table.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Max Brigh.", None))
                self.Show_O_C_Button.setText("Show Graph")
        else:
            if self.Extremum_ComboBox.currentText() == "Maximum Time":

                while self.Min_Max_Setting_GroupBox_VLayout.count() > 0: 
                    self.Min_Max_Setting_GroupBox_VLayout.itemAt(0).widget().setParent(None)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Stack_PS_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Points_PS_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoRP_of_Maxs_PS_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoLP_of_Maxs_PS_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Level_of_Maxs_PS_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Find_Region_Button)
                
                self.Methods_ComboBox1.model().item(0).setEnabled(True)
                self.Methods_ComboBox1.model().item(1).setEnabled(True)
                
                
                item = self.Min_Max_Table.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "Min/Max Time", None))
                item = self.Min_Max_Table.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Type", None))
                item = self.Min_Max_Table.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Error", None))
                self.Show_O_C_Button.setText("Show O-C")
             
            elif self.Extremum_ComboBox.currentText() == "Maximum Brightness":

                while self.Min_Max_Setting_GroupBox_VLayout.count() > 0: 
                    self.Min_Max_Setting_GroupBox_VLayout.itemAt(0).widget().setParent(None)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoRP_of_MaxsBR_PS_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.WoLP_of_MaxsBR_PS_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.PointsBR_PS_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Level_of_MaxsBR_PS_Frame)
                self.Min_Max_Setting_GroupBox_VLayout.addWidget(self.Find_Region_Button)
                
                self.WoRP_of_MaxsBR_PS_Frame.show()
                self.PointsBR_PS_Frame.show()
                self.WoLP_of_MaxsBR_PS_Frame.show()
                self.Level_of_MaxsBR_PS_Frame.show()

                self.Methods_ComboBox1.model().item(0).setEnabled(False)
                self.Methods_ComboBox1.model().item(1).setEnabled(False)
                if self.Methods_ComboBox1.currentIndex() in [0,1]:
                    self.Methods_ComboBox1.setCurrentIndex(2)
                

                item = self.Min_Max_Table.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "Time", None))
                item = self.Min_Max_Table.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Type", None))
                item = self.Min_Max_Table.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Max Brightness", None))
                self.Show_O_C_Button.setText("Show Graph")
            
    
    def Manuel_Selection(self):
        if self.Select_Min_Max_Region_CheckBox.isChecked() == False:
            if self.ToVS == 0:
                #self.Calculate_Button.setEnabled(False)

                self.Methods_1Min_HLLine.show()
                self.Methods_1Min_Label.show()
                self.Methods_1Min_HRLine.show()
                self.Methods_HLine.show()
                self.Methods_2Min_HLLine.show()
                self.Methods_2Min_Label.show()
                self.Methods_2Min_HRLine.show()
                self.Methods_ComboBox2.show()
                
                
                if self.Methods_ComboBox1.currentText() == 'Polynomial Fit':
                    self.Degree_of_Polynom_Frame1.show()
                              
                if self.Methods_ComboBox2.currentText() == 'Polynomial Fit':
                    self.Degree_of_Polynom_Frame2.show()
            
            
            self.data_x = XM.ui.OD.data_x
            self.data_y = XM.ui.OD.data_y
            self.LCurve()
                
            self.Min_Max_Region_Button.setEnabled(True)  
            self.Min_Max_Setting_GroupBox.setEnabled(True)
            self.Graph_Icons[7].setVisible(False)
            self.Graph_Icons[8].setVisible(False)
            
        elif self.Select_Min_Max_Region_CheckBox.isChecked() == True:
            #if self.ToVS == 0:
    
            self.Methods_1Min_HLLine.hide()
            self.Methods_1Min_Label.hide()
            self.Methods_1Min_HRLine.hide()
            self.Methods_HLine.hide()
            self.Methods_2Min_HLLine.hide()
            self.Methods_2Min_Label.hide()
            self.Methods_2Min_HRLine.hide()
            self.Methods_ComboBox2.hide()

            self.Degree_of_Polynom_Frame2.hide()
            
            try:
                items = self.Graph_Plot.get_items()
                
                x = np.hstack((items[1].get_data()[0],
                              items[2].get_data()[0]))
                y = np.hstack((items[1].get_data()[1],
                              items[2].get_data()[1]))
    
                sort = np.argsort(x)
                self.data_x = x[sort]
                self.data_y = y[sort] 
                self.Graph_Plot.del_all_items()
                curve_item = make.curve(self.data_x, self.data_y,
                                    marker='+', linestyle='NoPen',
                                    markerfacecolor='k',
                                    markeredgecolor='k', markersize=7)
                self.Graph_Plot.add_item(curve_item)
                self.Graph_Plot.show_items()
            except:
                pass
            self.Min_Max_Region_Button.setEnabled(False)  
            self.Calculate_Min_Max_Button.setEnabled(False)    
            self.Min_Max_Setting_GroupBox.setEnabled(False)
            self.Graph_Icons[7].setVisible(True)
            self.Graph_Icons[8].setVisible(True)
        
    def DoP_Widget1(self):
        if self.Methods_ComboBox1.currentText() == 'Polynomial Fit':
            self.Degree_of_Polynom_Frame1.show()
        else:
            self.Degree_of_Polynom_Frame1.hide()
        
    def DoP_Widget2(self):
        if self.Methods_ComboBox2.currentText() == 'Polynomial Fit':
            self.Degree_of_Polynom_Frame2.show()
        else:
            self.Degree_of_Polynom_Frame2.hide()
        
    def Find_Region(self):
        Bness = XM.ui.OD.yAxis_ComboBox.currentText()       
        Data_x = np.array(XM.ui.OD.data_x)
        Data_y = np.array(XM.ui.OD.data_y)
        
        self.Type = self.Extremum_ComboBox.currentIndex()
        
        T0 = XM.ui.MG.T0_Lineedit.text()
        P = XM.ui.MG.P_Lineedit.text()
        
        if (str(T0).replace('.','',1).isdigit() == True and
           str(P).replace('.','',1).isdigit() == True):
            Seperator = cl.Seperator(self.ToVS,self.Type,Bness,T0,P)
            Exts = Seperator.Seperate([Data_x,Data_y])
            self.Graph_Plot.del_all_items() 
            if self.ToVS == 0:                
                if self.Type == 0:
                    Stack = self.Stack_LineEdit.text()
                    WoP1R = self.WoRP_of_1Mins_LineEdit.text()
                    WoP1L = self.WoLP_of_1Mins_LineEdit.text()
                    WoP2R = self.WoRP_of_2Mins_LineEdit.text()
                    WoP2L = self.WoLP_of_2Mins_LineEdit.text()
                    Points1 = self.Points_1Mins_LineEdit.text()
                    Points2 = self.Points_2Mins_LineEdit.text()
                    lvl1 = self.Level_of_1Mins_LineEdit.text()
                    lvl2 = self.Level_of_2Mins_LineEdit.text()
                    
                    Check_lvl1 = lvl1
                    if str(Check_lvl1).startswith('-'):
                        Check_lvl1 = lvl1[1:]
                    
                    if (str(Check_lvl1).replace('.','',1).isdigit() != True or
                    self.Level_of_1Mins_CheckBox.isChecked() == False):
                        if Bness == 'Magnitude':
                            lvl1 = min(Data_y)
                        else:
                            lvl1 = max(Data_y)
                            
                    Check_lvl2 = lvl2
                    if str(Check_lvl2).startswith('-'):
                        Check_lvl2 = lvl2[1:]
                    
                    if (str(Check_lvl2).replace('.','',1).isdigit() != True or
                    self.Level_of_2Mins_CheckBox.isChecked() == False):
                        if Bness == 'Magnitude':
                            lvl2 = min(Data_y)
                        else:
                            lvl2 = max(Data_y)
                    
                    Profil_Ext1 = Seperator.Profil(Exts[0],float(WoP1R),float(WoP1L),float(Points1))
                    Profil_Ext2 = Seperator.Profil(Exts[1],float(WoP2R),float(WoP2L),float(Points2))
                    Stack_Ext1 = Seperator.Data_Stack(Profil_Ext1,int(Stack),Ofac=100,Hifac=1,MACC=10)
                    Stack_Ext2 = Seperator.Data_Stack(Profil_Ext2,int(Stack),Ofac=100,Hifac=1,MACC=10)                    
                    self.Level_Ext1 = Seperator.Level(Stack_Ext1,float(lvl1))
                    self.Level_Ext2 = Seperator.Level(Stack_Ext2,float(lvl2))
                    
                elif self.Type == 2:
                    Stack = None
                    Points1 = self.Points_1Maxs_LineEdit.text()
                    Points2 = self.Points_2Maxs_LineEdit.text()
                    WoP1R = self.WoRP_of_1Maxs_LineEdit.text()
                    WoP1L = self.WoLP_of_1Maxs_LineEdit.text()
                    WoP2R = self.WoRP_of_2Maxs_LineEdit.text()
                    WoP2L = self.WoLP_of_2Maxs_LineEdit.text()
                    lvl1 = self.Level_of_1Maxs_LineEdit.text()
                    lvl2 = self.Level_of_2Maxs_LineEdit.text()
                    
                    
                    Check_lvl1 = lvl1
                    if str(Check_lvl1).startswith('-'):
                        Check_lvl1 = lvl1[1:]
                    
                    if (str(Check_lvl1).replace('.','',1).isdigit() != True or
                    self.Level_of_1Maxs_CheckBox.isChecked() == False):
                        if Bness == 'Magnitude':
                            lvl1 = max(Data_y)
                        else:
                            lvl1 = min(Data_y)
                            
                    Check_lvl2 = lvl2
                    if str(Check_lvl2).startswith('-'):
                        Check_lvl2 = lvl2[1:]        
                            
                    if (str(Check_lvl2).replace('.','',1).isdigit() != True or
                    self.Level_of_2Maxs_CheckBox.isChecked() == False):
                        if Bness == 'Magnitude':
                            lvl2 = max(Data_y)
                        else:
                            lvl2 = min(Data_y)

                    Profil_Ext1 = Seperator.Profil(Exts[0],float(WoP1R),float(WoP1L), float(Points1))
                    Profil_Ext2 = Seperator.Profil(Exts[1],float(WoP2R),float(WoP2L), float(Points2))
                    self.Level_Ext1 = Seperator.Level(Profil_Ext1,float(lvl1))
                    self.Level_Ext2 = Seperator.Level(Profil_Ext2,float(lvl2))

                emp1 = len(self.Level_Ext1[0]) - sum(1 for ie1 in self.Level_Ext1[0] if isinstance(ie1, np.ndarray) and ie1.size == 0)
                emp2 = len(self.Level_Ext2[0]) - sum(1 for ie2 in self.Level_Ext2[0] if isinstance(ie2, np.ndarray) and ie2.size == 0)
                
                if emp1 == 0 and emp2 == 0:
                    Qt.QMessageBox.question(XM.window, 'Message',
                    'No data point is found according to specified criteria ',
                    Qt.QMessageBox.Ok)
                else:
                    if emp1 != 0:
                        self.x1 = np.hstack(self.Level_Ext1[0])
                        self.y1 = np.hstack(self.Level_Ext1[1])
                    else:
                        self.x1 = []
                        self.y1 = []
    
                    curve_item_1 = make.curve(self.x1, self.y1,
                                            "Primary Minimum"+" "+
                                            "("+str(emp1)+")",
                                            marker='+', linestyle='NoPen',
                                            markerfacecolor='b', markeredgecolor='b',
                                            
                                            markersize=7)
                    self.Graph_Plot.add_item(curve_item_1)
                    
                    if emp2 != 0:
                        self.x2 = np.hstack(self.Level_Ext2[0])
                        self.y2 = np.hstack(self.Level_Ext2[1])
                    else:
                        self.x2 = []
                        self.y2 = []
    
                    curve_item_2 = make.curve(self.x2, self.y2,
                                            "Secondary Minimum"+" "+
                                            "("+str(emp2)+")",
                                            marker='+', linestyle='NoPen',
                                            markerfacecolor='r', markeredgecolor='r',
                                            markersize=7)
                    self.Graph_Plot.add_item(curve_item_2)
                    legend = make.legend("TR", restrict_items=[curve_item_1,curve_item_2])
                    self.Graph_Plot.add_item(legend)
                
                
            elif self.ToVS == 1:
                if self.Type == 1:
                    Stack = self.Stack_PS_LineEdit.text()
                    Points = self.Points_PS_LineEdit.text()
                    WoPR = self.WoRP_of_Maxs_PS_LineEdit.text()
                    WoPL = self.WoLP_of_Maxs_PS_LineEdit.text()
                    lvlMaxs = self.Level_of_Maxs_PS_LineEdit.text()
                    
                    Check_lvlMaxs = lvlMaxs
                    if str(Check_lvlMaxs).startswith('-'):
                        Check_lvlMaxs = lvlMaxs[1:]
                    
                    if (str(Check_lvlMaxs).replace('.','',1).isdigit() != True or
                    self.Level_of_Maxs_PS_CheckBox.isChecked() == False):
                        if Bness == 'Magnitude':
                            lvlMaxs = max(Data_y)
                        else:
                            lvlMaxs = min(Data_y)
                    
                    Profil_Ext = Seperator.Profil(Exts,float(WoPR),float(WoPL), float(Points))
                    Stack_Ext = Seperator.Data_Stack(Profil_Ext,int(Stack))
                    self.Level_Ext = Seperator.Level(Stack_Ext,float(lvlMaxs))

                elif self.Type == 2:
                    Points = self.PointBR_PS_LineEdit.text()
                    WoPR = self.WoRP_of_MaxsBR_PS_LineEdit.text()
                    WoPL = self.WoLP_of_MaxsBR_PS_LineEdit.text()
                    lvlMaxs = self.Level_of_MaxsBR_PS_LineEdit.text()   
                    
                    Check_lvlMaxs = lvlMaxs
                    if str(Check_lvlMaxs).startswith('-'):
                        Check_lvlMaxs = lvlMaxs[1:]
                        
                    if (str(Check_lvlMaxs).replace('.','',1).isdigit() != True or
                    self.Level_of_MaxsBR_PS_CheckBox.isChecked() == False):
                        if Bness == 'Magnitude':
                            lvlMaxs = max(Data_y)
                        else:
                            lvlMaxs = min(Data_y)
                    Profil_Ext = Seperator.Profil(Exts,float(WoPR),float(WoPL), float(Points))
                    self.Level_Ext = Seperator.Level(Profil_Ext,float(lvlMaxs))

                emp = len(self.Level_Ext[0]) - sum(1 for ie in self.Level_Ext[0] if isinstance(ie, np.ndarray) and ie.size == 0)
                if emp == 0:
                    Qt.QMessageBox.question(XM.window, 'Message',
                    'No data point is found according to specified criteria ',
                    Qt.QMessageBox.Ok)
                else:
                    self.x = np.hstack(self.Level_Ext[0])
                    self.y = np.hstack(self.Level_Ext[1])
                    
                    curve_item = make.curve(self.x, self.y, "Maximum"+" "+
                                            "("+str(emp)+")",
                                            marker='+',
                                            linestyle='NoPen',markerfacecolor='b',
                                            markeredgecolor='b', markersize=7)
                    self.Graph_Plot.add_item(curve_item)
                    legend = make.legend("TR", restrict_items=[curve_item])
                    self.Graph_Plot.add_item(legend)
                

            self.Graph_Plot.show_items()
            self.Calculate_Min_Max_Button.setEnabled(True)
            self.Extremum_ComboBox.setEnabled(False)
            self.Calculate_Min_Max_Button.setEnabled(True)
            self.Min_Max_Region_Button.setEnabled(True)            
        else:
            Qt.QMessageBox.question(XM.window, 'Message',
            'Please enter a valid value for Referens Min/Max Time'+
            ' and Period in Main Window', Qt.QMessageBox.Ok)
    
    def Show_Region(self):
        self.Graph_Plot.del_all_items()

        if self.ToVS == 0:
            emp1 = len(self.Level_Ext1[0]) - sum(1 for ie1 in self.Level_Ext1[0] if isinstance(ie1, np.ndarray) and ie1.size == 0)
            emp2 = len(self.Level_Ext2[0]) - sum(1 for ie2 in self.Level_Ext2[0] if isinstance(ie2, np.ndarray) and ie2.size == 0)

            curve_item_1 = make.curve(self.x1, self.y1,
                                    "Primary Minimum"+" "+"("+str(emp1)+")", marker='+',
                                    linestyle='NoPen',markerfacecolor='b',
                                    markeredgecolor='b', markersize=7)
            self.Graph_Plot.add_item(curve_item_1)
            curve_item_2 = make.curve(self.x2, self.y2,
                                    "Secondary Minimum"+" "+"("+str(emp2)+")", marker='+',
                                    linestyle='NoPen',markerfacecolor='r',
                                    markeredgecolor='r', markersize=7)
            self.Graph_Plot.add_item(curve_item_2)
            legend = make.legend("TR", restrict_items=[curve_item_1,curve_item_2])
            
        else:
            emp0 = len(self.Level_Ext[0]) - sum(1 for ie1 in self.Level_Ext[0] if isinstance(ie1, np.ndarray) and ie1.size == 0)

            curve_item = make.curve(self.x, self.y,
                                    "Primary Minimum"+" "+"("+str(emp0)+")", marker='+',
                                    linestyle='NoPen',markerfacecolor='b',
                                    markeredgecolor='b', markersize=7)
            self.Graph_Plot.add_item(curve_item)            
            legend = make.legend("TR", restrict_items=[curve_item])
            
        self.Graph_Plot.add_item(legend)
        self.Graph_Plot.show_items()
        self.Calculate_Min_Max_Button.setEnabled(True)
        
    def LCurve(self):
        self.data_x = XM.ui.OD.data_x
        self.data_y = XM.ui.OD.data_y
    
        xLabel = XM.ui.MG.Graph_Plot.axisTitle(2).text()
    
        self.Graph_Plot.del_all_items() 
        self.Graph_Plot.set_axis_title("bottom",xLabel)
        curve_item = make.curve(self.data_x, self.data_y, marker='+', linestyle='NoPen',
                                    markerfacecolor='k',markeredgecolor='k', markersize=7)
        self.Graph_Plot.add_item(curve_item)
        self.Graph_Plot.show_items()
        self.Calculate_Min_Max_Button.setEnabled(False)
        self.Extremum_ComboBox.setEnabled(True)
        
    def Calculate(self):
        Bness = XM.ui.OD.yAxis_ComboBox.currentText() 
        self.Min_Max_Table.setRowCount(0)
        from plotpy.builder import PlotBuilder

        if self.Select_Min_Max_Region_CheckBox.isChecked() == False:
            self.Graph_Plot.del_all_items()
            self.Show_Region()
            
            if self.ToVS == 0:
                Ext_Data_x = []
                Ext_Data_y = []
                for i in range(len(self.Level_Ext1[0])):
                    Ext_Data_x.append(self.Level_Ext1[0][i])
                    Ext_Data_y.append(self.Level_Ext1[1][i])
                for i in range(len(self.Level_Ext2[0])): 
                    Ext_Data_x.append(self.Level_Ext2[0][i])
                    Ext_Data_y.append(self.Level_Ext2[1][i])
                
            else:
                Ext_Data_x = self.Level_Ext[0]               
                Ext_Data_y = self.Level_Ext[1]
            
            #vlines = []
            # XM.ui.MinMax_Window.setAttribute(QtCore.Qt.WA_OpaquePaintEvent, True)
            self.ProgressBar.setVisible(True)    
            for i in range(len(Ext_Data_x)):
                # if (i+1) % ((10+len(Ext_Data_x)/10)) == 0:
                per = int(100.0*i/len(Ext_Data_x))
                self.ProgressBar.setValue(per)
                self.ProgressBar_Label.setText('Calculating %'+ str('%0.2f' % per))

                # Qt.qApp.processEvents()

                
                if len(Ext_Data_x[i]) != 0:                    
                    if self.ToVS == 0 and i >= len(self.Level_Ext1[0]):
                        Type = str(2)
                        MC = self.Methods_ComboBox2.currentIndex()
                        n = self.Degree_of_Polynom_LineEdit2.text()
                        try:
                            func = self.func2
                        except:
                            pass
                    else:
                        Type = str(1)
                        MC = self.Methods_ComboBox1.currentIndex()
                        n = self.Degree_of_Polynom_LineEdit1.text()
                        try:
                            func = self.func1
                        except:
                            pass
                        
                    # try:
                    if MC == 2:
                       Ext = cl.Methods.polyn([Ext_Data_x[i],Ext_Data_y[i]], float(n), self.ToVS, self.Type, Bness)
                    if MC == 3:
                       Ext = cl.Methods.fourier([Ext_Data_x[i],Ext_Data_y[i]], self.ToVS, self.Type, Bness)
                    if MC == 4:
                       Ext = cl.Methods.Special_Func([Ext_Data_x[i],Ext_Data_y[i]], self.ToVS, self.Type, Bness, func)

                    if self.Type != 2:
                        if MC == 0:
                           Ext = cl.Methods.Kwee([Ext_Data_x[i],Ext_Data_y[i]], self.ToVS, Bness)
                        if MC == 1:
                           Ext = cl.Methods.Bisection([Ext_Data_x[i],Ext_Data_y[i]], self.ToVS, Bness)
                    # except:
                    #     Ext = ['NaN','NaN']
                    
                    Check_Ext = str(Ext[0])
                    if str(Check_Ext).startswith('-'):
                        Check_Ext = str(Ext[0][1:])
                        
                    if (str(Check_Ext).replace('.','',1).isdigit() == True
                    and str(Check_Ext).replace('.','',1).isdigit() == True):
                        Ext_item = Qt.QTableWidgetItem(str("%0.10f" % Ext[0]))
                        #Ext_item = Qt.QTableWidgetItem(str("%0.5f" % min(Ext[3])))
                        Ext_item.setTextAlignment(QtCore.Qt.AlignCenter)
                        Err_item = Qt.QTableWidgetItem(str("%0.10f" % Ext[1]))
                        #Err_item = Qt.QTableWidgetItem(str("%0.5f" % Ext[0]))
                        Err_item.setTextAlignment(QtCore.Qt.AlignCenter)
                        Type_item = Qt.QTableWidgetItem(Type)
                        Type_item.setTextAlignment(QtCore.Qt.AlignCenter)
                        row = self.Min_Max_Table.rowCount()
                        self.Min_Max_Table.insertRow(row)
                        self.Min_Max_Table.setItem(row,0,Ext_item)
                        self.Min_Max_Table.setItem(row,1,Type_item)
                        self.Min_Max_Table.setItem(row,2,Err_item)
                        if self.Show_Min_Max_PointorCurve_CheckButton.isChecked() == True:
                           Marker = PlotBuilder()
                           vline = Marker.marker(position=(Ext[0],0),
                                                 markerstyle='|',
                                                 movable=False,color='g',
                                                 label_cb=(lambda x, y: "x = %0.5f" % x))
                           self.Graph_Plot.add_item(vline)
                           self.Graph_Plot.show_items()
                           #vlines.append(vline)
#                           import matplotlib.pyplot as plt
#                           plt.ioff()
#                           fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
#                           ax.plot([Ext[0],Ext[0]],[min(Ext_Data_y[i]),max(Ext_Data_y[i])],'r')
#                           ax.plot(Ext_Data_x[i],Ext_Data_y[i], 'bo')
                           if MC not in [0,1]:
                               curve = make.curve(Ext[2], Ext[3], color = 'green')
                               self.Graph_Plot.add_item(curve)
                               
#                               ax.plot(Ext[2], Ext[3], 'g')
#                           plt.close(fig)
                               
                           #self.Graph_Plot.show_items()
            self.ProgressBar.setVisible(False)
            self.ProgressBar_Label.setText('')
            # XM.ui.MinMax_Window.setAttribute(QtCore.Qt.WA_OpaquePaintEvent, False)
        else:
            
            try:
                self.Graph_Plot.del_items(self.Curve_and_Marker_list)
            except:
                pass
            item_list =  self.Graph_Plot.get_items()
            self.Type = self.Extremum_ComboBox.currentIndex()
            
            n = self.Degree_of_Polynom_LineEdit1.text()
            MC = self.Methods_ComboBox1.currentIndex()
            self.Curve_and_Marker_list = []
            from plotpy.items import XRangeSelection
            for item in item_list:
                if type(item) == XRangeSelection:
                    Ext_Data = cl.PlotRangeData(item_list[1], item)
                    
#                    try:
                    if MC == 2:
                       Ext = cl.Methods.polyn(Ext_Data, float(n), self.ToVS, self.Type, Bness)
                    if MC == 3:
                       Ext = cl.Methods.fourier(Ext_Data, self.ToVS, self.Type, Bness)
                    if MC == 4:
                       Ext = cl.Methods.Special_Func(Ext_Data, self.ToVS, self.Type, Bness, self.func1)
                    if self.Type != 2:
                        if MC == 0:
                           Ext = cl.Methods.Kwee(Ext_Data, self.ToVS, Bness)
                        if MC == 1:
                           Ext = cl.Methods.Bisection(Ext_Data, self.ToVS, Bness)
#                    except:
#                        Ext = ['NaN','NaN']
                    
                    Check_Ext = str(Ext[0])
                    #print Check_Ext
                    if str(Check_Ext).startswith('-'):
                        Check_Ext = str(Ext[0][1:])
                    
                    if (str(Check_Ext).replace('.','',1).isdigit() == True
                    and str(Check_Ext).replace('.','',1).isdigit() == True):
                        Ext_item = Qt.QTableWidgetItem(str("%0.10f" % Ext[0]))
                        Ext_item.setTextAlignment(QtCore.Qt.AlignCenter)
                        Err_item = Qt.QTableWidgetItem(str("%0.10f" % Ext[1]))
                        Err_item.setTextAlignment(QtCore.Qt.AlignCenter)
                        Type_item = Qt.QTableWidgetItem('')
                        Type_item.setTextAlignment(QtCore.Qt.AlignCenter)
                        row = self.Min_Max_Table.rowCount()
                        self.Min_Max_Table.insertRow(row)
                        self.Min_Max_Table.setItem(row,0,Ext_item)
                        self.Min_Max_Table.setItem(row,1,Type_item)
                        self.Min_Max_Table.setItem(row,2,Err_item)
                        if self.Show_Min_Max_PointorCurve_CheckButton.isChecked() == True:
                           Marker = PlotBuilder()
                           vline = Marker.marker(position=(Ext[0],0),
                                                 markerstyle='|',
                                                 movable=False,color='g',
                                                 label_cb=(lambda x, y: "x = %0.5f" % x))
                           self.Curve_and_Marker_list.append(vline)
                           self.Graph_Plot.add_item(vline)
                           if MC not in [0,1]:
                               curve = make.curve(Ext[2], Ext[3], color = 'green')
                               self.Curve_and_Marker_list.append(curve)
                               self.Graph_Plot.add_item(curve)
                           #self.Graph_Plot.show_items()
                               
        
        self.Min_Max_Table.setColumnWidth(2,50)
        #self.Min_Max_Table.resizeColumnsToContents()
#        self.Min_Max_Table.horizontalHeader().setResizeMode(2,
#                                             Qt.QHeaderView.Stretch)
        if self.Min_Max_Table.rowCount() != 0:
            self.Save_Min_Max_Time_Button.setEnabled(True)
            self.Show_O_C_Button.setEnabled(True)
        else:
            self.Save_Min_Max_Time_Button.setEnabled(False)
            self.Show_O_C_Button.setEnabled(False)
        self.Graph_Plot.show_items()
        
    def Show_OC(self):
        Type = self.Extremum_ComboBox.currentIndex()
        
        T0 = XM.ui.MG.T0_Lineedit.text()
        P = XM.ui.MG.P_Lineedit.text()
        
        mins = np.arange(0,dtype=np.float64)
        types = np.arange(0,dtype=np.float64)
        
        # if Type == 0:
        #     XM.ui.OC.T0P_GetCBox.setChecked(False)
        
        XM.ui.OC.Main_Table.setRowCount(0)
        XM.ui.OC.Graph_Plot.del_all_items()
        if Type != 2:
            for i in range(self.Min_Max_Table.rowCount()):
                item_mins = self.Min_Max_Table.item(i,0).text()
                item_types = self.Min_Max_Table.item(i,1).text()
                item_err = self.Min_Max_Table.item(i,1).text()
                if True == (str(item_mins).replace('.','',1).isdigit() and
                            str(item_types).replace('.','',1).isdigit() and
                            str(item_err).replace('.','',1).isdigit()):
                    mins = np.hstack((mins,float(item_mins)))
                    types = np.hstack((types,int(item_types)))
                    
                    row =XM.ui.OC.Main_Table.rowCount()
                    XM.ui.OC.Main_Table.insertRow(row)
                    item = Qt.QTableWidgetItem(item_mins)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    XM.ui.OC.Main_Table.setItem(row,2,item)
                    if self.ToVS == 0:
                        item = Qt.QTableWidgetItem(item_types)
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        XM.ui.OC.Main_Table.setItem(row,3,item)
                        item = Qt.QTableWidgetItem('ccd')
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        XM.ui.OC.Main_Table.setItem(row,4,item)
                        
            OC = cl.OC(mins,types,T0,P)
            
            for i in range(len(OC[0])):
                item_Eduz = Qt.QTableWidgetItem(str(OC[0][i]))
                item_Eduz.setTextAlignment(QtCore.Qt.AlignCenter)
                XM.ui.OC.Main_Table.setItem(i,0,item_Eduz)
                item_OC = Qt.QTableWidgetItem(str('%0.10f' % (OC[1][i]*24*60)))
                item_OC.setTextAlignment(QtCore.Qt.AlignLeft)
                XM.ui.OC.Main_Table.setItem(i,1,item_OC)
                
            XM.ui.OC.Graph_Plot.set_axis_title("left","O-C (mins)")
            XM.ui.OC.Graph_Plot.set_axis_title("bottom","Epoch")
            XM.ui.OC.Graph_Plot.set_axis_font("left", QtGui.QFont("Courier", 10, 100))
            XM.ui.OC.Graph_Plot.set_axis_font("bottom", QtGui.QFont("Courier", 10, 100))            
            XM.ui.OC.Graph_Plot.set_antialiasing(True)
        
            where_min1 = np.argwhere(types == 1)
            where_min2 = np.argwhere(types == 2)
            where_min1 = np.reshape(where_min1, (len(where_min1),))
            where_min2 = np.reshape(where_min2, (len(where_min2),))
        
            OC1 = [OC[0][where_min1],OC[1][where_min1]]
            OC2 = [OC[0][where_min2],OC[1][where_min2]]
            
            if len(OC1) != 0:
                curve_item1 = make.curve(OC1[0], OC1[1]*24*60, 
                                         "Primary Minimum ("+ str(len(OC1[0]))+")",
                                         marker='Ellipse',
                                         linestyle='NoPen',
                                         markerfacecolor='b',
                                         markeredgecolor='b', 
                                         markersize=7)
                XM.ui.OC.Graph_Plot.add_item(curve_item1)

            if len(OC2) != 0:
                curve_item2 = make.curve(OC2[0], OC2[1]*24*60,
                                         "Secondary Minimum ("+ str(len(OC2[0]))+")", 
                                         marker='Ellipse', 
                                         linestyle='NoPen',
                                         markerfacecolor='r',
                                         markeredgecolor='r', 
                                         markersize=7)
                XM.ui.OC.Graph_Plot.add_item(curve_item2)
                    
            legend = make.legend("TR")
            XM.ui.OC.Graph_Plot.add_item(legend)
            """
            CCD_Pe = len(OC1[0][0]) + len(OC1[0][1]) + \
                     len(OC2[0][0]) + len(OC2[0][1])
            Pg     = len(OC1[0][2]) + len(OC2[0][2])
            Vis    = len(OC1[0][3]) + len(OC2[0][3])
            
            text = [
                    (u"\u25CF CCD/Photoelectric"+" ("+str(CCD_Pe)+")"),
                    (u"\u25A0 Photographic"+" ("+str(Pg)+")"),
                    (u"\u25B2 Visual"+" ("+str(Vis)+")")
                   ]
            self.label = make.label("<br/>".join(text),"BR", (0,0), "BR")
            self.OC.Graph_Plot.add_item(self.label)
            """
        elif Type == 2:
            item = XM.ui.OC.Main_Table.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "Max Brigh.", None))
            Epoch1 = np.arange(0,dtype=float)
            Mag1 = np.arange(0,dtype=float)
            Epoch2 = np.arange(0,dtype=float)
            Mag2= np.arange(0,dtype=float)
            for i in range(self.Min_Max_Table.rowCount()):
                item_time = self.Min_Max_Table.item(i,0).text()
                item_mag = self.Min_Max_Table.item(i,2).text()
                item_types = self.Min_Max_Table.item(i,1).text()
                if True == (str(item_time).replace('.','',1).isdigit() and
                            str(item_mag).replace('-','',1).replace('.','',1).isdigit() and
                            str(item_types).replace('.','',1).isdigit()):
                                
                    E = (float(item_time)-float(T0))/float(P)
    
                    row =XM.ui.OC.Main_Table.rowCount()
                    XM.ui.OC.Main_Table.insertRow(row)
                    item = Qt.QTableWidgetItem(str(np.ceil(E)))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    XM.ui.OC.Main_Table.setItem(row,0,item)
                    item = Qt.QTableWidgetItem(item_mag)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    XM.ui.OC.Main_Table.setItem(row,1,item)
                    item = Qt.QTableWidgetItem(item_time)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    XM.ui.OC.Main_Table.setItem(row,2,item)
                    if self.ToVS == 0:
                        item = Qt.QTableWidgetItem(item_types)
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        XM.ui.OC.Main_Table.setItem(row,3,item)
                    
                    
                    if float(item_types) == 1:
                        Epoch1 = np.hstack((Epoch1,np.ceil(E)))
                        Mag1 = np.hstack((Mag1,float(item_mag)))
                    else:
                        Epoch2 = np.hstack((Epoch2,np.ceil(E)))
                        Mag2 = np.hstack((Mag2,float(item_mag)))
             
            ylabel = self.Graph_Plot.axisTitle(0).text()
            XM.ui.OC.Graph_Plot.set_axis_title("left",ylabel)
            XM.ui.OC.Graph_Plot.set_axis_title("bottom","Epoch")
            curve_item1 = make.curve(Epoch1, Mag1, marker='o',linestyle='NoPen',
                                    markerfacecolor='b',markeredgecolor='b', markersize=7)
            
            XM.ui.OC.Graph_Plot.add_item(curve_item1)
            curve_item2 = make.curve(Epoch2, Mag2, marker='o',linestyle='NoPen',
                                    markerfacecolor='r',markeredgecolor='r', markersize=7)
            XM.ui.OC.Graph_Plot.add_item(curve_item2)
        
        XM.ui.OC.Graph_Plot.do_autoscale()
        
        if self.Extremum_ComboBox.currentIndex() == 2:
            XM.ui.OC.Correction_Frame.hide()
            # XM.ui.OC.GetData_Frame.hide()
            # XM.ui.OC.Draw_OC_PushButton.hide()
            # XM.ui.OC.Open_PushButton.hide()
        else:
            XM.ui.OC.Correction_Frame.show()
            # XM.ui.OC.GetData_Frame.show()
            # XM.ui.OC.Draw_OC_PushButton.show()
            # XM.ui.OC.Open_PushButton.show()
        
        XM.ui.OC.data_sta = XM.ui.OC.Main_Table.rowCount()
        XM.ui.ObsCal_Window.show()
        
        
    def Save(self):
    
        Path, _ = Qt.QFileDialog.getSaveFileName(
                        Qt.QMainWindow(), 'Save File', '', 'TXT(*.txt)')
   
        data_save = open(str(Path),'w')
        try:
            for i in range(self.Min_Max_Table.rowCount()):
                
                MinMax_Time = self.Min_Max_Table.item(i,0)
                Type = self.Min_Max_Table.item(i,1)
                Error = self.Min_Max_Table.item(i,2)
                
                if MinMax_Time == None:
                    MinMax_Time = '-'
                else:
                    MinMax_Time = MinMax_Time.text()                    
                if Type == None:
                    Type = '-'
                else:
                    Type = Type.text()     
                if Error == None:
                    Error = '-'
                else:
                    Error = Error.text()
            
                data_save.write(MinMax_Time + ' ' +Type + ' ' + \
                Error + '\n')
            
            data_save.close()
        except:
            pass
            
#################################################################
"Min/Max Window End"
#################################################################

class MinMax(Qt.QMainWindow):
    def closeEvent(self,event):
        XM.ui.MG.Activate_Buttons()
        


