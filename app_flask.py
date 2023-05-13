import flask
import movie as m



app = flask.Flask(__name__)



@app.route("/")
def movie():
    return flask.render_template("index.html")

@app.route("/sub",methods =["GET",'POST'])
def submit():
    # HTML -> .py
    if flask.request.method == "POST":
        user_movie_name = request.form["moviename"]
        recom_name = m.movie_recommend(user_movie_name)
        movies = recom_name
        return flask.render_template("sub.html",movies_recomm = movies)
        


    

if __name__ == "__main__":
    app.run(debug=True)
