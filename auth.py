from database import get_db
from utils.security import (
    hash_password,
    check_password,
    create_token
)

def register(username, password):

    db = get_db()

    hashed = hash_password(password)

    try:

        db.execute(
            """
            INSERT INTO users(username,password)
            VALUES(?,?)
            """,
            (
                username,
                hashed
            )
        )

        db.commit()

        return {
            "message":"register success"
        }

    except:

        return {
            "error":"username already exist"
        }

def login(username,password):

    db = get_db()

    user = db.execute(
        """
        SELECT * FROM users
        WHERE username=?
        """,
        (username,)
    ).fetchone()

    if not user:

        return {
            "error":"user not found"
        }

    if not check_password(
        password,
        user["password"]
    ):

        return {
            "error":"wrong password"
        }

    token = create_token(
        user["id"]
    )

    return {
        "token":token
    }