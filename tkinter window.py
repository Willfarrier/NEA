import tkinter as tk
import pandas as pd
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Login function when user presses button
def login():
    username = ClientID_entry.get()
    try:
        title = 'api_data' + username + '.txt'
        with open(title, 'r') as file:
            api_data = file.read()
            message_label.config(text="Login successful!", command=lambda: main_menu_dispalay(api_data))
    except FileNotFoundError:
        print("This file doesnt exist")
        message_label.config(text="Login failed. Please try again.")

def main_menu_dispalay(api_data):
    # Clear Window
    clear_window()

    window.title("Main Menu")
    message_label = tk.Label(window, text="Graph Options:")
    message_label.pack()
    Dist_AvSpd_button = tk.Button(window, text="Distance Vs Average Speed", command=print("test"))
    Dist_AvSpd_button.pack()
    Dist_MaxSpd_button = tk.Button(window, text="Distance Vs Average Speed")
    Dist_MaxSpd_button.pack()


def clear_window():
    for widgets in window.winfo_children():
        widgets.destroy()


def create_Dist_Av_Speed_graph(api_data):
    # Clear window
    clear_window()

    # Turn .txt into json object
    api_data = json.loads(api_data)
    events = pd.json_normalize(api_data)

    # remove all activities from the dataset which aren't bike rides
    events = events.drop(events[events.type != "Ride"].index)

    # Rename title
    window.title('Scatter plot')

    fig, ax = plt.subplots()
    ax.scatter(x=events['distance'], y=events['average_speed'], color='blue')
    ax.set_xlabel('Distance')
    ax.set_ylabel('Average speed')
    ax.set_title('Scatter plot')

    # embed the plot in a tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    return_button = tk.Button(window, text="Return To main menu")
    return_button.pack()


def create_Dist_Max_Speed_graph(api_data):
    # Clear window
    clear_window()

    # Turn .txt into json object
    api_data = json.loads(api_data)
    events = pd.json_normalize(api_data)

    # remove all activities from the dataset which aren't bike rides
    events = events.drop(events[events.type != "Ride"].index)

    # Rename title
    window.title('Scatter plot')

    fig, ax = plt.subplots()
    ax.scatter(x=events['distance'], y=events['max_speed'], color='blue')
    ax.set_xlabel('Distance')
    ax.set_ylabel('Average speed')
    ax.set_title('Scatter plot')

    # ePut the plot into the window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()


# create the tkinter login window
window = tk.Tk()
window.title("Login")
ClientID_label = tk.Label(window, text="ClientID:")
ClientID_label.pack()
ClientID_entry = tk.Entry(window, show="*")
ClientID_entry.pack()
login_button = tk.Button(window, text="Login", command=login)
login_button.pack()
message_label = tk.Label(window, text="")
message_label.pack()

# start the tkinter event loop
window.mainloop()
