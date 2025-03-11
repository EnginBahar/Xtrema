# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Xtrema_Optimization_Window.ui'
#
# Created: Mon Jul 13 01:03:34 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets as Qt
from plotpy.plot import PlotDialog
import Main_Window as XM
from plotpy.builder import make
import numpy as np

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

class Xtrema_Optimization_Window(object):
    def setupUi(self, Xtrema_Optimization_Window):
        Xtrema_Optimization_Window.setObjectName(_fromUtf8("Xtrema_Optimization_Window"))
        Xtrema_Optimization_Window.resize(640, 480)
        self.centralwidget = Qt.QWidget(Xtrema_Optimization_Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = Qt.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.GFrame = Qt.QFrame(self.centralwidget)
        self.GFrame.setFrameShape(Qt.QFrame.StyledPanel)
        self.GFrame.setFrameShadow(Qt.QFrame.Raised)
        self.GFrame.setObjectName(_fromUtf8("GFrame"))
        self.gridLayout.addWidget(self.GFrame, 0, 0, 1, 1)
        self.RFrame = Qt.QFrame(self.centralwidget)
        self.RFrame.setMinimumSize(QtCore.QSize(150, 0))
        self.RFrame.setMaximumSize(QtCore.QSize(150, 16777215))
        self.RFrame.setFrameShape(Qt.QFrame.StyledPanel)
        self.RFrame.setFrameShadow(Qt.QFrame.Raised)
        self.RFrame.setObjectName(_fromUtf8("RFrame"))
        self.verticalLayout = Qt.QVBoxLayout(self.RFrame)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Reject_Point_GroupBox = Qt.QGroupBox(self.RFrame)
        self.Reject_Point_GroupBox.setObjectName(_fromUtf8("Reject_Point_GroupBox"))
        self.verticalLayout_2 = Qt.QVBoxLayout(self.Reject_Point_GroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = Qt.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        
        
        self.RP_Part_Label = Qt.QLabel(self.Reject_Point_GroupBox)
        self.RP_Part_Label.setObjectName(_fromUtf8("RP_Part_Label"))
        self.horizontalLayout.addWidget(self.RP_Part_Label)
        spacerItem = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.RP_Part_LineEdit = Qt.QLineEdit(self.Reject_Point_GroupBox)
        self.RP_Part_LineEdit.setObjectName(_fromUtf8("RP_Part_LineEdit"))
        """
        self.horizontalLayout_r = Qt.QHBoxLayout()
        self.horizontalLayout_r.setObjectName(_fromUtf8("horizontalLayout"))
        #self.Rejec_Value_Label = Qt.QLabel(self.Reject_Point_GroupBox)
        self.Rejec_Value_Label.setObjectName(_fromUtf8("RP_Part_Label"))
        self.Rejec_Value_LineEdit = Qt.QLineEdit(self.Reject_Point_GroupBox)
        self.Rejec_Value_LineEdit.setObjectName(_fromUtf8("RP_Part_LineEdit"))
        self.horizontalLayout_r.addWidget(self.Rejec_Value_Label)
        self.horizontalLayout_r.addItem(spacerItem)
        self.horizontalLayout_r.addWidget(self.Rejec_Value_LineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_r)
        """
        
        self.horizontalLayout.addWidget(self.RP_Part_LineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = Qt.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.RP_StDev_Label = Qt.QLabel(self.Reject_Point_GroupBox)
        self.RP_StDev_Label.setObjectName(_fromUtf8("RP_StDev_Label"))
        self.horizontalLayout_2.addWidget(self.RP_StDev_Label)
        spacerItem1 = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.RP_StDev_LineEdit = Qt.QLineEdit(self.Reject_Point_GroupBox)
        self.RP_StDev_LineEdit.setObjectName(_fromUtf8("RP_StDev_LineEdit"))
        self.horizontalLayout_2.addWidget(self.RP_StDev_LineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.RP_Calculate_Button = Qt.QPushButton(self.Reject_Point_GroupBox)
        self.RP_Calculate_Button.setObjectName(_fromUtf8("RP_Calculate_Button"))
        
        self.Continue_Button = Qt.QPushButton(self.Reject_Point_GroupBox)
        self.Continue_Button.setObjectName(_fromUtf8("RP_Calculate_Button"))
        
        
        self.verticalLayout_2.addWidget(self.RP_Calculate_Button)
        self.verticalLayout.addWidget(self.Reject_Point_GroupBox)
        self.Normal_Point_GroupBox = Qt.QGroupBox(self.RFrame)
        self.Normal_Point_GroupBox.setObjectName(_fromUtf8("Normal_Point_GroupBox"))
        self.verticalLayout_3 = Qt.QVBoxLayout(self.Normal_Point_GroupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = Qt.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.NP_Part_label = Qt.QLabel(self.Normal_Point_GroupBox)
        self.NP_Part_label.setObjectName(_fromUtf8("NP_Part_label"))
        self.horizontalLayout_3.addWidget(self.NP_Part_label)
        self.NP_Part_LineEdit = Qt.QLineEdit(self.Normal_Point_GroupBox)
        self.NP_Part_LineEdit.setObjectName(_fromUtf8("NP_Part_LineEdit"))
        self.horizontalLayout_3.addWidget(self.NP_Part_LineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.NP_Calculation_Button = Qt.QPushButton(self.Normal_Point_GroupBox)
        self.NP_Calculation_Button.setObjectName(_fromUtf8("NP_Calculation_Button"))
        self.verticalLayout_3.addWidget(self.NP_Calculation_Button)
        self.verticalLayout.addWidget(self.Normal_Point_GroupBox)
        spacerItem2 = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Minimum, Qt.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout.addWidget(self.RFrame, 0, 1, 2, 1)
        self.BFrame = Qt.QFrame(self.centralwidget)
        self.BFrame.setMinimumSize(QtCore.QSize(400, 40))
        self.BFrame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.BFrame.setFrameShape(Qt.QFrame.StyledPanel)
        self.BFrame.setFrameShadow(Qt.QFrame.Raised)
        self.BFrame.setObjectName(_fromUtf8("BFrame"))
        self.horizontalLayout_4 = Qt.QHBoxLayout(self.BFrame)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem3 = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.Phase_Button = Qt.QPushButton(self.BFrame)
        self.Phase_Button.setObjectName(_fromUtf8("Phase_Button"))
        self.horizontalLayout_4.addWidget(self.Phase_Button)
        self.LightCurve_Button = Qt.QPushButton(self.BFrame)
        self.LightCurve_Button.setObjectName(_fromUtf8("LightCurve_Button"))
        self.horizontalLayout_4.addWidget(self.LightCurve_Button)
        spacerItem4 = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        
        self.verticalLayout.addWidget(self.Continue_Button)
        self.gridLayout.addWidget(self.BFrame, 1, 0, 1, 1)
        
        
        
        Xtrema_Optimization_Window.setCentralWidget(self.centralwidget)

        self.Graph_Win = PlotDialog(edit=False, toolbar=True)
        from plotpy.tools import CurveFit
        self.CurveFit = CurveFit
        self.Graph_Win.manager.add_tool(self.CurveFit)
        self.Graph_Plot = self.Graph_Win.get_plot()
        self.Graph_Plot.set_pointer('canvas')
        self.Graph_Toolbar = self.Graph_Win.get_toolbar()
        
        self.Graph_Icons  = self.Graph_Toolbar.actions()
        self.Graph_Icons[7].setVisible(False)
        self.Graph_Icons[8].setVisible(False)

        self.Graph_HLayout  = Qt.QHBoxLayout(self.GFrame)
        self.Graph_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Graph_HLayout.addWidget(self.Graph_Win)
        
        
        
        
        self.Graph_Plot.keyPressEvent = self.kRE
        self.Check = np.ones(1, dtype = float)*-1
        
        
        
        
        self.Continue_Button.clicked.connect(self.Continue_CurrentData)
        self.RP_Calculate_Button.clicked.connect(self.Reject_Point)
        self.NP_Calculation_Button.clicked.connect(self.Normal_Point)
        self.Phase_Button.clicked.connect(self.Phase)
        self.LightCurve_Button.clicked.connect(self.Light_Curve)
        
        
        self.retranslateUi(Xtrema_Optimization_Window)
        QtCore.QMetaObject.connectSlotsByName(Xtrema_Optimization_Window)

    def retranslateUi(self, Xtrema_Optimization_Window):
        Xtrema_Optimization_Window.setWindowTitle(_translate("Xtrema_Optimization_Window", "Optimization Window", None))
        self.Reject_Point_GroupBox.setTitle(_translate("Xtrema_Optimization_Window", "Reject Point", None))
        self.RP_Part_Label.setText(_translate("Xtrema_Optimization_Window", "Part    :", None))
        #self.Rejec_Value_Label.setText(_translate("Xtrema_Optimization_Window", "Value    :", None))
        self.RP_StDev_Label.setText(_translate("Xtrema_Optimization_Window", "StDev :", None))
        self.RP_Calculate_Button.setText(_translate("Xtrema_Optimization_Window", "Calculate", None))
        self.Normal_Point_GroupBox.setTitle(_translate("Xtrema_Optimization_Window", "Normal Point", None))
        self.NP_Part_label.setText(_translate("Xtrema_Optimization_Window", "Part    :   ", None))
        self.NP_Calculation_Button.setText(_translate("Xtrema_Optimization_Window", "Calculate", None))
        self.Continue_Button.setText(_translate("Xtrema_Optimization_Window", "Continue with This Data", None))
        self.Phase_Button.setText(_translate("Xtrema_Optimization_Window", "Phase", None))
        self.LightCurve_Button.setText(_translate("Xtrema_Optimization_Window", "Light Curve(s)", None))

    def Normal_Point(self):
        global NRP_x,NRP_y
        
        items = self.Graph_Plot.get_items()
        data = items[1].get_data()
        
        data_x = data[0]
        data_y = data[1]
        
        Part = self.NP_Part_LineEdit.text()
        Part = int(Part)
        
        
        sort = np.argsort(data_x)
        data_x = data_x[sort]
        data_y = data_y[sort]
        
        NRP_x = np.arange(0,dtype=float)
        NRP_y = np.arange(0,dtype=float)
        for i in range(Part):
            x = (len(data_x)/float(Part))
            #print i*x,(i+1)*x
            NRP_x = np.hstack((NRP_x,np.average(data_x[i*x:(i+1)*x])))
            NRP_y = np.hstack((NRP_y,np.average(data_y[i*x:(i+1)*x])))
        
        if (len(NRP_x) or len(NRP_y)) != 0:
            self.Graph_Plot.del_all_items() 
            curve_item = make.curve(NRP_x, NRP_y, marker='+', linestyle='NoPen',
                                        markerfacecolor='k',markeredgecolor='k', markersize=7)
            self.Graph_Plot.add_item(curve_item)
            self.Graph_Plot.do_autoscale()
        
        else:
            Qt.QMessageBox.question(XM.window, 'Message',
        'Do not find any point for given parameters', Qt.QMessageBox.Ok)
    
    def Reject_Point(self):
        global NRP_x,NRP_y
        
        
        old_data_x = XM.ui.OD.data_x
        old_data_y = XM.ui.OD.data_y
        
        sort = np.argsort(old_data_x)
        
        old_data_x = old_data_x[sort]
        old_data_y = old_data_y[sort]
        
        items = self.Graph_Plot.get_items()
        data = items[1].get_data()
        
        data_x = data[0]
        data_y = data[1]
        
        
        Part = self.RP_Part_LineEdit.text()
        Part = int(Part)
        
        St_Dev = self.RP_StDev_LineEdit.text()
        St_Dev = float(St_Dev)
        
        
        """
        reject_value = self.Rejec_Value_LineEdit.text()
        reject_value = float(reject_value)
        """  
        """
        sort = np.argsort(data_x)
        data_x = data_x[sort]
        data_y = data_y[sort]
        """
        
        NRP_x = np.arange(0,dtype=float)
        NRP_y = np.arange(0,dtype=float)
        for i in range(Part):
            x = (len(data_x)/float(Part))
            Part_Data_y = data_y[i*x:(i+1)*x]
            Part_Data_x = data_x[i*x:(i+1)*x]

            avg = np.average(Part_Data_y)
            std = np.std(Part_Data_y)
            for i in range(len(Part_Data_y)):
                if avg-St_Dev*std < Part_Data_y[i] < avg+St_Dev*std:
                        NRP_x = np.hstack((NRP_x,Part_Data_x[i]))
                        NRP_y =np.hstack((NRP_y,Part_Data_y[i]))
                        
        """            
        #old_x = np.arange(0,dtype=float)
        old_y = np.arange(0,dtype=float)
        for i in range(len(NRP_y)):
            for j in range(len(data_y)):
                if data_y[j] == NRP_y[i]:
                    #old_x = np.hstack(old_x,old_data_x[])
                    old_y = np.hstack((old_y,NRP_y[i]))
        
        print len(old_y)
        print len(data_y)
        print len(NRP_y)
        """
        if (len(NRP_x) or len(NRP_y)) != 0:
            self.Graph_Plot.del_all_items() 
            curve_item = make.curve(NRP_x, NRP_y, marker='+', linestyle='NoPen',
                                        markerfacecolor='k',markeredgecolor='k', markersize=7)
            self.Graph_Plot.add_item(curve_item)
            self.Graph_Plot.do_autoscale()
        else:
            Qt.QMessageBox.question(XM.window, 'Message',
        'Do not find any point for given parameters', Qt.QMessageBox.Ok)
        
        """
        import matplotlib.pyplot as plt
        
        plt.plot(old_x,old_y,'bo')
        """
    def Light_Curve(self):
        
        data_x = XM.ui.OD.data_x
        data_y = XM.ui.OD.data_y
        
        xLabel = XM.ui.OD.xAxis_ComboBox.currentText()
        
        self.Graph_Plot.del_all_items() 
        self.Graph_Plot.set_axis_title("bottom",xLabel)
        curve_item = make.curve(data_x, data_y, marker='+', linestyle='NoPen',
                                    markerfacecolor='k',markeredgecolor='k', markersize=7)
        self.Graph_Plot.add_item(curve_item)
        self.Graph_Plot.do_autoscale()
        
    def Phase(self):
        
        data_x = XM.ui.OD.data_x
        data_y = XM.ui.OD.data_y
        
        T0 = XM.ui.MG.T0_Lineedit.text()
        P = XM.ui.MG.P_Lineedit.text()
        
        
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
            'Please enter a valid T0 value', Qt.QMessageBox.Ok)
            
        elif str(P).replace('.','',1).isdigit() == False \
            and str(T0).replace('.','',1).isdigit() == True:
            Qt.QMessageBox.question(XM.window, 'Message',
        'Please enter a valid P value', Qt.QMessageBox.Ok)
        
        elif (str(T0) and str(P)).replace('.','',1).isdigit() == False:
            Qt.QMessageBox.question(XM.window, 'Message',
        'Please enter a valid T0 and P value', Qt.QMessageBox.Ok)
        
    def Continue_CurrentData(self):

        XM.ui.OD.data_x = NRP_x
        XM.ui.OD.data_y = NRP_y
        
        reply = Qt.QMessageBox.question(XM.window, 'Message',
        "Are you sure want to continue with Normalized Light Curve?" \
        ' Do not forget If you select ''yes'', raw data will be lost!',
        Qt.QMessageBox.Yes, Qt.QMessageBox.No)
        
        if reply == Qt.QMessageBox.Yes:
            
            XM.ui.MG.Graph_Plot.del_all_items()           
            curve_item = make.curve(NRP_x, NRP_y, marker='+', linestyle='NoPen',
                                        markerfacecolor='k',markeredgecolor='k', markersize=7)
            XM.ui.MG.Graph_Plot.add_item(curve_item)
            XM.ui.MG.Graph_Plot.do_autoscale()
            
            XM.ui.Optimization_Window.close()
    
    
    def kRE(self, evt):
        import scipy.interpolate as inter
        #items = self.Graph_Plot.get_items()
        itemList = self.Graph_Plot.itemList()
        from plotpy.builder import Marker
        for item in itemList:
            if type(item) == Marker:
                marker = item
                break
            
        for item in itemList:
            try:
                if item.curveparam.label == 'nodes':
                    self.nodes_x = item.get_data()[0]
                    self.nodes_y = item.get_data()[1]
                    self.Graph_Plot.del_item(item)
                if item.curveparam.label == 'spline':
                    self.Graph_Plot.del_item(item)
            except:
                pass
            
        x, y = marker.xValue(), marker.yValue()

        if evt.text() == 's':
            self.Check = np.hstack((self.Check, x))
            dis = [[],[]]
            for i in range(len(self.nodes_x)):
                dis[0].append(i)
                dis[1].append(abs(self.nodes_x[i] - x))

            c = dis[0][np.argmin(dis[1])]
            self.nodes_x[c] = x
            self.nodes_y[c] = y
        
        if self.Check[-2] != x:
            if evt.text() == 'a':
                self.nodes_x = np.append(self.nodes_x, x)
                self.nodes_y = np.append(self.nodes_y, y)
        
        if evt.text() == 'd':
            self.Check[-1] = -1
            dis = [[],[]]
            for i in range(len(self.nodes_x)):
                dis[0].append(i)
                dis[1].append(abs(self.nodes_x[i]-x))
            
            c = dis[0][np.argmin(dis[1])]
            self.nodes_x = np.delete(self.nodes_x,c)
            self.nodes_y = np.delete(self.nodes_y,c)
        
        sort = np.argsort(self.nodes_x)
        self.nodes_x = self.nodes_x[sort]
        self.nodes_y = self.nodes_y[sort]
        
        spline_x = np.linspace(min(self.nodes_x),max(self.nodes_x),5000)
        tck = inter.splrep(self.nodes_x,self.nodes_y)
        spline_y = inter.splev(spline_x, tck)
            
        nodes_item = make.curve(self.nodes_x, self.nodes_y, 'nodes',marker='o',
                                linestyle='NoPen',
                                markerfacecolor='b',
                                markeredgecolor='b', 
                                markersize=7)
        spline_item = make.curve(spline_x, spline_y, 'spline', color='r',
                                 linewidth=2)                        
        self.Graph_Plot.add_item(nodes_item)
        self.Graph_Plot.add_item(spline_item)
        self.Graph_Plot.do_autoscale() 
        

            
class Optimization(Qt.QMainWindow):
    def closeEvent(self,event):
        XM.ui.MG.Activate_Buttons()            
            
            
            
        