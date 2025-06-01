import streamlit as st
import pickle
import pandas as pd



def movie_search_recommend(movies ,similarity, text):
    if text in movies['title'].values:
        recommend_movies = []
        movie_index = movies[movies["title"] == text].index[0]
        distance = similarity[movie_index]
        movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
        for index, point in movie_list:
            recommend_movies.append(movies.iloc[index]["title"])
        return recommend_movies
    else:

        movie = list(movies[movies['tags'].str.contains(text, case=False)]['title'])
        return movie

movies_list = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
# movies_list = movies_list['title'].values

st.title('Movie Recommender System')

selected_movies = st.text_input("Search:", "")

if st.button('Show Recommendation'):

    for _ in movie_search_recommend(movies_list,similarity,selected_movies):
        st.write(_)
