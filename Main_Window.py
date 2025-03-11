import Data_Preparation_Window as DPW
import Main_Graph_Window as XMW
import Periodogram_Window as PW
import Normalization_Window as NW
import Min_Max_Window as MMW
import OC_Window as OW
# import Optimization_Window as OPW
import Combine_Extrema_Window as CEW

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


groupBoxStyle = '''
QGroupBox {
    font-weight: bold;
    border: 1px solid green;
    border-radius: 2px;
    margin-top: 20px;
           }

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 5px;
                  }
'''

class MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.resize(800, 600)
        MainWindow.showMaximized()
        
        Main_icon = QtGui.QIcon()
        Main_icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Xtrema.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(Main_icon)
        
        self.centralwidget = Qt.QWidget(MainWindow)

        self.Main_HLayout = Qt.QHBoxLayout(self.centralwidget)
        self.Main_HLayout.setSpacing(2)
        self.Main_HLayout.setContentsMargins(2, 2, 2, 2)
        
        self.ToolBar_Frame = Qt.QFrame(self.centralwidget)
        self.ToolBar_Frame.setFrameShape(Qt.QFrame.WinPanel)
        self.ToolBar_Frame.setFrameShadow(Qt.QFrame.Raised)
        self.ToolBar_Frame.setMaximumWidth(75)
        
        self.ToolButton_VLayout = Qt.QVBoxLayout(self.ToolBar_Frame)
        
        self.DP_Window = Qt.QToolButton(self.ToolBar_Frame)
        self.DP_Window.setFixedSize(50,50)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/DP.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DP_Window.setIcon(icon)
        
        self.ToolButton_VLayout.addWidget(self.DP_Window)
        
        self.MG_Window = Qt.QToolButton(self.ToolBar_Frame)
        self.MG_Window.setFixedSize(50,50)
        self.MG_Window.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/MG.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MG_Window.setIcon(icon1)

        self.ToolButton_VLayout.addWidget(self.MG_Window)
        
        self.OC_Window = Qt.QToolButton(self.ToolBar_Frame)
        self.OC_Window.setFixedSize(50,50)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("icons/OC.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OC_Window.setIcon(icon6)
        
        self.ToolButton_VLayout.addWidget(self.OC_Window)
        
        self.CW_Window = Qt.QToolButton(self.ToolBar_Frame)
        self.CW_Window.setFixedSize(50,50)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("icons/CE.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CW_Window.setIcon(icon7)
        
        self.ToolButton_VLayout.addWidget(self.CW_Window)

        self.About = Qt.QToolButton(self.ToolBar_Frame)
        self.About.setFixedSize(50,50)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/About.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.About.setIcon(icon)
        
        self.ToolButton_VLayout.addWidget(self.About)
        
        spacerItem = Qt.QSpacerItem(40, 20, Qt.QSizePolicy.Minimum, Qt.QSizePolicy.Expanding)
        self.ToolButton_VLayout.addItem(spacerItem)
                
        self.Exit = Qt.QToolButton(self.ToolBar_Frame)
        self.Exit.setFixedSize(50,50)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Exit.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit.setIcon(icon8)
        
        self.ToolButton_VLayout.addWidget(self.Exit)
        
        self.Main_HLayout.addWidget(self.ToolBar_Frame)
        
        self.Background_Frame = Qt.QFrame(self.centralwidget)     
        self.Background_Frame.setFrameShape(Qt.QFrame.WinPanel)
        self.Background_Frame.setFrameShadow(Qt.QFrame.Plain)                       
        
        self.Main_HLayout.addWidget(self.Background_Frame)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
#        self.menubar = Qt.QMenuBar(MainWindow)
#
#        
#        self.menuFile = Qt.QMenu(self.menubar)        
#        self.menuEdit = Qt.QMenu(self.menubar)
#        self.menuTools = Qt.QMenu(self.menubar)
#        self.menuView = Qt.QMenu(self.menubar)        
#        self.menuWindow = Qt.QMenu(self.menubar)
#        self.menuHelp = Qt.QMenu(self.menubar)
#
#        self.actionDP = Qt.QAction(MainWindow)
#        self.actionSave = Qt.QAction(MainWindow)
#        self.actionSave_as = Qt.QAction(MainWindow)
#        self.actionExit = Qt.QAction(MainWindow)
#        
#        self.menuFile.addAction(self.actionDP)
#        self.menuFile.addAction(self.actionSave)
#        self.menuFile.addAction(self.actionSave_as)
#        self.menuFile.addAction(self.actionExit)
        
        
#        self.actionTexttoColumn = Qt.QAction(MainWindow)
#        self.menuEdit.addAction(self.actionTexttoColumn)
#        
#        self.actionCombineExtremum = Qt.QAction(MainWindow)
#        self.actionOC = Qt.QAction(MainWindow)
#        self.actionNormalization = Qt.QAction(MainWindow)
#        self.actionPeriodogram = Qt.QAction(MainWindow)
#        self.actionOptimization = Qt.QAction(MainWindow)

#        self.menuTools.addAction(self.actionCombineExtremum)
#        self.menuTools.addAction(self.actionOC)
#        self.menuTools.addAction(self.actionNormalization)
#        self.menuTools.addAction(self.actionPeriodogram)
#        self.menuTools.addAction(self.actionOptimization)
        
#        self.menubar.addAction(self.menuFile.menuAction())        
#        self.menubar.addAction(self.menuEdit.menuAction())
#        self.menubar.addAction(self.menuTools.menuAction())
#        self.menubar.addAction(self.menuView.menuAction())
#        self.menubar.addAction(self.menuWindow.menuAction())
#        self.menubar.addAction(self.menuHelp.menuAction())
#
#        MainWindow.setMenuBar(self.menubar)
#        
        self.statusbar = Qt.QStatusBar(MainWindow)
        
        MainWindow.setStatusBar(self.statusbar)
        
        self.Data_Preparation_Window = Qt.QDialog(MainWindow)
        self.OD = DPW.Data_Preparation_Window()
        self.OD.setupUi(self.Data_Preparation_Window)
        
        
#        self.Data_Design = Qt.QMainWindow()
#        self.DD = DPW.Data_Design()
#        self.DD.setupUi(self.Data_Design)


        self.Main_Graph_Window = Qt.QMainWindow(MainWindow)
        self.MG = XMW.Main_Graph_Window()
        self.MG.setupUi(self.Main_Graph_Window)
        
        self.Periodogram_Window = PW.Periodogram(MainWindow)
        self.PD = PW.Periodogram_Window()
        self.PD.setupUi(self.Periodogram_Window)
        
        self.Normalization_Window = NW.Normalization(MainWindow)
        self.NZ = NW.Ui_Normalization_Widget()
        self.NZ.setupUi(self.Normalization_Window)
        
#        self.Optimization_Window = OPW.Optimization(MainWindow)
#        self.OW = OPW.Xtrema_Optimization_Window()
#        self.OW.setupUi(self.Optimization_Window)

        self.Combine_Extrema_Window = Qt.QDialog(MainWindow)
        self.CW = CEW.Combine_Extrema_Window()
        self.CW.setupUi(self.Combine_Extrema_Window)
        
        self.MinMax_Window = MMW.MinMax(MainWindow)
        self.MM = MMW.MinMax_Window()
        self.MM.setupUi(self.MinMax_Window)
  
        self.ObsCal_Window = OW.OC(MainWindow)
        self.OC = OW.Ui_OC_Widget()
        self.OC.setupUi(self.ObsCal_Window)
        
        
        self.DP_Window.clicked.connect(self.Data_Preparation_Window.show)
        self.MG_Window.clicked.connect(self.Main_Graph_Window.show)
        self.Exit.triggered.connect(sys.exit)
        self.About.clicked.connect(self.About_Window)
        #self.OW_Window.clicked.connect(self.Optimization_Window.show)
        #self.MM_Window.clicked.connect(self.MinMax_Window.show)

        self.OC_Window.clicked.connect(self.ObsCal)
        self.OC_Window.clicked.connect(lambda x: self.OC.T0P_GetCBox.setChecked(True))
        self.CW_Window.clicked.connect(self.Combine_Extrema_Window.show)
        
        #self.actionDP.triggered.connect(self.Data_Preparation_Window.show)
        
#        path = 'C:/Users/LichWing/Documents/Xtrema_Revize/small_data.txt'
#        self.OD.Data_Design(path)
#        print self.OD.path
        #try:
        def DD():
            ui.OD.saved_ext_edit = True
            ui.OD.DD.show()
            ui.OD.DD.TextToColumn()
            
            
            
#        self.actionTexttoColumn.triggered.connect(DD)
        #except:
            #raise
        #self.actionCombineExtremum.triggered.connect(self.Combine_Extrema)
        
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Xtrema BETA v1.0", None))
#        self.actionDP.setText(_translate("MainWindow","Data Preparation",None))
#        self.actionSave.setText(_translate("MainWindow","Save",None))
#        self.actionSave_as.setText(_translate("MainWindow","Save as...",None))
#        self.actionExit.setText(_translate("MainWindow","Exit",None))
#        self.actionTexttoColumn.setText(_translate("MainWindow","Text to Column",None))
#        self.actionCombineExtremum.setText(_translate("MainWindow","Combine Extrema",None))
#        self.actionOC.setText(_translate("MainWindow","O-C Diagram",None))
#        self.actionNormalization.setText(_translate("MainWindow","Normalization",None))
#        self.actionPeriodogram.setText(_translate("MainWindow","Periodogram",None))
#        self.actionOptimization.setText(_translate("MainWindow","Optimization",None))
#        
#        self.menuFile.setTitle(_translate("MainWindow", "File", None))
#        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
#        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
#        self.menuView.setTitle(_translate("MainWindow", "View", None))
#        self.menuWindow.setTitle(_translate("MainWindow", "Window", None))
#        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
#    

    def ObsCal(self):
        self.OC.Correction_Frame.show()
        # self.OC.GetData_Frame.show()
        # self.OC.Draw_OC_PushButton.show()
        # self.OC.Open_PushButton.show()
        
        self.ObsCal_Window.show()
    
    def About_Window(self):
        Widget = Qt.QDialog(window)
        Widget.setFixedSize(450,350)
        Widget.setWindowTitle('About')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/About.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Widget.setWindowIcon(icon)
        
        Layout = Qt.QHBoxLayout(Widget)
        
        TextEdit = Qt.QTextEdit()
        TextEdit.setReadOnly(True)
        content = (
            '<p style="text-align: justify;">'
            'Xtrema is a Python code that automatically calculates the times corresponding to '
            'the minimum or maximum light in each cycle from the light curves of stars. If you '
            'encounter any bugs or errors, please feel free to report them.'
            '</p>'

            '<p><b>Contact:</b><br>'
            'engnbahar@gmail.com</p>'

            '<p><b>Utilized libraries:</b><br>'
            'Numpy       (http://www.numpy.org/)<br>'
            'Scipy       (http://www.scipy.org/)<br>'
            'PyAstronomy (https://pyastronomy.readthedocs.io/en/latest/#)<br>'
            'Astropy     (https://www.astropy.org)<br>'
            'Guiqwt      (https://guiqwt.readthedocs.io/en/latest/#)<br>'
            'PyQt5       (https://riverbankcomputing.com/software/pyqt/intro)<br>'
            'Qt Designer (https://www.qt.io)<br>'
            '</p>'

            '<p><b>Icons:</b><br>'
            'Icon of Xtrema made by Freepik from www.flaticon.com<br>'
            'Other icons from www.findicons.com</p>'
        )

        TextEdit.setHtml(content)
        Layout.addWidget(TextEdit)
        
        Widget.show()

#if __name__ == '__main__':    
import sys
app = Qt.QApplication(sys.argv)
app.setStyle(Qt.QStyleFactory.create("cleanlooks"))
window = Qt.QMainWindow()
ui = MainWindow()
ui.setupUi(window)