from flask import Flask, request
from flask_cors import CORS
import pandas as pd
import pickle

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "Add '/api/Track Title With Spaces Between Words' to end of Heroku app URL in address field. Or, for HTML-compliance, '/api/Track%20Title%20With..."


@app.route('/api/<track_title>')
def get_track_recomm(track_title):
    pkl_file = open('track_titles_word2vec.pkl', 'rb')  # pickle file with trained model from AWS SageMaker
    word2vec_model = pickle.load(pkl_file)

    df = pd.read_csv('mood-title-tags-artists.csv')

    # print('first 5 lines of df:', df.head())
    track_words = track_title.split('%20')  # creates a list with one string
    track_words = track_words.pop(0)  # removes string from list
    track_words = track_words.split(' ')  # creates list with 1+ string
    # print('track_words is:', track_words)
    # print('type of track_words is:', type(track_words))
    track_recomm_list = []
    for word in track_words[:2]:
        try:
            output_list = word2vec_model.wv.most_similar(word, topn=1)
            print('\noutput_list is:', output_list)
            output_word = output_list[0][0]
            track_recomm = df.loc[df['title'].str.contains(output_word)]['title'].values
            artist_recomm = df.loc[df['title'].str.contains(output_word)]['artist_name'].values
            track_recomm = list(zip(track_recomm, artist_recomm))
            track_recomm_list.append(track_recomm)
            print('mood of track_recomm is:', \
                  df[df['title'].str.contains(output_word)]['mood'].values)

        except Exception as e:
            print(e, 'occurred.', word, 'not found in title vocabulary.')
            continue
    print('track_recomm_list is:', track_recomm_list)
    print('type of track_recomm_list is:', type(track_recomm_list))
    return pd.Series(track_recomm_list).to_json()


if __name__ == '__main__':
    app.run(debug=True)
