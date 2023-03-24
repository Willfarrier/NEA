import pandas as pd
import json
import matplotlib.pyplot as plt

# Load .txt file
try:
    with open('api_data.txt', 'r') as file:
        api_data = file.read()

except FileNotFoundError:
    print("This file doesnt exist")

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

