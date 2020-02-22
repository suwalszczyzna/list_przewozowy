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
        self.token_section = 'TOKEN'
        self.token_filename = 'token.ini'
        self.config_filename = 'config.ini'
        self.config = configparser.RawConfigParser()
        # self.logger = logging.getLogger(__name__)

    def _load_config(self) -> bool:
        logger.info('Otwieram plik config.ini')
        config_result = self.config.read(self.config_filename)
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

        self.config['TOKEN'] = {
            'last_token': ''
        }
        logger.info('Zapisuje pusty plik konfiguracyjny...')
        with open(self.config_filename, 'w') as configfile:
            self.config.write(configfile)

    def save_token(self, token):
        logger.info('Zapisuje token w pliku konfiguracyjnym')
        with open(self.token_filename, 'w') as tokenfile:
            tokenfile.write(token)

    def get_token_from_config(self):
        token = ''

        try:
            with open(self.token_filename) as tokenfile:
                token = tokenfile.readlines()
                if token:
                    token = token[0]
        except FileNotFoundError as error:
            logger.info('Plik z tokenem nie znaleziony.')

        return token

    def load_config(self) -> str:
        result = 'OK'
        config_file_exist = self._load_config()
        if not config_file_exist:
            self._create_empty_config_file()
            result = 'Skonfiguruj plik config.ini'
        return result
