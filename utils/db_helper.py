import pymysql
import logging
from utils.helpers import CONFIG

class DBHelper:
    def __init__(self):
        db_config = CONFIG['mysql']
        self.connection = pymysql.connect(
            host=db_config['host'],
            port=int(db_config['port']),
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database'],
            cursorclass=pymysql.cursors.DictCursor
        )
        self.logger = logging.getLogger(self.__class__.__name__)

    def fetch_all(self, query, params=None):
        self.logger.info(f"Executing SELECT: {query} | params: {params}")
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        return result

    def fetch_one(self, query, params=None):
        self.logger.info(f"Executing SELECT ONE: {query} | params: {params}")
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchone()
        return result

    def execute(self, query, params=None):
        self.logger.info(f"Executing SQL: {query} | params: {params}")
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
        self.connection.commit()

    def close(self):
        self.logger.info("Closing DB connection")
        self.connection.close()
