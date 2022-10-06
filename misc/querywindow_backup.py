# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'querywindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#custom headers
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from analasisAPI.fileLoader import LoadFile 
from analasisAPI.fileLoader import DESC_COL, DATE_COL, AMNT_COL, BAL_COL
from uiUtilities.pandasModel import PandasModel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1260, 811)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setMinimumSize(QtCore.QSize(880, 0))
        self.tableView.setObjectName("tableView")
        self.horizontalLayout_3.addWidget(self.tableView)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMaximumSize(QtCore.QSize(352, 16777215))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.queryButton = QtWidgets.QTextEdit(self.centralwidget)
        self.queryButton.setMaximumSize(QtCore.QSize(352, 44))
        self.queryButton.setObjectName("queryButton")
        self.verticalLayout_7.addWidget(self.queryButton)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_7.addWidget(self.line_2)
        self.isFilterByDate = QtWidgets.QCheckBox(self.centralwidget)
        self.isFilterByDate.setMaximumSize(QtCore.QSize(352, 16777215))
        self.isFilterByDate.setObjectName("isFilterByDate")
        self.verticalLayout_7.addWidget(self.isFilterByDate)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(352, 44))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.startDate = QtWidgets.QDateEdit(self.centralwidget)
        self.startDate.setMaximumSize(QtCore.QSize(352, 16777215))
        self.startDate.setObjectName("startDate")
        self.verticalLayout_7.addWidget(self.startDate)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(352, 44))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.endDate = QtWidgets.QDateEdit(self.centralwidget)
        self.endDate.setMaximumSize(QtCore.QSize(352, 16777215))
        self.endDate.setObjectName("endDate")
        self.verticalLayout_7.addWidget(self.endDate)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_7.addWidget(self.line)
        self.isFilterRange = QtWidgets.QCheckBox(self.centralwidget)
        self.isFilterRange.setMaximumSize(QtCore.QSize(352, 16777215))
        self.isFilterRange.setObjectName("isFilterRange")
        self.verticalLayout_7.addWidget(self.isFilterRange)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(352, 44))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(352, 44))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.lowSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lowSpinBox.setMaximumSize(QtCore.QSize(352, 16777215))
        self.lowSpinBox.setMaximum(500000.0)
        self.lowSpinBox.setObjectName("lowSpinBox")
        self.verticalLayout_7.addWidget(self.lowSpinBox)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(352, 44))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.highSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.highSpinBox.setMaximumSize(QtCore.QSize(352, 16777215))
        self.highSpinBox.setMaximum(500000.0)
        self.highSpinBox.setObjectName("highSpinBox")
        self.verticalLayout_7.addWidget(self.highSpinBox)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_7.addWidget(self.line_3)
        self.summaryText = QtWidgets.QLabel(self.centralwidget)
        self.summaryText.setText("")
        self.summaryText.setObjectName("summaryText")
        self.verticalLayout_7.addWidget(self.summaryText)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setMaximumSize(QtCore.QSize(176, 16777215))
        self.applyButton.setObjectName("applyButton")
        self.horizontalLayout.addWidget(self.applyButton)
        self.plotButton = QtWidgets.QPushButton(self.centralwidget)
        self.plotButton.setMaximumSize(QtCore.QSize(176, 16777215))
        self.plotButton.setObjectName("plotButton")
        self.horizontalLayout.addWidget(self.plotButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1260, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionInfo)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # custom code begin here
        self.startDate.setReadOnly(True)
        self.endDate.setReadOnly(True)
        self.lowSpinBox.setReadOnly(True)
        self.highSpinBox.setReadOnly(True)
        self.isFilterByDate.stateChanged.connect(lambda: self.toggleDate())
        self.isFilterRange.stateChanged.connect(lambda: self.toggleAmount())

        # file loader
        self.dataFrame = []
        self.viewDataFrame = []
        self.actionLoad.triggered.connect(lambda: self.loadFile())

        # apply button

    def toggleDate(self):
        if self.isFilterByDate.isChecked():
            self.startDate.setReadOnly(False)
            self.endDate.setReadOnly(False)
        else:
            self.startDate.setReadOnly(True)
            self.endDate.setReadOnly(True)

    def toggleAmount(self):
        if self.isFilterRange.isChecked():
            self.lowSpinBox.setReadOnly(False)
            self.highSpinBox.setReadOnly(False)
        else:
            self.lowSpinBox.setReadOnly(True)
            self.highSpinBox.setReadOnly(True)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Query Bank Statement"))
        self.label_7.setText(_translate("MainWindow", " Query:"))
        self.isFilterByDate.setText(_translate("MainWindow", "Filter By Date"))
        self.label_2.setText(_translate("MainWindow", " Start Date"))
        self.label_3.setText(_translate("MainWindow", " End Date"))
        self.isFilterRange.setText(_translate("MainWindow", "FIlter by range"))
        self.label_4.setText(_translate("MainWindow", " Cost Range:"))
        self.label_5.setText(_translate("MainWindow", " low:"))
        self.label_6.setText(_translate("MainWindow", " high:"))
        self.applyButton.setText(_translate("MainWindow", "Apply Filter"))
        self.plotButton.setText(_translate("MainWindow", "Plot"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad.setText(_translate("MainWindow", "Load..."))
        self.actionInfo.setText(_translate("MainWindow", "Info"))

        # begin user defined functions
    def loadTable(self):
        '''
            Loads the viewDataFrame onto the table, the viewDataFrame must be processed before this function
            is called.
        '''
        model = PandasModel(self.viewDataFrame)
        self.tableView.setModel(model)
        self.tableView.setSortingEnabled(True)
        return 0.0
    
    def loadFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "All Files (*);;CSV Files (*.csv);;Text Files (*.txt)",
                        options=options)
        if fileName:
            try:
                self.dataFrame = LoadFile(fileName)
                self.viewDataFrame = self.dataFrame.sort_values(by=[DATE_COL])
            except:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("File type not supported.")
                msgBox.setWindowTitle("Invalid File")
                msgBox.show()

            self.loadTable()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
