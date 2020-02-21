#!/usr/bin/env bash

docker build -f Dockerfile -t "my-app-image" .

docker build -f Dockerfile-mysql -t "mysql-app-image" .