from flask import Flask,render_template, request
import movie as m



app = Flask(__name__)



@app.route("/")
def movie():
    return render_template("index.html")

@app.route("/sub",methods =["GET",'POST'])
def submit():
    # HTML -> .py
    if request.method == "POST":
        user_movie_name = request.form["moviename"]
        recom_name = m.movie_recommend(user_movie_name)
        movies = recom_name
        return render_template("sub.html",movies_recomm = movies)
        


    

if __name__ == "__main__":
    app.run(debug=True)