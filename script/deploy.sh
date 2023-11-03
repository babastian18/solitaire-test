#!/bin/bash

echo "Starting deployment process on the target VM..."
#deployment commands
# Pull the latest Docker image
docker pull 21052002/solitaire-test:latest
# Run the Docker container
docker run -d -p 8000:5000 21052002/solitaire-test:latest

echo "Deployment process completed."
    
