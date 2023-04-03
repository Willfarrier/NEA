import tkinter as tk
import pandas as pd
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
import time
import numpy as np
import math


def clear_window():
    for widgets in window.winfo_children():
        widgets.destroy()


# Login function when user presses button
def bridge(ClientID_entry, ClientID):
    if ClientID_entry == "":
        ClientID = ClientID
    else:
        ClientID = ClientID_entry.get()
    label = tk.Label(window, text='')
    label.pack()
    try:
        title = 'api_data' + ClientID + '.txt'
        with open(title, 'r') as file:
            api_data = file.read()
            label.config(text="Login successful!")
            window.update()
            time.sleep(2)
            main_menu_display(api_data)
    except FileNotFoundError:
        label.config(text="Login failed. Please try again.")


def main_menu_display(api_data):
    # Clear Window
    clear_window()

    window.title("Main Menu")
    graph_label = tk.Label(window, text="Graph Options:")
    graph_label.grid(row=0, column=0)
    dist_avspd_button = tk.Button(window, text="Distance Vs Average Speed",
                                  command=lambda: create_dist_av_speed_graph(api_data))
    dist_avspd_button.grid(row=1, column=0)
    dist_maxspd_button = tk.Button(window, text="Distance Vs Maximum Speed",
                                   command=lambda: create_dist_max_speed_graph(api_data))
    dist_maxspd_button.grid(row=2, column=0)
    elevation_avspd_button = tk.Button(window, text="Elevation Change Vs Average Speed",
                                       command=lambda: create_elevation_change_average_speed_graph(api_data))
    elevation_avspd_button.grid(row=3, column=0)
    elevation_maxspd_button = tk.Button(window, text="Elevation Change Vs Maximum Speed",
                                        command=lambda: create_elevation_change_max_speed_graph(api_data))
    elevation_maxspd_button.grid(row=4, column=0)
    averages_label = tk.Label(window, text="Averages Options:")
    averages_label.grid(row=0, column=1)
    averages_average_speed_button = tk.Button(window, text="Average Speed Data",
                                              command=lambda: average_speed_calculations(api_data))
    averages_average_speed_button.grid(row=1, column=1)
    averages_average_speed_button = tk.Button(window, text="Maximum Speed Data",
                                              command=lambda: max_speed_calculations(api_data))
    averages_average_speed_button.grid(row=2, column=1)
    averages_average_speed_button = tk.Button(window, text="Distance Data",
                                              command=lambda: distance_calculations(api_data))
    averages_average_speed_button.grid(row=3, column=1)
    averages_average_speed_button = tk.Button(window, text="Elevation Data",
                                              command=lambda: elevation_calculations(api_data))
    averages_average_speed_button.grid(row=4, column=1)


def average_speed_calculations(api_data):
    # Clear window
    clear_window()

    api_data = json.loads(api_data)
    events = pd.DataFrame(api_data)
    events = events[events.type == "Ride"]
    array = events["average_speed"].tolist()

    length = len(array)
    total = 0
    values_squared = 0

    for i in array:
        total += array[int(i)]

    mean = total / length

    for i in array:
        values_squared += (array[int(i)] * array[int(i)])

    variance = (values_squared / length) - (mean * mean)
    standard_dev = math.sqrt(variance)

    array = sorted(array)

    Q1 = array[length // 4]
    Q2 = array[length // 2]
    Q3 = array[int(length // (4 / 3))]

    api_data = json.dumps(api_data)

    window.title("Average Speed Data (Metres/Second)")
    mean = "Mean: " + str(mean)
    mean_label = tk.Label(window, text=mean)
    mean_label.pack()
    Q1 = "Lower Quartile: " + str(Q1)
    Q1_label = tk.Label(window, text=Q1)
    Q1_label.pack()
    Q2 = "Median: " + str(Q2)
    Q2_label = tk.Label(window, text=Q2)
    Q2_label.pack()
    Q3 = "Upper Quartile: " + str(Q3)
    Q3_label = tk.Label(window, text=Q3)
    Q3_label.pack()
    variance = "Variance: " + str(variance)
    variance_label = tk.Label(window, text=variance)
    variance_label.pack()
    standard_dev = "Standard Deviation: " + str(standard_dev)
    standard_dev_label = tk.Label(window, text=standard_dev)
    standard_dev_label.pack()
    return_button = tk.Button(window, text="Return to main menu", command=lambda: main_menu_display(api_data))
    return_button.pack()


def max_speed_calculations(api_data):
    # Clear window
    clear_window()

    api_data = json.loads(api_data)
    events = pd.DataFrame(api_data)
    events = events[events.type == "Ride"]
    array = events["max_speed"].tolist()

    length = len(array)
    total = 0
    values_squared = 0

    for i in array:
        total += array[int(i)]

    mean = total / length

    for i in array:
        values_squared += (array[int(i)] * array[int(i)])

    variance = (values_squared / length) - (mean * mean)
    standard_dev = math.sqrt(variance)

    array = sorted(array)

    Q1 = array[length // 4]
    Q2 = array[length // 2]
    Q3 = array[int(length // (4 / 3))]

    api_data = json.dumps(api_data)

    window.title("Maximum Speed Data (Metres/Second")
    mean = "Mean: " + str(mean)
    mean_label = tk.Label(window, text=mean)
    mean_label.pack()
    Q1 = "Lower Quartile: " + str(Q1)
    Q1_label = tk.Label(window, text=Q1)
    Q1_label.pack()
    Q2 = "Median: " + str(Q2)
    Q2_label = tk.Label(window, text=Q2)
    Q2_label.pack()
    Q3 = "Upper Quartile: " + str(Q3)
    Q3_label = tk.Label(window, text=Q3)
    Q3_label.pack()
    variance = "Variance: " + str(variance)
    variance_label = tk.Label(window, text=variance)
    variance_label.pack()
    standard_dev = "Standard Deviation: " + str(standard_dev)
    standard_dev_label = tk.Label(window, text=standard_dev)
    standard_dev_label.pack()
    return_button = tk.Button(window, text="Return to main menu", command=lambda: main_menu_display(api_data))
    return_button.pack()


def distance_calculations(api_data):
    # Clear window
    clear_window()

    api_data = json.loads(api_data)
    events = pd.DataFrame(api_data)
    events = events[events.type == "Ride"]
    array = events["distance"].tolist()

    length = len(array)
    total = 0
    values_squared = 0

    for i in array:
        total += i

    mean = total / length

    for i in array:
        values_squared += (i * i)

    variance = (values_squared / length) - (mean * mean)
    standard_dev = math.sqrt(variance)

    array = sorted(array)

    Q1 = array[length // 4]
    Q2 = array[length // 2]
    Q3 = array[int(length // (4 / 3))]

    api_data = json.dumps(api_data)

    window.title("Distance Data (Metres)")
    mean = "Mean: " + str(mean)
    mean_label = tk.Label(window, text=mean)
    mean_label.pack()
    Q1 = "Lower Quartile: " + str(Q1)
    Q1_label = tk.Label(window, text=Q1)
    Q1_label.pack()
    Q2 = "Median: " + str(Q2)
    Q2_label = tk.Label(window, text=Q2)
    Q2_label.pack()
    Q3 = "Upper Quartile: " + str(Q3)
    Q3_label = tk.Label(window, text=Q3)
    Q3_label.pack()
    variance = "Variance: " + str(variance)
    variance_label = tk.Label(window, text=variance)
    variance_label.pack()
    standard_dev = "Standard Deviation: " + str(standard_dev)
    standard_dev_label = tk.Label(window, text=standard_dev)
    standard_dev_label.pack()
    return_button = tk.Button(window, text="Return to main menu", command=lambda: main_menu_display(api_data))
    return_button.pack()


def elevation_calculations(api_data):
    # Clear window
    clear_window()

    api_data = json.loads(api_data)
    events = pd.DataFrame(api_data)
    events = events[events.type == "Ride"]
    array = events["total_elevation_gain"].tolist()

    length = len(array)
    total = 0
    values_squared = 0

    for i in array:
        total += i

    mean = total / length

    for i in array:
        values_squared += i * i

    variance = (values_squared / length) - (mean * mean)
    standard_dev = math.sqrt(variance)

    array = sorted(array)

    Q1 = array[length // 4]
    Q2 = array[length // 2]
    Q3 = array[int(length // (4 / 3))]

    api_data = json.dumps(api_data)

    window.title("Elevation Change Data (Metres)")
    mean = "Mean: " + str(mean)
    mean_label = tk.Label(window, text=mean)
    mean_label.pack()
    Q1 = "Lower Quartile: " + str(Q1)
    Q1_label = tk.Label(window, text=Q1)
    Q1_label.pack()
    Q2 = "Median: " + str(Q2)
    Q2_label = tk.Label(window, text=Q2)
    Q2_label.pack()
    Q3 = "Upper Quartile: " + str(Q3)
    Q3_label = tk.Label(window, text=Q3)
    Q3_label.pack()
    variance = "Variance: " + str(variance)
    variance_label = tk.Label(window, text=variance)
    variance_label.pack()
    standard_dev = "Standard Deviation: " + str(standard_dev)
    standard_dev_label = tk.Label(window, text=standard_dev)
    standard_dev_label.pack()
    return_button = tk.Button(window, text="Return to main menu", command=lambda: main_menu_display(api_data))
    return_button.pack()


def create_dist_av_speed_graph(api_data):
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
    coefficients = np.polyfit(events['distance'], events['average_speed'], 1)
    trendline_x = np.array([events['distance'].min(), events['distance'].max()])
    trendline_y = np.polyval(coefficients, trendline_x)
    ax.plot(trendline_x, trendline_y, color='red')
    gradient = coefficients[0]
    ax.set_xlabel('Distance (M)')
    ax.set_ylabel('Average speed (M/S)')
    api_data = json.dumps(api_data)

    # embed the plot in a tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    gradient = "Gradient of the trend line is: " + str(gradient) + " Metres per Second per Metre"
    gradient_value = tk.Label(window, text=gradient)
    gradient_value.pack()
    return_button = tk.Button(window, text="Return to main menu", command=lambda: main_menu_display(api_data))
    return_button.pack()


def create_dist_max_speed_graph(api_data):
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
    coefficients = np.polyfit(events['distance'], events['max_speed'], 1)
    trendline_x = np.array([events['distance'].min(), events['distance'].max()])
    trendline_y = np.polyval(coefficients, trendline_x)
    ax.plot(trendline_x, trendline_y, color='blue')
    gradient = coefficients[0]
    ax.set_xlabel('Distance (M)')
    ax.set_ylabel('Average speed (M/S)')
    api_data = json.dumps(api_data)

    # Put the plot into the window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    gradient = "Gradient of the trend line is: " + str(gradient) + " Metres per Second per Metre"
    gradient_value = tk.Label(window, text=gradient)
    gradient_value.pack()
    return_button = tk.Button(window, text="Return to main menu", command=lambda: main_menu_display(api_data))
    return_button.pack()


def create_elevation_change_average_speed_graph(api_data):
    # Clear window
    clear_window()

    # Turn .txt into a json object and normalise the api data
    api_data = json.loads(api_data)
    events = pd.json_normalize(api_data)

    # remove all activities from the dataset which aren't bike rides
    events = events.drop(events[events.type != "Ride"].index)

    # Rename title
    window.title('Elevation Change Vs Average Speed Plot')

    fig, ax = plt.subplots()
    ax.scatter(x=events['total_elevation_gain'], y=events['average_speed'], color='orange')
    coefficients = np.polyfit(events['total_elevation_gain'], events['average_speed'], 1)
    trendline_x = np.array([events['total_elevation_gain'].min(), events['total_elevation_gain'].max()])
    trendline_y = np.polyval(coefficients, trendline_x)
    ax.plot(trendline_x, trendline_y, color='purple')
    gradient = coefficients[0]
    ax.set_xlabel('Elevation Change (M)')
    ax.set_ylabel('Speed (M/S)')
    api_data = json.dumps(api_data)

    # embed the plot in a tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    gradient = "Gradient of the trend line is: " + str(gradient) + " Metres per Second per Metre Change"
    gradient_value = tk.Label(window, text=gradient)
    gradient_value.pack()
    return_button = tk.Button(window, text="Return to main menu", command=lambda: main_menu_display(api_data))
    return_button.pack()


def create_elevation_change_max_speed_graph(api_data):
    # Clear window
    clear_window()

    # Turn .txt into a json object and normalise the api data
    api_data = json.loads(api_data)
    events = pd.json_normalize(api_data)

    # remove all activities from the dataset which aren't bike rides
    events = events.drop(events[events.type != "Ride"].index)

    # Rename title
    window.title('Elevation Change Vs Maximum Speed Plot')

    fig, ax = plt.subplots()
    ax.scatter(x=events['total_elevation_gain'], y=events['max_speed'], color='green')
    coefficients = np.polyfit(events['total_elevation_gain'], events['max_speed'], 1)
    trendline_x = np.array([events['total_elevation_gain'].min(), events['total_elevation_gain'].max()])
    trendline_y = np.polyval(coefficients, trendline_x)
    ax.plot(trendline_x, trendline_y, color='lightblue')
    gradient = coefficients[0]
    ax.set_xlabel('Elevation Change (M)')
    ax.set_ylabel('Speed (M/S)')
    api_data = json.dumps(api_data)

    # embed the plot in a tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    gradient = "Gradient of the trend line is: " + str(gradient) + " Metres per Second per Metre"
    gradient_value = tk.Label(window, text=gradient)
    gradient_value.pack()
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

    authorise = "https://www.strava.com/oauth/token"
    data = "https://www.strava.com/api/v3/athlete/activities"

    with requests.Session() as session:
        session.verify = False
        session.headers.update({'f': 'json'})

        inputs = {'client_id': str(ClientID), 'client_secret': str(Client_Secret), 'refresh_token': str(Refresh_Token), 'grant_type': 'refresh_token',}
        response = session.post(authorise, json=inputs)
        response.raise_for_status()
        access_token = response.json()['access_token']
        session.headers.update({'Authorization': f'Bearer {access_token}'})

        api_data = []
        page = 1
        while True:
            params = {'per_page': 200, 'page': page}
            response = session.get(data, params=params)
            response.raise_for_status()
            activities = response.json()
            if not activities:
                break
            api_data.extend(activities)
            page += 1

    api_data = json.dumps(api_data)
    client_id = inputs['client_id']

    title = 'api_data' + client_id + '.txt'
    with open(title, 'ab') as file:
        for item in api_data:
            file.write(item.encode())
    bridge("", client_id)

# start the tkinter event loop
window = tk.Tk()
start()
window.mainloop()
