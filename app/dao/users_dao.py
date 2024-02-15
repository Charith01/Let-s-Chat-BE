from app.db.mariadb_connector import MariaDbConnector

class UsersDao:
    def __init__(self, db_conn_obj):
        self.db_conn_obj: MariaDbConnector = db_conn_obj

    def get_users(self):
        print("enter get_users dao")
        query="select * from users"
        args=[]
        return self.db_conn_obj.process_query(query,arguments=args,fetch_result=True,dictionary=True)

    def create_user(self, input):
        print("enter create_user dao")
        query='insert into users(first_name, last_name,user_name,email,password,status,phone_number) values(%s,%s,%s,%s,%s,%s,%s)'
        args=[input["first_name"],input["last_name"],input["user_name"],input["email"],input["password"],"active",input["phone_number"]]
        return self.db_conn_obj.process_query(query,arguments=args,fetch_result=False,row_count=True)

    def validate_user(self, input):
        print("enter validate_user dao")
        query="select first_name,last_name,user_name,email,password from users where email=%s"
        args=[input["email"]]
        return self.db_conn_obj.process_query(query,arguments=args,fetch_result=True)
