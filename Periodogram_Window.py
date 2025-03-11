# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 05:30:50 2015

@author: TheLichWing
"""
import Main_Window as XM
from plotpy.builder import make
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets as Qt
import Calculations as cl
from astropy.timeseries import LombScargle
import numpy as np
from scipy.signal import find_peaks

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
"Periodogram Window Start"
#################################################################
class Periodogram_Window(object):
    def setupUi(self, Periodogram_Window):
        Periodogram_Window.setObjectName(_fromUtf8("Periodogram_Window"))
        Periodogram_Window.resize(QtCore.QSize(590, 385))
        Periodogram_Window.setMinimumSize(QtCore.QSize(590, 385))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/PD.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Periodogram_Window.setWindowIcon(icon)

        self.centralwidget = Qt.QWidget(Periodogram_Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.gridLayout = Qt.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout.setContentsMargins(2,2,2,2)
        self.gridLayout.setSpacing(2)
        
        self.Graph_Frame = Qt.QFrame(self.centralwidget)
        self.Graph_Frame.setFrameShape(Qt.QFrame.StyledPanel)
        self.Graph_Frame.setObjectName(_fromUtf8("Graph_Frame"))      
        self.gridLayout.addWidget(self.Graph_Frame, 0, 0, 1, 1)
        
        self.line = Qt.QFrame(self.centralwidget)
        self.line.setFrameShape(Qt.QFrame.VLine)
        self.line.setFrameShadow(Qt.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))       
        self.gridLayout.addWidget(self.line, 0, 1, 3, 1)
        
        self.Right_Frame = Qt.QFrame(self.centralwidget)
        self.Right_Frame.setMinimumSize(QtCore.QSize(175, 0))
        self.Right_Frame.setMaximumSize(QtCore.QSize(175, 16777215))
        self.Right_Frame.setFrameShape(Qt.QFrame.StyledPanel)
        self.Right_Frame.setObjectName(_fromUtf8("Right_Frame"))
        
        self.Right_Frame_VLayout = Qt.QVBoxLayout(self.Right_Frame)
        self.Right_Frame_VLayout.setSpacing(6)
        self.Right_Frame_VLayout.setContentsMargins(2, 2, 2, 2)
        self.Right_Frame_VLayout.setObjectName(_fromUtf8("Right_Frame_VLayout"))
        
        self.Ofac_HLayout = Qt.QHBoxLayout()
        self.Ofac_HLayout.setSpacing(0)
        self.Ofac_HLayout.setObjectName(_fromUtf8("Ofac_HLayout"))
        
        self.Ofac_Label = Qt.QLabel()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setItalic(True)
        self.Ofac_Label.setFont(font)
        self.Ofac_Label.setObjectName(_fromUtf8("Ofac_Label"))    
        self.Ofac_HLayout.addWidget(self.Ofac_Label)
        
        Ofac_SpacerItem = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)      
        self.Ofac_HLayout.addItem(Ofac_SpacerItem)
        
        self.Ofac_Colon_Label = Qt.QLabel()
        self.Ofac_Colon_Label.setMinimumSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Ofac_Colon_Label.setFont(font)
        self.Ofac_Colon_Label.setObjectName(_fromUtf8("Ofac_Colon_Label"))        
        self.Ofac_HLayout.addWidget(self.Ofac_Colon_Label)
        
        self.Ofac_Lineedit = Qt.QLineEdit()  
        self.Ofac_Lineedit.setFixedSize(QtCore.QSize(50, 20))
        self.Ofac_Lineedit.setObjectName(_fromUtf8("Ofac_Lineedit"))
        self.Validator_Ofac = QtGui.QDoubleValidator()
        self.Ofac_Lineedit.setValidator(self.Validator_Ofac)
        self.Ofac_HLayout.addWidget(self.Ofac_Lineedit)      
        self.Right_Frame_VLayout.addLayout(self.Ofac_HLayout)
        
        self.Hifac_HLayout = Qt.QHBoxLayout()
        self.Hifac_HLayout.setSpacing(0)
        self.Hifac_HLayout.setObjectName(_fromUtf8("Hifac_HLayout"))
        
        self.Hifac_Label = Qt.QLabel(self.Right_Frame)      
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setItalic(True)
        self.Hifac_Label.setFont(font)
        self.Hifac_Label.setObjectName(_fromUtf8("Hifac_Label"))
        self.Hifac_HLayout.addWidget(self.Hifac_Label)
        
        Hifac_SpacerItem = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.Hifac_HLayout.addItem(Hifac_SpacerItem)
        
        self.Hifac_Colon_Label = Qt.QLabel()
        self.Hifac_Colon_Label.setMinimumSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Hifac_Colon_Label.setFont(font)
        self.Hifac_Colon_Label.setObjectName(_fromUtf8("Hifac_Colon_Label"))
        self.Hifac_HLayout.addWidget(self.Hifac_Colon_Label)
        
        self.Hifac_Lineedit = Qt.QLineEdit()
        self.Hifac_Lineedit.setFixedSize(QtCore.QSize(50, 20))
        self.Hifac_Lineedit.setObjectName(_fromUtf8("Hifac_Lineedit"))
        self.Validator_Hifac = QtGui.QDoubleValidator()
        self.Hifac_Lineedit.setValidator(self.Validator_Hifac)
        self.Hifac_HLayout.addWidget(self.Hifac_Lineedit)       
        self.Right_Frame_VLayout.addLayout(self.Hifac_HLayout)
        
        self.Calculate_Button = Qt.QPushButton()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Calculate_Button.setFont(font)
        self.Calculate_Button.setObjectName(_fromUtf8("Calculate_Button"))
        self.Right_Frame_VLayout.addWidget(self.Calculate_Button)
        
        self.MinMaxTime_Table = Qt.QTableWidget()
        self.MinMaxTime_Table.setMaximumSize(QtCore.QSize(167, 50))
        self.MinMaxTime_Table.setObjectName(_fromUtf8("MinMaxTime_Table"))
        self.MinMaxTime_Table.setColumnCount(1)
        self.MinMaxTime_Table.setRowCount(0)
        self.MinMaxTime_Table.verticalHeader().setVisible(False)
        item = Qt.QTableWidgetItem()
        self.MinMaxTime_Table.setHorizontalHeaderItem(0, item)
        self.MinMaxTime_Table.setEditTriggers(Qt.QAbstractItemView.NoEditTriggers)
        self.MinMaxTime_Table.horizontalHeader().setSectionResizeMode(Qt.QHeaderView.Stretch)
        self.MinMaxTime_Table.verticalHeader().setDefaultSectionSize(28)
        self.MinMaxTime_Table.verticalHeader().setMinimumSectionSize(28)
        self.Right_Frame_VLayout.addWidget(self.MinMaxTime_Table)
        
        self.Periods_Table = Qt.QTableWidget()
        self.Periods_Table.setObjectName(_fromUtf8("Periods_Table"))
        self.Periods_Table.setColumnCount(1)
        self.Periods_Table.setRowCount(0)
        item = Qt.QTableWidgetItem()
        self.Periods_Table.setHorizontalHeaderItem(0, item)
        self.Periods_Table.setSelectionBehavior(Qt.QAbstractItemView.SelectRows)
        self.Periods_Table.setSelectionMode(Qt.QAbstractItemView.SingleSelection)  
        self.Periods_Table.setEditTriggers(Qt.QAbstractItemView.NoEditTriggers)
        self.Periods_Table.horizontalHeader().setSectionResizeMode(Qt.QHeaderView.Stretch)
        self.Periods_Table.verticalHeader().setSectionResizeMode(Qt.QHeaderView.Fixed)
        #self.Periods_Table.verticalHeader(). setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.Right_Frame_VLayout.addWidget(self.Periods_Table)
        
        #Right_Frame_SpacerItem = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Minimum, Qt.QSizePolicy.Expanding)
        #self.Right_Frame_VLayout.addItem(Right_Frame_SpacerItem)
        
        self.Continue_Button = Qt.QPushButton()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Continue_Button.setFont(font)
        self.Continue_Button.setObjectName(_fromUtf8("Continue_Button"))
        self.Right_Frame_VLayout.addWidget(self.Continue_Button)
        
        self.gridLayout.addWidget(self.Right_Frame, 0, 2, 3, 1)
        
        self.Bottom_Frame = Qt.QFrame(self.centralwidget)     
        self.Bottom_Frame.setFrameShape(Qt.QFrame.StyledPanel)
        self.Bottom_Frame.setObjectName(_fromUtf8("Bottom_Frame"))
        self.Bottom_Frame_HLayout = Qt.QHBoxLayout(self.Bottom_Frame)
        self.Bottom_Frame_HLayout.setObjectName(_fromUtf8("Bottom_Frame_HLayout"))
        
        Bottom_Frame_SpacerItem = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)       
        self.Bottom_Frame_HLayout.addItem(Bottom_Frame_SpacerItem)
        
        self.Phase_Button = Qt.QPushButton()      
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Phase_Button.setFont(font)
        self.Phase_Button.setObjectName(_fromUtf8("Phase_Button"))
        self.Bottom_Frame_HLayout.addWidget(self.Phase_Button)
        
        self.LightCurve_Button = Qt.QPushButton()       
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.LightCurve_Button.setFont(font)
        self.LightCurve_Button.setObjectName(_fromUtf8("LightCurve_Button"))
        self.Bottom_Frame_HLayout.addWidget(self.LightCurve_Button)
        
        self.Power_Spectrum_Button = Qt.QPushButton()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Power_Spectrum_Button.setFont(font)
        self.Power_Spectrum_Button.setObjectName(_fromUtf8("Power_Spectrum_Button"))
        self.Bottom_Frame_HLayout.addWidget(self.Power_Spectrum_Button)
        
        Bottom_Frame_SpacerItem1 = Qt.QSpacerItem(0, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.Bottom_Frame_HLayout.addItem(Bottom_Frame_SpacerItem1)
        
        self.gridLayout.addWidget(self.Bottom_Frame, 2, 0, 1, 1)
        
        self.Continue_Button.setEnabled(False)
        self.Phase_Button.setEnabled(False)
        self.Power_Spectrum_Button.setEnabled(False)
        self.LightCurve_Button.setEnabled(False)

        self.Win = PlotDialog(edit=False, toolbar=True)
        self.Plot = self.Win.get_plot()
        self.toolbar = self.Win.get_toolbar()
        self.icons  = self.toolbar.actions()
        self.icons[7].setVisible(False)
        self.icons[8].setVisible(False)
        
        self.Win_HLayout  = Qt.QHBoxLayout(self.Graph_Frame)
        self.Win_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Win_HLayout.setObjectName(_fromUtf8("Win_HLayout"))
        self.Win_HLayout.addWidget(self.Win)
        
        Periodogram_Window.setCentralWidget(self.centralwidget)
     
        
        self.Periods_Table.cellClicked.connect(self.PD_Phase)
        self.Periods_Table.keyReleaseEvent = lambda event: self.PD_Phase() if event.key() == QtCore.Qt.Key_Up or event.key() == QtCore.Qt.Key_Down else None
        self.Continue_Button.clicked.connect(self.Continue_PD)
        self.Power_Spectrum_Button.clicked.connect(self.PD_PS)
        self.LightCurve_Button.clicked.connect(self.PD_LC)
        self.Phase_Button.clicked.connect(self.PD_Phase)
        self.Calculate_Button.clicked.connect(self.PD_Calculate)
        self.retranslateUi(Periodogram_Window)
        QtCore.QMetaObject.connectSlotsByName(Periodogram_Window)
        
    
            
            
    def retranslateUi(self, Periodogram_Window):
        Periodogram_Window.setWindowTitle(_translate("Periodogram_Window", "Periodogram Window", None))
        self.Ofac_Label.setText(_translate("Periodogram_Window", "Samples Per Peak", None))
        self.Ofac_Colon_Label.setText(_translate("Periodogram_Window", ":", None))
        self.Hifac_Label.setText(_translate("Periodogram_Window", "Nyquist Factor", None))
        self.Hifac_Colon_Label.setText(_translate("Periodogram_Window", ":", None))
        self.Calculate_Button.setText(_translate("Periodogram_Window", "Calculate", None))
        item = self.MinMaxTime_Table.horizontalHeaderItem(0)
        item.setText(_translate("Periodogram_Window", "Reference Min/Max Time", None))
        item = self.Periods_Table.horizontalHeaderItem(0)
        item.setText(_translate("Periodogram_Window", "Periods", None))
        self.Phase_Button.setText(_translate("Periodogram_Window", "Phase", None))
        self.Continue_Button.setText(_translate("Periodogram_Window", "Continue with This T0 and P", None))
        self.LightCurve_Button.setText(_translate("Periodogram_Window", "Light Curve(s)", None))
        self.Power_Spectrum_Button.setText(_translate("Periodogram_Window", "Power Spectrum", None))

    
    def PD_Calculate(self):
        ToVS = XM.ui.MG.Info_Table.item(3,0).text()
        Bness = XM.ui.MG.Info_Table.item(2,0).text()
        
        if ToVS == 'EBS':
            ToVS = 0
        else:
            ToVS = 1
        
        items = self.Plot.get_items()
        self.T0_range = items[3]
        self.P_range = items[2]
        
        Data_P = cl.PlotRangeData(items[1],self.P_range)
        Data_T0 = cl.PlotRangeData(items[1],self.T0_range)
        
        Ref_T0 = cl.Methods.Kwee([Data_T0[0],Data_T0[1]], ToVS, Bness)

        self.MinMaxTime_Table.setRowCount(1)
        self.MinMaxTime_Table.setItem(0,0,Qt.QTableWidgetItem(str('%0.6f' %  float(Ref_T0[0]))))

        Ofac = self.Ofac_Lineedit.text()
        Hifac = self.Hifac_Lineedit.text()
        
        # try:
        if (str(Ofac) and str(Hifac)).replace('.','',1).isdigit() == True:

            PD_Arr = LombScargle(Data_P[0],Data_P[1]).autopower(samples_per_peak=float(Ofac),
                                                                nyquist_factor=float(Hifac))

            # PD_Arr = lscargle.fasper(Data_P[0],Data_P[1], float(Ofac), float(Hifac), MACC=1)

            self.PSx = PD_Arr[0]
            self.PSy = PD_Arr[1]

            # maxtab,mintab = cl.peakdet(self.PSy,1)
            # self.Peaks_x = np.arange(0,dtype=float)
            # self.Peaks_y = np.arange(0,dtype=float)
            # for i in range(len(maxtab)):
            #     self.Peaks_x = np.hstack((self.Peaks_x,self.PSx[int(maxtab[i][0])]))
            #     self.Peaks_y = np.hstack((self.Peaks_y,maxtab[i][1]))

            peak_inds, _ = find_peaks(self.PSy)
            self.Peaks_x = self.PSx[peak_inds]
            self.Peaks_y = self.PSy[peak_inds]

            all_peaks = len(self.Peaks_x)

            Peaks_x_sort = self.Peaks_x[np.argsort(self.Peaks_y)]
            Peaks_y_sort = self.Peaks_y[np.argsort(self.Peaks_y)]

            if len(self.Peaks_x) > 99:
                peak_number = 100
            else:
                peak_number = len(self.Peaks_x)

            self.Peaks_x = Peaks_x_sort[all_peaks-peak_number:]
            self.Peaks_y = Peaks_y_sort[all_peaks-peak_number:]

            self.Periods_Table.setRowCount(peak_number)
            for i in range(peak_number):
                if ToVS == 0:
                    self.Periods_Table.setItem(i,0,
                        Qt.QTableWidgetItem(str('%0.6f' % float(2.0/Peaks_x_sort[-1-i]))))
                else:
                    self.Periods_Table.setItem(i,0,
                        Qt.QTableWidgetItem(str('%0.6f' % float(1.0/Peaks_x_sort[-1-i]))))
            self.Plot.del_all_items()
            self.Plot.set_axis_title("left","Power")
            self.Plot.set_axis_title("bottom","Frequency (Hz)")
            curve_item = make.curve(self.PSx, self.PSy)
            self.Plot.add_item(curve_item)
            curve_item = make.curve(self.Peaks_x, self.Peaks_y,
                                    marker='o',linestyle='NoPen',
                                    markerfacecolor='b',markeredgecolor='b',
                                    markersize=7)
            self.Plot.add_item(curve_item)
            self.Plot.set_axis_direction(0, reverse=False)
            self.Plot.do_autoscale()

            self.Continue_Button.setEnabled(True)
            self.LightCurve_Button.setEnabled(True)
            self.Phase_Button.setEnabled(True)
            self.Power_Spectrum_Button.setEnabled(True)
            self.Calculate_Button.setEnabled(False)

        elif str(Ofac).replace('.','',1).isdigit() == False \
            and str(Hifac).replace('.','',1).isdigit() == True:
            Qt.QMessageBox.question(XM.window, 'Message',
        'Please enter a valid Samples Per Peak value', Qt.QMessageBox.Ok)

        elif str(Hifac).replace('.','',1).isdigit() == False \
            and str(Ofac).replace('.','',1).isdigit() == True:
            Qt.QMessageBox.question(XM.window, 'Message',
        'Please enter a valid Nyquist Factor value', Qt.QMessageBox.Ok)

        elif (str(Hifac) and str(Ofac)).replace('.','',1).isdigit() == False:
            Qt.QMessageBox.question(XM.window, 'Message',
        'Please enter a valid Samples Per Peak and Nyquist Factor value',
            Qt.QMessageBox.Ok)
        # except:
        #     Qt.QMessageBox.question(XM.window, 'Message',
        #     'Memory error! Please diminish Samples Per Peak and/or'+
        #     ' Nyquist Factor value or data range',
        #         Qt.QMessageBox.Ok)
    
    def PD_Phase(self):

        yLabel = XM.ui.MG.Graph_Plot.axisTitle(0).text()
        
        #items =  XM.ui.MG.Graph_Plot.get_items()
        
        #Datas = items[1].get_data()
                
        #data_x = Datas[0]
        #data_y = Datas[1]
    
        data_x = XM.ui.OD.data_x
        data_y = XM.ui.OD.data_y
    
        T0 = self.MinMaxTime_Table.item(0,0)
        
        Cur_Row = self.Periods_Table.currentRow()
        if Cur_Row == -1:
            Cur_Row = 0
        P = self.Periods_Table.item(Cur_Row,0)
        
        if (str(T0) and str(P)) != None and (str(T0.text()) and str(P.text())).replace('.','',1).isdigit() \
            == True:
            
            Phase = ((np.array(data_x) - float(T0.text()))/float(P.text()))- \
                np.floor((np.array(data_x) - float(T0.text()))/float(P.text()))
                
            
            self.Plot.del_all_items() 
            self.Plot.set_axis_title("left",yLabel)
            self.Plot.set_axis_title("bottom","Phase")
            curve_item = make.curve(Phase, data_y, marker='+', linestyle='NoPen',
                                    markerfacecolor='k',markeredgecolor='k', markersize=7)
            self.Plot.add_item(curve_item)
            
            self.Plot.set_axis_direction(0, reverse=False)
            if yLabel == 'Magnitude':
                self.Plot.set_axis_direction(0, reverse=True)
            self.Plot.do_autoscale()
            
            self.Power_Spectrum_Button.setEnabled(True)
            self.Calculate_Button.setEnabled(False)
            
            self.LightCurve_Button.setEnabled(True)
        
        else:
            
            Qt.QMessageBox.question(XM.window, 'Message',
                "Please select a region on graph for calculate a reference minimum time" \
                " before press calculate button",
                Qt.QMessageBox.Ok)
    
    def PD_LC(self):
        #items =  XM.ui.MG.Graph_Plot.get_items()
        
        #Datas = items[1].get_data()
                
        #data_x = Datas[0]
        #data_y = Datas[1]
        
        
        data_x = XM.ui.OD.data_x
        data_y = XM.ui.OD.data_y
        
        
        xLabel = XM.ui.MG.Graph_Plot.axisTitle(2).text()
        yLabel = XM.ui.MG.Graph_Plot.axisTitle(0).text()
        
        
        
        self.Plot.del_all_items()
        
        self.Plot.set_axis_title("left",yLabel)
        self.Plot.set_axis_title("bottom",xLabel)
    
        self.Plot.set_axis_direction(0, reverse=False)
        if yLabel == 'Magnitude':
            self.Plot.set_axis_direction(0, reverse=True)
        curve_item = make.curve(data_x, data_y, marker='+', linestyle='NoPen',
                                    markerfacecolor='k',markeredgecolor='k', markersize=7)
        self.Plot.add_item(curve_item)
        self.Plot.add_item(self.P_range)
        self.Plot.add_item(self.T0_range)
        self.Plot.do_autoscale()
    
        self.Power_Spectrum_Button.setEnabled(True)
        self.Calculate_Button.setEnabled(True)
    
    def PD_PS(self):
        
        self.Plot.del_all_items() 
        self.Plot.set_axis_title("left","Power")
        self.Plot.set_axis_title("bottom","Frequency (Hz)")
        curve_item = make.curve(self.PSx, self.PSy)
        self.Plot.add_item(curve_item)
        curve_item = make.curve(self.Peaks_x, self.Peaks_y,marker='o', linestyle='NoPen',
                                    markerfacecolor='b',markeredgecolor='b', markersize=7)
        self.Plot.add_item(curve_item)
        self.Plot.set_axis_direction(0, reverse=False)
        self.Plot.do_autoscale()
        
        self.Calculate_Button.setEnabled(False)
        
    def Continue_PD(self):
    

        Cur_Row_P = self.Periods_Table.currentRow()
        if self.Periods_Table.rowCount() == 1:
            Cur_Row_P = 0
        
        
        if Cur_Row_P != -1:
            T0 = self.MinMaxTime_Table.item(0,0)
            P = self.Periods_Table.item(Cur_Row_P,0).text()
            
            if T0 is None:
                
                    Qt.QMessageBox.question(XM.window, 'Warning',
                          "Min/Max table is empty because yon did not choose any region" \
                          " on light curve for calculate T0 value!",
                          Qt.QMessageBox.Ok)
            else:
                
                T0 = T0.text()
                XM.ui.MG.T0_Lineedit.setText(str(T0))
                
            
            reply = Qt.QMessageBox.question(XM.window, 'Message',
                    "Current T0 and P that you entered will be lost Are you sure want" \
                    " to continue with this T0 and P?",
                    Qt.QMessageBox.Yes, Qt.QMessageBox.No )
            
            if reply == Qt.QMessageBox.Yes:
    
                
                
                XM.ui.MG.P_Lineedit.setText(str(P))
                
                #XM.ui.PD.Continue_Button.setEnabled(False)
                #Activate_Buttons()
                XM.ui.Periodogram_Window.close()
                
                
        else:
            Qt.QMessageBox.question(XM.window, 'Message',
                "Please select a row that you want on period table",
                Qt.QMessageBox.Ok)

#################################################################
"Periodogram Window End"
#################################################################
class Periodogram(Qt.QMainWindow):
    def closeEvent(self,event):
        XM.ui.MG.Activate_Buttons()
        """
        reply =  Qt.QMessageBox.question(XM.window, 'Message',
                'Please enter a valid Samples Per Peak and Nyquist Factor value',
        Qt.QMessageBox.Yes, Qt.QMessageBox.No)
        
        event.ignore()
        
        if  reply == Qt.QMessageBox.Yes:
            
            XGF.Activate_Buttons()
            #self.MinMax_Table.clear()

        
            event.accept()"""