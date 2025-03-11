# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:39:43 2015

@author: TheLichWing
"""
import Calculations as cl
import Main_Window as XM
import numpy as np
from plotpy.builder import make
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets as Qt


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
"O-C Window Start"
#################################################################
class Ui_OC_Widget(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/OC.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        self.centralwidget = Qt.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_5 = Qt.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.MainSplitter = Qt.QSplitter(self.centralwidget)
        self.MainSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.MainSplitter.setObjectName(_fromUtf8("MainSplitter"))
        self.Graph_Frame = Qt.QFrame(self.MainSplitter)
        self.Graph_Frame.setMinimumSize(QtCore.QSize(475, 0))
        self.Graph_Frame.setFrameShape(Qt.QFrame.StyledPanel)
        self.Graph_Frame.setFrameShadow(Qt.QFrame.Raised)
        self.Graph_Frame.setObjectName(_fromUtf8("Graph_Frame"))
        self.Panel_Frame = Qt.QFrame(self.MainSplitter)
        self.Panel_Frame.setMinimumSize(QtCore.QSize(305, 0))
        self.Panel_Frame.setMaximumSize(QtCore.QSize(305, 16777215))
        self.Panel_Frame.setFrameShape(Qt.QFrame.StyledPanel)
        self.Panel_Frame.setFrameShadow(Qt.QFrame.Raised)
        self.Panel_Frame.setObjectName(_fromUtf8("Panel_Frame"))
        self.verticalLayout = Qt.QVBoxLayout(self.Panel_Frame)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Edit_Frame = Qt.QFrame(self.Panel_Frame)
        self.Edit_Frame.setMinimumSize(QtCore.QSize(300, 0))
        self.Edit_Frame.setMaximumSize(QtCore.QSize(305, 185))
        self.Edit_Frame.setFrameShape(Qt.QFrame.StyledPanel)
        self.Edit_Frame.setFrameShadow(Qt.QFrame.Raised)
        self.Edit_Frame.setObjectName(_fromUtf8("Edit_Frame"))
        self.horizontalLayout_6 = Qt.QHBoxLayout(self.Edit_Frame)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.Edit_HLayout = Qt.QHBoxLayout()
        self.Edit_HLayout.setSpacing(2)
        self.Edit_HLayout.setObjectName(_fromUtf8("Edit_HLayout"))
        self.Correction_Frame = Qt.QFrame(self.Edit_Frame)
        # self.Correction_Frame.setFixedSize(QtCore.QSize(159, 181))
        self.Correction_Frame.setFrameShape(Qt.QFrame.NoFrame)
        self.Correction_Frame.setFrameShadow(Qt.QFrame.Raised)
        self.Correction_Frame.setLineWidth(1)
        self.Correction_Frame.setObjectName(_fromUtf8("Correction_Frame"))
        self.horizontalLayout_3 = Qt.QHBoxLayout(self.Correction_Frame)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.Correction_GBox = Qt.QGroupBox(self.Correction_Frame)
        self.Correction_GBox.setObjectName(_fromUtf8("Correction_GBox"))
        self.verticalLayout_2 = Qt.QVBoxLayout(self.Correction_GBox)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Show_Correct_Fit_PushButton = Qt.QPushButton(self.Correction_GBox)
        self.Show_Correct_Fit_PushButton.setObjectName(_fromUtf8("Show_Correct_Fit_PushButton"))
        self.verticalLayout_2.addWidget(self.Show_Correct_Fit_PushButton)
        self.Correct_PushButton = Qt.QPushButton(self.Correction_GBox)
        self.Correct_PushButton.setObjectName(_fromUtf8("Correct_PushButton"))
        self.Correct_PushButton.setEnabled(False)
        self.verticalLayout_2.addWidget(self.Correct_PushButton)
        self.Correction_Table = Qt.QTableWidget(self.Correction_GBox)
        self.Correction_Table.setColumnCount(1)
        self.Correction_Table.setObjectName(_fromUtf8("Correction_Table"))
        self.Correction_Table.setRowCount(4)
        item = Qt.QTableWidgetItem()
        self.Correction_Table.setVerticalHeaderItem(0, item)
        item = Qt.QTableWidgetItem()
        self.Correction_Table.setVerticalHeaderItem(1, item)
        item = Qt.QTableWidgetItem()
        self.Correction_Table.setVerticalHeaderItem(2, item)
        item = Qt.QTableWidgetItem()
        self.Correction_Table.setVerticalHeaderItem(3, item)
        self.Correction_Table.horizontalHeader().setVisible(False)
        self.Correction_Table.horizontalHeader().setDefaultSectionSize(94)
        self.Correction_Table.horizontalHeader().setMinimumSectionSize(94)
        self.Correction_Table.horizontalHeader().setSortIndicatorShown(False)
        self.Correction_Table.verticalHeader().setDefaultSectionSize(25)
        self.Correction_Table.verticalHeader().setMinimumSectionSize(25)
        self.Correction_Table.setEditTriggers(Qt.QAbstractItemView.NoEditTriggers)
        self.Correction_Table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.Correction_Table)
        self.horizontalLayout_3.addWidget(self.Correction_GBox)
        self.Edit_HLayout.addWidget(self.Correction_Frame)
        # self.GetData_Frame = Qt.QFrame(self.Edit_Frame)
        # self.GetData_Frame.setFixedSize(QtCore.QSize(135, 181))
        # self.GetData_Frame.setFrameShape(Qt.QFrame.NoFrame)
        # self.GetData_Frame.setFrameShadow(Qt.QFrame.Raised)
        # self.GetData_Frame.setLineWidth(1)
        # self.GetData_Frame.setObjectName(_fromUtf8("GetData_Frame"))
        # self.horizontalLayout_4 = Qt.QHBoxLayout(self.GetData_Frame)
        # self.horizontalLayout_4.setSpacing(2)
        # self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        # self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        # self.Get_Data_GBox = Qt.QGroupBox(self.GetData_Frame)
        # self.Get_Data_GBox.setObjectName(_fromUtf8("Get_Data_GBox"))
        # self.verticalLayout_3 = Qt.QVBoxLayout(self.Get_Data_GBox)
        # self.verticalLayout_3.setSpacing(5)
        # self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        # self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        # self.Star_Name_HLayout = Qt.QHBoxLayout()
        # self.Star_Name_HLayout.setSpacing(2)
        # self.Star_Name_HLayout.setObjectName(_fromUtf8("Star_Name_HLayout"))
        # self.Star_Name_Label = Qt.QLabel(self.Get_Data_GBox)
        # self.Star_Name_Label.setObjectName(_fromUtf8("Star_Name_Label"))
        # self.Star_Name_HLayout.addWidget(self.Star_Name_Label)
        # self.Star_Name_LineEdit = Qt.QLineEdit(self.Get_Data_GBox)
        # self.Star_Name_LineEdit.setObjectName(_fromUtf8("Star_Name_LineEdit"))
        # self.Star_Name_HLayout.addWidget(self.Star_Name_LineEdit)
        # self.verticalLayout_3.addLayout(self.Star_Name_HLayout)
        # self.OC_Gateway_CBox = Qt.QCheckBox(self.Get_Data_GBox)
        # self.OC_Gateway_CBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        # self.OC_Gateway_CBox.setObjectName(_fromUtf8("OC_Gateway_CBox"))
        # self.OC_Gateway_CBox.setChecked(True)
        # self.OC_Gateway_CBox.setEnabled(False)
        # self.verticalLayout_3.addWidget(self.OC_Gateway_CBox)
        # self.BAV_CBox = Qt.QCheckBox(self.Get_Data_GBox)
        # self.BAV_CBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        # self.BAV_CBox.setObjectName(_fromUtf8("BAV_CBox"))
        # self.BAV_CBox.setEnabled(False)
        # self.verticalLayout_3.addWidget(self.BAV_CBox)
        # self.T0P_GetCBox = Qt.QCheckBox(self.Get_Data_GBox)
        # self.T0P_GetCBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        # self.T0P_GetCBox.setObjectName(_fromUtf8("T0P_GetCBox"))
        # self.verticalLayout_3.addWidget(self.T0P_GetCBox)
        # self.GetData_PushButton = Qt.QPushButton(self.Get_Data_GBox)
        # self.GetData_PushButton.setObjectName(_fromUtf8("GetData_PushButton"))
        # self.verticalLayout_3.addWidget(self.GetData_PushButton)
        
        # self.GetData_T0_LineEdit = Qt.QLineEdit()
        # self.GetData_T0_LineEdit.setReadOnly(True)
        # self.GetData_T0_LineEdit.setFixedWidth(100)
        # self.GetData_T0_Label = Qt.QLabel()
        # self.GetData_T0_Label.setText('T0 :')
        # self.GetData_T0_HLayout = Qt.QHBoxLayout()
        # self.GetData_T0_HLayout.addWidget(self.GetData_T0_Label)
        # self.GetData_T0_HLayout.addWidget(self.GetData_T0_LineEdit)

        # self.GetData_P_LineEdit = Qt.QLineEdit()
        # self.GetData_P_LineEdit.setReadOnly(True)
        # self.GetData_P_LineEdit.setFixedWidth(100)
        # self.GetData_P_Label = Qt.QLabel()
        # self.GetData_P_Label.setText('P :')
        # self.GetData_P_HLayout = Qt.QHBoxLayout()
        # self.GetData_P_HLayout.addWidget(self.GetData_P_Label)
        # self.GetData_P_HLayout.addWidget(self.GetData_P_LineEdit)

        # self.verticalLayout_3.addLayout(self.GetData_T0_HLayout)
        # self.verticalLayout_3.addLayout(self.GetData_P_HLayout)



        # self.horizontalLayout_4.addWidget(self.Get_Data_GBox)
        # self.Edit_HLayout.addWidget(self.GetData_Frame)
        self.horizontalLayout_6.addLayout(self.Edit_HLayout)
        self.verticalLayout.addWidget(self.Edit_Frame)
        self.Table_Frame = Qt.QFrame(self.Panel_Frame)
        self.Table_Frame.setMinimumSize(QtCore.QSize(300, 0))
        self.Table_Frame.setMaximumSize(QtCore.QSize(305, 16777215))
        self.Table_Frame.setFrameShape(Qt.QFrame.StyledPanel)
        self.Table_Frame.setFrameShadow(Qt.QFrame.Raised)
        self.Table_Frame.setObjectName(_fromUtf8("Table_Frame"))
        self.verticalLayout_4 = Qt.QVBoxLayout(self.Table_Frame)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.Main_Table = Qt.QTableWidget(self.Table_Frame)
        self.Main_Table.setSortingEnabled(True)
        self.Main_Table.setObjectName(_fromUtf8("Main_Table"))
        self.ToVS = XM.ui.OD.ToVS_ComboBox.currentIndex()
        
        if self.ToVS == 0:
            self.Main_Table.setColumnCount(5)
        else:
            self.Main_Table.setColumnCount(4)
        self.Main_Table.setRowCount(0)
        
        item = Qt.QTableWidgetItem()
        self.Main_Table.setHorizontalHeaderItem(0, item)
        self.Main_Table.setColumnWidth(0,69)
        item = Qt.QTableWidgetItem()
        self.Main_Table.setHorizontalHeaderItem(1, item)
        self.Main_Table.setColumnWidth(1,65)
        item = Qt.QTableWidgetItem()
        self.Main_Table.setHorizontalHeaderItem(2, item)
        self.Main_Table.setColumnWidth(2,85)
        
        if self.ToVS == 0:
            item = Qt.QTableWidgetItem()
            self.Main_Table.setHorizontalHeaderItem(3, item)
            self.Main_Table.setColumnWidth(3,33)
            item = Qt.QTableWidgetItem()
            self.Main_Table.setHorizontalHeaderItem(4, item)
            self.Main_Table.setColumnWidth(4,48)
        else:
            item = Qt.QTableWidgetItem()
            self.Main_Table.setHorizontalHeaderItem(3, item)
            self.Main_Table.setColumnWidth(3,48)
        
        self.verticalLayout_4.addWidget(self.Main_Table)
        # self.Draw_OC_PushButton = Qt.QPushButton(self.Table_Frame)
        # self.Draw_OC_PushButton.setObjectName(_fromUtf8("Draw_OC_PushButton"))
        # self.verticalLayout_4.addWidget(self.Draw_OC_PushButton)
        self.Open_Save_HLayout = Qt.QHBoxLayout()
        self.Open_Save_HLayout.setSpacing(2)
        self.Open_Save_HLayout.setObjectName(_fromUtf8("Open_Save_HLayout"))
        # self.Open_PushButton = Qt.QPushButton(self.Table_Frame)
        # self.Open_PushButton.setObjectName(_fromUtf8("Open_PushButton"))
        # self.Open_Save_HLayout.addWidget(self.Open_PushButton)
        self.Save_PushButton = Qt.QPushButton(self.Table_Frame)
        self.Save_PushButton.setObjectName(_fromUtf8("Save_PushButton"))
        self.Open_Save_HLayout.addWidget(self.Save_PushButton)
        self.verticalLayout_4.addLayout(self.Open_Save_HLayout)
        self.verticalLayout.addWidget(self.Table_Frame)
        self.verticalLayout_5.addWidget(self.MainSplitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = Qt.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = Qt.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        
        from plotpy.plot import PlotDialog
        self.Graph_Win = PlotDialog(edit=False, toolbar=True)
        from plotpy.tools import HCursorTool
        self.Graph_Win.manager.add_tool(HCursorTool)
        self.Graph_Plot = self.Graph_Win.get_plot()
        self.Graph_Toolbar = self.Graph_Win.get_toolbar()        
        self.Graph_Icons  = self.Graph_Toolbar.actions()
#        self.Graph_Icons[7].setVisible(False)
#        self.Graph_Icons[8].setVisible(False)
        self.Graph_HLayout  = Qt.QHBoxLayout(self.Graph_Frame)
        self.Graph_HLayout.setContentsMargins(0, 0, 0, 0)
        self.Graph_HLayout.addWidget(self.Graph_Win)

        self.Save_PushButton.clicked.connect(self.Save)
        # self.Open_PushButton.clicked.connect(self.Open)
        # self.Draw_OC_PushButton.clicked.connect(self.Draw_OC)
        # self.Star_Name_LineEdit.returnPressed.connect(self.GDFT)
        # self.GetData_PushButton.clicked.connect(self.GDFT)
        self.Show_Correct_Fit_PushButton.clicked.connect(self.Show_Cor_Fit)
        self.Correct_PushButton.clicked.connect(self.Correct)
        
        self.data_sta = []
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "O-C Window", None))
        self.Correction_GBox.setTitle(_translate("MainWindow", "Correction", None))
        self.Show_Correct_Fit_PushButton.setText(_translate("MainWindow", "Show Correction Fit", None))
        self.Correct_PushButton.setText(_translate("MainWindow", "Correct", None))
        item = self.Correction_Table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Delta T0", None))
        item = self.Correction_Table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Delta P", None))
        item = self.Correction_Table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New T0", None))
        item = self.Correction_Table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New P", None))
        # self.Get_Data_GBox.setTitle(_translate("MainWindow", "Get Data From Net", None))
        # self.Star_Name_Label.setText(_translate("MainWindow", "Star Name:", None))
        # self.OC_Gateway_CBox.setText(_translate("MainWindow", "O-C Gateway", None))
        # self.BAV_CBox.setText(_translate("MainWindow", "BAV", None))
        # self.T0P_GetCBox.setText(_translate("MainWindow", "Use selected database T0 and P", None))
        # self.GetData_PushButton.setText(_translate("MainWindow", "Get Data", None))
        item = self.Main_Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Epoch", None))
        item = self.Main_Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "O-C", None))
        item = self.Main_Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Min/Max Time", None))
        if XM.ui.OD.ToVS_ComboBox.currentIndex() == 0:
            item = self.Main_Table.horizontalHeaderItem(3)
            item.setText(_translate("MainWindow", "Type", None))
            item = self.Main_Table.horizontalHeaderItem(4)
            item.setText(_translate("MainWindow", "Method", None))
        else:
            item = self.Main_Table.horizontalHeaderItem(3)
            item.setText(_translate("MainWindow", "Method", None))
        # self.Draw_OC_PushButton.setText(_translate("MainWindow", "Draw O-C", None))
        # self.Open_PushButton.setText(_translate("MainWindow", "Open", None))
        self.Save_PushButton.setText(_translate("MainWindow", "Save", None))

    def Save(self):
        path, _ = Qt.QFileDialog.getSaveFileName(
                        Qt.QMainWindow(), 'Save File', '', 'TXT(*.txt)')

        try:    
            data = open(str(path),'w')
            for i in range(self.Main_Table.rowCount()):
            #for j in range(self.Main_Table.columnCount()):
                T = str(self.Main_Table.item(i,2).text())
                type_ = str(self.Main_Table.item(i,3).text())
                epoch = str(self.Main_Table.item(i,0).text())
                oc = str(self.Main_Table.item(i,1).text())
                if self.Main_Table.item(i,4) != None:
                    met = str(self.Main_Table.item(i,4).text())
                else:
                    met = ''
                data.write(T+' '+type_+' '+epoch+' '+oc+' '+met+'\n')
                    
                    
                    
                    
#                    try:
#                        item = str(self.Main_Table.item(i,j).text())
#                        data.write((item if len(item.strip()) != 0 else 'N/A') + '\t')
#                    except:
#                        data.write('N/A')
#                data.write('\n')
        except:
            pass
    
    def Open(self):   
        path = Qt.QFileDialog.getOpenFileName(
            Qt.QMainWindow(), 'Open File', '', "Open Files (*.txt *.csv)")
        
        try:
            with open(str(path), 'rb') as stream:
                print(stream)
                self.Main_Table.setRowCount(0)
                import csv
                for rowdata in csv.reader(stream):
                    row = self.Main_Table.rowCount()
                    self.Main_Table.insertRow(row)
                    item = Qt.QTableWidgetItem(rowdata[0].split()[0])
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.Main_Table.setItem(row, 2, item)
                    item = Qt.QTableWidgetItem(rowdata[0].split()[1])
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.Main_Table.setItem(row, 3, item)
            self.Draw_OC()
        except:
            pass                
        
    def Draw_OC(self):
        
        T0 = XM.ui.MG.T0_Lineedit.text()
        P = XM.ui.MG.P_Lineedit.text()

        mins = np.arange(0,dtype=np.float64)
        types = np.arange(0,dtype=np.float64)
        method = np.arange(0,dtype=np.float64)
        for i in range(self.Main_Table.rowCount()):
            item_mm = self.Main_Table.item(i,2)
            item_types = self.Main_Table.item(i,3)
            item_method = self.Main_Table.item(i,4)
            if str(item_mm.text()).replace('.','',1).isdigit() == True and \
               str(item_types.text()).replace('.','',1).isdigit() == True:
                mins = np.hstack((mins,float(item_mm.text())))
                types = np.hstack((types,int(item_types.text())))
                if item_method is None:
                    method = np.hstack((method,'ccd'))
                else:
                    if item_method.text() == '':
                        method = np.hstack((method,'ccd'))
                    else:
                        method = np.hstack((method,str(item_method.text())))

        if len(mins) > 0:
            OC = cl.OC(mins,types,T0,P)

            self.Main_Table.setRowCount(len(mins))
            for i in range(len(OC[0])):
                item_Eduz = Qt.QTableWidgetItem(str(OC[0][i]))
                item_Eduz.setTextAlignment(QtCore.Qt.AlignCenter)
                self.Main_Table.setItem(i, 0, item_Eduz)
                item_OC = Qt.QTableWidgetItem(str('%0.2f' % (float(OC[1][i])*24*60)))
                item_OC.setTextAlignment(QtCore.Qt.AlignCenter)
                self.Main_Table.setItem(i, 1, item_OC)
                item_mm = Qt.QTableWidgetItem(str('%0.5f' % float(mins[i])))
                item_mm.setTextAlignment(QtCore.Qt.AlignCenter)
                self.Main_Table.setItem(i, 2, item_mm)
                item_types = Qt.QTableWidgetItem(str(int(types[i])))
                item_types.setTextAlignment(QtCore.Qt.AlignCenter)
                self.Main_Table.setItem(i, 3, item_types)
                item_method = Qt.QTableWidgetItem(str(method[i]))
                item_method.setTextAlignment(QtCore.Qt.AlignCenter)
                self.Main_Table.setItem(i, 4, item_method)

            self.Graph_Plot.del_all_items()
            self.Graph_Plot.set_axis_title("left","O-C (mins)")
            self.Graph_Plot.set_axis_title("bottom","Epoch")
            self.Graph_Plot.set_axis_font("left", QtGui.QFont("Courier", 10, 100))
            self.Graph_Plot.set_axis_font("bottom", QtGui.QFont("Courier", 10, 100))
            self.Graph_Plot.set_antialiasing(True)

            where_min1 = np.argwhere(types == 1)
            where_min2 = np.argwhere(types == 2)
            where_min1 = np.reshape(where_min1, (len(where_min1),))
            where_min2 = np.reshape(where_min2, (len(where_min2),))

            OC1 = [OC[0][where_min1],OC[1][where_min1]]
            OC2 = [OC[0][where_min2],OC[1][where_min2]]

            method1 = method[np.argwhere(types == 1)]
            method2 = method[np.argwhere(types == 2)]

            method1 = np.reshape(method1, (len(method1),))
            method2 = np.reshape(method2, (len(method2),))

            met1 = np.unique(method1)
            met2 = np.unique(method2)

            for i in range(len(met1)):
                where_met1 = np.argwhere(method1 == met1[i])
                where_met1 = np.reshape(where_met1, (len(where_met1),))

                if met1[i] == 'ccd':
                    marker = 'Ellipse'
                elif met1[i] == 'pe':
                    marker = 'Diamond'
                elif met1[i] == 'pg':
                    marker = 'Triangle'
                elif met1[i] == 'vis':
                    marker = 'Cross'

                curve_item_1 = make.curve(OC1[0][where_met1], OC1[1][where_met1]*24*60,
                                            'Primary Minimum' + "(" + str(len(where_met1))+")",
                                            marker=marker,
                                            linestyle='NoPen',
                                            markerfacecolor='b',
                                            markeredgecolor='b',
                                            markersize=7)
                self.Graph_Plot.add_item(curve_item_1)

            for i in range(len(met2)):
                where_met2 = np.argwhere(method2 == met2[i])
                where_met2 = np.reshape(where_met2, (len(where_met2),))

                if met2[i] == 'ccd':
                    marker2 = 'Ellipse'
                elif met2[i] == 'pe':
                    marker2 = 'Diamond'
                elif met2[i] == 'pg':
                    marker2 = 'Triangle'
                elif met2[i] == 'vis':
                    marker2 = 'Cross'

                curve_item_2 = make.curve(OC2[0][where_met2], OC2[1][where_met2]*24*60,
                                        'Secondary Minimum' + "(" + str(len(where_met2)) + ")",
                                        marker=marker2,
                                        linestyle='NoPen',
                                        markerfacecolor='r',
                                        markeredgecolor='r',
                                        markersize=7)
                self.Graph_Plot.add_item(curve_item_2)
            legend = make.legend("TR")#, restrict_items=[curve_item_1,curve_item_2])
            self.Graph_Plot.add_item(legend)
            self.Graph_Plot.do_autoscale()
        else:
            Qt.QMessageBox.question(XM.window, 'Message',
            'The Table has no any Min/Max value and/or type', Qt.QMessageBox.Ok)

    def Show_Cor_Fit(self):
        T0 = XM.ui.MG.T0_Lineedit.text()
        P = XM.ui.MG.P_Lineedit.text()

        items =  self.Graph_Plot.get_items()
        from plotpy.items import CurveItem
        from plotpy.items import XRangeSelection

        self.curves = []
        range_ = []
        for item in items:
            if type(item) == CurveItem:
                self.curves.append(item)
            if type(item) == XRangeSelection:
                range_.append(item)
        try:
            data_x = np.arange(0,dtype=float)
            data_y = np.arange(0,dtype=float)
            for item in self.curves:
                if type(item) == CurveItem:
                    data_x = np.hstack((data_x,
                             cl.PlotRangeData(item,range_[0])[0]))
                    data_y = np.hstack((data_y,
                             cl.PlotRangeData(item,range_[0])[1]))

    #        import matplotlib.pyplot as plt
    #        plt.figure(1)
    #        plt.plot(data_x, data_y, 'bo')

            sort = np.argsort(data_x)
            data_x = data_x[sort]
            data_y = data_y[sort]

            while str(data_x[-1]).replace('-','',1).replace('.','',1).isdigit() == False:
                data_x = data_x[:-1]
                data_y = data_y[:-1]

            #print data_x
            if len(data_x) > 1:
                z,z1,z2,z3,z4=np.polyfit(data_x, data_y, 1, full=True)
                self.conf=np.poly1d(z)

                self.Delta_T0 = z[1]/float(60*24)
                self.Delta_P = z[0]/float(60*24)

                item_delta_T0 = Qt.QTableWidgetItem(str('%0.11f' % self.Delta_T0))
                self.Correction_Table.setItem(0,0,item_delta_T0)
                item_delta_P = Qt.QTableWidgetItem(str('%0.11f' % self.Delta_P))
                self.Correction_Table.setItem(1,0,item_delta_P)
                item_New_T0 = Qt.QTableWidgetItem(str('%0.6f' % (float(T0) + self.Delta_T0)))
                self.Correction_Table.setItem(2,0,item_New_T0)
                item_New_P = Qt.QTableWidgetItem(str('%0.6f' % (float(P) + self.Delta_P)))
                self.Correction_Table.setItem(3,0,item_New_P)

                range_=np.linspace(min(data_x), max(data_x), 1000)

                try:
                    self.Graph_Plot.del_item(self.curve_item)
                except:
                    pass

                self.curve_item = make.curve(range_, self.conf(range_), "Fit", color = 'k')
                self.Graph_Plot.add_item(self.curve_item)
                self.Graph_Plot.show_items()
                self.Correct_PushButton.setEnabled(True)
            else:
                Qt.QMessageBox.question(XM.window, 'Message',
                'Need at least two points', Qt.QMessageBox.Ok)
        except:
            Qt.QMessageBox.question(XM.window, 'Message',
            'Please select a region on O-C curve', Qt.QMessageBox.Ok)

    def Correct(self):
        T0 = XM.ui.MG.T0_Lineedit.text()
        P = XM.ui.MG.P_Lineedit.text()

        XM.ui.MG.T0_Lineedit.setText(str('%06f' % (float(T0) + self.Delta_T0)))
        XM.ui.MG.P_Lineedit.setText(str('%06f' % (float(P) + self.Delta_P)))

        # self.GetData_T0_LineEdit.setText(str('%06f' % (float(T0) + self.Delta_T0)))
        # self.GetData_P_LineEdit.setText(str('%06f' % (float(P) + self.Delta_P)))

        self.Draw_OC()
        self.Correct_PushButton.setEnabled(False)

#     def GDFT(self):
#         Star_Name = str(self.Star_Name_LineEdit.text())
#         Star_Name = Star_Name.split()
#
#         #try:
#         if len(Star_Name) > 1:
#             if self.OC_Gateway_CBox.isChecked() == True:
#                 link = "http://var.astro.cz/ocgate/ocgate.php?star="+ \
#                         Star_Name[0]+"+"+Star_Name[1]+"&submit=Submit&lang=en"
#
#             import StringIO
#             import urllib2
#             import BeautifulSoup
#
#             htmlSource = urllib2.urlopen(urllib2.Request(link)).read()
#             soup =  BeautifulSoup.BeautifulSoup(htmlSource)
#
#             raw_data = str(soup.find(attrs={'name':'tmp'}))[132:-12]
#             IO_data = StringIO.StringIO(raw_data)
#             data_lines = IO_data.readlines()
#
#             LE = str(soup.find(attrs={'name':'ocdiagram'}))
#             LE = LE.split('&')
#
#             if len(LE) > 1:
#                 T0 = LE[2].split(';')
#                 P = LE[3].split(';')
#
#                 if self.T0P_GetCBox.isChecked() == True:
#                     XM.ui.MG.T0_Lineedit.setText(str(T0[1][2:]))
#                     XM.ui.MG.P_Lineedit.setText(str(P[1][4:]))
#
#                 self.GetData_T0_LineEdit.setText(str(T0[1][2:]))
#                 self.GetData_P_LineEdit.setText(str(P[1][4:]))
#
#                 data_x = np.arange(0,dtype=float)
#                 data_y = np.arange(0,dtype=float)
#
#                 for i in range(self.Main_Table.rowCount()-1,0,-1):
#                     if i >= self.data_sta:
#                         self.Main_Table.removeRow(i)
#
#                 for i in range(len(data_lines)):
#                     data = data_lines[i].split()
#
#                     data_x = np.hstack((data_x,float(data[2])))
#                     row = self.Main_Table.rowCount()
#                     self.Main_Table.insertRow(row)
#
#                     item = Qt.QTableWidgetItem(str(data[2]))
#                     #item.setBackground(Qt.QColor(128, 128, 128))
#                     self.Main_Table.setItem(row,2,item)
#                     if data[4] not in ['vis','pe','pg']:
#                         data[4] = 'ccd'
#                     item = Qt.QTableWidgetItem(data[4])
#                     self.Main_Table.setItem(row,4,item)
#                     if data[3] == 'p':
#                        item = Qt.QTableWidgetItem(str(1))
#                        self.Main_Table.setItem(row,3,item)
#                        data_y = np.hstack((data_y,1))
#                     else:
#                        item = Qt.QTableWidgetItem(str(2))
#                        self.Main_Table.setItem(row,3,item)
#                        data_y = np.hstack((data_y,2))
#
#                     item = Qt.QTableWidgetItem(str(row+1))
#                     item.setBackground(Qt.QColor('Green'))
#                     self.Main_Table.setVerticalHeaderItem(row, item)
#
#                 self.Draw_OC()
#             else:
#                 Qt.QMessageBox.question(XM.window, 'Message',
#             'O-C Gateway does not have such a star or this star'+ \
#             ' does not have any data point', Qt.QMessageBox.Ok)
#         else:
#             Qt.QMessageBox.question(XM.window, 'Message',
#             'Please enter a valid star name', Qt.QMessageBox.Ok)
# #        except:
# #            Qt.QMessageBox.question(XM.window, 'Message',
# #                'Please check your internet conection', Qt.QMessageBox.Ok)
#################################################################
"O-C Window End"
#################################################################

class OC(Qt.QMainWindow):
    def closeEvent(self,event):
        pass
        #XGF.Activate_Buttons()
