import json
import pickle
import pandas as pd

# opens the pickle file
with open('film_dictionary.pickle', 'rb') as input_file:
    # loads the pickle file
    data = pickle.load(input_file)

# Convert the list of dictionaries to a DataFrame
data_df = pd.DataFrame(data)

# resets the index of the DataFrame
data_df.reset_index(drop=True, inplace=True)

# converts the DataFrame to JSON and write it to a file
data_df.to_json('data.json', orient='columns', indent=4)
