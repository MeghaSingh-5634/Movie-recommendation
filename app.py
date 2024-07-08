# import streamlit as st
# import pickle
# import pandas as pd
# import requests
# def fetch_poster(movie_id):
#     url = 'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-USA'.format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path
#
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#
#     recommend_movies = []
#     recommend_movies_poster = []
#
#     for i in distances[1:6]:  # sorting on the basis of 2nd number
#         movie_id = movies.iloc[i[0]].movie_id
#         recommend_movies.append(movies.iloc[i[0]].title)
#         recommend_movies_poster.append(fetch_poster(movie_id))
#     return recommend_movies , recommend_movies_poster
#
# movies_dict = pickle.load(open('movies_dict.pkl','rb'))
# similarity = pickle.load(open('similarity.pkl' , 'rb'))
# movies = pd.DataFrame(movies_dict)
# st.header("Movies Recommendation Model")
#
# movie_list = movies['title'].values
# selected_movie = st.selectbox(
#     "SELECT THE MOVIE FROM THE DROPDOWN",
#     movie_list
# )
#
# if st.button('Show Recommendation'):
#     names , poster = recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(names[0])
#         st.image(poster[0])
#     with col2:
#         st.text(names[1])
#         st.image(poster[1])
#
#     with col3:
#         st.text(names[2])
#         st.image(poster[2])
#     with col4:
#         st.text(names[3])
#         st.image(poster[3])
#     with col5:
#         st.text(names[4])
#         st.image(poster[4])

######3333333333333333333333333
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# API_KEY = '1d253f027a32914051707c5804a6b261'
# def fetch_movie_data(movie_name):
#     search_url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}'
#     response = requests.get(search_url)
#     data = response.json()
#     if data['results']:
#         return data['results'][0]
#     return None
#
# def fetch_recommendations(movie_id):
#     recommend_url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={API_KEY}'
#     response = requests.get(recommend_url)
#     data = response.json()
#     return data['results']
#
#
#
# def fetch_poster(movie_id):
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US'
#     data = requests.get(url).json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path
#
#
# def fetch_movie_id(movie_name):
#     url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}'
#     data = requests.get(url).json()
#     results = data['results']
#     if results:
#         return results[0]['id']
#     return None
#
#
# def fetch_recommendations_from_tmdb(movie_name):
#     movie_id = fetch_movie_id(movie_name)
#     if not movie_id:
#         return [], []
#
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={API_KEY}&language=en-US'
#     data = requests.get(url).json()
#     recommendations = data['results']
#
#     recommended_movies = []
#     recommended_posters = []
#
#     for movie in recommendations[:10]:  # Limiting to 5 recommendations
#         recommended_movies.append(movie['title'])
#         recommended_posters.append(fetch_poster(movie['id']))
#
#     return recommended_movies, recommended_posters
#
#
# def recommend(movie):
#     if movie in movies['title'].values:
#         index = movies[movies['title'] == movie].index[0]
#         distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#
#         recommended_movies = []
#         recommended_movies_posters = []
#
#         for i in distances[1:11]:
#             movie_id = movies.iloc[i[0]].movie_id
#             recommended_movies.append(movies.iloc[i[0]].title)
#             recommended_movies_posters.append(fetch_poster(movie_id))
#
#         return recommended_movies, recommended_movies_posters
#     else:
#         movie_data = fetch_movie_data(movie)
#         if movie_data:
#             recommendations = fetch_recommendations(movie_data['id'])
#             recommend_movies = [rec['title'] for rec in recommendations[:10]]
#             recommend_movies_poster = [fetch_poster(rec['id']) for rec in recommendations[:10]]
#             return recommend_movies, recommend_movies_poster
#         else:
#             return [], []
#         #return fetch_recommendations_from_tmdb(movie)
#
# st.header('Movies Recommender System')
# movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
#
# movie_list = movies['title'].values
# selected_movie = st.text_input("Type a movie name:", "")
#
# st.button('Show Recommendation'):
#     if selected_movie:
#         names, posters = recommend(selected_movie)
#
#         if names:
#             col1, col2, col3, col4, col5 = st.columns(5)
#             for i in range(5):
#                 with [col1, col2, col3, col4, col5][i]:
#                     st.text(names[i])
#                     st.image(posters[i])
#
#             col6, col7, col8, col9, col10 = st.columns(5)
#             for i in range(5, 10):
#                 with [col6, col7, col8, col9, col10][i - 5]:
#                     st.text(names[i])
#                     st.image(posters[i])
#333333333333333333333333333
import streamlit as st
import pickle
import pandas as pd
import requests

# Load your data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# TMDb API key
API_KEY = '1d253f027a32914051707c5804a6b261'


def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US'
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
        return full_path
    return None


def fetch_movie_data(movie_name):
    search_url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}'
    response = requests.get(search_url).json()
    if response['results']:
        return response['results'][0]  # Return the first search result
    return None


def fetch_recommendations(movie_id):
    recommend_url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={API_KEY}'
    response = requests.get(recommend_url).json()
    return response['results']


def recommend(movie):
    if movie in movies['title'].values:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommend_movies = []
        recommend_movies_poster = []
        for i in distances[1:6]:  # Get top 5 recommendations excluding the movie itself
            movie_id = movies.iloc[i[0]].movie_id
            recommend_movies.append(movies.iloc[i[0]].title)
            recommend_movies_poster.append(fetch_poster(movie_id))
        return recommend_movies, recommend_movies_poster


#Streamlit app
st.header("Movies Recommendation Model")
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "SELECT THE MOVIE FROM THE DROPDOWN",
    movie_list
)
if st.button('Show Recommendation'):
    names , poster = recommend(selected_movie)
    if selected_movie:
        names, posters = recommend(selected_movie)

        if names:
            col1, col2, col3, col4, col5 = st.columns(5)
            for i in range(5):
                with [col1, col2, col3, col4, col5][i]:
                    st.text(names[i])
                    st.image(posters[i])
        else:
            st.write("No recommendations found.")
    else:
        st.write("Please enter a movie name.")

#3333333333333333333333333
#-------------------------
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# # Load your data
# movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
#
# # TMDb API key
# API_KEY = '1d253f027a32914051707c5804a6b261'
#
# def fetch_poster(movie_id):
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US'
#     data = requests.get(url).json()
#     poster_path = data.get('poster_path')
#     if poster_path:
#         full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
#         return full_path
#     return None
#
# def fetch_movie_data(movie_name):
#     search_url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}'
#     response = requests.get(search_url).json()
#     if response['results']:
#         return response['results'][0]  # Return the first search result
#     return None
#
# def fetch_recommendations(movie_id):
#     recommend_url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={API_KEY}'
#     response = requests.get(recommend_url).json()
#     return response['results']
#
# def fetch_movie_details(movie_name):
#     movie_data = fetch_movie_data(movie_name)
#     if movie_data:
#         details_url = f'https://api.themoviedb.org/3/movie/{movie_data["id"]}?api_key={API_KEY}&language=en-US'
#         details_response = requests.get(details_url).json()
#         title = details_response['title']
#         genres = [genre['name'] for genre in details_response['genres']]
#         return title, genres
#     return None, None
#
# def recommend(movie):
#     if movie in movies['title'].values:
#         index = movies[movies['title'] == movie].index[0]
#         distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#         recommend_movies = []
#         recommend_movies_poster = []
#         for i in distances[1:6]:  # Get top 10 recommendations excluding the movie itself
#             movie_id = movies.iloc[i[0]].movie_id
#             recommend_movies.append(movies.iloc[i[0]].title)
#             recommend_movies_poster.append(fetch_poster(movie_id))
#         return recommend_movies, recommend_movies_poster
#     else:
#         movie_data = fetch_movie_data(movie)
#         if movie_data:
#             recommendations = fetch_recommendations(movie_data['id'])
#             recommend_movies = []
#             recommend_movies_poster = []
#             for rec in recommendations:
#                 recommend_movies.append(rec['title'])
#                 recommend_movies_poster.append(fetch_poster(rec['id']))
#             return recommend_movies, recommend_movies_poster
#         else:
#             return [], []
#
# # Streamlit app
# st.header("Movies Recommendation Model")
#
# selected_movie = st.text_input("Type a movie name:", "")
#
# if st.button('Show Recommendation'):
#     if selected_movie:
#         names, posters = recommend(selected_movie)
#
#         if names:
#             col1, col2, col3, col4, col5 = st.columns(5)
#             for i in range(5):
#                 with [col1, col2, col3, col4, col5][i]:
#                     st.text(names[i])
#                     st.image(posters[i])
#
#
#         else:
#             st.write("No recommendations found.")
#     else:
#         st.write("Please enter a movie name.")
#-------------------------------------------
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# # Function to fetch poster from TMDb
# def fetch_poster(movie_id):
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US'
#     response = requests.get(url)
#     data = response.json()
#     if 'poster_path' in data:
#         poster_path = data['poster_path']
#         full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
#         return full_path
#     else:
#         return None
#
# # Function to fetch movie details from TMDb
# def fetch_movie_details(movie_name):
#     url = f'https://api.themoviedb.org/3/search/movie?api_key=YOUR_API_KEY&query={movie_name}'
#     response = requests.get(url)
#     data = response.json()
#     if data['results']:
#         movie = data['results'][0]
#         return movie['id'], movie['title']
#     else:
#         return None, None
#
# # Function to recommend movies
# def recommend(movie, movies_dict, similarity):
#     if movie in movies_dict['title'].values:
#         index = movies_dict[movies_dict['title'] == movie].index[0]
#         distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#         recommended_movies = []
#         recommended_movies_posters = []
#         for i in distances[1:6]:
#             movie_id = movies_dict.iloc[i[0]].movie_id
#             recommended_movies.append(movies_dict.iloc[i[0]].title)
#             recommended_movies_posters.append(fetch_poster(movie_id))
#         return recommended_movies, recommended_movies_posters
#     else:
#         # Fetch new movie details and recommend
#         movie_id, movie_title = fetch_movie_details(movie)
#         if movie_id:
#             # Use some logic to find similar movies to the new movie
#             # This part depends on how you define similarity for new movies
#             recommended_movies = ['New Movie 1', 'New Movie 2', 'New Movie 3', 'New Movie 4', 'New Movie 5']
#             recommended_movies_posters = [fetch_poster(movie_id)] * 5
#             return recommended_movies, recommended_movies_posters
#         else:
#             return [], []
#
# # Load your data
# movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))
# movies_dict = pd.DataFrame(movies_dict)
# st.header("Movies Recommendation System")
#
# movie_list = movies_dict['title'].values
# selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)
#
# if st.button('Show Recommendation'):
#     names, posters = recommend(selected_movie, movies_dict, similarity)
#     if names:
#         col1, col2, col3, col4, col5 = st.columns(5)
#         with col1:
#             st.text(names[0])
#             st.image(posters[0])
#         with col2:
#             st.text(names[1])
#             st.image(posters[1])
#         with col3:
#             st.text(names[2])
#             st.image(posters[2])
#         with col4:
#             st.text(names[3])
#             st.image(posters[3])
#         with col5:
#             st.text(names[4])
#             st.image(posters[4])
#     else:
#         st.write("Movie not found!")

#444444444444444444444444444444444


import streamlit as st
# import pickle
# import pandas as pd
# import requests
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.feature_extraction.text import CountVectorizer
#
# # Load your data
# movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
#
# # TMDb API key
# API_KEY = '1d253f027a32914051707c5804a6b261'
#
#
# def fetch_movie_data(movie_name):
#     search_url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}'
#     response = requests.get(search_url).json()
#     if response['results']:
#         return response['results'][0]  # Return the first search result
#     return None


# def fetch_movie_details(movie_id):
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US'
#     data = requests.get(url).json()
#     return data
#
#
# def fetch_poster(movie_id):
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US'
#     data = requests.get(url).json()
#     poster_path = data.get('poster_path')
#     if poster_path:
#         full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
#         return full_path
#     return None
#
#
# def create_similarity_matrix(movies):
#     count_vectorizer = CountVectorizer(stop_words='english')
#     count_matrix = count_vectorizer.fit_transform(movies['tags'])
#     similarity_matrix = cosine_similarity(count_matrix, count_matrix)
#     return similarity_matrix
#
#
# similarity = create_similarity_matrix(movies)
#
#
# def recommend(movie):
#     if movie in movies['title'].values:
#         index = movies[movies['title'] == movie].index[0]
#         distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#         recommend_movies = []
#         recommend_movies_poster = []
#         for i in distances[1:6]:  # Get top 5 recommendations excluding the movie itself
#             movie_id = movies.iloc[i[0]].movie_id
#             recommend_movies.append(movies.iloc[i[0]].title)
#             recommend_movies_poster.append(fetch_poster(movie_id))
#         return recommend_movies, recommend_movies_poster
#     else:
#         movie_data = fetch_movie_data(movie)
#         if movie_data:
#             movie_details = fetch_movie_details(movie_data['id'])
#             genres = " ".join([genre['name'] for genre in movie_details['genres']])
#             overview = movie_details['overview']
#             tags = genres + " " + overview
#             recommendations = find_similar_movies(tags)
#             recommend_movies = [rec['title'] for rec in recommendations[:5]]
#             recommend_movies_poster = [fetch_poster(rec['movie_id']) for rec in recommendations[:5]]
#             return recommend_movies, recommend_movies_poster
#         else:
#             return [], []
#
#
#
# def find_similar_movies(tags):
#     count_vectorizer = CountVectorizer(stop_words='english')
#     tags_series = movies['tags'].append(pd.Series([tags]), ignore_index=True)
#     count_matrix = count_vectorizer.fit_transform(tags_series)
#     similarity_matrix = cosine_similarity(count_matrix, count_matrix)
#     similar_indices = similarity_matrix[-1][:-1].argsort()[::-1][:10]
#     return movies.iloc[similar_indices].to_dict('records')
#
#
#
# # Streamlit app
# st.header("Movies Recommendation Model")
#
# selected_movie = st.text_input("Type a movie name:", "")
#
# if st.button('Show Recommendation'):
#     if selected_movie:
#         names, posters = recommend(selected_movie)
#
#         if names:
#             for i in range(0, len(names), 5):
#                 cols = st.columns(5)
#                 for j in range(5):
#                     if i + j < len(names):
#                         with cols[j]:
#                             st.text(names[i + j])
#                             st.image(posters[i + j])
#         else:
#             st.write("No recommendations found.")
#     else:
#         st.write("Please enter a movie name.")


