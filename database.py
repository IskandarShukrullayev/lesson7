import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

class database:
    @staticmethod
    def connect(query:str , query_type: str ) -> list or str :
        db = psql.connect(
            database = os.getenv('DB_NAME'),
            user = os.getenv("DB_USER"),
            host = os.getenv("DB_HOST"),
            pasword = os.getenv("DB_PASWORD"),
            port = os.getenv("DB_PORT"),
        )
        cursor = db.cursor()
        data = ['insert', 'delet', 'update', 'alter']
        cursor.execute(query)
        if query_type in data:
            db.commit()
            if query_type == 'insert':
                return "insert data"

            else:
                return cursor.fetchall()