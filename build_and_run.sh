#!/usr/bin/env bash

docker build . -t notty-development
echo "Docker build complete, starting container..."
docker run -d -p 80:80 -e SQLALCHEMY_CONFIG='mysql://USER:PASSWORD@DATABASE_IP/DATABASE_NAME' --name notty notty-development
echo "Container is running, please open http://0.0.0.0:80/login"