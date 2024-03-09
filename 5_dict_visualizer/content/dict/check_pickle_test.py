import json
import pickle


# Open the pickle file in binary mode for reading
with open('film_dictionary.pickle', 'rb') as f:
    # Load the data from the pickle file
    data = pickle.load(f)



print(data)
