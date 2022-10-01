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

from analasisAPI.queries import queryBankDataFrame
from analasisAPI.plotUtilities import plotBalanceAndCosts
from enum import Enum
from analasisAPI.plotUtilities import plotDataFrameTimeSeriesCol

from analasisAPI.fileLoader import npNum2Str

from classification.rule_based_classfier import classify_statement_from_rule_set
import querywindow

class Classifier_Ui_MainWindow(querywindow.Query_Ui_MainWindow):
    def setupUi(self, MainWindow):
        super(Classifier_Ui_MainWindow, self).setupUi(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Classify Bank Statement"))


    def loadTable(self):
        '''
            Loads the viewDataFrame onto the table, the viewDataFrame must be processed before this function
            is called.
        '''
        if self.viewDataFrame is None:
            return
        # TODO : figure out which classifier will go here
        self.viewDataFrame = classify_statement_from_rule_set(self.viewDataFrame)
        model = PandasModel(self.viewDataFrame)
        self.tableView.setModel(model)
        self.tableView.setSortingEnabled(True)

        # -- sizing --
        self.tableView.setColumnWidth(1, 100)
        self.tableView.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        return 0.0


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Classifier_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
