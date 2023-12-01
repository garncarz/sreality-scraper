import os

DATABASE = os.getenv('DATABASE', 'postgresql://postgres@db/postgres')
