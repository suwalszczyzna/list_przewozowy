import sys

from Config import Config
from MainWindow import *
from Logs import create_logger
from RestClient import RestClient


logger = create_logger(__name__)
logger.info('------------------ Start programu')

# load main window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()


config = Config()
config_result_message = config.load_config()
if not config_result_message == 'OK':
    error_dialog = QtWidgets.QErrorMessage()
    error_dialog.showMessage(config_result_message)
else:
    rest_client = RestClient(config.shoper_url)
    ui = MainWindow(window, config, rest_client)
    window.show()


# file_name = r"C:\Users\Damian\Desktop\fv_test.xlsx"
# data = ui.read_data_from_file(file_name)
# ui.populate_data(data)
sys.exit(app.exec_())
