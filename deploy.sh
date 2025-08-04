#!/bin/bash

# Set image name and tag
IMAGE_NAME="myapp"
IMAGE_TAG="latest"
EXPERTAL_PORT="3000"
# Extract base image from Dockerfile
BASE_IMAGE=$(grep ^FROM Dockerfile | awk '{print $2}')

#!/bin/bash
set -e  # hace que falle al primer error
set -x  # imprime cada comando antes de ejecutarlo


echo "Pulling base image: ${BASE_IMAGE}..."
docker pull ${BASE_IMAGE}

# Stop and remove existing container if running
echo "Stopping existing container..."
docker stop github-actions-testing 2>/dev/null
docker rm github-actions-testing 2>/dev/null

# Run the Docker container with correct port mapping
echo "Running Docker container..."
docker run -d --name github-actions-testing -p ${EXPERTAL_PORT}:8000 ${IMAGE_NAME}:${IMAGE_TAG}

# Check if container is running
if [ $? -eq 0 ]; then
  echo "✅ Container started successfully!"
  echo "🌐 Access your app at: http://localhost:$EXPERTAL_PORT"
  echo "📚 API docs at: http://localhost:$EXPERTAL_PORT/docs"
else
  echo "❌ Failed to start container"
fi

# Show running containers
echo "Running containers:"
docker ps