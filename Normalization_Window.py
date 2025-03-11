# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 05:31:48 2015

@author: TheLichWing
"""
import numpy as np
from plotpy.builder import make
import Main_Window as XM
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets as Qt
from plotpy.items import XRangeSelection
import Calculations as cl

from plotpy.plot import PlotDialog

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
"Normalization Window Start"
#################################################################
class Ui_Normalization_Widget(object):
    def setupUi(self, Normalization_Widget):
        Normalization_Widget.setObjectName(_fromUtf8("Normalization_Widget"))
        Normalization_Widget.resize(640, 383)
        Normalization_Widget.setMinimumSize(640, 384)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/NZ.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Normalization_Widget.setWindowIcon(icon)
        
        self.centralwidget = Qt.QWidget(Normalization_Widget)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = Qt.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout.setContentsMargins(2,2,2,2)
        self.gridLayout.setSpacing(2)
        self.line = Qt.QFrame(self.centralwidget)
        self.line.setFrameShape(Qt.QFrame.VLine)
        self.line.setFrameShadow(Qt.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 1, 3, 1)
        self.Norm_ToolBar_Frame = Qt.QFrame(self.centralwidget)
        sizePolicy = Qt.QSizePolicy(Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Norm_ToolBar_Frame.sizePolicy().hasHeightForWidth())
        self.Norm_ToolBar_Frame.setSizePolicy(sizePolicy)
        #self.Norm_ToolBar_Frame.setMinimumSize(QtCore.QSize(400, 30))
        #self.Norm_ToolBar_Frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Norm_ToolBar_Frame.setSizeIncrement(QtCore.QSize(0, 0))
        self.Norm_ToolBar_Frame.setFrameShape(Qt.QFrame.StyledPanel)
        self.Norm_ToolBar_Frame.setFrameShadow(Qt.QFrame.Raised)
        self.Norm_ToolBar_Frame.setObjectName(_fromUtf8("Norm_ToolBar_Frame"))
        self.gridLayout.addWidget(self.Norm_ToolBar_Frame, 0, 0, 1, 1)
        self.Norm_Bottom_Frame = Qt.QFrame(self.centralwidget)
        sizePolicy = Qt.QSizePolicy(Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Norm_Bottom_Frame.sizePolicy().hasHeightForWidth())
        self.Norm_Bottom_Frame.setSizePolicy(sizePolicy)
        # self.Norm_Bottom_Frame.setMinimumSize(QtCore.QSize(400, 40))
        self.Norm_Bottom_Frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Norm_Bottom_Frame.setFrameShape(Qt.QFrame.StyledPanel)
        self.Norm_Bottom_Frame.setFrameShadow(Qt.QFrame.Raised)
        self.Norm_Bottom_Frame.setObjectName(_fromUtf8("Norm_Bottom_Frame"))
        self.horizontalLayout_3 = Qt.QHBoxLayout(self.Norm_Bottom_Frame)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.Norm_Phase_Button = Qt.QPushButton(self.Norm_Bottom_Frame)
        sizePolicy = Qt.QSizePolicy(Qt.QSizePolicy.Preferred, Qt.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Norm_Phase_Button.sizePolicy().hasHeightForWidth())
        self.Norm_Phase_Button.setSizePolicy(sizePolicy)
        self.Norm_Phase_Button.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Norm_Phase_Button.setFont(font)
        self.Norm_Phase_Button.setObjectName(_fromUtf8("Norm_Phase_Button"))
        self.horizontalLayout_3.addWidget(self.Norm_Phase_Button)
        self.Norm_NormLC_Button = Qt.QPushButton(self.Norm_Bottom_Frame)
        self.Norm_NormLC_Button.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Norm_NormLC_Button.setFont(font)
        self.Norm_NormLC_Button.setObjectName(_fromUtf8("Norm_NormLC_Button"))
        self.horizontalLayout_3.addWidget(self.Norm_NormLC_Button)
        spacerItem1 = Qt.QSpacerItem(0, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout.addWidget(self.Norm_Bottom_Frame, 2, 0, 1, 1)
        self.Norm_Right_Frame = Qt.QFrame(self.centralwidget)
        sizePolicy = Qt.QSizePolicy(Qt.QSizePolicy.Fixed, Qt.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Norm_Right_Frame.sizePolicy().hasHeightForWidth())
        self.Norm_Right_Frame.setSizePolicy(sizePolicy)
        self.Norm_Right_Frame.setMinimumSize(QtCore.QSize(200, 0))
        self.Norm_Right_Frame.setMaximumSize(QtCore.QSize(200, 16777215))
        #self.Norm_Right_Frame.setSizeIncrement(QtCore.QSize(0, 0))
        self.Norm_Right_Frame.setFrameShape(Qt.QFrame.StyledPanel)
        self.Norm_Right_Frame.setFrameShadow(Qt.QFrame.Raised)
        self.Norm_Right_Frame.setObjectName(_fromUtf8("Norm_Right_Frame"))
        self.gridLayout_2 = Qt.QGridLayout(self.Norm_Right_Frame)
        self.gridLayout_2.setContentsMargins(2, 6, 2, 6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        
        
        
        
        self.Norm_Show_Button = Qt.QPushButton(self.Norm_Right_Frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Norm_Show_Button.setFont(font)
        self.Norm_Show_Button.setObjectName(_fromUtf8("Norm_Show_Button"))
        #self.gridLayout_2.addWidget(self.Norm_Show_Button, 1, 0, 1, 1)
        
        
        
        self.Norm_Calculaton_Button = Qt.QPushButton(self.Norm_Right_Frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Norm_Calculaton_Button.setFont(font)
        self.Norm_Calculaton_Button.setObjectName(_fromUtf8("Norm_Calculaton_Button"))
        #self.gridLayout_2.addWidget(self.Norm_Calculaton_Button, 1, 0, 1, 1)
        
        self.Norm_Continue_Button = Qt.QPushButton(self.Norm_Right_Frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Norm_Continue_Button.setFont(font)
        self.Norm_Continue_Button.setObjectName(_fromUtf8("Norm_Continue_Button"))
        
        self.Norm_Save_Button = Qt.QPushButton(self.Norm_Right_Frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Norm_Save_Button.setFont(font)
        self.Norm_Save_Button.setObjectName(_fromUtf8("Norm_Save_Button"))
        
        
                


        self.Norm_SS_Layout = Qt.QHBoxLayout()
        self.Norm_SS_Layout.setSpacing(0)
        self.Norm_SS_Layout.setObjectName(_fromUtf8("Norm_SS_Layout"))
        self.Norm_SS_Layout.addWidget(self.Norm_Show_Button)   
        self.Norm_SS_Layout.addWidget(self.Norm_Calculaton_Button)
        self.gridLayout_2.addLayout(self.Norm_SS_Layout, 1, 0, 1, 1)
        
        self.verticalLayout = Qt.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        """
        self.Norm_Space_Frame = Qt.QFrame(self.Norm_Right_Frame)
        self.Norm_Space_Frame.setMinimumSize(QtCore.QSize(155, 20))
        self.Norm_Space_Frame.setMaximumSize(QtCore.QSize(155, 20))
        """
        self.Norm_LCC_Lable = Qt.QLabel(self.Norm_Right_Frame)
        self.Norm_LCC_Lable.setMinimumSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(8)
        self.Norm_LCC_Lable.setFont(font)
        self.Norm_LCC_Lable.setFrameShape(Qt.QFrame.WinPanel)
        self.Norm_LCC_Lable.setFrameShadow(Qt.QFrame.Raised)
        self.Norm_LCC_Lable.setAlignment(QtCore.Qt.AlignCenter)
        self.Norm_LCC_Lable.setObjectName(_fromUtf8("Norm_LCC_Lable"))
        self.verticalLayout.addWidget(self.Norm_LCC_Lable)
        
        self.Norm_LCC_Table = Qt.QTableWidget(self.Norm_Right_Frame)
        # self.Norm_LCC_Table.setMinimumSize(QtCore.QSize(147, 228))
        # self.Norm_LCC_Table.setMaximumSize(QtCore.QSize(147, 228))
        self.Norm_LCC_Table.setObjectName(_fromUtf8("Norm_LCC_Table"))
        self.Norm_LCC_Table.setEditTriggers(Qt.QAbstractItemView.NoEditTriggers)
        self.Norm_LCC_Table.setColumnCount(1)
        self.Norm_LCC_Table.setRowCount(8)
        self.Norm_LCC_Table.verticalHeader().setSectionResizeMode(Qt.QHeaderView.Stretch)
        item = Qt.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Norm_LCC_Table.setVerticalHeaderItem(0, item)
        item = Qt.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Norm_LCC_Table.setVerticalHeaderItem(1, item)
        item = Qt.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Norm_LCC_Table.setVerticalHeaderItem(2, item)
        item = Qt.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Norm_LCC_Table.setVerticalHeaderItem(3, item)
        item = Qt.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Norm_LCC_Table.setVerticalHeaderItem(4, item)
        item = Qt.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Norm_LCC_Table.setVerticalHeaderItem(5, item)
        item = Qt.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Norm_LCC_Table.setVerticalHeaderItem(6, item)
        item = Qt.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Norm_LCC_Table.setVerticalHeaderItem(7, item)
        item = Qt.QTableWidgetItem()
        self.Norm_LCC_Table.setHorizontalHeaderItem(0, item)
        self.Norm_LCC_Table.horizontalHeader().setVisible(True)
        self.Norm_LCC_Table.horizontalHeader().setDefaultSectionSize(70)
        self.Norm_LCC_Table.horizontalHeader().setMinimumSectionSize(70)
        self.Norm_LCC_Table.verticalHeader().setDefaultSectionSize(24)
        self.Norm_LCC_Table.verticalHeader().setMinimumSectionSize(24)
        self.Norm_LCC_Table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.Norm_LCC_Table)
        #self.verticalLayout.addWidget(self.Norm_Space_Frame)
        #spacerItem2 = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Minimum, Qt.QSizePolicy.Expanding)
        #self.verticalLayout.addItem(spacerItem2)
        
        self.verticalLayout.addWidget(self.Norm_Save_Button)
        
        # spacerItem2 = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Minimum, Qt.QSizePolicy.Expanding)
        # self.verticalLayout.addItem(spacerItem2)
        
        self.verticalLayout.addWidget(self.Norm_Continue_Button)
        
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.horizontalLayout = Qt.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Norm_Interval_Label = Qt.QLabel(self.Norm_Right_Frame)
        sizePolicy = Qt.QSizePolicy(Qt.QSizePolicy.Preferred, Qt.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Norm_Interval_Label.sizePolicy().hasHeightForWidth())
        self.Norm_Interval_Label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setItalic(True)
        self.Norm_Interval_Label.setFont(font)
        self.Norm_Interval_Label.setObjectName(_fromUtf8("Norm_Interval_Label"))
        self.horizontalLayout.addWidget(self.Norm_Interval_Label)
        spacerItem3 = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.Norm_Interval_Colon_Label = Qt.QLabel(self.Norm_Right_Frame)
        self.Norm_Interval_Colon_Label.setMinimumSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Norm_Interval_Colon_Label.setFont(font)
        self.Norm_Interval_Colon_Label.setObjectName(_fromUtf8("Norm_Interval_Colon_Label"))
        self.horizontalLayout.addWidget(self.Norm_Interval_Colon_Label)
        self.Norm_Interval_Lineedit = Qt.QLineEdit(self.Norm_Right_Frame)
        self.Norm_Interval_Lineedit.setMaximumSize(QtCore.QSize(100, 20))
        self.Norm_Interval_Lineedit.setObjectName(_fromUtf8("Norm_Interval_Lineedit"))
        self.validator_P = QtGui.QDoubleValidator()
        self.Norm_Interval_Lineedit.setValidator(self.validator_P)
        self.horizontalLayout.addWidget(self.Norm_Interval_Lineedit)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.Norm_Right_Frame, 0, 2, 3, 1)
        Normalization_Widget.setCentralWidget(self.centralwidget)
        
        self.Normalization_win = PlotDialog(edit=False, toolbar=True)
        self.Normalization_plot = self.Normalization_win.get_plot()
        
        self.toolbar = self.Normalization_win.get_toolbar()
        self.icons  = self.toolbar.actions()
        self.icons[7].setVisible(False)
        self.icons[8].setVisible(False)
        
        
        self.Normalization_ToolBar_Layout  = Qt.QHBoxLayout(self.Norm_ToolBar_Frame)
        self.Normalization_ToolBar_Layout.setContentsMargins(0, 0, 0, 0)
        self.Normalization_ToolBar_Layout.setObjectName(_fromUtf8("verticalLayout"))
        self.Normalization_ToolBar_Layout.addWidget(self.Normalization_win)

        self.Norm_Save_Button.clicked.connect(self.Save_Button)
        self.Norm_Continue_Button.clicked.connect(self.Continue_NormLC)
        self.Norm_NormLC_Button.clicked.connect(self.Norm_NormLC)
        self.Norm_Phase_Button.clicked.connect(self.NZ_Phase)
        self.Norm_Calculaton_Button.clicked.connect(self.Norm_Calculate)
        self.Norm_Show_Button.clicked.connect(self.Norm_Show)
        
        self.retranslateUi(Normalization_Widget)
        QtCore.QMetaObject.connectSlotsByName(Normalization_Widget)

    def retranslateUi(self, Normalization_Widget):
        Normalization_Widget.setWindowTitle(_translate("Normalization_Widget", "Normalization Window", None))
        self.Norm_Phase_Button.setText(_translate("Normalization_Widget", "Phase", None))
        self.Norm_Save_Button.setText(_translate("Normalization_Widget", "Save Table", None))
        self.Norm_NormLC_Button.setText(_translate("Normalization_Widget", "Norm. LC", None))
        self.Norm_Calculaton_Button.setText(_translate("Normalization_Widget", "Calculate", None))
        self.Norm_Show_Button.setText(_translate("Normalization_Widget", "Show", None))
        self.Norm_LCC_Lable.setText(_translate("Normalization_Widget", "Light Curve Characterictis", None))
        self.Norm_Continue_Button.setText(_translate("Normalization_Widget", "Continue with Norm. LC", None))
        item = self.Norm_LCC_Table.verticalHeaderItem(0)
        item.setText(_translate("Normalization_Widget", "Min 1", None))
        item = self.Norm_LCC_Table.verticalHeaderItem(1)
        item.setText(_translate("Normalization_Widget", "Min 2", None))
        item = self.Norm_LCC_Table.verticalHeaderItem(2)
        item.setText(_translate("Normalization_Widget", "Max 1", None))
        item = self.Norm_LCC_Table.verticalHeaderItem(3)
        item.setText(_translate("Normalization_Widget", "Max 2", None))
        item = self.Norm_LCC_Table.verticalHeaderItem(4)
        item.setText(_translate("Normalization_Widget", "Min 1 Depth", None))
        item = self.Norm_LCC_Table.verticalHeaderItem(5)
        item.setText(_translate("Normalization_Widget", "Min 2 Depth", None))
        item = self.Norm_LCC_Table.verticalHeaderItem(6)
        item.setText(_translate("Normalization_Widget", "Delta Max", None))
        item = self.Norm_LCC_Table.verticalHeaderItem(7)
        item.setText(_translate("Normalization_Widget", "Delta Min", None))
        item = self.Norm_LCC_Table.horizontalHeaderItem(0)
        item.setText(_translate("Normalization_Widget", "", None))
        self.Norm_Interval_Label.setText(_translate("Normalization_Widget", "Interval", None))
        self.Norm_Interval_Colon_Label.setText(_translate("Normalization_Widget", ":", None))
        
    def Save_Button(self):
        path = Qt.QFileDialog.getSaveFileName(
                        Qt.QMainWindow(), 'Save File', '', 'TXT(*.txt)')
                        
        try:    
            data_save = open(str(path),'w')
            
            for i in range(self.Norm_LCC_Table.rowCount()):
                LCC = self.Norm_LCC_Table.item(i,0)
                data_save.write(self.Norm_LCC_Table.verticalHeaderItem(i).text() \
                    +' '+'='+' '+LCC.text()+'\n')
                    
            data_save.close()
        except:
            pass    
    
    def Norm_Show(self):
        IL = self.Norm_Interval_Lineedit.text()
        
        items =  self.Normalization_plot.get_items()

        self.Normalization_plot.del_items(items[2:])                

        if (str(IL).replace('.','',1).isdigit() == True
        and 1 >= float(IL) > 0):
            
            IL = float(IL)

            ToVS = XM.ui.MG.Info_Table.item(3,0).text()

            for i in range(1 if ToVS == 'EBS' else 4,5):
                Range_item = XRangeSelection(0.25*i - IL,0.25*i + IL)
                self.Normalization_plot.add_item(Range_item)
                
            self.Normalization_plot.show_items()
            
            self.Norm_Continue_Button.setEnabled(False)
            self.Norm_Calculaton_Button.setEnabled(True)
            
        else:
             Qt.QMessageBox.question(XM.window, 'Message',
                'Please enter a number that is between 0 and 1!',
                Qt.QMessageBox.Ok)
 
    def Norm_Calculate(self):
        yLabel = XM.ui.OD.yAxis_ComboBox.currentText()
        
        items =  self.Normalization_plot.get_items()
    
        ToVS = XM.ui.MG.Info_Table.item(3,0).text()

        if ToVS == 'EBS':
            Avg025 = np.average(cl.PlotRangeData(items[1],items[2])[1])
            Avg050 = np.average(cl.PlotRangeData(items[1],items[3])[1])
            Avg075 = np.average(cl.PlotRangeData(items[1],items[4])[1])
            Avg100 = np.average(cl.PlotRangeData(items[1],items[5])[1])
            max_point_where = [Avg075,Avg025]
            
            self.Norm_LCC_Table.setItem(0,0,Qt.QTableWidgetItem('%07f' % Avg100))
            self.Norm_LCC_Table.setItem(1,0,Qt.QTableWidgetItem('%07f' % Avg050))
            self.Norm_LCC_Table.setItem(2,0,Qt.QTableWidgetItem('%07f' % Avg025))
            self.Norm_LCC_Table.setItem(3,0,Qt.QTableWidgetItem('%07f' % Avg075))
            self.Norm_LCC_Table.setItem(4,0,Qt.QTableWidgetItem('%07f' % (Avg025-Avg100)))
            self.Norm_LCC_Table.setItem(5,0,Qt.QTableWidgetItem('%07f' % (Avg075-Avg050)))
            self.Norm_LCC_Table.setItem(6,0,Qt.QTableWidgetItem('%07f' % (Avg025-Avg075)))
            self.Norm_LCC_Table.setItem(7,0,Qt.QTableWidgetItem('%07f' % (Avg100-Avg050)))
        else:
            Avg100 = np.average(cl.PlotRangeData(items[1],items[2])[1])
            max_point_where = [Avg100]
        
        data_norm = np.array(XM.ui.MG.Data_norm)
        Phase_norm = np.array(XM.ui.MG.Phase_norm)

        data_y = XM.ui.OD.data_y
        
        try:
            if yLabel == 'Magnitude':
                max_point = min(max_point_where)
    #            print max_point
    #            if -0.4*(data_y-max_point) <= 308:
                self.Norm_data_y = 10**(-0.4*(data_y-max_point))
                Norm = 10**(-0.4*(data_norm-max_point))
    #            else:
    #                Qt.QMessageBox.question(XM.window, 'Message',
    #            'Values of magnitude too big. Please checck your magnitude values',
    #            Qt.QMessageBox.Ok)
                
            else:
                max_point = max(max_point_where)
                self.Norm_data_y = data_y/float(max_point)
                Norm = data_norm/float(max_point)
    
            self.Normalization_plot.del_all_items()
            self.Normalization_plot.set_axis_title("left",'Normalized Flux')
            self.Normalization_plot.set_axis_title("bottom",'Phase')
            curve_item = make.curve(Phase_norm, Norm, marker='+', linestyle='NoPen',
                                        markerfacecolor='k',markeredgecolor='k', markersize=7)
            curve_one = make.curve(Phase_norm, [1]*len(Phase_norm),color='red')
            self.Normalization_plot.set_axis_direction(0, reverse=False)
            self.Normalization_plot.add_item(curve_item)
            self.Normalization_plot.add_item(curve_one)
            self.Normalization_plot.do_autoscale()
    
            self.Norm_Show_Button.setEnabled(False)
            self.Norm_NormLC_Button.setEnabled(True)
            self.Norm_Calculaton_Button.setEnabled(False)
            self.Norm_Continue_Button.setEnabled(True)
            self.Norm_Save_Button.setEnabled(True)
        
        except:
            self.Norm_Continue_Button.setEnabled(False)
            Qt.QMessageBox.question(XM.window, 'Message',
                'There is no any data point where selected one or more regions.' \
                ' If you want to get a healthy result, please check your regions',
                Qt.QMessageBox.Ok)
  
    def NZ_Phase(self):
        yLabel = XM.ui.MG.Graph_Plot.axisTitle(0).text()
        
        Phase_add_025 = XM.ui.MG.Phase_add_025
        data_add_025 = XM.ui.MG.Data_add_025
       
        self.Normalization_plot.del_all_items()
        self.Normalization_plot.set_axis_title("left", yLabel)
        self.Normalization_plot.set_axis_title("bottom",'Phase')
        curve_item = make.curve(Phase_add_025, data_add_025, marker='+', linestyle='NoPen',
                                    markerfacecolor='k',markeredgecolor='k', markersize=7)
        self.Normalization_plot.add_item(curve_item)
        if yLabel == 'Magnitude':
            self.Normalization_plot.set_axis_direction(0, reverse=True)
        self.Normalization_plot.do_autoscale()
        
        self.Norm_Show_Button.setEnabled(True)
        self.Norm_Calculaton_Button.setEnabled(False)
    
    def Norm_NormLC(self):
        data_x = XM.ui.OD.data_x
        
        self.Normalization_plot.del_all_items()
        self.Normalization_plot.set_axis_title("left",'Normalized Flux')
        self.Normalization_plot.set_axis_title("bottom",'Phase')
        curve_item = make.curve(data_x, self.Norm_data_y, marker='+', linestyle='NoPen',
                                    markerfacecolor='k',markeredgecolor='k', markersize=7)
        self.Normalization_plot.add_item(curve_item)
        self.Normalization_plot.do_autoscale()
        
        self.Norm_Show_Button.setEnabled(False)
        self.Norm_Calculaton_Button.setEnabled(False)
        
    def Continue_NormLC(self):
        data_x = XM.ui.OD.data_x
        XM.ui.OD.data_y = self.Norm_data_y

        yLabel = self.Normalization_plot.axisTitle(0).text()
        
        reply = Qt.QMessageBox.question(XM.window, 'Message',
        "Are you sure want to continue with Normalized Light Curve?" \
        ' Do not forget! If you select ''yes'', raw data will be lost!',
        Qt.QMessageBox.Yes, Qt.QMessageBox.No)
        
        if reply == Qt.QMessageBox.Yes:
            XM.ui.MG.Graph_Plot.del_all_items()
            XM.ui.MG.Graph_Plot.set_axis_title("left",yLabel)
            #XM.ui.MG.Graph_Plot.set_axis_title("bottom",xLabel)
            curve_item = make.curve(data_x, self.Norm_data_y, marker='+', linestyle='NoPen',
                                        markerfacecolor='k',markeredgecolor='k', markersize=7)
            XM.ui.MG.Graph_Plot.set_axis_direction(0, reverse=False)
            XM.ui.MG.Graph_Plot.add_item(curve_item)
            XM.ui.MG.Graph_Plot.do_autoscale()
            
            XM.ui.MG.Info_Table.setItem(2,0,
                        Qt.QTableWidgetItem("Norm. Flux"))
            
            XM.ui.Normalization_Window.close()
            XM.ui.OD.yAxis_ComboBox.setCurrentIndex(0)
#################################################################
"Normalization Window End"
#################################################################

class Normalization(Qt.QMainWindow):
    def closeEvent(self,event):
        XM.ui.MG.Activate_Buttons()
        """
        reply =  Qt.QMessageBox.question(XM.window, 'Message',
                'Please enter a valid Oversampling factor and Nyquist limit value',
        Qt.QMessageBox.Yes, Qt.QMessageBox.No)
        event.ignore()
        
        if  reply == Qt.QMessageBox.Yes:
            
            XGF.Activate_Buttons()
            #self.MinMax_Table.clear()
        
            event.accept()"""
        