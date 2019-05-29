import os


USER = os.getenv('POSTGRES_USER') or 'postgres'
PASSWORD = os.getenv('POSTGRES_PASSWORD') or 'password'
HOST = os.getenv('POSTGRES_HOST') or 'postgres'
DATABASE = os.getenv('POSTGRES_DB') or 't206db'
PORT = os.getenv('POSTGRES_PORT') or '5432'

DATABASE_CONNECTION_URI = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
    USER, PASSWORD, HOST, PORT, DATABASE)
