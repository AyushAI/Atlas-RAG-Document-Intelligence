#!/bin/bash

# Function to kill background processes on exit
cleanup() {
    echo "Stopping services..."
    kill $BACKEND_PID
    exit
}

# Trap SIGINT (Ctrl+C)
trap cleanup SIGINT

echo "Starting Backend (FastAPI)..."
uvicorn backend.main:app --reload --port 8000 &
BACKEND_PID=$!

# Wait a moment for backend to initialize
sleep 3

echo "Starting Frontend (Streamlit)..."
streamlit run app.py

# Wait for backend process
wait $BACKEND_PID
