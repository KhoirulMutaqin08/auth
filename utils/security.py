import bcrypt
import jwt
import datetime

SECRET_KEY = "secret-key"

def hash_password(password):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )


def check_password(password, hashed):
    return bcrypt.checkpw(
        password.encode(),
        hashed
    )


def create_token(user_id):

    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow()
        + datetime.timedelta(hours=24)
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )


def verify_token(token):

    try:
        data = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        return data

    except:
        return None