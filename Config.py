import configparser
from Logs import create_logger

logger = create_logger(__name__)


class Config:

    def __init__(self):
        self.shoper_url = ''
        self.login = ''
        self.password = ''
        self.shippingID = ''
        self.default_section = 'DEFAULT'
        self.config = configparser.RawConfigParser()
        # self.logger = logging.getLogger(__name__)

    def _load_config(self) -> bool:
        logger.info('Próba otwarcia pliku konfiguracyjnego config.ini')
        config_result = self.config.read('config.ini')
        if config_result:
            logger.info('Znaleziono plik konfiguracyjny config.ini. Pobieram parametry...')
            self.shoper_url = self.config[self.default_section]['shoperURL']
            self.login = self.config[self.default_section]['login']
            self.password = self.config[self.default_section]['passphraze']
            self.shippingID = self.config[self.default_section]['shippingID']

            return True
        else:
            logger.warning('Nie znaleziono pliku konfiguracyjnego!')
            return False

    def _create_empty_config_file(self):
        self.config[self.default_section] = {
            'shoperURL': '',
            'login': '',
            'passphraze': '',
            'shippingID': '',
        }
        logger.info('Zapisuje pusty plik konfiguracyjny...')
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

    def load_config(self) -> str:
        result = 'OK'
        config_file_exist = self._load_config()
        if not config_file_exist:
            self._create_empty_config_file()
            result = 'Skonfiguruj plik config.ini'
        return result
