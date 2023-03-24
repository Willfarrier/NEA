import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

# Load .txt file
try:
    with open('my_dataset.txt', 'r') as file:
        my_dataset = file.read()

except FileNotFoundError:
    print("The specified file does not exist.")

# Turn .txt into json object
my_dataset = json.loads(my_dataset)
activities = pd.json_normalize(my_dataset)

activities = activities.drop(activities[activities.type != "Ride"].index)

# graph data for distance against max speed
activities.plot(kind='scatter', x='distance', y='average_speed', color='blue')
plt.show()

# graph data for distance against average speed
activities.plot(kind='scatter', x='distance', y='max_speed', color='red')
plt.show()
print()

