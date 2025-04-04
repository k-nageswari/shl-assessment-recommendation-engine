from flask import Flask, request, render_template
from recommender.recommender import recommend_assessments

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form["query"]
        results = recommend_assessments(query)
        results_html = results.to_html(classes="table table-bordered table-striped", index=False)
        return render_template("results.html", tables=[results_html])
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
