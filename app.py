from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd
import requests
import os

app = FastAPI(
    title="Movie Recommender API",
    version="1.1"
)

 
# Constants
 
TMDB_API_KEY = "68bf2d5ecf62356140afda67ffa54f1b"
TMDB_BASE_URL = "https://api.themoviedb.org/3"
POSTER_BASE_URL = "https://image.tmdb.org/t/p/w500"

 
# Load models
 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

movies_dict = pickle.load(open(os.path.join(BASE_DIR, "models", "movies_dict.pkl"), "rb"))
similarity = pickle.load(open(os.path.join(BASE_DIR, "models", "similarity.pkl"), "rb"))

movies = pd.DataFrame(movies_dict)
movies["title_lower"] = movies["title"].str.lower()
movies["tags_lower"] = movies["tags"].str.lower()

 
# Mood keywords
 
mood_keywords = {
    "happy": ["comedy", "fun", "adventure", "family", "animation", "romance"],
    "sad": ["drama", "tragedy", "loss", "emotional", "romantic"],
    "excited": ["action", "thriller", "crime", "superhero", "fight", "spy"],
    "scared": ["horror", "mystery", "ghost", "zombie", "dark"],
    "sci-fi lover": ["sci-fi", "space", "alien", "future", "technology"],
}

 
# Helpers
 
def fetch_poster(movie_id):
    try:
        r = requests.get(
            f"{TMDB_BASE_URL}/movie/{movie_id}",
            params={"api_key": TMDB_API_KEY},
            timeout=5
        )
        poster = r.json().get("poster_path")
        return POSTER_BASE_URL + poster if poster else None
    except:
        return None


def fetch_trailer(movie_id):
    try:
        r = requests.get(
            f"{TMDB_BASE_URL}/movie/{movie_id}/videos",
            params={"api_key": TMDB_API_KEY},
            timeout=5
        )
        for v in r.json().get("results", []):
            if v.get("type") == "Trailer" and v.get("site") == "YouTube":
                return f"https://www.youtube.com/watch?v={v['key']}"
        return None
    except:
        return None

 
# Schemas
 
class MovieRequest(BaseModel):
    title: str


class MoodRequest(BaseModel):
    mood: str

 
# Routes
 
@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/movies")
def get_movies():
    return movies["title"].tolist()

@app.post("/recommend/title")
def recommend_title(req: MovieRequest):
    title = req.title.lower().strip()
    if title not in movies["title_lower"].values:
        raise HTTPException(404, "Movie not found")

    idx = movies[movies["title_lower"] == title].index[0]
    distances = similarity[idx]

    recs = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    results = []
    for i in recs:
        movie_id = movies.iloc[i[0]].movie_id
        results.append({
            "title": movies.iloc[i[0]].title,
            "poster": fetch_poster(movie_id),
            "trailer": fetch_trailer(movie_id)
        })

    return {"recommendations": results}

@app.post("/recommend/mood")
def recommend_mood(req: MoodRequest):
    mood = req.mood.lower().strip()
    if mood not in mood_keywords:
        raise HTTPException(400, "Invalid mood")

    keywords = mood_keywords[mood]
    matched = movies[movies["tags_lower"].apply(lambda x: any(k in x for k in keywords))]

    if matched.empty:
        return {"recommendations": []}

    sample = matched.sample(1).iloc[0]
    idx = movies[movies["title_lower"] == sample["title"].lower()].index[0]
    distances = similarity[idx]

    recs = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    results = []
    for i in recs:
        movie_id = movies.iloc[i[0]].movie_id
        results.append({
            "title": movies.iloc[i[0]].title,
            "poster": fetch_poster(movie_id),
            "trailer": fetch_trailer(movie_id)
        })

    return {"recommendations": results}
