from Config import Config
from RestClient import RestClient
from PyQt5 import QtCore, QtGui, QtWidgets
from Logs import create_logger

logger = create_logger(__name__)


class ParcelService:
    def __init__(self,
                 table_widget: QtWidgets.QTableWidget,
                 config: Config,
                 rest_client: RestClient):

        self.items = []
        self.table_widget = table_widget
        self.config = config
        self.rest_client = rest_client

    def set_status_text(self, row, status_txt: str):
        self.table_widget.item(row, 4).setText(status_txt)

    def colorize_row(self, row, rgb_color: tuple):
        self.table_widget.item(row, 0).setBackground(QtGui.QColor(rgb_color[0], rgb_color[1], rgb_color[2]))
        self.table_widget.item(row, 1).setBackground(QtGui.QColor(rgb_color[0], rgb_color[1], rgb_color[2]))
        self.table_widget.item(row, 2).setBackground(QtGui.QColor(rgb_color[0], rgb_color[1], rgb_color[2]))
        self.table_widget.item(row, 3).setBackground(QtGui.QColor(rgb_color[0], rgb_color[1], rgb_color[2]))
        self.table_widget.item(row, 4).setBackground(QtGui.QColor(rgb_color[0], rgb_color[1], rgb_color[2]))

    def convert_data(self):
        logger.info('Konwertuje wysylki...')
        row_count = self.table_widget.rowCount()
        for row in range(row_count):
            if self.table_widget.item(row, 0).checkState():
                order_number = self.table_widget.item(row, 1).text()
                parcel_number = self.table_widget.item(row, 0).text()
                if order_number and parcel_number:
                    self.items.append((int(order_number), parcel_number, row))
                    self.set_status_text(row, 'Gotowa do wysyłki')
                else:
                    logger.warning('Bledy w wierszu {}'.format(row))
                    self.set_status_text(row, 'Błędna')
                    self.colorize_row(row, (230, 0, 38))

    def send_parcels(self):
        logger.info('Wysyłam numery przesyłek do shopera...')
        token = self.config.get_token_from_config()
        login = self.config.login
        password = self.config.password
        shipping_id = self.config.shippingID

        for item in self.items:
            status_code = 0
            row = item[2]
            id_parcel = self.rest_client.get_id_parcel(token, shipping_id, item[0])
            if isinstance(id_parcel, dict):
                status_code = id_parcel.get('status_code')
                if status_code == 401:
                    token = self.rest_client.get_token(login, password)
                    if isinstance(token, dict):
                        self.set_status_text(row, token.get('message'))
                        self.colorize_row(row, (230, 0, 38))
                    else:
                        self.config.save_token(token)
                        id_parcel = self.rest_client.get_id_parcel(token, shipping_id, item[0])

            if not status_code == 400 and isinstance(id_parcel, int):
                is_sent = self.rest_client.set_shipping_code(token, id_parcel, item[1])
                if is_sent == 1:
                    self.set_status_text(row, 'Wysłana do shopera')
                    self.colorize_row(row, (0, 204, 0))
                    logger.info('Przesyłka z wiersza: {} - wysłana poprawnie'.format(row+1))
            else:
                if isinstance(id_parcel, dict):
                    error_message = id_parcel.get('message')
                    if error_message == "All products has been already sent":
                        self.set_status_text(row, 'Błąd: zamówienie ma już przesyłkę')
                        self.colorize_row(row, (230, 0, 38))
                        logger.info('Przesyłka z wiersza: {} - Błąd: zamówienie ma już przesyłkę'.format(row + 1))
                    elif "Wartość pola 'order_id' jest niepoprawna: Nie znaleziono wartości" in error_message:
                        self.set_status_text(row, 'Błąd: zły numer zamówienia shoper')
                        self.colorize_row(row, (230, 0, 38))
                        logger.info('Przesyłka z wiersza: {} - Błąd: zły numer zamówienia shoper'.format(row + 1))
                else:
                    self.set_status_text(row, 'Nieznany błąd wysyłki')
                    self.colorize_row(row, (230, 0, 38))
                    logger.info('Przesyłka z wiersza: {} - inny błąd wysyłki'.format(row + 1))
