import mariadb


MYSQL_PORT=3306
class MariaDbConnector(object):
    def __init__(self):
        self.db_conn = None
        self.db_properties = {
            'host': "localhost",
            'user': "root",
            'password': "Cherry2001",
            'database': "lets_chat",
            'port': MYSQL_PORT
        }

    def create_connection(self):
        """
        Method to create a db connection
        :return:
        """
        try:
            self.db_conn = mariadb.connect(
                user=self.db_properties.get('user'),
                password=self.db_properties.get('password'),
                host=self.db_properties.get('host'),
                port=self.db_properties.get('port'),
                database=self.db_properties.get('database')
            )
            return self.db_conn
        except mariadb.Error as e:
            print("Exception in Creating DB connection: ")
            raise

    def process_query(self, query: str, arguments=None, fetch_result=True, bulk_insert=False, count=None,
                      dictionary=True,
                      row_count=False):

        try:
            query = query
            print(f"Query : {query}")
            print(f"Args : {arguments}")
            cursor = self.db_conn.cursor(dictionary=dictionary)
            result = None
            if bulk_insert:
                cursor.executemany(query, arguments)
            else:
                cursor.execute(query, arguments)
                if row_count:
                    return cursor.rowcount
                if fetch_result:
                    result = cursor.fetchall()
                    if not dictionary:
                        result_set = []
                        for row in result:
                            result_set.append(row[0])
                        result = result_set
                    else:
                        if count:
                            result = result[:count]
                else:
                    result = cursor.lastrowid
            return result

        except mariadb.Error as exception:
            print("Exception in processing query: %s", exception)
            raise

    def save_transaction(self):
        self.db_conn.commit()

    def rollback_transaction(self):
        self.db_conn.rollback()

    def end_connection(self):
        self.db_conn.close()

    def is_connected(self):
        try:
            self.db_conn.ping()
            return True
        except mariadb.InterfaceError as err:
            return False