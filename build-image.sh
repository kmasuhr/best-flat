#!/usr/bin/env bash

docker buildx create --use
docker buildx build --platform linux/amd64 -t best-flat:latest -f docker/Dockerfile .
