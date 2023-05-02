from fastapi import FastAPI, HTTPException, Form, Response
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from config import settings
import sqlite3

app = FastAPI()
print(settings)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


conn = sqlite3.connect(settings.DATABASE)

# create user table if it doesn't exist
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (username text, password text)")
conn.commit()

# Path: /register
@app.post("/register")
async def register(username: str = Form(...), password: str = Form(...)):
    # check if username already exists
    print(username, password)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    if c.fetchone() is not None:
        raise HTTPException(status_code=400, detail="Username already exists")
    # insert user into database
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()
    return {"username": username, "status": "success"}


# Path: /login
@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    # check if username and password match
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if c.fetchone() is None:
        raise HTTPException(status_code=400, detail="Username or password is incorrect")
    return {"username": username}

# Path: /users
@app.get("/users")
async def users():
    print("get users")
    c = conn.cursor()
    c.execute("SELECT username FROM users")
    users = c.fetchall()
    return {"users": users, "status": "success"}

@app.get("/user")
async def user(username: str):
    c = conn.cursor()
    c.execute("SELECT username FROM users WHERE username=?", (username,))
    user = c.fetchone()
    if user is None:
        raise HTTPException(status_code=400, detail="User does not exist")
    return {"user": user, "status": "success"}