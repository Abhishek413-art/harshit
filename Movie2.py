import streamlit as st
import pickle
import pandas as pd

movies = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:4]

    r = []
    for i in movie_list:
        r.append(movies.iloc[i[0]].title)
    return r

st.title('Movie recommender system')

m = movies['title']
x = st.selectbox('Which movies you like', m.values)

if st.button('Recommended'):
    recommendations = recommend(x)
    for i in recommendations:
        st.write(i)
