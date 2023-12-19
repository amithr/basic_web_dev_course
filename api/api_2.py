import sqlite3
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Database connection function
def get_db_connection():
    # connection object
    conn = sqlite3.connect('user.db')
    # rows are returned as tuples
    # Once a tuple is created, you can't change, add, or remove elements.
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database and create table if not exists
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
    conn.close()

# Initialize the database
init_db()

@app.post("/users/")
def create_user(name: str, email: str):
    conn = get_db_connection()
    # cursor object used to traverse database and get a result accordingly
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()
    return {"message": "User created"}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return dict(user)

@app.put("/users/{user_id}/{change_param}/{payload}")
def update_user(user_id: int, change_param: str=None, payload: str=None):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    if user is None:
        conn.close()
        raise HTTPException(status_code=404, detail="User not found")

    if change_param == "name":
        conn.execute('UPDATE users SET name = ? WHERE id = ?', (payload, user_id))
    if change_param == "email":
        conn.execute('UPDATE users SET email = ? WHERE id = ?', (payload, user_id))
    conn.commit()
    conn.close()
    return {"message": "User updated"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    return {"message": "User deleted"}
