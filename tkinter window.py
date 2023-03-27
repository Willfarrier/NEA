import tkinter as tk
import pandas as pd
import json
import matplotlib.pyplot as plt

# Login function when user presses button
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        message_label.config(text="Login successful!", command=retrieve(username))
    else:
        message_label.config(text="Login failed. Please try again.")

def retrieve(client_id):
    try:
        with open('api_data.txt', 'r') as file:
            api_data = file.read()
            create_graphs(api_data)

    except FileNotFoundError:
        print("This file doesnt exist")

def create_graphs(api_data):
    # Turn .txt into json object
    api_data = json.loads(api_data)
    events = pd.json_normalize(api_data)

    # remove all activities from the dataset which aren't bike rides
    events = events.drop(events[events.type != "Ride"].index)

    # graph data for distance against max speed
    events.plot(kind='scatter', x='distance', y='average_speed', color='blue')
    plt.show()

    # graph data for distance against average speed
    events.plot(kind='scatter', x='distance', y='max_speed', color='red')
    plt.show()
    print()


# create the tkinter login window
window = tk.Tk()
window.title("Login")
username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()
password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()
login_button = tk.Button(window, text="Login", command=login)
login_button.pack()
message_label = tk.Label(window, text="")
message_label.pack()

# start the tkinter event loop
window.mainloop()

