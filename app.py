from flask import Flask, render_template, request

from config.database import get_connection

from services.query_executor import (
    execute_query,
    save_query_history
)

from services.analyzer import analyze_query

from services.explain import (
    get_execution_plan,
    parse_execution_plan
)

from services.health_score import calculate_health_score


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    # Variables passed to the template
    rows = []
    columns = []
    execution_time = None
    recommendations = []
    error = None

    plan = []
    plan_info = None
    health_score = None

    if request.method == "POST":

        query = request.form["query"]

        try:

            # Execute SQL Query
            rows, columns, execution_time = execute_query(query)

            # Save query history
            save_query_history(
                query,
                execution_time,
                len(rows)
            )

            # Rule-based recommendations
            recommendations = analyze_query(query)

            # Get execution plan
            plan = get_execution_plan(query)

            # Parse execution plan
            plan_info = parse_execution_plan(plan)

            # Calculate health score
            health_score = calculate_health_score(
                query,
                plan_info
            )

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        rows=rows,
        columns=columns,
        execution_time=execution_time,
        recommendations=recommendations,
        plan=plan,
        plan_info=plan_info,
        health_score=health_score,
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
