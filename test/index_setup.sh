#!/bin/bash

DST_SERVER="http://127.0.0.1:9200"

INDEX_MAPPINGS='
{
  "settings": {
    "analysis": {
      "filter": {
        "esdeploy_ngram": {
          "type": "edge_ngram",
          "min_gram": 3,
          "max_gram": 20
        },
        "turkish_lowercase": {
          "type": "lowercase",
          "language": "turkish"
        }
      },
      "analyzer": {
        "esdeploy_search_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "apostrophe",
            "turkish_lowercase",
            "asciifolding"
          ]
        },
        "esdeploy_index_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "apostrophe",
            "turkish_lowercase",
            "asciifolding",
            "esdeploy_ngram"
          ]
        }
      }
    }
  },
  "mappings": {
    "_default_": {
      "properties": {
        "id": {
          "type": "integer",
          "index": "no"
        },
        "name": {
          "type": "string",
          "analyzer": "esdeploy_index_analyzer",
          "search_analyzer": "esdeploy_search_analyzer"
        },
        "description": {
          "type": "string",
          "analyzer": "esdeploy_index_analyzer",
          "search_analyzer": "esdeploy_search_analyzer"
        },
        "search_image": {
          "type": "string",
          "index": "no"
        },
        "category_names": {
          "type": "string",
          "index": "no"
        },
        "cast": {
          "type": "string",
          "analyzer": "esdeploy_index_analyzer",
          "search_analyzer": "esdeploy_search_analyzer"
        },
        "director_name": {
          "type": "string",
          "analyzer": "esdeploy_index_analyzer",
          "search_analyzer": "esdeploy_search_analyzer"
        }
      }
    }
  }
}'

map_index(){
  curl -XPUT ${DST_SERVER}/${1} -d "${INDEX_MAPPINGS}"
}

migrate_index(){
  map_index $1
  migrate_data $1
}

migrate_data() {
  elasticdump --input=./indexes/${1}.json --output=${DST_SERVER}/${1} --type=data
}

deploy_index() {
  migrate_index dramas
  migrate_index movies
}


main(){
  deploy_index
}

main