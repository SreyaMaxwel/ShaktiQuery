import time
from database import get_connection


def execute_query(query):

    conn = get_connection()
    cur = conn.cursor()

    start = time.time()

    cur.execute(query)

    rows = []

    if query.strip().lower().startswith("select"):
        rows = cur.fetchall()

    execution_time = (time.time() - start) * 1000

    conn.commit()

    cur.close()
    conn.close()

    return rows, execution_time
