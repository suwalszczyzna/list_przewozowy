# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Damian\Desktop\ListPrzewozowy.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(623, 372)
        MainWindow.setMaximumSize(QtCore.QSize(623, 372))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.openFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFileButton.setGeometry(QtCore.QRect(20, 20, 101, 31))
        self.openFileButton.setObjectName("openFileButton")

        self.filePathLabel = QtWidgets.QLabel(self.centralwidget)
        self.filePathLabel.setGeometry(QtCore.QRect(130, 20, 171, 31))
        self.filePathLabel.setObjectName("filePathLabel")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 581, 192))
        self.tableWidget.setMinimumSize(QtCore.QSize(571, 0))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 157, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 157, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 157, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)

        self.tableWidget.setPalette(palette)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.addParcelManButton = QtWidgets.QPushButton(self.centralwidget)
        self.addParcelManButton.setGeometry(QtCore.QRect(500, 20, 101, 31))
        self.addParcelManButton.setObjectName("addParcelManButton")

        self.sendParcelsButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendParcelsButton.setGeometry(QtCore.QRect(500, 280, 101, 31))
        self.sendParcelsButton.setObjectName("sendParcelsButton")

        self.deleteSelectedParcelsButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteSelectedParcelsButton.setGeometry(QtCore.QRect(20, 280, 121, 31))
        self.deleteSelectedParcelsButton.setObjectName("deleteSelectedParcelsButton")

        self.deleteAllParcelsButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteAllParcelsButton.setGeometry(QtCore.QRect(150, 280, 121, 31))
        self.deleteAllParcelsButton.setObjectName("deleteAllParcelsButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 21))
        self.menubar.setObjectName("menubar")
        self.menuPlik = QtWidgets.QMenu(self.menubar)
        self.menuPlik.setObjectName("menuPlik")
        MainWindow.setMenuBar(self.menubar)

        self.actionOpenFile = QtWidgets.QAction(MainWindow)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.menuPlik.addAction(self.actionOpenFile)
        self.menuPlik.addAction(self.actionSettings)
        self.menuPlik.addSeparator()
        self.menuPlik.addAction(self.actionExit)
        self.menubar.addAction(self.menuPlik.menuAction())

        self.translate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def translate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Listy przewozowe Optima -> Shoper"))
        self.openFileButton.setText(_translate("MainWindow", "Otwórz plik..."))
        self.filePathLabel.setText(_translate("MainWindow", "Brak pliku :("))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nr zam. Shopper"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "List przewozowy"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Nr dok. Optima"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Nazwa"))
        self.addParcelManButton.setText(_translate("MainWindow", "Dodaj ręcznie"))
        self.sendParcelsButton.setText(_translate("MainWindow", "Wyślij..."))
        self.deleteSelectedParcelsButton.setText(_translate("MainWindow", "Usuń zaznaczone"))
        self.deleteAllParcelsButton.setText(_translate("MainWindow", "Usuń wszystkie"))
        self.menuPlik.setTitle(_translate("MainWindow", "Plik"))
        self.actionOpenFile.setText(_translate("MainWindow", "Otwórz plik..."))
        self.actionSettings.setText(_translate("MainWindow", "Ustawienia"))
        self.actionExit.setText(_translate("MainWindow", "Zamknij program"))

    def add_parcel(self):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

        cell_widget = QtWidgets.QWidget()
        chk_bx = QtWidgets.QCheckBox()
        chk_bx.setCheckState(QtCore.Qt.Unchecked)
        lay_out = QtWidgets.QHBoxLayout(cell_widget)
        lay_out.addWidget(chk_bx)
        lay_out.setAlignment(QtCore.Qt.AlignCenter)
        lay_out.setContentsMargins(0, 0, 0, 0)
        cell_widget.setLayout(lay_out)

        self.tableWidget.setCellWidget(row_position, 0, cell_widget)
        self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem('Test'))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = MainWindow(window)
    window.show()
    ui.add_parcel()
    sys.exit(app.exec_())
