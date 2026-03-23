from dotenv import load_dotenv
load_dotenv()

import psycopg2
import os

def get_connection():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))

if __name__ == "__main__":
    conn = get_connection()
    print("Connection successful!")
    conn.close()