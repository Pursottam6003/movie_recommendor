# import streamlit as st 


import streamlit as st
import pickle 
import requests 
from PIL import Image

movies_list = pickle.load(open('movies.pkl','rb'))
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movies_list = movies_list['title'].values
st.title('Movie recommendor system')

selected_movie = st.selectbox(
    'Which is your favourite movie',
     movies_list)

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}/images"
#     url = url.format(movie_id)

#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4YjU4YTNkN2Q2ZTk3YTMwNTA4ZjIwMjhiYTY4YTRiOCIsInN1YiI6IjY0OTc0ZWFmNmY0M2VjMDEzOTk5ZWNhZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.i_V2-WA3LNxceeDV6Uv5UfcjW5Vrke0BDyeSvYAxjwg"
#     }

#     response = requests.get(url, headers=headers)
#     data = response.json() 

#     return "https://image.tmdb.org/t/p/original/"+data['file_path']


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    
    distances = similarity[movie_index]
    movies_list = sorted((list(enumerate(distances))),reverse=True,key=lambda x: x[1])[1:6]
    
    recommended_movies=[]
    recommended_movies_poster = []

    for i in movies_list :
        movie_id = movies.iloc[i[0]].movie_id
      
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    
    return recommended_movies,recommended_movies_poster

if st.button('Recommend') :
    st.write(selected_movie)
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    
# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

 