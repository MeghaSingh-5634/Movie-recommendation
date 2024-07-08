# Content-Based Movie Recommendation System

This project is a Content-Based Movie Recommendation System built using Streamlit. The system recommends movies to users based on the content of movies they have liked in the past. It utilizes metadata such as genre, director, cast, and plot to generate recommendations.

## Features

Interactive User Interface: Built with Streamlit for an interactive and user-friendly experience.
Content-Based Filtering: Recommends movies based on metadata similarity.
Search Functionality: Allows users to search for movies and get 5 recommendations.

## How to run the project?
1. Clone or download this repository to your local machine.<br>
2. Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt <br>
3. Get your API key from https://www.themoviedb.org/. <br>
4. Replace YOUR_API_KEY in all the places of app.py file and hit save. <br>
5. Open your terminal/command prompt from your pycharm and run "streamlit run app.py" . <br>
Hurray! That's it.

## Similarity Score :
How does it decide which item is most similar to the item user likes? Here come the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

## How Cosine Similarity works?
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

![cosine](https://github.com/MeghaSingh-5634/Movie-recommendation/assets/147227266/8b57c67a-6e13-4a12-94ed-9130681a309b)

## Source of the datasets
IMDB 5000 Movie Dataset from Kaggle

## Preview of Project
![pro](https://github.com/MeghaSingh-5634/Movie-recommendation/assets/147227266/0146327a-d11e-4f04-8431-5e680e1cf72f)

