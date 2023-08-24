from flask import Flask
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')

cursor.execute("INSERT INTO users (name) VALUES (?)", ('NAMETEST',))


conn.commit()

cursor.execute("SELECT name FROM users WHERE id = ?", (1,))
result = cursor.fetchone()[0]

cursor.close()
conn.close()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! TESTTESTTEST'

@app.route('/test')
def test():
    return 'WOW, TEST!'

@app.route('/name')
def get_name():
    return 'WOW, THE NAME IS ' + result
