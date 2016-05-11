__author__ = 'hexenoid'
from lib.config_manager import ConfigManager


class EsEnv(object):

    def __init__(self):
        self._config = ConfigManager()

    @property
    def es_host(self):
        return self._config.get('es_host', '127.0.0.1')

    @es_host.setter
    def es_host(self, conf_val):
        self._config.set('es_host', conf_val)

    @property
    def es_port(self):
        return self._config.get('es_port', '9200')

    @es_port.setter
    def es_port(self, conf_val):
        self._config.set('es_port', conf_val)

    @property
    def es_ssl(self):
        return self._config.get('es_ssl', False)

    @es_ssl.setter
    def es_ssl(self, conf_val):
        self._config.set('es_ssl', conf_val)

    @property
    def auth_user(self):
        return self._config.get('auth_user', '')

    @auth_user.setter
    def auth_user(self, conf_val):
        if not conf_val == '':
            self._config.set('auth_user', conf_val)

    @property
    def auth_pass(self):
        return self._config.get('auth_pass', '')

    @auth_pass.setter
    def auth_pass(self, conf_val):
        if not conf_val == '':
            self._config.set('auth_pass', conf_val)

    def check_config(self):
        # TODO validate and clean config params
        # this is a stopper for initiation
        # exit with exceptions
        return True

    def build_conn_string(self):
        conn_string = dict()
        conn_string['host'] = self.es_host
        if self.auth_user and self.auth_pass:
            conn_string['http_auth'] = (self.auth_user, self.auth_pass)
        if self.es_ssl:
            import certifi

            conn_string['use_ssl'] = True
            conn_string['verify_certs'] = True
            conn_string['ca_certs'] = certifi.where()
        return conn_string
