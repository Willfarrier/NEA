import pandas as pd
import json
try:
    with open('my_dataset.txt', 'r') as file:
        my_dataset = file.read()

except FileNotFoundError:
    print("The specified file does not exist.")

my_dataset = json.loads(my_dataset)
activities = pd.json_normalize(my_dataset)
print(activities)
