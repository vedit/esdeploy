#!/bin/bash
docker kill es
docker rm es
docker run -p 9200:9200 -p 9300:9300 -p 9400:9400 --name es -d es_changes elasticsearch -Des.node.name="TestNode" -Des.http.cors.enabled="true" -Des.http.cors.allow-origin="/.*/" -Des.http.cors.allow-methods="OPTIONS, HEAD, GET, POST, PUT, DELETE" -Des.http.cors.allow-headers="X-Requested-With,X-Auth-Token,Content-Type, Content-Length, Authorization"
while true; do
	curl -m 30 -Sso /dev/null -w '%{http_code}' 127.0.0.1:9200 2>/dev/null | grep '^200$' && break
	echo "Pausing until elasticsearch is up"
	sleep 1
done
