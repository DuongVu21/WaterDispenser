from flask import Flask, render_template, request, url_for, flash, redirect # Flask is the web framework
import sqlite3 # sqlite3 is the database framework
from werkzeug.exceptions import abort # For handling errors

# Function to connect to database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function for reading database
def get_user(username):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?',
                        (username,)).fetchone()
    conn.close()
    if user is None:
        abort(404)
    return user

# Create a webapp instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'vskey'

# Each route corresponse with a link
# First one is the home page
@app.route('/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user(username)
        if (user):
            if (password == user[3]):
                print("Logged in")

        return redirect(url_for('user', username=user['username']))
    else: 
        return render_template('login.html')

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if (username):
            if (password):
                print("Signed up")
                connection = sqlite3.connect('database.db')

                with open("schema.sql") as f:
                    connection.executescript(f.read())

                cur = connection.cursor()

                cur.execute("INSERT INTO users (username, password, reserve) VALUES (?, ?, ?)",
                            (username, password, 0))

                connection.commit()
                connection.close()
                
        return redirect(url_for('login'))
    
    else:
        return render_template('signup.html')
        

@app.route('/user/<string:username>')
def user(username):
    user = get_user(username)
    return render_template('user.html', user=user)

@app.route('/user/<string:username>/disp')
def disp(username):
    user = get_user(username)
    return render_template('dispense.html', user=user)

if __name__ =="__main__":
    app.run(debug = False)