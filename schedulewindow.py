# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schedulewindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
# TODO TODO: date range filtering

# custom imports
from analasisAPI.fileLoader import LoadFile
from analasisAPI.fileLoader import DESC_COL, DATE_COL, AMNT_COL, BAL_COL
from uiUtilities.pandasModel import PandasModel

from uiUtilities.pandasModel import PandasModel
from uiUtilities.dropdownData import stringToEnumGrouping,stringToEnumTextProcess
from uiUtilities.dropdownData import dayOfWeekToName, EnumScheduleToString
from uiUtilities.dropdownData import settingsDefault
from uiUtilities.makeScheduleDFdisplayable import makeScheduleDFdisplayable

from analasisAPI.subscriptionFinder import getSchedules
from analasisAPI.subscriptionFinder import scheduleTypeEnum
from analasisAPI.subscriptionFinder import getRepresentativeDFfromSchedules

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
        self.textProcessSelection = QtWidgets.QComboBox(self.centralwidget)
        self.textProcessSelection.setObjectName("textProcessSelection")
        self.verticalLayout_7.addWidget(self.textProcessSelection)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_7.addWidget(self.line_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(352, 44))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.algorithmSelection = QtWidgets.QComboBox(self.centralwidget)
        self.algorithmSelection.setObjectName("algorithmSelection")
        self.verticalLayout_7.addWidget(self.algorithmSelection)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_7.addWidget(self.line)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(352, 44))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(352, 44))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.firstNchar = QtWidgets.QSpinBox(self.centralwidget)
        self.firstNchar.setObjectName("firstNchar")
        self.verticalLayout_7.addWidget(self.firstNchar)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.lastNchar = QtWidgets.QSpinBox(self.centralwidget)
        self.lastNchar.setObjectName("lastNchar")
        self.verticalLayout_7.addWidget(self.lastNchar)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(352, 44))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.similarityMeasure = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.similarityMeasure.setObjectName("similarityMeasure")
        self.verticalLayout_7.addWidget(self.similarityMeasure)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setMaximumSize(QtCore.QSize(352, 1))
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
        self.actionbalances = QtWidgets.QAction(MainWindow)
        self.actionbalances.setObjectName("actionbalances")
        self.actiondebits = QtWidgets.QAction(MainWindow)
        self.actiondebits.setObjectName("actiondebits")
        self.actiondeposit_plot = QtWidgets.QAction(MainWindow)
        self.actiondeposit_plot.setObjectName("actiondeposit_plot")
        self.actionall = QtWidgets.QAction(MainWindow)
        self.actionall.setObjectName("actionall")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionInfo)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.customizedInit()

    def customizedInit(self):
        self.algorithmSelection.addItems(stringToEnumGrouping.keys())
        self.textProcessSelection.addItems(stringToEnumTextProcess.keys())
        self.firstNchar.setValue(settingsDefault['firstNchar'])
        self.lastNchar.setValue(settingsDefault['lastNchar'])
        self.similarityMeasure.setValue(settingsDefault['similarityMeasure'])

        # main view data frame
        self.scheduleDataFrame = None
        self.schedules = []


        # file loader
        self.dataFrame = None
        self.actionLoad.triggered.connect(lambda: self.loadFile())

        # export menu
        self.actionExport.triggered.connect(lambda: self.exportFile())

        # # apply button
        self.isProcessing = False
        self.applyButton.clicked.connect(lambda: self.applyScheduler())
        return

    def loadFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "CSV Files (*.csv);;Text Files (*.txt);;All Files (*)",
                        options=options)
        if fileName:
            try:
                self.dataFrame = LoadFile(fileName)
                self.dataFrame = self.dataFrame.sort_values(by=[DATE_COL])
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("File loaded, apply query.")
                msgBox.setWindowTitle("Valid File")
                msgBox.show()
                msgBox.exec_()
            except:
                print(sys.exc_info()[0])
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("File type not supported.")
                msgBox.setWindowTitle("Invalid File")
                msgBox.show()
                msgBox.exec()

    def exportFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(None,"QFileDialog.getSaveFileName()","","CSV files (*.csv)", options=options)
        if fileName:
            try:
                self.scheduleDataFrame.to_csv(fileName)
            except:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("File type not supported.")
                msgBox.setWindowTitle("Invalid File")
                msgBox.show()


    def applyScheduler(self):
        if self.isProcessing:
            return
        self.isProcessing = True
        self.applyButton.setDisabled(True)
        FirstNchar = self.firstNchar.value()
        LastMchar = self.lastNchar.value()
        algorithm = str(self.algorithmSelection.currentText())
        textProcess = str(self.textProcessSelection.currentText())
        similarity = self.similarityMeasure.value()
        optionsDict = {'firstNchar': FirstNchar,
                        'lastNchar': LastMchar,
                        'similarity': similarity}

        textProcessEnum = stringToEnumTextProcess[textProcess]
        algoEnum = stringToEnumGrouping[algorithm]
        scheduledDataFrames = getSchedules(self.dataFrame, textProcessEnum, algoEnum,optionsDict)
        self.schedules = scheduledDataFrames
        self.scheduleDataFrame = makeScheduleDFdisplayable(getRepresentativeDFfromSchedules(scheduledDataFrames))
        model = PandasModel(self.scheduleDataFrame)
        self.tableView.setModel(model)
        self.tableView.setSortingEnabled(True)

        # -- sizing --
        self.tableView.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.isProcessing = False
        self.applyButton.setDisabled(False)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Bank Statement Schedules"))
        self.label_7.setText(_translate("MainWindow", " Text processing"))
        self.label_2.setText(_translate("MainWindow", " Grouping algorithm"))
        self.label_4.setText(_translate("MainWindow", " Settings for algorithms:"))
        self.label_5.setText(_translate("MainWindow", " Number of first character matches:"))
        self.label_3.setText(_translate("MainWindow", " Number of last character matches:"))
        self.label_6.setText(_translate("MainWindow", " String similarity threshold:"))
        self.applyButton.setText(_translate("MainWindow", "Find Schedule"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad.setText(_translate("MainWindow", "Load..."))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionbalances.setText(_translate("MainWindow", "deposits"))
        self.actiondebits.setText(_translate("MainWindow", "debits"))
        self.actiondeposit_plot.setText(_translate("MainWindow", "deposit plot"))
        self.actionall.setText(_translate("MainWindow", "all"))
        self.actionExport.setText(_translate("MainWindow", "Export..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
