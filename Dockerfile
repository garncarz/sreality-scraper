from python:3-slim

workdir /app

copy requirements.txt .
run pip install --no-cache-dir -r requirements.txt

copy . .
