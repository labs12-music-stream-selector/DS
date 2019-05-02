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
def get_mood(track_title):
    pkl_file = open('track_titles_word2vec.pkl', 'rb')
    word2vec_model = pickle.load(pkl_file)

    # pkl_file2 = open('recomm_by_title.pkl', 'rb') -- errored out
    # recomm_by_title = pickle.load(pkl_file2)
    df = pd.read_csv('mood-title-tags-artists.csv')

    # print('first 5 lines of df:', df.head())
    track_words = track_title.split('%20')  # creates a list with one string
    track_words = track_words.pop(0)  # removes string from list
    track_words = track_words.split(' ')  # creates list with 1+ string
    # print('track_words is:', track_words)
    # print('type of track_words is:', type(track_words))
    mood_string = ''
    for word in track_words[:2]:
        try:
            output_list = word2vec_model.wv.most_similar(word, topn=1)
            print('output_list is:', output_list)
            output_word = output_list[0][0]
            mood = df.loc[df['title'].str.contains(word)]['mood'].values
            mood = str(mood)
            mood_string += mood
        except Exception as e:
            print(e, 'occurred.', word, 'not found in title vocabulary.')
            continue
    print(mood_string)
    return mood_string
    # r = pd.Series(recomm_by_title()).to_json()
    # print(r)


if __name__ == '__main__':
    app.run(debug=True)
