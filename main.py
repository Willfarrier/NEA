import pandas as pd
from pandas.io.json import json_normalize
try:
    with open('my_dataset.txt', 'r') as file:
        my_dataset = file.read()

except FileNotFoundError:
    print("The specified file does not exist.")

activities = json_normalize(my_dataset)
activities.columns
