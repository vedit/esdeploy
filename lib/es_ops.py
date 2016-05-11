__author__ = 'hexenoid'
import json
from lib.es_env import EsEnv
from elasticsearch import Elasticsearch, helpers


class EsOps(object):

    def __init__(self):
        es_env = EsEnv()
        self._es = Elasticsearch(**es_env.build_conn_string())

    def migrate_index(self, index_alias):
        old_index = self._get_index_from_alias(index_alias)
        new_index = EsOps._bump_version(old_index)
        index_config = EsOps._read_index_mapping(index_alias)
        self._create_index(new_index, index_config)
        self._migrate_data(new_index, old_index)
        self._switch_aliases(new_index, old_index, index_alias)
        self._close_index(old_index)

    def initialize_index(self, index):
        index_config = self._get_index(index)
        new_index = self._bump_version(index)
        self._write_index_mapping(index, index_config)
        self._create_index(new_index, index_config)
        self._migrate_data(new_index, index)
        self._delete_index(index)
        self._add_alias(new_index, index)

    def _get_index(self, index):
        index_mapping = self._es.indices.get_mapping(index)
        index_settings = self._es.indices.get_settings(index)
        index_mapping['settings'] = {'analysis': index_settings[
            index]['settings']['index']['analysis']}
        print index_mapping
        return index_mapping

    def _create_index(self, index, body):
        self._es.indices.create(index, body=body)

    def _delete_index(self, index):
        self._es.indices.delete(index)

    def _add_alias(self, index, alias_name):
        self._es.indices.put_alias(index, alias_name)

    def _remove_alias(self, index, alias_name):
        self._es.indices.delete_alias(index, alias_name)

    def _switch_aliases(self, new_index, old_index, alias_name):
        self._remove_alias(old_index, alias_name)
        self._add_alias(new_index, alias_name)

    def _close_index(self, index):
        self._es.indices.close(index)

    @staticmethod
    def _write_index_mapping(index, index_mapping):
        with open('%s.json' % index, 'w') as fp:
            json.dump(index_mapping, fp)

    @staticmethod
    def _read_index_mapping(index):
        with open('%s.json' % index, 'r') as fp:
            index_mapping = json.load(fp)
        return index_mapping

    @staticmethod
    def _bump_version(index):
        version_delimiter = '%'
        index_name_parts = index.split(version_delimiter)
        if len(index_name_parts) == 1:
            version = 1
        else:
            version = int(index_name_parts[1]) + 1
        return "%s%s%s" % (index_name_parts[0], '%', version)

    def _migrate_data(self, new_index, old_index):
        helpers.reindex(self._es, old_index, new_index)

    def _get_index_from_alias(self, index_alias):
        index = self._es.indices.get_alias(name=index_alias).keys()[0]
        print index
        return index
