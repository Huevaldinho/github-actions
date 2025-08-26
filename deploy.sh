#!/bin/bash
set -e  # hace que falle al primer error
set -x  # imprime cada comando antes de ejecutarlo

IMAGE_NAME="github-actions-testing"
IMAGE_TAG="latest"

docker login
docker build -t huevaldinho/${IMAGE_NAME} .
docker push  huevaldinho/${IMAGE_NAME}:${IMAGE_TAG}