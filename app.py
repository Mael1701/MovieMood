import os
import requests

from flask import Flask, flash, redirect, render_template, request, session
from tempfile import mkdtemp
from flask import flash


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/recommendations")
def recommendations():
    
    mood = request.args.get('mood')
    api_key = "9e37e2ce0c92d68ffc87c0f4f5821bd4"


    genre = ""
    if mood == 'happy':
        genre = '35'  # Comedy
    elif mood == 'sad':
        genre = '18'  # Drama
    elif mood == 'curious':
        genre = '99'
    elif mood == 'bored':
        genre = '27'  # Horror
    elif mood == 'angry':
        genre = '28'  # War
    elif mood == 'childish':
        genre = '16'  # Animation

    # Faire une requête à l'API pour obtenir une liste de films du genre correspondant
    response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=vote_average.desc&with_genres={genre}&vote_count.gte=1000")

    movie_data = response.json()

    # Renvoyer la page de recommandations avec les données des films
    return render_template("recommendations.html", movies=movie_data['results'])



if __name__ == '__main__':
    app.run(debug=True)
