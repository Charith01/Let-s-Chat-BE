
from app.db.mariadb_connector import MariaDbConnector

def create_mariadb_connection():
    db_conn_obj = MariaDbConnector()
    db_conn_obj.create_connection()
    return db_conn_obj