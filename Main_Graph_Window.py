# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 05:26:23 2015

@author: TheLichWing
"""

import numpy as np
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets as Qt
from plotpy.builder import make
import Main_Window as XM
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
"Main_Graph Window Start"
#################################################################
class Main_Graph_Window(object):
    def setupUi(self, Main_Graph_Window):
   
        Main_Graph_Window.resize(590, 385)
        Main_Graph_Window.setMinimumSize(590, 385)
        #Main_Graph_Window.setStyle(Qt.QStyleFactory.create('cleanlooks'))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/MG.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main_Graph_Window.setWindowIcon(icon)
        
        self.centralwidget = Qt.QWidget(Main_Graph_Window)

        self.Main_GLayout = Qt.QGridLayout(self.centralwidget)
        self.Main_GLayout.setContentsMargins(2, 2, 2, 2)
        self.Main_GLayout.setSpacing(2)
        
        self.RFrame = Qt.QFrame(self.centralwidget)
        self.RFrame.setMinimumSize(155, 0)
        self.RFrame.setFrameShape(Qt.QFrame.StyledPanel)
        self.RFrame.setFrameShadow(Qt.QFrame.Raised)
        self.RFrame.setMaximumSize(155, 16777215)
        
        self.RFrame_VLayout = Qt.QVBoxLayout(self.RFrame)
        self.RFrame_VLayout.setContentsMargins(0, 1, 0, 1)

        self.Periodogram_Button = Qt.QPushButton(self.RFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Periodogram_Button.setFont(font)
        
        self.RFrame_VLayout.addWidget(self.Periodogram_Button)
        
        self.Normalization_Button = Qt.QPushButton(self.RFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Normalization_Button.setFont(font)

        self.RFrame_VLayout.addWidget(self.Normalization_Button)
        
        self.Optimization_Button = Qt.QPushButton(self.RFrame)
        self.Optimization_Button.setEnabled(False)
        self.Optimization_Button.hide()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Optimization_Button.setFont(font)

        self.RFrame_VLayout.addWidget(self.Optimization_Button)
        
        self.MinMaxCalculation_Button = Qt.QPushButton(self.RFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.MinMaxCalculation_Button.setFont(font)
        
        self.RFrame_VLayout.addWidget(self.MinMaxCalculation_Button)
        
        self.Info_Table = Qt.QTableWidget(self.RFrame)
        self.Info_Table.setMaximumSize(160, 160)        
        self.Info_Table.setColumnCount(1)
        self.Info_Table.setRowCount(4)
        item = Qt.QTableWidgetItem()
        self.Info_Table.setVerticalHeaderItem(0, item)
        item = Qt.QTableWidgetItem()
        self.Info_Table.setVerticalHeaderItem(1, item)
        item = Qt.QTableWidgetItem()
        self.Info_Table.setVerticalHeaderItem(2, item)
        item = Qt.QTableWidgetItem()
        self.Info_Table.setVerticalHeaderItem(3, item)
        item = Qt.QTableWidgetItem()
        self.Info_Table.setVerticalHeaderItem(4, item)
        self.Info_Table.horizontalHeader().setVisible(False)
        self.Info_Table.setEditTriggers(Qt.QAbstractItemView.NoEditTriggers)
        self.Info_Table.verticalHeader().setSectionResizeMode(Qt.QHeaderView.Stretch)
        
        self.RFrame_VLayout.addWidget(self.Info_Table)
        
        self.Main_GLayout.addWidget(self.RFrame, 0, 2, 3, 1)
        
        self.BFrame = Qt.QFrame(self.centralwidget)

        self.BFrame.setMinimumSize(400, 40)
        self.BFrame.setMaximumSize(16777215, 40)
        self.BFrame.setFrameShape(Qt.QFrame.StyledPanel)
        self.BFrame.setFrameShadow(Qt.QFrame.Raised)

        self.BFrame_HLayout = Qt.QHBoxLayout(self.BFrame)
        spacerItem1 = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.BFrame_HLayout.addItem(spacerItem1)

        self.LElements_GroupBox = Qt.QGroupBox(self.RFrame)      
        self.LElements_VLayout = Qt.QVBoxLayout(self.LElements_GroupBox)
        self.LElements_VLayout.setContentsMargins(2,2,2,2)
        
        self.RFrame_VLayout.addWidget(self.LElements_GroupBox)
        
        self.T0_Label = Qt.QLabel(self.RFrame)
        self.T0_Label.setMinimumSize(0, 23)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.T0_Label.setFont(font)

        self.T0_Lineedit = Qt.QLineEdit(self.RFrame)
        self.T0_Validator = QtGui.QDoubleValidator()
        self.T0_Lineedit.setValidator(self.T0_Validator)
        self.T0_Lineedit.setMinimumSize(120, 20)


        self.LElements_VLayout.addWidget(self.T0_Label)
        self.LElements_VLayout.addWidget(self.T0_Lineedit)
        
        self.P_Label = Qt.QLabel()
        self.P_Label.setMinimumSize(0, 23)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.P_Label.setFont(font)

        self.P_Lineedit = Qt.QLineEdit()
        self.P_Validator = QtGui.QDoubleValidator()
        self.P_Lineedit.setValidator(self.P_Validator)
        self.P_Lineedit.setMinimumSize(120, 20)

        self.LElements_VLayout.addWidget(self.P_Label)
        self.LElements_VLayout.addWidget(self.P_Lineedit) 
         
        spacerItem = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Minimum, Qt.QSizePolicy.Expanding)
        self.RFrame_VLayout.addItem(spacerItem)
        
        self.Phase_Button = Qt.QPushButton(self.BFrame)
        self.Phase_Button.setMinimumSize(0, 23)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Phase_Button.setFont(font)

        self.BFrame_HLayout.addWidget(self.Phase_Button)
        
        self.LightCurve_Button = Qt.QPushButton(self.BFrame)
        self.LightCurve_Button.setMinimumSize(0, 23)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.LightCurve_Button.setFont(font)

        self.BFrame_HLayout.addWidget(self.LightCurve_Button)
        spacerItem2 = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.BFrame_HLayout.addItem(spacerItem2)
        
        self.Main_GLayout.addWidget(self.BFrame, 2, 0, 1, 1)
        
        self.Graph_Frame = Qt.QFrame(self.centralwidget)
        self.Graph_Frame.setFrameShape(Qt.QFrame.StyledPanel)
        self.Graph_Frame.setFrameShadow(Qt.QFrame.Raised)
        
        self.Main_GLayout.addWidget(self.Graph_Frame, 0, 0, 1, 1)
        
        self.line = Qt.QFrame(self.centralwidget)
        self.line.setFrameShape(Qt.QFrame.VLine)
        self.line.setFrameShadow(Qt.QFrame.Sunken)

        self.Main_GLayout.addWidget(self.line, 0, 1, 3, 1)
        
        self.Graph_Win = PlotDialog(edit=False, toolbar=True)
        self.Graph_Plot = self.Graph_Win.get_plot()
        self.Graph_Toolbar = self.Graph_Win.get_toolbar()
        
        self.Graph_Icons  = self.Graph_Toolbar.actions()
        self.Graph_Icons[7].setVisible(False)
        self.Graph_Icons[8].setVisible(False)

        self.Graph_HLayout  = Qt.QHBoxLayout(self.Graph_Frame)
        self.Graph_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Graph_HLayout.addWidget(self.Graph_Win)
        
#        self.Phase_norm = []
#        self.Data_norm = []
#        self.Phase_add_025 = []
#        self.Data_add_025 = []
        
        Main_Graph_Window.setCentralWidget(self.centralwidget)

        #self.Optimization_Button.clicked.connect(self.Optimization_Win)
        self.MinMaxCalculation_Button.clicked.connect(self.MinMax_Win)
        self.Phase_Button.clicked.connect(self.Phase)
        self.LightCurve_Button.clicked.connect(self.LCurve)
        self.Periodogram_Button.clicked.connect(self.Periodogram_Win)
        self.Normalization_Button.clicked.connect(self.Normalization_Win)
  
        self.retranslateUi(Main_Graph_Window)
        QtCore.QMetaObject.connectSlotsByName(Main_Graph_Window)

    def retranslateUi(self, Main_Graph_Window):
        Main_Graph_Window.setWindowTitle(_translate("Main_Graph_Window", "Graph Window", None))
        self.Periodogram_Button.setText(_translate("Main_Graph_Window", "Periodogram", None))
        self.Normalization_Button.setText(_translate("Main_Graph_Window", "Normalization", None))
        self.Optimization_Button.setText(_translate("Main_Graph_Window", "Optimization", None))
        self.MinMaxCalculation_Button.setText(_translate("Main_Graph_Window", "Min/Max Calculation", None))
        
        item = self.Info_Table.verticalHeaderItem(0)
        item.setText(_translate("Main_Graph_Window", "Points", None))
        item = self.Info_Table.verticalHeaderItem(3)
        item.setText(_translate("Main_Graph_Window", "Type", None)) 
        item = self.Info_Table.verticalHeaderItem(1)
        item.setText(_translate("Main_Graph_Window", "Time", None))
        item = self.Info_Table.verticalHeaderItem(2)
        item.setText(_translate("Main_Graph_Window", "Brightness", None))

        self.T0_Label.setText(_translate("Main_Graph_Window", "Referans Min/Max Time :", None))
        self.P_Label.setText(_translate("Main_Graph_Window", "Period :", None))
        self.Phase_Button.setText(_translate("Main_Graph_Window", "Phase", None))
        self.LightCurve_Button.setText(_translate("Main_Graph_Window", "Light Curve(s)", None))
    

    def Optimization_Win(self):
        
        xLabel = XM.ui.MG.Graph_Plot.axisTitle(2).text()
        yLabel = XM.ui.MG.Graph_Plot.axisTitle(0).text()
        
        data_x = XM.ui.OD.data_x
        data_y = XM.ui.OD.data_y
        
        
       
        XM.ui.OW.Graph_Plot.del_all_items() 
        XM.ui.OW.Graph_Plot.set_axis_title("left", yLabel)
        XM.ui.OW.Graph_Plot.set_axis_title("bottom", xLabel)
        XM.ui.OW.Graph_Plot.set_axis_font("left", QtGui.QFont("Courier", 10, 100))
        XM.ui.OW.Graph_Plot.set_axis_font("bottom", QtGui.QFont("Courier", 10, 100))
        XM.ui.OW.Graph_Plot.set_axis_direction(0, reverse=False)
        if yLabel == 'Magnitude':
            XM.ui.OW.Graph_Plot.set_axis_direction(0, reverse=True)
        XM.ui.OW.Graph_Plot.set_antialiasing(True) 
        curve_item = make.curve(data_x, data_y, marker='+', linestyle='NoPen',
                                    markerfacecolor='k',markeredgecolor='k', markersize=7)
        XM.ui.OW.Graph_Plot.add_item(curve_item)
        XM.ui.OW.Graph_Plot.do_autoscale()
        XM.ui.OW.Graph_Plot.show_items()
        
        

        
        XM.ui.MG.deActivate_Buttons()
        
        
        XM.ui.Optimization_Window.show()
        
    
    def Periodogram_Win(self):
        XM.ui.PD.Calculate_Button.setEnabled(True)

        xLabel = XM.ui.MG.Graph_Plot.axisTitle(2).text()
        yLabel = XM.ui.MG.Graph_Plot.axisTitle(0).text()
        
        data_x = XM.ui.OD.data_x
        data_y = XM.ui.OD.data_y
        
        from plotpy.items import XRangeSelection
        
        P_range = XRangeSelection(min(data_x), max(data_x))
        P_range_col = QtGui.QColor('green')
        P_range.pen.setColor(P_range_col)
        P_range.sel_pen.setColor(P_range_col)

#        a = P_range.symbol.brush()
#        a.setColor(P_range_col)

        P_range_col.setAlphaF(.15)
        P_range.brush.setColor(P_range_col)
        
        x_mid = (max(data_x) + min(data_x))/2.
        T0_range = XRangeSelection(x_mid - (max(data_x)- min(data_x)) / 50.,
                                   x_mid + (max(data_x)- min(data_x)) / 50.)
        
        #print x_mid - (max(data_x)- min(data_x)) / 25.,x_mid + (max(data_x)- min(data_x)) / 25.
                 
        XM.ui.PD.Plot.del_all_items()
        XM.ui.PD.Plot.set_axis_title("left", yLabel)
        XM.ui.PD.Plot.set_axis_title("bottom", xLabel)
        XM.ui.PD.Plot.set_axis_font("left", QtGui.QFont("Courier", 10, 100))
        XM.ui.PD.Plot.set_axis_font("bottom", QtGui.QFont("Courier", 10, 100))
        XM.ui.PD.Plot.set_axis_direction(0, reverse=False)
        if yLabel == 'Magnitude':
            XM.ui.PD.Plot.set_axis_direction(0, reverse=True)
        XM.ui.PD.Plot.set_antialiasing(True) 
        curve_item = make.curve(data_x, data_y, marker='+', linestyle='NoPen',
                                    markerfacecolor='k',markeredgecolor='k', markersize=7)
        XM.ui.PD.Plot.add_item(curve_item)
        XM.ui.PD.Plot.add_item(P_range)
        XM.ui.PD.Plot.add_item(T0_range)
        XM.ui.PD.Plot.do_autoscale()
        XM.ui.PD.Plot.show_items()
        
        XM.ui.MG.deActivate_Buttons()
        XM.ui.Periodogram_Window.show()
        
    def Normalization_Win(self):
        if XM.ui.OD.ToVS_ComboBox.currentIndex() == 1:
            XM.ui.NZ.Norm_LCC_Table.setEnabled(False)
            XM.ui.NZ.Norm_Save_Button.setEnabled(False)
        
        yLabel = XM.ui.MG.Graph_Plot.axisTitle(0).text()
        XM.ui.NZ.Norm_LCC_Table.horizontalHeaderItem(0).setText(yLabel)
        
        data_x = XM.ui.OD.data_x
        data_y = XM.ui.OD.data_y
        
        T0 = XM.ui.MG.T0_Lineedit.text()
        P = XM.ui.MG.P_Lineedit.text()
        
        if str(T0).replace('.','',1).isdigit() and str(P).replace('.','',1).isdigit() \
            == True:
            
            T0 = float(T0)
            P = float(P)
            
            Phase_norm = ((data_x - T0)/P)- np.floor((data_x - T0)/P)
            
            Data_norm = data_y[np.argsort(Phase_norm)]
            Phase_norm = Phase_norm[np.argsort(Phase_norm)]
            
            w025 = np.argwhere(Phase_norm < 0.25)
            w025 = np.reshape(w025, (len(w025),))
            
            Phase_add_025 = np.hstack((Phase_norm, Phase_norm[w025] + 1))
            Data_add_025 = np.hstack((Data_norm, Data_norm[w025]))
            
            self.Phase_norm = Phase_norm
            self.Data_norm = Data_norm
            self.Phase_add_025 = Phase_add_025
            self.Data_add_025 = Data_add_025
            
            XM.ui.NZ.Normalization_plot.del_all_items() 
            XM.ui.NZ.Normalization_plot.set_axis_title("left", yLabel)
            XM.ui.NZ.Normalization_plot.set_axis_title("bottom", "Phase")
            XM.ui.NZ.Normalization_plot.set_axis_font("left", QtGui.QFont("Courier", 10, 100))
            XM.ui.NZ.Normalization_plot.set_axis_font("bottom", QtGui.QFont("Courier", 10, 100))
            XM.ui.NZ.Normalization_plot.set_axis_direction(0, reverse=False)
            if yLabel == 'Magnitude':
                XM.ui.NZ.Normalization_plot.set_axis_direction(0, reverse=True)
            XM.ui.NZ.Normalization_plot.set_antialiasing(True)
            
            curve_item = make.curve(Phase_add_025, Data_add_025, marker='+', linestyle='NoPen',
                                        markerfacecolor='k',markeredgecolor='k', markersize=7)
            XM.ui.NZ.Normalization_plot.add_item(curve_item)
            XM.ui.NZ.Normalization_plot.do_autoscale()
            XM.ui.NZ.Normalization_plot.show_items()
            
            XM.ui.MG.deActivate_Buttons()
            
            XM.ui.NZ.Norm_Continue_Button.setEnabled(False)
            XM.ui.NZ.Norm_Show_Button.setEnabled(True)
            XM.ui.NZ.Norm_Calculaton_Button.setEnabled(False)
            XM.ui.NZ.Norm_NormLC_Button.setEnabled(False)
            XM.ui.NZ.Norm_Save_Button.setEnabled(False)
            
            XM.ui.Normalization_Window.show()
        
        else:
            
            Qt.QMessageBox.question(XM.window, 'Message',
            'Please enter a valid T0 and P value. If you dont have' \
            ' them, then you can go Periodogram section!', Qt.QMessageBox.Ok)

    def MinMax_Win(self):
        XM.ui.MM.setupUi(XM.ui.MinMax_Window)
        xLabel = XM.ui.MG.Graph_Plot.axisTitle(2).text()
        yLabel = XM.ui.MG.Graph_Plot.axisTitle(0).text()
        
        data_x = XM.ui.OD.data_x
        data_y = XM.ui.OD.data_y
        

        XM.ui.MM.Graph_Plot.del_all_items() 
        XM.ui.MM.Graph_Plot.set_axis_title("left",yLabel)
        XM.ui.MM.Graph_Plot.set_axis_title("bottom", xLabel)
        XM.ui.MM.Graph_Plot.set_axis_font("left", QtGui.QFont("Courier", 10, 100))
        XM.ui.MM.Graph_Plot.set_axis_font("bottom", QtGui.QFont("Courier", 10, 100))
        XM.ui.MM.Graph_Plot.set_axis_direction(0, reverse=False)
        if yLabel == 'Magnitude':
            XM.ui.MM.Graph_Plot.set_axis_direction(0, reverse=True)
        XM.ui.MM.Graph_Plot.set_antialiasing(True) 
        curve_item = make.curve(data_x, data_y, marker='+', linestyle='NoPen',
                                    markerfacecolor='k',markeredgecolor='k', markersize=7)
        XM.ui.MM.Graph_Plot.add_item(curve_item)
        XM.ui.MM.Graph_Plot.do_autoscale()
        XM.ui.MM.Graph_Plot.show_items()
        
        XM.ui.MG.deActivate_Buttons()
        XM.ui.MinMax_Window.show()

        
    def Phase(self):

        data_x = XM.ui.OD.data_x
        data_y = XM.ui.OD.data_y
        
        T0 = self.T0_Lineedit.text()
        P = self.P_Lineedit.text()
        
        
        if str(P).replace('.','',1).isdigit() == True and \
            str(T0).replace('.','',1).isdigit() == True:
                
            Phase = ((np.array(data_x) - float(T0))/float(P))- \
            np.floor((np.array(data_x) - float(T0))/float(P))
    
            data = data_y[np.argsort(Phase)]
            Phase = Phase[np.argsort(Phase)]
            
            
            self.Graph_Plot.del_all_items()
            self.Graph_Plot.set_axis_title("bottom",'Phase')
            curve_item = make.curve(Phase, data, marker='+', linestyle='NoPen',
                                    markerfacecolor='k',markeredgecolor='k', markersize=7)
            self.Graph_Plot.add_item(curve_item)
            self.Graph_Plot.do_autoscale()
    
        elif str(T0).replace('.','',1).isdigit() == False \
                and str(P).replace('.','',1).isdigit() == True:
                Qt.QMessageBox.question(XM.window, 'Message',
            'Please enter a valid Referans Min/Max Time value', Qt.QMessageBox.Ok)
            
        elif str(P).replace('.','',1).isdigit() == False \
            and str(T0).replace('.','',1).isdigit() == True:
            Qt.QMessageBox.question(XM.window, 'Message',
        'Please enter a valid Period value', Qt.QMessageBox.Ok)
        
        elif (str(T0) and str(P)).replace('.','',1).isdigit() == False:
            Qt.QMessageBox.question(XM.window, 'Message',
        'Please enter a valid Referans Min/Max Time and Period value', Qt.QMessageBox.Ok)



    def LCurve(self):

        
        data_x = XM.ui.OD.data_x
        data_y = XM.ui.OD.data_y
        
        xLabel = XM.ui.OD.xAxis_ComboBox.currentText()
        
        self.Graph_Plot.del_all_items() 
        self.Graph_Plot.set_axis_title("bottom",xLabel)
        curve_item = make.curve(data_x, data_y, marker='+', linestyle='NoPen',
                                    markerfacecolor='k',markeredgecolor='k', markersize=7)
        self.Graph_Plot.add_item(curve_item)
        self.Graph_Plot.do_autoscale()
        
    def deActivate_Buttons(self):

        self.Periodogram_Button.setEnabled(False)
        self.Normalization_Button.setEnabled(False)
        self.MinMaxCalculation_Button.setEnabled(False)
        self.Optimization_Button.setEnabled(False)
        
    def Activate_Buttons(self):
    
        self.Periodogram_Button.setEnabled(True)
        self.Normalization_Button.setEnabled(True)
        self.MinMaxCalculation_Button.setEnabled(True)
        self.Optimization_Button.setEnabled(True) 


import sys
app = Qt.QApplication(sys.argv)
app.setStyle(Qt.QStyleFactory.create("cleanlooks"))
window = Qt.QMainWindow()
ui = Main_Graph_Window()
ui.setupUi(window)
#################################################################
"Main_Graph Window End"
#################################################################   
