# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 19:39:52 2015

@author: TheLichWing
"""

import Main_Window as XM
import numpy as np
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
"Combine_Extrema_Window Start"
#################################################################       
class Combine_Extrema_Window(object):
    def setupUi(self, Combine_Extrema_Window):
        Combine_Extrema_Window.setObjectName(_fromUtf8("Combine Extrema Window"))
        Combine_Extrema_Window.resize(350, 209)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/CE.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Combine_Extrema_Window.setWindowIcon(icon)

        self.horizontalLayout = Qt.QHBoxLayout(Combine_Extrema_Window)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = Qt.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.TableWidget = Qt.QTableWidget(Combine_Extrema_Window)
        self.TableWidget.setMaximumSize(QtCore.QSize(220, 16777215))
        self.TableWidget.setObjectName(_fromUtf8("TableWidget"))
        self.TableWidget.setColumnCount(2)
        self.TableWidget.setRowCount(0)
        item = Qt.QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(0, item)
        item = Qt.QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(1, item)
        self.TableWidget.setRowCount(4)
        self.TableWidget.horizontalHeader().setSectionResizeMode(Qt.QHeaderView.Stretch)
        #self.TableWidget.setColumnWidth(0,126)
        #self.TableWidget.setColumnWidth(1,70)
        self.TableWidget.setSelectionBehavior(Qt.QAbstractItemView.SelectRows)
        self.TableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.TableWidget.customContextMenuRequested.connect(self.Data_TableWidget_Menu)
        
        self.verticalLayout_2.addWidget(self.TableWidget)
        self.Calculate_Button = Qt.QPushButton(Combine_Extrema_Window)
        self.Calculate_Button.setObjectName(_fromUtf8("Calculate_Button"))
        self.verticalLayout_2.addWidget(self.Calculate_Button)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line = Qt.QFrame(Combine_Extrema_Window)
        self.line.setFrameShape(Qt.QFrame.VLine)
        self.line.setFrameShadow(Qt.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout = Qt.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Extremum_Label = Qt.QLabel(Combine_Extrema_Window)
        self.Extremum_Label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Extremum_Label.setObjectName(_fromUtf8("Extremum_Label"))
        self.verticalLayout.addWidget(self.Extremum_Label)
        self.Extremum_LieEdit = Qt.QLineEdit(Combine_Extrema_Window)
        self.Extremum_LieEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Extremum_LieEdit.setObjectName(_fromUtf8("Extremum_LieEdit"))
        self.Extremum_LieEdit.setReadOnly(True)
        self.verticalLayout.addWidget(self.Extremum_LieEdit)
        self.Error_Label = Qt.QLabel(Combine_Extrema_Window)
        self.Error_Label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Error_Label.setObjectName(_fromUtf8("Error_Label"))
        self.verticalLayout.addWidget(self.Error_Label)
        self.Error_LieEdit = Qt.QLineEdit(Combine_Extrema_Window)
        self.Error_LieEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Error_LieEdit.setObjectName(_fromUtf8("Error_LieEdit"))
        self.verticalLayout.addWidget(self.Error_LieEdit)
        self.Error_LieEdit.setReadOnly(True)
        spacerItem = Qt.QSpacerItem(20, 40, Qt.QSizePolicy.Minimum, Qt.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.Done_Button = Qt.QPushButton(Combine_Extrema_Window)
        self.Done_Button.setObjectName(_fromUtf8("Done_Button"))
        self.verticalLayout.addWidget(self.Done_Button)
        self.horizontalLayout.addLayout(self.verticalLayout)


        self.Done_Button.clicked.connect(self.Done)
        self.Calculate_Button.clicked.connect(self.Calculate)

        self.retranslateUi(Combine_Extrema_Window)
        QtCore.QMetaObject.connectSlotsByName(Combine_Extrema_Window)

    def retranslateUi(self, Combine_Extrema_Window):
        Combine_Extrema_Window.setWindowTitle(_translate("Combine_Extrema_Window", "Combine_Extrema_Window", None))
        item = self.TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Combine_Extrema_Window", "Extremum Time", None))
        item = self.TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Combine_Extrema_Window", "Error", None))
        self.Calculate_Button.setText(_translate("Combine_Extrema_Window", "Calculate", None))
        self.Extremum_Label.setText(_translate("Combine_Extrema_Window", "Extremum :", None))
        self.Error_Label.setText(_translate("Combine_Extrema_Window", "Error :", None))
        self.Done_Button.setText(_translate("Combine_Extrema_Window", "Done", None))
        

        
        
    def Data_TableWidget_Menu(self):
        
        menu = Qt.QMenu()
        Delete = Qt.QAction(menu)
        Delete.setText('Delete')
        Delete.setShortcut('Delete')
        menu.addAction(Delete)
        Delete.triggered.connect(self.Delete)
        
        Add = Qt.QAction(menu)
        Add.setText('Add Row')
        Add.setShortcut('Ctrl + A')

        menu.addAction(Add)
        Add.triggered.connect(self.Add)
  
        menu.exec_(Qt.QCursor.pos())
        
    def Done(self):
        XM.ui.Combine_Extrema_Window.close()
    
    def Calculate(self):
        
        row = self.TableWidget.rowCount()
        
        try:
            if row != 0:
                extremum_times = np.arange(0,dtype=float)
                extremum_errors = np.arange(0,dtype=float)
                for i in range(row):
                    try:
                        item_time = self.TableWidget.item(i,0).text()
                        item_error = self.TableWidget.item(i,1).text()
                        if (str(item_time).replace('.','',1).isdigit() == True
                        and str(item_error).replace('.','',1).isdigit() == True):
                            #print item_time, item_error
                            extremum_times = np.hstack((extremum_times,
                                                        float(item_time)))
                            extremum_errors = np.hstack((extremum_errors,
                                                     float(item_error)))
                    except:
                        pass
            
    #        print extremum_times
    #        print extremum_errors
            
            a = 0
            b = 0
            for i in range(len(extremum_times)):
                a += float(extremum_times[i])/(float(extremum_errors[i])**2)
                b += 1./(float(extremum_errors[i])**2)
                
            
            Combine_Extremum = a/b
            Combine_Error = 1./np.sqrt(b)
            
            print('%06f' % Combine_Extremum,'%06f' % Combine_Error)
            
            self.Extremum_LieEdit.setText(str('%06f' % Combine_Extremum))
            self.Error_LieEdit.setText(str('%06f' % Combine_Error))
                
        except:
            Qt.QMessageBox.question(XM.window, 'Message',
                         "Check table", Qt.QMessageBox.Ok)
        
        
    def Add(self):
        row_count = self.TableWidget.rowCount()

        self.TableWidget.insertRow(row_count)

    def Delete(self):
        
        row = self.TableWidget.currentRow()
        if row != -1:
            reply = Qt.QMessageBox.question(XM.window, 'Message',
                 "Are you sure to delete?", Qt.QMessageBox.Yes, Qt.QMessageBox.No)
            
            if reply == Qt.QMessageBox.Yes:
                
                
                
                rows = self.TableWidget.selectionModel().selectedRows()
                
                index = []
                for row in rows:
                    index.append(row.row())
                
                index = sorted(index, reverse=True)
                
                for rowid in index:
                    self.TableWidget.removeRow(rowid)

                
                
                
                    
        else:
            reply = Qt.QMessageBox.question(XM.window, 'Message',
                 "Please choose one or more row!", Qt.QMessageBox.Ok)
        
#################################################################
"Combine_Extrema_Window End"
#################################################################