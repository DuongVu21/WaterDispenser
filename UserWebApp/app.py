from distutils.util import execute
from flask import Flask, render_template, request, url_for, flash, redirect # Flask is the web framework
import sqlite3 # sqlite3 is the database framework
from werkzeug.exceptions import abort # For handling errors
from socket_server import ServerCommunicator
import time

NitroIP = "10.247.201.235"
port = 28710

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

def update_reserve(username, new_res):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET reserve = ? WHERE username = ?", 
                                        (new_res, username))
    conn.commit()
    conn.close()
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

@app.route('/user/<string:username>/disp', methods=('GET', 'POST'))
def disp(username):
    user = get_user(username)
    print(user[4])
    if request.method == 'POST':
        amount = int(request.form.get('hrd')) * 100
        if amount > user[4]:
            return render_template('insufficient.html', user=user)
        else:
            tempReserve = user[4]
            tempReserve -= amount
            update_reserve(user[2], tempReserve)
            # # enter 0 or exit to end program
            # if amount == "0" or amount == "exit":
            #     communicator.send_message("-1")

            # # send message if amount is positive
            # elif float(amount) > 0:
        
            #     communicator.send_message(str(amount))
            time.sleep(amount/28.8)
            return render_template('dispenseComplete.html', user=user)
        
    else:
        return render_template('dispense.html', user=user)

if __name__ == "__main__":
    # Create a server socket for sending and receiving messages
    # communicator = ServerCommunicator(NitroIP, port, "message")
    app.run(debug = False)