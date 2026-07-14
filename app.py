from flask import Flask,request,jsonify
from database import init_db
from auth import register,login
from utils.security import verify_token

app = Flask(__name__)

init_db()

@app.route("/")
def home():

    return {
        "status":"API running"
    }


@app.post("/register")
def register_api():

    data=request.json
    result=register(
        data["username"],
        data["password"]
    )

    return jsonify(result)


@app.post("/login")
def login_api():

    data=request.json
    result=login(
        data["username"],
        data["password"]
    )

    return jsonify(result)


@app.get("/profile")
def profile():

    header=request.headers.get(
        "Authorization"
    )

    if not header:

        return {
            "error":"token required"
        },401

    token=header.replace(
        "Bearer ",
        ""
    )

    user=verify_token(token)

    if not user:

        return {
            "error":"invalid token"
        },401

    return {

        "message":"welcome",
        "user_id":user["user_id"]
    }

if __name__=="__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )