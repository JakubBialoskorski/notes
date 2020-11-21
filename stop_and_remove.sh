#!/usr/bin/env bash

docker stop notty
echo "Stopping container"
docker rm notty
echo "Removing container"