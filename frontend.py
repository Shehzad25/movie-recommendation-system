import streamlit as st
import requests

API_URL = "http://51.20.64.104:8004"

st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")


@st.cache_data
def get_movies():
    return requests.get(f"{API_URL}/movies").json()

option = st.radio("Search by", ["Movie Title", "Mood"])

if option == "Movie Title":
    movies = get_movies()
    selected_movie = st.selectbox("Select a movie", movies)
else:
    selected_mood = st.selectbox(
        "Select mood",
        ["Happy", "Sad", "Excited", "Scared", "Sci-Fi Lover"]
    )

if st.button("Recommend"):
    with st.spinner("Fetching recommendations..."):
        if option == "Movie Title":
            res = requests.post(
                f"{API_URL}/recommend/title",
                json={"title": selected_movie}
            )
        else:
            res = requests.post(
                f"{API_URL}/recommend/mood",
                json={"mood": selected_mood}
            )

    if res.status_code != 200:
        st.error("Something went wrong")
    else:
        data = res.json()["recommendations"]
        cols = st.columns(5)

        for i, movie in enumerate(data):
            with cols[i]:
                st.subheader(movie["title"])
                if movie["poster"]:
                    st.image(movie["poster"])
                if movie["trailer"]:
                    st.markdown(f"[▶ Watch Trailer]({movie['trailer']})")
