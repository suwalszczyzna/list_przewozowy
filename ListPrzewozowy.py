# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Damian\Desktop\ListPrzewozowy.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtWidgets import QFileDialog


class MainWindow(object):
    def __init__(self, MainWindow):

        self.filePath = ''

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(713, 788)
        MainWindow.setMaximumSize(QtCore.QSize(2000, 2000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 701, 711))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openFileButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.openFileButton.setMinimumSize(QtCore.QSize(0, 40))
        self.openFileButton.setMaximumSize(QtCore.QSize(120, 100))
        self.openFileButton.setObjectName("openFileButton")
        self.horizontalLayout.addWidget(self.openFileButton)
        self.filePathLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.filePathLabel.setObjectName("filePathLabel")
        self.horizontalLayout.addWidget(self.filePathLabel)
        self.addParcelManButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addParcelManButton.setMinimumSize(QtCore.QSize(0, 40))
        self.addParcelManButton.setMaximumSize(QtCore.QSize(120, 40))
        self.addParcelManButton.setObjectName("addParcelManButton")
        self.horizontalLayout.addWidget(self.addParcelManButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(570, 0))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget.setFont(font)
        self.tableWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setIconSize(QtCore.QSize(10, 10))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(0)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.select_all_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.select_all_button.setObjectName("select_all_button")
        self.horizontalLayout_2.addWidget(self.select_all_button)
        self.deleteAllParcelsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.deleteAllParcelsButton.setObjectName("deleteAllParcelsButton")
        self.horizontalLayout_2.addWidget(self.deleteAllParcelsButton)
        self.deleteSelectedParcelsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.deleteSelectedParcelsButton.setObjectName("deleteSelectedParcelsButton")
        self.horizontalLayout_2.addWidget(self.deleteSelectedParcelsButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sendParcelsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sendParcelsButton.setMinimumSize(QtCore.QSize(0, 50))
        self.sendParcelsButton.setMaximumSize(QtCore.QSize(350, 16777215))
        self.sendParcelsButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sendParcelsButton.setAutoFillBackground(True)
        self.sendParcelsButton.setFlat(False)
        self.sendParcelsButton.setObjectName("sendParcelsButton")
        self.horizontalLayout_3.addWidget(self.sendParcelsButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 26))
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

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

        self.translate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def translate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openFileButton.setText(_translate("MainWindow", "Otwórz plik..."))
        self.filePathLabel.setText(_translate("MainWindow", "Brak pliku :("))
        self.addParcelManButton.setText(_translate("MainWindow", "Dodaj ręcznie"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nr zam. Shopper"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "List przewozowy"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Nr dok. Optima"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Nazwa"))
        self.select_all_button.setText(_translate("MainWindow", "Zaznacz wszystkie"))
        self.deleteAllParcelsButton.setText(_translate("MainWindow", "Usuń wszystkie"))
        self.deleteSelectedParcelsButton.setText(_translate("MainWindow", "Usuń zaznaczone"))
        self.sendParcelsButton.setText(_translate("MainWindow", "Wyślij..."))
        self.menuPlik.setTitle(_translate("MainWindow", "Plik"))
        self.actionOpenFile.setText(_translate("MainWindow", "Otwórz plik..."))
        self.actionSettings.setText(_translate("MainWindow", "Ustawienia"))
        self.actionExit.setText(_translate("MainWindow", "Zamknij program"))

        self.openFileButton.clicked.connect(self.open_file_button_handler)

    def open_file_button_handler(self):
        self.open_file_name_dialog()

    def add_parcel(self, shoper, parcel_no, optima_invoice, name):
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
        self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(shoper))
        self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(parcel_no))
        self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(optima_invoice))
        self.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(name))

    def populate_data(self, input_data):
        for dictionary in input_data:
            self.add_parcel(str(dictionary.get('Opis')),
                            str(dictionary.get('Nr listu przewozowego')),
                            str(dictionary.get('Numer dokumentu')),
                            str(dictionary.get('Kontrahent'))
                            )

    def read_data_from_file(self, path):
        import pandas
        self.filePath = path
        self.filePathLabel.setText(self.filePath)
        excel_df = pandas.read_excel(path,
                                     usecols=['Nr listu przewozowego', 'Opis', 'Numer dokumentu', 'Kontrahent'])
        data = excel_df.to_dict(orient='record')
        data_clear = [x for x in data if str(x.get('Nr listu przewozowego')) != 'nan']

        if data_clear:
            for dictionary in data_clear:
                opis = str(dictionary.get('Opis'))
                nr_listu = str(dictionary.get('Nr listu przewozowego'))

                import re
                regex_zamowienie = re.compile(r'Zam.wienie.(\d{5})$|(\d{5})$')
                regex_nr_listu = re.compile(r'(\d+\w)')

                zamowienie_results = re.findall(regex_zamowienie, opis)
                if zamowienie_results:
                    opis = zamowienie_results[0][0] if zamowienie_results[0][0] else zamowienie_results[0][1]
                    dictionary['Opis'] = opis

                numer_listu_results = re.findall(regex_nr_listu, nr_listu)
                if numer_listu_results:
                    dictionary['Nr listu przewozowego'] = numer_listu_results[-1]

            return data_clear
        else:
            return None

    def open_file_name_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName()
        if file_name:
            print(file_name)
            data = self.read_data_from_file(file_name)
            self.populate_data(data)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = MainWindow(window)
    window.show()
    sys.exit(app.exec_())
