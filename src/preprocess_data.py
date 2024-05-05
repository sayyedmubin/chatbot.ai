# preprocess_data.py
# This script preprocesses the data for chatbot training

# Import necessary libraries
import nltk
import string

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Define preprocess function
def preprocess(text):
    # Tokenization
    tokens = nltk.word_tokenize(text.lower())
    # Remove punctuation
    tokens = [word for word in tokens if word.isalnum()]
    return ' '.join(tokens)

# Load and preprocess data
with open('data/climate_data.txt', 'r') as file:
    data = file.readlines()

preprocessed_data = [preprocess(line.strip()) for line in data]

# Save preprocessed data
with open('data/preprocessed_data.txt', 'w') as file:
    for line in preprocessed_data:
        file.write(line + '\n')


