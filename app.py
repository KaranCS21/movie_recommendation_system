import pickle
import streamlit as st
import pandas as pd
import requests

def recomended(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    for i in movies_list:
        # fetch poster from API
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names


movies = pickle.load(open('movie.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')

movies_list = movies['title'].values
option = st.selectbox(
    "Type or select a movie from the dropdown",
    movies_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recomended(option)
    for i in recommended_movie_names:
        st.write(i)