from flask import Flask, render_template, request
from config.database import get_connection
from services.query_executor import (
    execute_query,
    save_query_history
)
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
            save_query_history(
    query,
    execution_time,
    len(rows)
)

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

@app.route("/history")
def history():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM query_history
        ORDER BY executed_at DESC
    """)

    history = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "history.html",
        history=history
    )
if __name__ == "__main__":
    app.run(debug=True)
