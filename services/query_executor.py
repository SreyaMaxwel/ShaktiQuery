import time
from config.database import get_connection


def execute_query(query):
    conn = get_connection()
    cur = conn.cursor()

    start = time.perf_counter()

    cur.execute(query)

    rows = []
    columns = []

    if cur.description:
        columns = [desc[0] for desc in cur.description]
        rows = cur.fetchall()

    execution_time = round((time.perf_counter() - start) * 1000, 3)

    conn.commit()

    cur.close()
    conn.close()

    return rows, columns, execution_time
