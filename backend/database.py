import psycopg2
import os

def get_connection():
    return psycopg2.conneect(os.environ.get("DATABASE_URL"))