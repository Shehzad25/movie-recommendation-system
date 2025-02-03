Movie Recommendation System

Overview

This Movie Recommendation System suggests movies based on content similarity. It processes movie metadata (genres, keywords, cast, crew, overview) and applies NLP techniques to generate recommendations. The system uses cosine similarity to find the most similar movies.

Features

Data Preprocessing: Merges movie and credits datasets and extracts key attributes.

Text Processing: Converts text into numerical vectors using CountVectorizer with stop-word removal and stemming.

Similarity Computation: Uses cosine similarity to measure movie similarity.

Movie Recommendation: Provides the top 5 most similar movies for a given input movie.

Model Persistence: Saves processed data and similarity matrix using pickle for efficient future use.

Tech Stack

Python

Pandas & NumPy (Data Processing)

NLTK (Text Processing - Stemming)

Scikit-learn (Vectorization & Similarity Computation)

Flask (Web Application)

Project Structure

movie-recommendation-system/
│-- tmdb_5000_movies.csv
│-- tmdb_5000_credits.csv
│-- Movie_recommender_system.ipynb
│-- app.py
│-- movies_dict.pkl
│-- similarity.pkl
│-- README.md

Installation & Usage

Clone the repository:

git clone https://github.com/Shehzad25/movie-recommendation-system.git
cd movie-recommendation-system

Install dependencies:

pip install -r requirements.txt

Run the Flask app:

python app.py

Open the browser and go to http://127.0.0.1:5000/ to access the app.

How It Works

The system processes the datasets and extracts important features.

It applies stemming and converts text into vectors.

Cosine similarity is used to compare movies based on their content.

The user inputs a movie title, and the system returns the top 5 most similar movies.

Contributing

Feel free to contribute by opening issues or submitting pull requests.

License

This project is licensed under the MIT License.

