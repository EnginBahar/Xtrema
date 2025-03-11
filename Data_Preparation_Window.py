# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 05:29:00 2015

@author: TheLichWing
"""

import Main_Window as XM
from PyAstronomy.pyasl.asl import astroTimeLegacy as atl
import numpy as np
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets as Qt

# XM.groupBoxStyle

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
        
# def Read_Data(Path, Sep=None, col=None, dtype=float, skiprow=0):
#     with open(Path, 'rb') as stream:
#         lines = stream.readlines()
#         if not col:
#             col = len(lines[0].split(Sep))
#
#         data = np.zeros((len(lines), col), dtype)
#         rej = []
#         for j, item in enumerate(lines):
#             for i in range(col):
#                 try:
#                     data[j][i] = dtype(item.split(Sep)[i].replace('"','').strip())
#                 except:
#                     rej.append(j)
#                     break
#         if rej != []:
#             print("#####################")
#             print('Number of Invalid Characters = ',len(rej))
#             print('For Example = ',lines[rej[0]])
#             print('File = ',Path)
#             print("#####################")
#     return np.delete(data, (rej), axis=0).T
        
#################################################################
"Data_Preparation_Window Start"
#################################################################     
class Data_Preparation_Window(object):
    def setupUi(self, Data_Preparation_Window):
        
        Data_Preparation_Window.resize(640, 480)
        Data_Preparation_Window.setMinimumSize(640, 480)
        Data_Preparation_Window.setMaximumSize(640, 16777215)
        
        self.path = ''
        
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/DP.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Data_Preparation_Window.setWindowIcon(icon)

        self.Main_VLayout = Qt.QVBoxLayout(Data_Preparation_Window)
        
        self.Splitter = Qt.QSplitter(Data_Preparation_Window)
        self.Splitter.setHandleWidth(5)
        
        self.Main_VLayout.addWidget(self.Splitter)
               
        self.ProgressBar_GridLayout = Qt.QGridLayout()
        
        self.ProgressBar_Label = Qt.QLabel()
        self.ProgressBar_Label.setStyleSheet("QLabel { font-size: 15px }")
        self.ProgressBar_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.ProgressBar_Label.setVisible(False)
        
        self.ProgressBar = Qt.QProgressBar(Data_Preparation_Window)     
        self.ProgressBar.setVisible(False)
        self.ProgressBar.setTextVisible(False)
        
        self.ProgressBar_GridLayout.addWidget(self.ProgressBar, 0, 0)
        self.ProgressBar_GridLayout.addWidget(self.ProgressBar_Label, 0, 0)
             
        self.LWidget = Qt.QWidget(self.Splitter)
          
        self.LWidget_VLayout = Qt.QVBoxLayout(self.LWidget)
        self.LWidget_VLayout.setContentsMargins(0, 0, 0, 0)
        
        self.Import_HLayout = Qt.QHBoxLayout()        
        Import_LSpacerItem = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.Import_HLayout.addItem(Import_LSpacerItem)
        
        self.Import_Button = Qt.QPushButton(self.LWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.Import_Button.setFont(font)
        
        self.TtoC_Button = Qt.QPushButton(self.LWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.TtoC_Button.setFont(font)
        
        self.Import_HLayout.addWidget(self.Import_Button)
        self.Import_HLayout.addWidget(self.TtoC_Button)
        Import_RSpacerItem = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.Import_HLayout.addItem(Import_RSpacerItem)
        
        self.LWidget_VLayout.addLayout(self.Import_HLayout)
        
        self.Data_TableWidget = Qt.QTableWidget(self.LWidget)
        self.Data_TableWidget.setMinimumSize(211, 351)
        #self.Data_TableWidget.setRowCount(0)        
        self.Data_TableWidget.setColumnCount(2)         
        item = Qt.QTableWidgetItem()
        self.Data_TableWidget.setHorizontalHeaderItem(0, item)
        item = Qt.QTableWidgetItem()        
        self.Data_TableWidget.setHorizontalHeaderItem(1, item)
        self.Data_TableWidget.horizontalHeader().setSectionResizeMode(Qt.QHeaderView.Stretch)
        self.Data_TableWidget.setAlternatingRowColors(True)
        self.Data_TableWidget.setSortingEnabled(True)
        self.Data_TableWidget.setSelectionBehavior(Qt.QAbstractItemView.SelectRows)
        self.Data_TableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Data_TableWidget.customContextMenuRequested.connect(self.Data_TableWidget_Menu)
        
        self.LWidget_VLayout.addWidget(self.Data_TableWidget)
        
        self.RWidget = Qt.QWidget(self.Splitter)
        
        self.RWidget_VLayout = Qt.QVBoxLayout(self.RWidget)
        self.RWidget_VLayout.setContentsMargins(0, 0, 0, 0)
        USpacerItem = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Minimum, Qt.QSizePolicy.Expanding)
        self.RWidget_VLayout.addItem(USpacerItem)
        
        self.Filename_GroupBox = Qt.QGroupBox(self.RWidget)
        self.Filename_GroupBox.setStyleSheet(XM.groupBoxStyle)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Filename_GroupBox.setFont(font)        
        self.Filename_GroupBox.setMinimumSize(210, 60)
        
        self.Filename_VLayout = Qt.QVBoxLayout(self.Filename_GroupBox)
               
        self.RWidget_VLayout.addWidget(self.Filename_GroupBox)
        
        self.Filename_LineEdit = Qt.QLineEdit(self.Filename_GroupBox)
        self.Filename_LineEdit.setMinimumSize(90, 25)
        self.Filename_LineEdit.setReadOnly(True)
        
        self.Filename_VLayout.addWidget(self.Filename_LineEdit)
        
        self.AxesCon_GroupBox = Qt.QGroupBox(self.RWidget)
        self.AxesCon_GroupBox.setStyleSheet(XM.groupBoxStyle)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AxesCon_GroupBox.setFont(font)        
        self.AxesCon_GroupBox.setMinimumSize(210, 100)
      
        
        self.AxesCon_GroupBox_VLayout = Qt.QVBoxLayout(self.AxesCon_GroupBox)
        
        self.xAxis_HLayout = Qt.QHBoxLayout()
          
        self.xAxis_Label = Qt.QLabel(self.AxesCon_GroupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setItalic(True)
        font.setWeight(50)
        self.xAxis_Label.setFont(font)
        
        self.xAxis_HLayout.addWidget(self.xAxis_Label)
        
        self.xAxis_ComboBox = Qt.QComboBox(self.AxesCon_GroupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        self.xAxis_ComboBox.setFont(font)        
        self.xAxis_ComboBox.addItem(_fromUtf8(""))
        self.xAxis_ComboBox.addItem(_fromUtf8(""))
        self.xAxis_ComboBox.addItem(_fromUtf8(""))
        self.xAxis_ComboBox.addItem(_fromUtf8(""))
        
        
        self.xAxis_HLayout.addWidget(self.xAxis_ComboBox)
        
        self.AxesCon_GroupBox_VLayout.addLayout(self.xAxis_HLayout)
        
        self.yAxis_HLayout = Qt.QHBoxLayout()
               
        self.yAxis_Label = Qt.QLabel(self.AxesCon_GroupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setItalic(True)
        font.setWeight(50)
        self.yAxis_Label.setFont(font)
               
        self.yAxis_HLayout.addWidget(self.yAxis_Label)
        
        self.yAxis_ComboBox = Qt.QComboBox(self.AxesCon_GroupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        self.yAxis_ComboBox.setFont(font)       
        self.yAxis_ComboBox.addItem(_fromUtf8(""))
        self.yAxis_ComboBox.addItem(_fromUtf8(""))
        
        
        self.yAxis_HLayout.addWidget(self.yAxis_ComboBox)
        
        self.AxesCon_GroupBox_VLayout.addLayout(self.yAxis_HLayout)
        
        self.RWidget_VLayout.addWidget(self.AxesCon_GroupBox)
        
        self.ToVS_GroupBox = Qt.QGroupBox(self.RWidget)
        self.ToVS_GroupBox.setStyleSheet(XM.groupBoxStyle)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ToVS_GroupBox.setFont(font)        
        self.ToVS_GroupBox_VLayout = Qt.QVBoxLayout(self.ToVS_GroupBox)
        
        self.ToVS_HLayout = Qt.QHBoxLayout()
        
        self.ToVS_Label = Qt.QLabel(self.ToVS_GroupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setItalic(True)
        font.setWeight(50)
        self.ToVS_Label.setFont(font)
        
        self.ToVS_HLayout.addWidget(self.ToVS_Label)
        
        self.ToVS_ComboBox = Qt.QComboBox(self.ToVS_GroupBox)
        self.ToVS_ComboBox.setMinimumSize(155, 0)
        font = QtGui.QFont()
        font.setWeight(50)
        self.ToVS_ComboBox.setFont(font)        
        self.ToVS_ComboBox.addItem(_fromUtf8(""))
        self.ToVS_ComboBox.addItem(_fromUtf8(""))
       
        
        self.ToVS_HLayout.addWidget(self.ToVS_ComboBox)
        
        self.ToVS_GroupBox_VLayout.addLayout(self.ToVS_HLayout)
        
        self.RWidget_VLayout.addWidget(self.ToVS_GroupBox)
           
        self.Convertion_GroupBox = Qt.QGroupBox(self.RWidget)
        self.Convertion_GroupBox.setStyleSheet(XM.groupBoxStyle)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Convertion_GroupBox.setFont(font)
        self.Convertion_GroupBox.setMinimumSize(210, 150)

        self.Convertion_GroupBox_VLayout = Qt.QVBoxLayout(self.Convertion_GroupBox)
        
        self.Converiton_HLayout = Qt.QHBoxLayout()
        
        self.Converiton_ComboBox1 = Qt.QComboBox(self.Convertion_GroupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        self.Converiton_ComboBox1.setFont(font)
        self.Converiton_ComboBox1.addItem(_fromUtf8(""))
        self.Converiton_ComboBox1.setEnabled(False)
        
        
        self.Converiton_HLayout.addWidget(self.Converiton_ComboBox1)
        
        self.To_Label = Qt.QLabel(self.Convertion_GroupBox)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setWeight(50)
        self.To_Label.setFont(font)
        self.To_Label.setAlignment(QtCore.Qt.AlignCenter)

        self.Converiton_HLayout.addWidget(self.To_Label)
        
        self.Converiton_ComboBox2 = Qt.QComboBox(self.Convertion_GroupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        self.Converiton_ComboBox2.setFont(font)
        self.Converiton_ComboBox2.addItem(_fromUtf8(""))
        self.Converiton_ComboBox2.addItem(_fromUtf8(""))
        self.Converiton_ComboBox2.addItem(_fromUtf8(""))
        self.Converiton_ComboBox2.model().item(1).setEnabled(False)
              
        self.Converiton_HLayout.addWidget(self.Converiton_ComboBox2)
        
        self.Convertion_GroupBox_VLayout.addLayout(self.Converiton_HLayout)
        
        self.RA_HlLayout = Qt.QHBoxLayout()
        
        self.RA_Label = Qt.QLabel(self.Convertion_GroupBox)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setWeight(50)
        self.RA_Label.setFont(font)

        self.RA_HlLayout.addWidget(self.RA_Label)
        LSpacerItem = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.RA_HlLayout.addItem(LSpacerItem)
        
        self.RA_Lineedit = Qt.QLineEdit(self.Convertion_GroupBox)
        self.RA_Lineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.RA_Lineedit.setPlaceholderText("HH MM SS")
        
        self.RA_HlLayout.addWidget(self.RA_Lineedit)
        
        self.Convertion_GroupBox_VLayout.addLayout(self.RA_HlLayout)
        
        self.DEC_HLayout = Qt.QHBoxLayout()

        self.DEC_Label = Qt.QLabel(self.Convertion_GroupBox)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setWeight(50)
        self.DEC_Label.setFont(font)

        self.DEC_HLayout.addWidget(self.DEC_Label)
        LSpacerItem = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.DEC_HLayout.addItem(LSpacerItem)
        
        self.DEC_Lineedit = Qt.QLineEdit(self.Convertion_GroupBox)
        self.DEC_Lineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.DEC_Lineedit.setPlaceholderText("-DD"+u"\u00b0"+" "+"MM'' SS'")
        
        self.DEC_HLayout.addWidget(self.DEC_Lineedit)
        
        self.Convertion_GroupBox_VLayout.addLayout(self.DEC_HLayout)
        
        self.Calculate_HLayout = Qt.QHBoxLayout()
        
        self.Calculate_Button = Qt.QPushButton(self.Convertion_GroupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        self.Calculate_Button.setFont(font)
        
        self.Calculate_HLayout.addWidget(self.Calculate_Button)
        
        self.Convertion_GroupBox_VLayout.addLayout(self.Calculate_HLayout)
        
        self.RWidget_VLayout.addWidget(self.Convertion_GroupBox)
        
        self.Done_HLayout = Qt.QHBoxLayout()        
        LSpacerItem = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Fixed, Qt.QSizePolicy.Minimum)
        self.Done_HLayout.addItem(LSpacerItem)
        
        self.Done_Button = Qt.QPushButton(self.RWidget)
        self.Done_Button.setMinimumSize(75, 0)
        self.Done_Button.setMaximumSize(75, 16777215)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setWeight(50)
        self.Done_Button.setFont(font)
        
        self.Done_HLayout.addWidget(self.Done_Button)
        RSpacerItem = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Fixed, Qt.QSizePolicy.Minimum)
        self.Done_HLayout.addItem(RSpacerItem)
        
        DSpacerItem = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Minimum, Qt.QSizePolicy.Expanding)
        self.RWidget_VLayout.addItem(DSpacerItem)
        self.RWidget_VLayout.addLayout(self.Done_HLayout)        
        self.RWidget_VLayout.addLayout(self.ProgressBar_GridLayout)
        
        #self.GridLayout.addWidget(self.Splitter, 0, 0, 1, 1)
        
        self.data_x = []
        self.data_y = []
        
        self.TtoC_Button.clicked.connect(self.DD)
        self.Calculate_Button.clicked.connect(self.Cal_Convert)
        self.Done_Button.clicked.connect(self.Done)
        self.Import_Button.clicked.connect(self.Import)
        self.xAxis_ComboBox.currentIndexChanged.connect(self.Conv_Conf)
        self.Converiton_ComboBox2.currentIndexChanged.connect(self.MJD_Passive)
        
        self.retranslateUi(Data_Preparation_Window)
        QtCore.QMetaObject.connectSlotsByName(Data_Preparation_Window)
        
    def DD(self):
        try:
            self.saved_ext_edit = True
            self.DD.show()
            self.DD.TextToColumn()
        except:
            pass

    def retranslateUi(self, Data_Preparation_Window):
        
        Data_Preparation_Window.setWindowTitle(_translate("Data_Preparation_Window", "Data Preparation", None))
        self.Import_Button.setText(_translate("Data_Preparation_Window", "Import Data", None))
        self.TtoC_Button.setText(_translate("Data_Preparation_Window", "Text to Column", None))
        item = self.Data_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Data_Preparation_Window", "Time", None))
        item = self.Data_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Data_Preparation_Window", "Brightness", None))
        self.Filename_GroupBox.setTitle(_translate("Data_Preparation_Window", "Filename", None))
        self.AxesCon_GroupBox.setTitle(_translate("Data_Preparation_Window", "Axes Configuration", None))
        self.xAxis_Label.setText(_translate("Data_Preparation_Window", "x-Axis :", None))
        self.xAxis_ComboBox.setItemText(0, _translate("Data_Preparation_Window", "JD", None))
        self.xAxis_ComboBox.setItemText(1, _translate("Data_Preparation_Window", "HJD", None))
        self.xAxis_ComboBox.setItemText(2, _translate("Data_Preparation_Window", "BJD", None))
        self.xAxis_ComboBox.setItemText(3, _translate("Data_Preparation_Window", "MJD", None))
        
        self.yAxis_Label.setText(_translate("Data_Preparation_Window", "y-Axis :", None))
        self.yAxis_ComboBox.setItemText(0, _translate("Data_Preparation_Window", "Flux", None))
        self.yAxis_ComboBox.setItemText(1, _translate("Data_Preparation_Window", "Magnitude", None))
        
        self.ToVS_GroupBox.setTitle(_translate("Data_Preparation_Window", "Type of Variable Star", None))
        self.ToVS_Label.setText(_translate("Data_Preparation_Window", "Type   :", None))
        self.ToVS_ComboBox.setItemText(0, _translate("Data_Preparation_Window", "Eclipsing Binary System", None))
        self.ToVS_ComboBox.setItemText(1, _translate("Data_Preparation_Window", "Pulsating Star", None))
        self.ProgressBar_Label.setText(_translate("Data_Preparation_Window","Loading", None))
    
        self.Convertion_GroupBox.setTitle(_translate("Data_Preparation_Window", "Convertion (optional)", None))
        self.Converiton_ComboBox1.setItemText(0, _translate("Data_Preparation_Window", "JD", None))
        self.Converiton_ComboBox2.setItemText(0, _translate("Data_Preparation_Window", "HJD", None))
        self.Converiton_ComboBox2.setItemText(1, _translate("Data_Preparation_Window", "BJD", None))
        self.Converiton_ComboBox2.setItemText(2, _translate("Data_Preparation_Window", "MJD", None))
        self.To_Label.setText(_translate("Data_Preparation_Window", "to", None))
        self.RA_Label.setText(_translate("Data_Preparation_Window", "RA       :", None))
        self.DEC_Label.setText(_translate("Data_Preparation_Window", "DEC    :", None))
        self.Calculate_Button.setText(_translate("Data_Preparation_Window", "Calculate", None))
       
        self.Done_Button.setText(_translate("Data_Preparation_Window", "Done", None))
    
    def MJD_Passive(self):
        if self.Converiton_ComboBox2.currentText() == 'MJD':
            self.DEC_Lineedit.setEnabled(False)
            self.RA_Lineedit.setEnabled(False) 
     
        else:
            self.DEC_Lineedit.setEnabled(True)
            self.RA_Lineedit.setEnabled(True)
        
    def Cal_Convert(self):
        
        RA = self.RA_Lineedit.text()
        DEC = self.DEC_Lineedit.text()
        
        if self.Data_TableWidget.rowCount() != 0:
            xAxis_CB = self.xAxis_ComboBox.currentText()
            Convertion_CB2 = self.Converiton_ComboBox2.currentText()
            if  xAxis_CB == 'JD' and Convertion_CB2 == 'HJD':
                if (RA and DEC) is not None:
                    RA = str(RA).split()
                    DEC = str(DEC).split()
                
                try:
                    
                    if all([int(RA[0]) >= 0, int(RA[1]) >= 0, float(RA[2]) >= 0,
                            int(DEC[1]) >= 0, float(DEC[2]) >= 0]):
                        reply = Qt.QMessageBox.question(XM.ui.Data_Preparation_Window, 'Message',
                        "If you click 'Yes' raw data will be lost!", Qt.QMessageBox.Yes,Qt.QMessageBox.No)

                        if reply == Qt.QMessageBox.Yes:

                            RA = ((((float(RA[2])/60.0)+float(RA[1]))/60.0)+float(RA[0]))*15

                            if float(DEC[0]) < 0:
                                DEC = -1*(((float(DEC[2])/60.0)+float(DEC[1]))/60.0)+float(DEC[0])
                            else:
                                DEC = (((float(DEC[2])/60.0)+float(DEC[1]))/60.0)+float(DEC[0])
                            # print(RA, DEC)
                            # XM.ui.Data_Preparation_Window.setEnabled(False)
                            XM.ui.Data_Preparation_Window.setWindowModality(QtCore.Qt.ApplicationModal)
                            self.ProgressBar.setVisible(True)
                            self.ProgressBar_Label.setVisible(True)
                            HJD = np.arange(0,dtype=float)
                            nop = self.Data_TableWidget.rowCount()
                            for i in range(nop):
                                JD = self.Data_TableWidget.item(i,0).text()
                                if len(JD) == 5:
                                    hjd_single = atl.helio_jd(float(JD),float(RA),float(DEC))
                                else:
                                    hjd_single = atl.helio_jd(float(JD)-2400000,float(RA),float(DEC))
                                    hjd_single = hjd_single + 2400000

                                HJD = np.hstack((HJD,hjd_single))
                                self.Data_TableWidget.setItem(i,0,Qt.QTableWidgetItem(str(hjd_single)))

                                self.ProgressBar.setValue(int(i*100/nop))
                                self.ProgressBar_Label.setText("Converting"+"  "+str(int(i*100/nop))+"%")

                                # if i/1500 == i/1500.0:
                                #     Qt.qApp.processEvents()

                            self.xAxis_ComboBox.setCurrentIndex(1)
                    else:
                        Qt.QMessageBox.question(XM.ui.Data_Preparation_Window, 'Message',
                         "Please enter a valid RA and DEC", Qt.QMessageBox.Ok)
                except:
                    Qt.QMessageBox.question(XM.ui.Data_Preparation_Window, 'Message',
                         "Please enter a valid RA and DEC", Qt.QMessageBox.Ok)
            
            if xAxis_CB == 'JD' and Convertion_CB2 == 'MJD':
                reply = Qt.QMessageBox.question(XM.ui.Data_Preparation_Window, 'Message',
                        "If you click 'Yes' raw data will be lost!", Qt.QMessageBox.Yes,Qt.QMessageBox.No)
                if reply == Qt.QMessageBox.Yes:
                    # XM.ui.Data_Preparation_Window.setEnabled(False)
                    XM.ui.Data_Preparation_Window.setWindowModality(QtCore.Qt.ApplicationModal)
                    self.ProgressBar.setVisible(True)
                    self.ProgressBar_Label.setVisible(True)
                    nop = self.Data_TableWidget.rowCount()
                    for i in range(nop):
                        JD = self.Data_TableWidget.item(i,0).text()
                        if len(str(JD).split('.')[0]) == 7:
                            MJD = float(JD) - 2400000.5
                        else:
                            MJD = float(JD) - 0.5
                        self.ProgressBar.setValue(int(i*100/nop))
                        self.ProgressBar_Label.setText("Converting"+"  "+str(int(i*100/nop))+"%")
                        
                        # if i/1500 == i/1500.0:
                        #     Qt.qApp.processEvents()
                        self.Data_TableWidget.setItem(i,0,Qt.QTableWidgetItem(str(MJD)))
                    self.xAxis_ComboBox.setCurrentIndex(3)
        
        else:
            Qt.QMessageBox.question(XM.ui.Data_Preparation_Window, 'Message',
                        "Table is empty!", Qt.QMessageBox.Ok)
        
        self.ProgressBar.setVisible(False)
        self.ProgressBar_Label.setVisible(False)
        # XM.ui.Data_Preparation_Window.setEnabled(True)
        XM.ui.Data_Preparation_Window.setWindowModality(QtCore.Qt.NonModal)
    def Save(self):
    
        path = Qt.QFileDialog.getSaveFileName(
                        Qt.QMainWindow(), 'Save File', '', 'TXT(*.txt)')

 
        try:    
            data_save = open(str(path),'w')
            
            for i in range(self.Data_TableWidget.rowCount()):
                
                Time = self.Data_TableWidget.item(i,0)
                Flux = self.Data_TableWidget.item(i,1)
                
                if Time == None:
                    Time = '-'
                if Flux == None:
                    Flux = '-'

            
            
                data_save.write(str(Time.text())+' '+str(Flux.text()) + '\n')
        except:
            pass
        data_save.close()
    
    def Data_TableWidget_Menu(self):
        
        menu = Qt.QMenu()
        Delete = Qt.QAction(menu)
        Delete.setText('Delete')
        Delete.setShortcut('Delete')
        menu.addAction(Delete)
        Delete.triggered.connect(self.Delete)
        
        Save = Qt.QAction(menu)
        Save.setText('Save Table')
        Save.setShortcut('Ctrl + S')

        menu.addAction(Save)
        Save.triggered.connect(self.Save)
  
        menu.exec_(Qt.QCursor.pos())
        
    def Delete(self):
        
        row = self.Data_TableWidget.currentRow()
        if row != -1:
            reply = Qt.QMessageBox.question(XM.ui.Data_Preparation_Window, 'Message',
                 "Are you sure to delete?", Qt.QMessageBox.Yes, Qt.QMessageBox.No)
            
            if reply == Qt.QMessageBox.Yes:
                
                rows = self.Data_TableWidget.selectionModel().selectedRows()
                index = []
                for row in rows:
                    index.append(row.row())
                
                index = sorted(index, reverse=True)
                
                for rowid in index:
                    self.Data_TableWidget.removeRow(rowid)
                
                if self.Data_TableWidget.rowCount() == 0:
                    self.Filename_LineEdit.clear()
        else:
            reply = Qt.QMessageBox.question(XM.ui.Data_Preparation_Window, 'Message',
                 "Please choose one or more row!", Qt.QMessageBox.Ok)
        
    
    def Conv_Conf(self):
    
        xAxis_Current_Text = self.xAxis_ComboBox.currentText()
        self.Converiton_ComboBox1.removeItem(0)
        self.Converiton_ComboBox1.addItem(str(xAxis_Current_Text))
        
        self.Converiton_ComboBox2.clear()  
        if xAxis_Current_Text == 'HJD':
            self.Convertion_GroupBox.setEnabled(False)
            self.Converiton_ComboBox2.addItem('HJD')
        if xAxis_Current_Text == 'BJD':
            self.Converiton_ComboBox2.addItem('BJD')
            self.Convertion_GroupBox.setEnabled(False)
        if xAxis_Current_Text == 'JD':
            self.Convertion_GroupBox.setEnabled(True)
            self.Converiton_ComboBox2.addItems(['HJD','BJD','MJD'])
            self.Converiton_ComboBox2.model().item(1).setEnabled(False)
        if xAxis_Current_Text == 'MJD':
            self.Converiton_ComboBox2.addItem('MJD')
            self.Convertion_GroupBox.setEnabled(False)
        
    def Import(self):
        path, _ = Qt.QFileDialog.getOpenFileName(XM.ui.Data_Preparation_Window, 'Open File', '',"Open Files (*.*)")

        if path:
    #        data = Read_Data(path, col=3)
    #        self.Data_TableWidget.setRowCount(0)
    #        for i in range(len(data[0])):
    #            if (self.isfloat(data[0][i]) == True and
    #                self.isfloat(data[2][i]) == True):
    #                row = self.Data_TableWidget.rowCount()
    #                self.Data_TableWidget.insertRow(row)
    #
    #                self.Data_TableWidget.setItem(row, 0,
    #                                              Qt.QTableWidgetItem(str(data[0][i])))
    #                self.Data_TableWidget.setItem(row, 1,
    #                                              Qt.QTableWidgetItem(str(data[2][i])))


            #try:
            self.path = path
            self.saved_ext_edit = False
            self.Data_Design = Qt.QMainWindow()
            self.DD = Data_Design()
            self.DD.setupUi(self.Data_Design)



            self.Filename_LineEdit.setText(str(path))

            #except:
                #pass
    #       Qt.QMessageBox.question(XM.ui.Data_Preparation_Window, 'Message',
    #            'Invalid file extention or incompatible file!' , Qt.QMessageBox.Ok)
        
    def Done(self):
        if self.Data_TableWidget.rowCount() != 0:

            xLabel = self.xAxis_ComboBox.currentText()
            yLabel = self.yAxis_ComboBox.currentText()
            #Filter = self.Open_Dialog_Filter_ComboBox.currentText()
            ToVS = self.ToVS_ComboBox.currentText()
            
            
            if ToVS == "Eclipsing Binary System":
                ToVS = "EBS"
            else:
                ToVS = "PS"
            
            
            data_1 = np.arange(self.Data_TableWidget.rowCount(),dtype = float)
            data_2 = np.arange(self.Data_TableWidget.rowCount(),dtype = float)
#            try:
            if self.Data_TableWidget.rowCount() > 3000:
                # XM.ui.Data_Preparation_Window.setEnabled(False)
                XM.ui.Data_Preparation_Window.setWindowModality(QtCore.Qt.ApplicationModal)
                self.ProgressBar.setVisible(True)
                self.ProgressBar_Label.setVisible(True)
                
            for i in range(self.Data_TableWidget.rowCount()):
                
                self.ProgressBar.setValue(int(i*100/self.Data_TableWidget.rowCount()))
                self.ProgressBar_Label.setText("Ploting"+"  "+str(int(i*100/self.Data_TableWidget.rowCount()))+"%")
                
                data_1[i] = float(self.Data_TableWidget.item(i,0).text())
                data_2[i] = float(self.Data_TableWidget.item(i,1).text())
                
                # if i/1500 == i/1500.0:
                #     Qt.qApp.processEvents()
        
            self.ProgressBar.setVisible(False)
            self.ProgressBar_Label.setVisible(False)
            XM.ui.Data_Preparation_Window.setWindowModality(QtCore.Qt.NonModal)
            
            data_x = data_1[np.argsort(data_1)]
            data_y = data_2[np.argsort(data_1)]
            
            self.data_x = data_x
            self.data_y = data_y
            
            items = [str(len(data_x)), xLabel, yLabel, ToVS]
            
            for i, item in enumerate(items):
                XM.ui.MG.Info_Table.setItem(i,0,Qt.QTableWidgetItem(item))
          
        
            XM.ui.MG.Graph_Plot.del_all_items() 
            XM.ui.MG.Graph_Plot.set_axis_title("left",yLabel)
            XM.ui.MG.Graph_Plot.set_axis_title("bottom",xLabel)
            XM.ui.MG.Graph_Plot.set_axis_font("left", QtGui.QFont("Courier", 10, 100))
            XM.ui.MG.Graph_Plot.set_axis_font("bottom", QtGui.QFont("Courier", 10, 100))
            XM.ui.MG.Graph_Plot.set_axis_direction(0, reverse=False)            
            if yLabel == 'Magnitude':
                XM.ui.MG.Graph_Plot.set_axis_direction(0, reverse=True)                
            XM.ui.MG.Graph_Plot.set_antialiasing(True)  
            # from guiqwt.builder import make

            from plotpy.builder import make

            curve_item = make.curve(data_x, data_y, marker='+', linestyle='NoPen',
                                    markerfacecolor='k',markeredgecolor='k', markersize=7)
            XM.ui.MG.Graph_Plot.add_item(curve_item)
            XM.ui.MG.Graph_Plot.do_autoscale()
            
            XM.ui.MG_Window.setEnabled(True)
            
#            XM.ui.MinMax_Window.close()
#            XM.ui.ObsCal_Window.close()
#            XM.ui.Optimization_Window.close()
#            XM.ui.Normalization_Window.close()    
#            XM.ui.Periodogram_Window.close()
            XM.ui.Data_Preparation_Window.close()     
            XM.ui.Main_Graph_Window.show()
#
#            except:
#                Qt.QMessageBox.question(self, 'Message',
#                            'Check your data in table!' , Qt.QMessageBox.Ok)
            #import Xtrema_Main_Window as XMW
            #XMW.ui.MinMax_Window.close()
    
class Data_Design(Qt.QMainWindow):
    def setupUi(self, Data_Design):
        path = XM.ui.OD.path
        # print(path)
        File = open(path, 'r')
        file_ext = path.split('.')[-1]
#        self.Data_Preparation_Window_ = Qt.QDialog(XM.MainWindow)
#        self.DP = Data_Preparation_Window()
#        self.DP.setupUi(self.Data_Preparation_Window)
        
        
        
        #self.DP = Qt.QMainWindow(self)        
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle('Delimitor')
        self.resize(500, 400)
        
        Panel_Frame = Qt.QFrame()
        Panel_Frame_HLayout = Qt.QHBoxLayout(Panel_Frame)
        Panel_Frame.setFixedHeight(150)

        self.Space_CheckBox = Qt.QCheckBox()
        self.Space_CheckBox.setText('space')
        self.Comma_CheckBox = Qt.QCheckBox()
        self.Comma_CheckBox.setText('comma')
        self.Tab_CheckBox = Qt.QCheckBox()
        self.Tab_CheckBox.setText('tab')
        self.Semicolon_CheckBox = Qt.QCheckBox()
        self.Semicolon_CheckBox.setText('semicolon')
        self.Other_CheckBox = Qt.QCheckBox()
        self.Other_CheckBox.setText('other')
        self.Other_LineEdit = Qt.QLineEdit()
        self.Other_LineEdit.setFixedSize(30,20)
        self.Other_LineEdit.setEnabled(False)
        Other_HBLayout = Qt.QHBoxLayout()
        Other_HBLayout.addWidget(self.Other_CheckBox)
        Other_HBLayout.addWidget(self.Other_LineEdit)
        
        self.Delimiter_GroupBox = Qt.QGroupBox()
        self.Delimiter_GroupBox.setStyleSheet(XM.groupBoxStyle)
        self.Delimiter_GroupBox.setFixedWidth(150)
        self.Delimiter_GroupBox.setTitle('Delimiters')
        Delimiter_GroupBox_VLayout = Qt.QVBoxLayout(self.Delimiter_GroupBox)
        
        Delimiter_GroupBox_VLayout.addWidget(self.Space_CheckBox)
        Delimiter_GroupBox_VLayout.addWidget(self.Comma_CheckBox)
        Delimiter_GroupBox_VLayout.addWidget(self.Tab_CheckBox)
        Delimiter_GroupBox_VLayout.addWidget(self.Semicolon_CheckBox)
        Delimiter_GroupBox_VLayout.addLayout(Other_HBLayout)
        
        Panel_Frame_HLayout.addWidget(self.Delimiter_GroupBox)

        
        self.Remember_GroupBox = Qt.QGroupBox()
        self.Remember_GroupBox.setStyleSheet(XM.groupBoxStyle)
        self.Remember_GroupBox.setTitle('Saved Extension(s)')
        Remember_GroupBox_VLayout = Qt.QVBoxLayout(self.Remember_GroupBox)
        
        Ext_Label1 = Qt.QLabel()
        Ext_Label1.setText('Extension')
        Ext_SC_Label = Qt.QLabel()
        Ext_SC_Label.setText(':')
        Ext_Label2 = Qt.QLabel()
        Ext_Label2.setText(file_ext)
        Ext_Label2.setFixedWidth(60)
        Ext_Label2.setAlignment(QtCore.Qt.AlignCenter)
        Ext_HLayout = Qt.QHBoxLayout()
        Ext_HLayout.addWidget(Ext_Label1)
        Space = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding,
                                    Qt.QSizePolicy.Minimum)
        Ext_HLayout.addItem(Space)
        Ext_HLayout.addWidget(Ext_SC_Label)
        Ext_HLayout.addWidget(Ext_Label2)
        """
        Delim_Label = Qt.QLabel()
        Delim_Label.setText('Delimiter')
        Delim_SC_Label = Qt.QLabel()
        Delim_SC_Label.setText(':')
        Delim_LineEdit = Qt.QLineEdit()
        Delim_LineEdit.setFixedWidth(60)
        Delim_HLayout = Qt.QHBoxLayout()
        Delim_HLayout.addWidget(Delim_Label)
        Space = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding,
                                    Qt.QSizePolicy.Minimum)
        Delim_HLayout.addItem(Space)
        Delim_HLayout.addWidget(Delim_SC_Label)
        Delim_HLayout.addWidget(Delim_LineEdit)
        """
        CharIng_Label = Qt.QLabel()
        CharIng_Label.setText('Ignored Character(s)')
        CharIng_SC_Label = Qt.QLabel()
        CharIng_SC_Label.setText(':')
        self.CharIng_LineEdit = Qt.QLineEdit()
        self.CharIng_LineEdit.setPlaceholderText("#")
        self.CharIng_LineEdit.setFixedWidth(60)
        CharIng_HLayout = Qt.QHBoxLayout()
        CharIng_HLayout.addWidget(CharIng_Label)
        Space = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding,
                                    Qt.QSizePolicy.Minimum)
        CharIng_HLayout.addItem(Space)
        CharIng_HLayout.addWidget(CharIng_SC_Label)
        CharIng_HLayout.addWidget(self.CharIng_LineEdit)
        RejectRow_Label = Qt.QLabel()
        RejectRow_Label.setText('Rejected Row(s)')
        RejectRow_SC_Label = Qt.QLabel()
        RejectRow_SC_Label.setText(':')
        self.RejectRow_LineEdit = Qt.QLineEdit()
        self.RejectRow_LineEdit.setPlaceholderText("1:1")
        self.RejectRow_LineEdit.setFixedWidth(60)
        RejectRow_HLayout = Qt.QHBoxLayout()
        RejectRow_HLayout.addWidget(RejectRow_Label)
        Space = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding,
                                    Qt.QSizePolicy.Minimum)
        RejectRow_HLayout.addItem(Space)
        RejectRow_HLayout.addWidget(RejectRow_SC_Label)
        RejectRow_HLayout.addWidget(self.RejectRow_LineEdit)
        Remember_GroupBox_VLayout.addLayout(Ext_HLayout)
        #Remember_GroupBox_VLayout.addLayout(Delim_HLayout)
        Remember_GroupBox_VLayout.addLayout(CharIng_HLayout)
        Remember_GroupBox_VLayout.addLayout(RejectRow_HLayout)
        Space = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Minimum,
                                       Qt.QSizePolicy.Expanding)
        Remember_GroupBox_VLayout.addItem(Space)
        

        import os.path
        
        self.ext = np.empty(0, dtype=str)
        self.delim = np.empty(0, dtype=str)
        self.sel_col = np.empty(0, dtype=str)
        self.rr = np.empty(0, dtype=str)
        self.exc = np.empty(0, dtype=str)
        if os.path.exists('save_ext') == True:
            exts = open('save_ext','r')
            for item in exts.readlines():
                self.ext = np.append(self.ext, item.split(';')[0])
                self.delim = np.append(self.delim, item.split(';')[1])
                self.sel_col = np.append(self.sel_col, item.split(';')[2])
                self.rr = np.append(self.rr, item.split(';')[3])
                self.exc = np.append(self.exc, item.split(';')[4].replace('\n',''))

        self.ep = np.argwhere(self.ext == file_ext)
        self.ep = np.reshape(self.ep,(len(self.ep),))
        self.saved_ext = False
        if len(self.ep) == 0:
            self.ext = np.append(self.ext, file_ext)
            self.delim = np.append(self.delim, '')
            self.sel_col = np.append(self.sel_col, '')
            self.rr = np.append(self.rr, '')
            self.exc = np.append(self.exc, '')
            self.show()
        else:
            self.CharIng_LineEdit.setText(self.exc[self.ep][0])
            self.RejectRow_LineEdit.setText(self.rr[self.ep][0])
            if self.delim[self.ep][0] == 'space': 
                self.Space_CheckBox.setChecked(True)
            elif self.delim[self.ep][0] == 'comma': 
                self.Comma_CheckBox.setChecked(True)
            elif self.delim[self.ep][0] == 'tab': 
                self.Tab_CheckBox.setChecked(True)
            elif self.delim[self.ep][0] == 'semicolon': 
                self.Semicolon_CheckBox.setChecked(True)
            else: 
                self.Other_CheckBox.setChecked(True)
                self.Other_LineEdit.setEnabled(True)
                self.Other_LineEdit.setText(self.delim[self.ep][0])
            
            self.saved_ext = True
#            else:
#                self.show()
#         print(self.rr)
        Panel_Frame_HLayout.addWidget(self.Remember_GroupBox)
            
        Spacer = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        Panel_Frame_HLayout.addItem(Spacer)

        Data_Frame = Qt.QFrame()
        Data_Frame_VLayout = Qt.QVBoxLayout(Data_Frame)
        
        self.Data_Table = Qt.QTableWidget()
        self.Data_Table.setHorizontalScrollMode(Qt.QAbstractItemView.ScrollPerPixel)
        self.Data_Table.setSelectionBehavior(Qt.QAbstractItemView.SelectColumns)
        self.Data_Table.setSelectionMode(Qt.QAbstractItemView.MultiSelection)
               
        Preview_GroupBox = Qt.QGroupBox()
        Preview_GroupBox.setStyleSheet(XM.groupBoxStyle)
        Preview_GroupBox.setTitle('Data Preview')
        Preview_GroupBox_VLayout = Qt.QVBoxLayout(Preview_GroupBox)
        
        Preview_GroupBox_VLayout.addWidget(self.Data_Table)
        
        Data_Frame_VLayout.addWidget(Preview_GroupBox)
        
        Finish_Button = Qt.QPushButton()
        Finish_Button.setText('Finish')
        Finish_LSpacerItem = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        
        Finish_HBLayout = Qt.QHBoxLayout()
        Finish_HBLayout.addItem(Finish_LSpacerItem)
        Finish_HBLayout.addWidget(Finish_Button)
        
        Main_Widget = Qt.QWidget()
        Main_VLayout = Qt.QVBoxLayout(Main_Widget)
        Main_VLayout.addWidget(Panel_Frame)
        Main_VLayout.addWidget(Data_Frame)
        Main_VLayout.addLayout(Finish_HBLayout)

        self.RejectRow_LineEdit.textChanged.connect(self.TextToColumn)
        self.CharIng_LineEdit.textChanged.connect(self.TextToColumn)
        self.Space_CheckBox.stateChanged.connect(self.TextToColumn)
        self.Comma_CheckBox.stateChanged.connect(self.TextToColumn)
        self.Tab_CheckBox.stateChanged.connect(self.TextToColumn)
        self.Semicolon_CheckBox.stateChanged.connect(self.TextToColumn)
        self.Other_CheckBox.stateChanged.connect(lambda x: self.Other_LineEdit.setEnabled(True) if 
                                                 self.Other_CheckBox.isChecked() == True else
                                                 self.Other_LineEdit.setEnabled(False))
        self.Other_CheckBox.stateChanged.connect(self.TextToColumn)                             
        self.Other_LineEdit.textChanged.connect(self.TextToColumn)
        Finish_Button.clicked.connect(self.Finish)

        # self.Data_Table.horizontalHeader().setSectionResizeMode(Qt.QHeaderView.ResizeToContents)
        #
        self.Data_Table.horizontalHeader().setStretchLastSection(True)
        # self.Data_Table.setTextElideMode(QtCore.Qt.ElideNone)

        self.setCentralWidget(Main_Widget)

        self.data_lines = File.readlines()
        # if self.saved_ext is not True:
        #     self.Data_Table.setRowCount(len(self.data_lines))
        #     self.Data_Table.setColumnCount(1)
        #     for i, item in enumerate(self.data_lines):
        #         self.Data_Table.setItem(i,0,Qt.QTableWidgetItem(item.strip()))
        #
        #     self.Data_Table.horizontalHeader().setSectionResizeMode(Qt.QHeaderView.ResizeToContents)

        self.TextToColumn()
        
        
        #self.retranslateUi(Data_Design)
        QtCore.QMetaObject.connectSlotsByName(Data_Design)
        
        
    def TextToColumn(self):
        #from multiprocessing import Pool
        # self.Data_Table.horizontalHeader().setSectionResizeMode(Qt.QHeaderView.Interactive)
        
        delim = []
        if self.Space_CheckBox.isChecked() == True:
            delim.append(None)
        if self.Comma_CheckBox.isChecked() == True:
            delim.append(',')
        if self.Semicolon_CheckBox.isChecked() == True:
            delim.append(';')
        if self.Tab_CheckBox.isChecked() == True:
            delim.append('\t')
        if self.Other_CheckBox.isChecked() == True:
            if self.Other_LineEdit.text() != '':
                delim.append(str(self.Other_LineEdit.text()))
                
        """
        def doWork(rows):
            self.final_data = [[],[]]
            for item in rows:
                for del_ in delim:
                    item = '|'.join(item.split(del_))
                self.final_data[0].append(item.split('|'))    
                self.final_data[1].append(len(item.split('|')))
            
            self.Data_Table.setRowCount(len(self.final_data[1]))
            self.Data_Table.setColumnCount(max(self.final_data[1]))
            for i, row_item in enumerate(self.final_data[0]):
                for j, item in enumerate(row_item):
                    self.Data_Table.setItem(i, j, Qt.QTableWidgetItem(str(item)))    
        
        
        pool = Pool(processes=8)
        l = len(self.data_lines)
        pool.apply_async(doWork, (self.data_lines))
        """
    
        """        
        q = Queue()
        #create 4 sub-processes to do the work
        l = len(self.data_lines)
        p1 = Process(target=doWork, args=(self.data_lines[0:l/4]))
        p1.start()
        p2 = Process(target=doWork, args=(self.data_lines[l/4:2*l/4]))
        p2.start()
        p3 = Process(target=doWork, args=(self.data_lines[2*l/4:3*l/4]))
        p3.start()
        p4 = Process(target=doWork, args=(self.data_lines[3*l/4:4*l/4]))
        p4.start()         
                
        results = []
        #grab 4 values from the queue, one for each process
        for i in range(4):
            #set block=True to block until we get a result
            results.append(q.get(True))
         
        #sum the partial results to get the final result
        #finalSum = sumList(results)
         
        p1.join()
        p2.join()
        p3.join()
        p4.join()        
        """       
        
        """
        def prepTable(rows):
            self.final_data = [[],[]]
            for item in rows:
                for del_ in delim:
                    item = '|'.join(item.split(del_))
                self.final_data[0].append(item.split('|'))    
                self.final_data[1].append(len(item.split('|')))
            return self.final_data
            
            
        p = Pool(processes=8)        
        m = p.imap(prepTable, self.data_lines)
        print m.next()
            
        self.Data_Table.setRowCount(len(self.final_data[1]))
        self.Data_Table.setColumnCount(max(self.final_data[1]))
        def loadTable(rows):
            for i, row_item in enumerate(rows):
                for j, item in enumerate(row_item):
                    self.Data_Table.setItem(i, j, Qt.QTableWidgetItem(str(item)))
        
        
        p.apply_async(loadTable, self.final_data[0])
        p.close()
        """
        CI = str(self.CharIng_LineEdit.text())
        RR = str(self.RejectRow_LineEdit.text())
        try:
            rr = [int(RR.split(':')[0]),
                       len(self.data_lines)-int(RR.split(':')[1])]
        except:
            rr = [0,len(self.data_lines)]     

        self.final_data = [[],[]]
        for item in self.data_lines[rr[0]:rr[1]]:
            for del_ in delim:
                if CI:
                    for i in CI.split(','):
                        item = item.replace(i,'')
                item = '|'.join(item.split(del_))
            self.final_data[0].append(item.split('|'))    
            self.final_data[1].append(len(item.split('|')))

        if self.saved_ext is not True or XM.ui.OD.saved_ext_edit == True:
            self.Data_Table.setRowCount(len(self.final_data[1]))
            self.Data_Table.setColumnCount(max(self.final_data[1]))
            for i, row_item in enumerate(self.final_data[0]):
                for j, item in enumerate(row_item):
                    self.Data_Table.setItem(i, j, Qt.QTableWidgetItem(str(item)))

            # self.Data_Table.horizontalHeader().setSectionResizeMode(Qt.QHeaderView.ResizeToContents)
            try:
                self.Data_Table.selectColumn(int(self.sel_col[self.ep[0]].split(',')[0]))
                self.Data_Table.selectColumn(int(self.sel_col[self.ep[0]].split(',')[1]))
            except:
                pass
        else:
            self.Finish()
        
        
        
    def Finish(self):
        
        if self.saved_ext is not True or XM.ui.OD.saved_ext_edit == True:
            SecColInd = self.Data_Table.selectionModel().selectedColumns()
        else:
            SecColInd = SecCol = [int(self.sel_col[self.ep[0]].split(',')[0]),
                                  int(self.sel_col[self.ep[0]].split(',')[1])]
            
        if len(SecColInd) == 2:
            self.close()
            
            if self.saved_ext is not True or XM.ui.OD.saved_ext_edit == True:
                SecCol = [SecColInd[0].column(), SecColInd[1].column()]

            # XM.ui.Data_Preparation_Window.setEnabled(False)
            XM.ui.Data_Preparation_Window.setWindowModality(QtCore.Qt.ApplicationModal)
            XM.ui.OD.ProgressBar.setVisible(True)
            XM.ui.OD.ProgressBar_Label.setVisible(True)
            
            XM.ui.OD.Data_TableWidget.setRowCount(0)
            nop = len(self.final_data[0])
            for i, item in enumerate(self.final_data[0]):
                try:
                    if (self.isfloat(item[SecCol[0]]) == True and
                        self.isfloat(item[SecCol[1]]) == True):
                        row = XM.ui.OD.Data_TableWidget.rowCount()
                        XM.ui.OD.Data_TableWidget.insertRow(row)
                        XM.ui.OD.Data_TableWidget.setItem(row, 0,
                                                         Qt.QTableWidgetItem(str(float(item[SecCol[0]]))))
                        XM.ui.OD.Data_TableWidget.setItem(row, 1,
                                                         Qt.QTableWidgetItem(str(float(item[SecCol[1]]))))
                except:
                    pass
                                                 
                XM.ui.OD.ProgressBar.setValue(int(i*100/nop))
                XM.ui.OD.ProgressBar_Label.setText("Loading"+"  "+str(int(i*100/nop))+"%")

                # if i/1500 == i/1500.0:
                #     Qt.qApp.processEvents()

            XM.ui.OD.ProgressBar.setVisible(False)
            XM.ui.OD.ProgressBar_Label.setVisible(False)
            # XM.ui.Data_Preparation_Window.setEnabled(True)
            XM.ui.Data_Preparation_Window.setWindowModality(QtCore.Qt.NonModal)
            XM.ui.Data_Preparation_Window.show()
            
            if XM.ui.OD.Data_TableWidget.rowCount() == 0:
                XM.ui.OD.saved_ext_edit = True
                XM.ui.OD.DD.show()
                XM.ui.OD.DD.TextToColumn()

            exts = open('save_ext','w')
            
            delim = [0]*len(self.delim)
            delim[:] = self.delim[:]
            rr = [0]*len(self.rr)
            rr[:] = self.rr[:]
            sel_col = [0]*len(self.sel_col)
            sel_col[:] = self.sel_col[:]
            exc = [0]*len(self.sel_col)
            exc[:] = self.exc[:]
            
            
            CW = self.Delimiter_GroupBox.findChildren(Qt.QCheckBox)
            del_ = ''
            for C in CW:
                if C.checkState() == 2:
                    del_ = str(C.text()) +','+ del_
            
            if len(self.ep) == 0:
                rr[-1] = self.RejectRow_LineEdit.text()
                delim[-1] = del_[:-1]
                sel_col[-1] = str(SecCol[0])+','+str(SecCol[1])
                exc[-1] = self.CharIng_LineEdit.text()
                
            else:
                rr[self.ep[0]] = self.RejectRow_LineEdit.text()
                sel_col[self.ep[0]] = str(SecCol[0])+','+str(SecCol[1])
                exc[self.ep[0]] = self.CharIng_LineEdit.text()
            
            for i in range(len(self.ext)):
                exts.write(str(self.ext[i])+';'+
                           str(delim[i])+';'+
                           str(sel_col[i])+';'+
                           str(rr[i])+';'+
                           str(exc[i])+'\n')
        else:
            Qt.QMessageBox.question(self, 'Message',
                'Please select only two column' , Qt.QMessageBox.Ok)

    def isfloat(self, x):
        try:
            float(x)
            return True
        except:
            return False
# import sys
#
# app = Qt.QApplication(sys.argv)
# app.setStyle(Qt.QStyleFactory.create("cleanlooks"))
# window = Qt.QDialog()
# ui = Data_Preparation_Window()
# ui.setupUi(window)
#################################################################
"Data_Preparation_Window End"
#################################################################