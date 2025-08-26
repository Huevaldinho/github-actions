#!/bin/bash
set -e

# Variables
IMAGE_NAME="github-actions-testing"
IMAGE_TAG="latest"
EXTERNAL_PORT="3000"
CONTAINER_NAME="github-actions-testing-container"

# Stop and remove existing container if running
docker stop $CONTAINER_NAME 2>/dev/null || true
docker rm $CONTAINER_NAME 2>/dev/null || true

# Run the Docker container with correct port mapping
docker run -d --name $CONTAINER_NAME -p ${EXTERNAL_PORT}:8000 huevaldinho/${IMAGE_NAME}:${IMAGE_TAG}

# Check if container started correctly
if [ $? -eq 0 ]; then
  echo "✅ Container started successfully!"
  echo "🌐 Access your app at: http://localhost:$EXTERNAL_PORT"
  echo "📚 API docs at: http://localhost:$EXTERNAL_PORT/docs"
  curl -I http://localhost/health
else
  echo "❌ Failed to start container"
fi

# Show running containers
echo "Running containers:"
docker ps
