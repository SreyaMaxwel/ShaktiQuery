from flask import Flask, render_template, request

from services.query_executor import execute_query
from services.analyzer import analyze_query

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    rows = []
    columns = []
    execution_time = None
    recommendations = []
    error = None

    if request.method == "POST":

        query = request.form["query"]

        try:
            rows, columns, execution_time = execute_query(query)
            recommendations = analyze_query(query)

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        rows=rows,
        columns=columns,
        execution_time=execution_time,
        recommendations=recommendations,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
