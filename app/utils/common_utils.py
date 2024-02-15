import bcrypt,jwt,datetime
from app.config.env import JWT_SECRET_KEY

def password_hasher(password):
    hashed_pass=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
    return hashed_pass

def check_user_password(login_attempt_password,hashed_password_from_db):
    if bcrypt.checkpw(login_attempt_password.encode('utf-8'),hashed_password_from_db.encode('utf-8')):
        return True
    else:
        return False

def generate_jwt_token(input):
    input['exp']=datetime.datetime.utcnow()+datetime.timedelta(hours=1)
    token=jwt.encode(input,JWT_SECRET_KEY,algorithm="HS256")
    return token