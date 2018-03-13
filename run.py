import os
from flask import Flask, redirect, render_template, request
from datetime import datetime

app = Flask(__name__)

def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)


def add_messages(username, message):
    """Add messages to the 'messages' text file """
    
    #write the chat message to the messages.txt file
    with open("data/messages.txt", "a") as chat_list:
        chat_list.writelines("({0}) {1} - {2}\n".format(
        datetime.now().strftime("%H:%M:%S"), 
        username.title(), 
        message))
        
def get_all_messages():
    """Get all of messages"""
    messages = []
    with open("data/messages.txt", "r") as chat_messages:
        messages = chat_messages.readlines()
    return messages

@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        with open("data/users.txt", "a") as user_list:
            write_to_file("data/users.txt", request.form["username" + "/n"])
            return redirect(request.form["username"])
    return render_template("index.html")
    
@app.route('/<username>')
def user(username):
    """Display chat message"""
    message = get_all_messages()
    return render_template("chat.html", username=username, chat_messages=message)
     
@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect(username)
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)