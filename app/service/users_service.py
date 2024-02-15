from starlette.responses import JSONResponse

from app.dao.users_dao import UsersDao
from app.utils.db_utils import create_mariadb_connection
from app.utils import common_utils


class UsersService:
    def __init__(self):
        self.db_conn_obj = None

    def get_users(self):
        try:
            print("enter get_users service")
            self.db_conn_obj = create_mariadb_connection()
            dao_obj = UsersDao(self.db_conn_obj)
            resp = dao_obj.get_users()
            return resp
        except Exception as e:
            print("exception occured in servie:-", e)
            raise
        finally:
            self.db_conn_obj.end_connection()

    def create_user(self, input):
        try:
            print("enter create_user service")
            self.db_conn_obj = create_mariadb_connection()
            dao_obj = UsersDao(self.db_conn_obj)
            input["password"] = common_utils.password_hasher(input["password"])
            resp = dao_obj.create_user(input)
            return {"status": "Ok", "msg": "User created successfully", "success": True}
        except Exception as e:
            print("exception occured in service:-", e)
            raise

        finally:
            self.db_conn_obj.save_transaction()
            self.db_conn_obj.end_connection()

    def validate_user(self, input):
        try:
            print("enter validate_user service")
            self.db_conn_obj = create_mariadb_connection()
            dao_obj = UsersDao(self.db_conn_obj)
            user_data = dao_obj.validate_user(input)[0]
            if not len(user_data) > 0:
                return JSONResponse(status_code=401, content={"data": "Invalid user email"})

            print(user_data)
            print(input)
            if user_data and common_utils.check_user_password(input["password"], user_data["password"]):
                del user_data["password"]
                token = common_utils.generate_jwt_token(user_data)
                return {"data": {"token": token}}
            return JSONResponse(status_code=500, content={"data": {"token": ""}})
        except Exception as e:
            print("exception occured in service:-", e)
            raise
        finally:
            self.db_conn_obj.end_connection()
