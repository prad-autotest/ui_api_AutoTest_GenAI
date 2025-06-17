import mysql.connector
from utils.helpers import CONFIG
from utils.logger import get_logger

logger = get_logger("DBUtils")

def get_db_connection():
    return mysql.connector.connect(
        host=CONFIG['db']['host'],
        user=CONFIG['db']['user'],
        password=CONFIG['db']['password'],
        database=CONFIG['db']['database']
    )

def fetch_all(query):
    conn = get_db_connection()
    cursor = conn.cursor()
    logger.info(f"Executing Query: {query}")
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result
