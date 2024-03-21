.PHONY: help train run predict clean docker-build docker-run

help:
    @echo "Available commands:"
    @echo "  run            Run the Flask app"
    @echo "  predict        Make a prediction"
    @echo "  clean          Clean up temporary files"
    @echo "  docker-build   Build Docker image"
    @echo "  docker-run     Run Docker container"

run:
    python app.py

predict:
    @echo "Sending POST request to Flask endpoint..."
    curl -X POST -H "Content-Type: application/json" -d "{\"calories\": 70, \"protein\": 4, \"fat\": 1, \"sodium\": 130, \"fiber\": 10}" http://127.0.0.1:5000/predict

clean:
    @echo "Cleaning up temporary files..."
    # Add commands to clean up temporary files here

docker-build:
    @echo "Building Docker image..."
    docker build -t cereals-api .

docker-run:
    @echo "Running Docker container..."
    docker run -d -p 5000:5000 --name cereals-container cereals-api
