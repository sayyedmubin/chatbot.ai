# chatbot.py
# This script defines the chatbot functionality

# Import necessary libraries
import pickle

# Load pipeline
with open('model/chatbot_pipeline.pickle', 'rb') as handle:
    pipeline = pickle.load(handle)

# Define function to generate chatbot response
def generate_response(text):
    return pipeline.predict([text])[0]
