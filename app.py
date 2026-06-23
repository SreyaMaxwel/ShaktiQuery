from flask import Flask, render_template, request

from query_executor import execute_query
from analyzer import analyze_query

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    execution_time = None
    recommendations = []

    if request.method == "POST":

        query = request.form["query"]

        rows, execution_time = execute_query(query)

        recommendations = analyze_query(query)

    return render_template(
        "index.html",
        execution_time=execution_time,
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)
