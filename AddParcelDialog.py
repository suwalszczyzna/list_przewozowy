# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Damian\Desktop\list_przewozowy\dialog_addparcel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class AddParcelDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AddParcelDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("Dodaj przesyłkę")
        self.setFixedWidth(300)
        self.setFixedHeight(200)

        layout = QVBoxLayout()

        self.parcel_no_input = QLineEdit()
        self.parcel_no_input.setPlaceholderText("Numer listu przewozowego")
        self.parcel_no_input.textChanged.connect(self._disable_button)
        layout.addWidget(self.parcel_no_input)

        self.shoper_no_input = QLineEdit()
        self.shoper_no_input.setPlaceholderText("Numer zamówienia Shoper")
        self.shoper_no_input.textChanged.connect(self._disable_button)
        layout.addWidget(self.shoper_no_input)

        self.optima_no_input = QLineEdit()
        self.optima_no_input.setPlaceholderText("Numer dokumentu Optima")
        layout.addWidget(self.optima_no_input)

        self.name = QLineEdit()
        self.name.setPlaceholderText("Nazwa odbiorcy")
        layout.addWidget(self.name)

        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.buttons.setDisabled(True)

        layout.addWidget(self.buttons)
        self.setLayout(layout)

    def _disable_button(self):
        parcel_no_len = len(self.parcel_no_input.text())
        shoper_no_len = len(self.shoper_no_input.text())
        if parcel_no_len > 0 and shoper_no_len > 0:
            self.buttons.setDisabled(False)

    def get_parcel(self):
        return self.parcel_no_input.text()

    def get_shoper(self):
        return self.shoper_no_input.text()

    def get_optima(self):
        return self.optima_no_input.text()

    def get_name(self):
        return self.name.text()

    @staticmethod
    def get_new_parcel(parent=None):
        dialog = AddParcelDialog(parent)
        result = dialog.exec_()
        parcel = dialog.get_parcel()
        shoper = dialog.get_shoper()
        optima = dialog.get_optima()
        name = dialog.get_name()
        return parcel, shoper, optima, name, result == QDialog.Accepted
