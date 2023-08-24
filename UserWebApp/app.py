from flask import Flask, render_template, request, url_for, flash, redirect # Flask is the web framework
import sqlite3 # sqlite3 is the database framework
from werkzeug.exceptions import abort # For handling errors

# Function to connect to database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function for reading database
def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?',
                        (user_id,)).fetchone()
    conn.close()
    if user is None:
        abort(404)
    return user

# Create a webapp instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Each route corresponse with a link
# First one is the home page
@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

if __name__ =="__main__":
    app.run(debug = False)