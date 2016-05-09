__author__ = 'hexenoid'

import os
import json


class ConfigManager(object):
    def __init__(self):
        self._config_json_path = '/'.join([os.getcwd(), 'esdeploy.json'])
        if not os.path.isfile(self._config_json_path):
            self.write_to_file({})

    def get_all(self):
        return self.read_from_file()

    def get(self, key, default):
        return self.read_from_file().get(key, default)

    def set(self, key, value):
        config_data = self.read_from_file()
        config_data[key] = value
        self.write_to_file(config_data)

    def write_to_file(self, conf_dict):
        try:
            with open(self._config_json_path, "w") as json_file:
                json_file.write(json.dumps(conf_dict, indent=4, sort_keys=True))
        except Exception, e:
            print 'Error Writing'
            print e.message
            exit(1)

    def read_from_file(self):
        result = {}
        if os.path.isfile(self._config_json_path):
            try:
                with open(self._config_json_path) as json_file:
                    result = json.load(json_file)
            except Exception, e:
                print 'Invalid json'
                print e.message
                exit(1)
        else:
            print 'Environment needs to be initiated'
            exit(1)
        return result
