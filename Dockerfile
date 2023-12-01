from python:3-slim

copy requirements.txt .
run pip install --no-cache-dir -r requirements.txt

workdir /app
copy . .
