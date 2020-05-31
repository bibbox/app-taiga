#!/usr/bin/env bash
mkdir -p data/conf
mkdir -p data/conf/back
mkdir -p data/conf/front
mkdir -p data/conf/proxy
mkdir -p data/db
chmod -R 777 data
docker-compose up -d
