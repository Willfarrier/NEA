import tkinter as tk
import pandas as pd
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
import urllib3
import time


def clear_window():
    for widgets in window.winfo_children():
        widgets.destroy()


# Login function when user presses button
def bridge(ClientID_entry, ClientID):
    if ClientID_entry == "":
        ClientID = ClientID
    else:
        ClientID = ClientID_entry.get()
    try:
        title = 'api_data' + ClientID + '.txt'
        with open(title, 'r') as file:
            api_data = file.read()
            success_label = tk.Label(window, text='')
            success_label.pack()
            success_label.config(text="Login successful")
            time.sleep(5)
            main_menu_display(api_data)
    except FileNotFoundError:
        fail_label = tk.Label(window, text='')
        fail_label.pack()
        fail_label.config(text="Login failed. Please try again.")


def main_menu_display(api_data):
    # Clear Window
    clear_window()

    window.title("Main Menu")
    message_label = tk.Label(window, text="Graph Options:")
    message_label.pack()
    Dist_AvSpd_button = tk.Button(window, text="Distance Vs Average Speed",
                                  command=lambda: create_Dist_Av_Speed_graph(api_data))
    Dist_AvSpd_button.pack()
    Dist_MaxSpd_button = tk.Button(window, text="Distance Vs Maximum Speed",
                                   command=lambda: create_Dist_Max_Speed_graph(api_data))
    Dist_MaxSpd_button.pack()


def create_Dist_Av_Speed_graph(api_data):
    # Clear window
    clear_window()

    # Turn .txt into a json object and normalise the api data
    api_data = json.loads(api_data)
    events = pd.json_normalize(api_data)

    # remove all activities from the dataset which aren't bike rides
    events = events.drop(events[events.type != "Ride"].index)

    # Rename title
    window.title('Distance Vs Average Speed Plot')

    fig, ax = plt.subplots()
    ax.scatter(x=events['distance'], y=events['average_speed'], color='blue')
    ax.set_xlabel('Distance')
    ax.set_ylabel('Average speed')
    ax.set_title('Scatter plot')
    api_data = json.dumps(api_data)

    # embed the plot in a tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    return_button = tk.Button(window, text="Return to main menu", command=lambda: main_menu_display(api_data))
    return_button.pack()


def create_Dist_Max_Speed_graph(api_data):
    # Clear window
    clear_window()

    # Turn .txt into json object and normalise the api data
    api_data = json.loads(api_data)
    events = pd.json_normalize(api_data)

    # remove all activities from the dataset which aren't bike rides
    events = events.drop(events[events.type != "Ride"].index)

    # Rename title
    window.title('Distance Vs Maximum Speed Plot')

    fig, ax = plt.subplots()
    ax.scatter(x=events['distance'], y=events['max_speed'], color='red')
    ax.set_xlabel('Distance')
    ax.set_ylabel('Average speed')
    api_data = json.dumps(api_data)

    # Put the plot into the window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    return_button = tk.Button(window, text="Return to main menu", command=lambda: main_menu_display(api_data))
    return_button.pack()


# create the tkinter login window
def login():
    clear_window()
    window.title("Login")
    ClientID_label = tk.Label(window, text="ClientID:")
    ClientID_label.pack()
    ClientID_entry = tk.Entry(window, show="*")
    ClientID_entry.pack()
    login_button = tk.Button(window, text="Login", command=lambda: bridge(ClientID_entry, ""))
    login_button.pack()
    return_button = tk.Button(window, text="Return to previous page", command=lambda: start())
    return_button.pack()


def start():
    clear_window()
    window.title("Strava API Program")
    Opening_label = tk.Label(window, text="Have you already registered your API details?")
    Opening_label.pack()
    Login_button = tk.Button(window, text="Yes", command=lambda: login())
    Login_button.pack()
    API_Register_buton = tk.Button(window, text="No", command=lambda: api_pull_gui())
    API_Register_buton.pack()


def api_pull_gui():
    # Clear window
    clear_window()

    # Create entry points
    window.title("API Request")
    ClientID_label = tk.Label(window, text="ClientID:")
    ClientID_label.pack()
    ClientID_entry = tk.Entry(window)
    ClientID_entry.pack()
    Client_Secret_label = tk.Label(window, text="Client Secret")
    Client_Secret_label.pack()
    Client_Secret_entry = tk.Entry(window)
    Client_Secret_entry.pack()
    Refresh_Token_label = tk.Label(window, text="Refresh Token")
    Refresh_Token_label.pack()
    Refresh_Token_entry = tk.Entry(window)
    Refresh_Token_entry.pack()
    Submit_button = tk.Button(window, text="Submit details",
                              command=lambda: api_pull(ClientID_entry, Client_Secret_entry, Refresh_Token_entry))
    Submit_button.pack()
    return_button = tk.Button(window, text="Return to previous page", command=lambda: start())
    return_button.pack()


def api_pull(ClientID_entry, Client_Secret_entry, Refresh_Token_entry):
    ClientID = ClientID_entry.get()
    Client_Secret = Client_Secret_entry.get()
    Refresh_Token = Refresh_Token_entry.get()

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    auth_url = "https://www.strava.com/oauth/token"
    activites_url = "https://www.strava.com/api/v3/athlete/activities"

    payload = {
        'client_id': str(ClientID),
        'client_secret': str(Client_Secret),
        'refresh_token': str(Refresh_Token),
        'grant_type': "refresh_token",
        'f': 'json'
    }

    res = requests.post(auth_url, data=payload, verify=False)
    access_token = res.json()['access_token']
    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': 200, 'page': 1}
    api_data = requests.get(activites_url, headers=header, params=param).json()

    api_data = json.dumps(api_data)
    client_id = payload['client_id']

    title = 'api_data' + client_id + '.txt'
    with open(title, 'ab') as file:
        for item in api_data:
            file.write(item.encode())
    bridge("", client_id)


# start the tkinter event loop
window = tk.Tk()
start()
window.mainloop()
