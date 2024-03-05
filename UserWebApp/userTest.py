from flask import Flask, render_template, request, url_for, flash, redirect # Flask is the web framework
import sqlite3 # sqlite3 is the database framework
from werkzeug.exceptions import abort # For handling errors
from socket_server import ServerCommunicator

NitroIP = "10.247.201.235"
port = 28710

# Create a webapp instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'vskey'

# Each route corresponse with a link
# First one is the home page
@app.route('/', methods=('GET', 'POST'))
def userTestDispense():
    
    if request.method == 'POST':

        
        amount = int(request.form.get('hrd')) * 100
        if (amount >= 0):
            # enter 0 or exit to end program
            if amount == "0" or amount == "exit":
                communicator.send_message("-1")

            # send message if amount is positive
            elif float(amount) > 0:
        
                communicator.send_message(str(amount))
            print(amount)
        return render_template('userTestEnd.html')
    else: 
        return render_template('userTestDispense.html')

if __name__ == "__main__":
    # Create a server socket for sending and receiving messages
    communicator = ServerCommunicator(NitroIP, port, "message")
    app.run(debug = False)