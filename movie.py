import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def movie_recommend(user_movie_name):
    # loading the data from the csv file to apandas dataframe
    movies_data = pd.read_csv('movies.csv')

    # selecting the relevant features for recommendation
    selected_features = ['genres','keywords','tagline','cast','director']

    # replacing the null valuess with null string
    for feature in selected_features:
        movies_data[feature] = movies_data[feature].fillna('')

    # combining all the 5 selected features
    combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
    
    # converting the text data to feature vectors
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(combined_features)

    # getting the similarity scores using cosine similarity
    similarity = cosine_similarity(feature_vectors)


    #movie_name = input(' Enter your favourite movie name : ')
    # getting the movie name from the user
    movie_name = user_movie_name

    # creating a list with all the movie names given in the dataset
    list_of_all_titles = movies_data['title'].tolist()

    # finding the close match for the movie name given by the user
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    close_match = find_close_match[0]

    # finding the index of the movie with title
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

    # getting a list of similar movies
    similarity_score = list(enumerate(similarity[index_of_the_movie]))

    # sorting the movies based on their similarity score
    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 

    #print('Movies suggested for you : \n')

    i = 1
    movie_recom = []
    # print the name of similar movies based on the index
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies_data[movies_data.index==index]['title'].values[0]
        if i<32:
            movie_recom.append(title_from_index)
            #print(i, '.',title_from_index)
            i+=1
    movie_recom.pop(0)
    return movie_recom


