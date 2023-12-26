import sqlite3
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def get_db_connection():
    conn = sqlite3.connect('user.db')
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     name TEXT NOT NULL,
     email TEXT NOT NULL UNIQUE
    )
''')
    conn.commit()

init_db()

@app.post("/users/")
async def create_user(request: Request):
    try:
        data = await request.json()
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            raise ValueError("User and email are not included.")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users(name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        conn.close()
        return {"message": "User created."}
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON.")
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


@app.get('/users/{user_id}')
def read_user(user_id:int):
    conn = get_db_connection()
    cursor = conn.cursor()
    user = cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    if user is None:
        raise HTTPException(status=404, detail="User not found")
    return {"id": user[0], "name": user[1], "email":user[2]}

@app.put('/users/')
async def update_user(request:Request):
    try:
        data = await request.json()
        user_id = data.get('user_id')
        update_type = data.get('update_type')
        update_value = data.get('update_value')

        if not user_id or not update_type or not update_value:
            raise ValueError("Either User ID, update type, or update value are not present.")

        conn = get_db_connection()
        cursor = conn.cursor()
        user = cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        if user is None:
            raise HTTPException(status=404, detail="User not found")
        if update_type == "name":
            cursor.execute("UPDATE users SET name = ? WHERE id = ?", (update_value, user_id))
        elif update_type == "email":
            cursor.execute("UPDATE users SET email = ? WHERE id = ?", (update_value, user_id))
        conn.commit()
        conn.close()
        return {"message": "User updated"}
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON.")
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    return {"message": "User deleted"}