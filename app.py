import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
  response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=68bf2d5ecf62356140afda67ffa54f1b'.format(movie_id))
  data=response.json()
  return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']


st.title('Movie Recommendation System')

def recommend(movie):
  movie_index=movies[movies['title']==movie].index[0]
  distances=similarity[movie_index]
  movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  recommended_movies=[]
  recommended_movies_posters=[]
  for i in movie_list:
    movie_id=movies.iloc[i[0]].movie_id

    recommended_movies.append(movies.iloc[i[0]].title)
    recommended_movies_posters.append(fetch_poster(movie_id))
  return recommended_movies,recommended_movies_posters

movies=pickle.load(open('movie.pkl','rb'))
movies=pd.DataFrame(movies)
similarity=pickle.load(open('similarity.pkl','rb'))

selected_movie=st.selectbox(
  "Get a recommendation of Movie ",
  movies['title'].values
)

if st.button('Recommend'):
  name,posters=recommend(selected_movie)

  col1, col2, col3,col4,col5 = st.columns(5)

  with col1:
    st.text(name[0])
    st.image(posters[0])
    
  with col2:
    st.text(name[1])
    st.image(posters[1])
  with col3:
    st.text(name[2])
    st.image(posters[2])
  with col4:
    st.text(name[3])
    st.image(posters[3])
  with col5:
    st.text(name[4])
    st.image(posters[4])
