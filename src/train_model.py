# train_model.py
# This script trains the chatbot model

# Import necessary libraries
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.svm import LinearSVC

# Load preprocessed data
with open('data/preprocessed_data.txt', 'r') as file:
    data = file.readlines()

# Define pipeline
pipeline = make_pipeline(
    FunctionTransformer(lambda x: x, validate=False),
    TfidfVectorizer(),
    LinearSVC()
)

# Train pipeline
pipeline.fit(data)

# Save pipeline
with open('model/chatbot_pipeline.pickle', 'wb') as handle:
    pickle.dump(pipeline, handle)

