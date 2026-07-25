import re
from config.database import get_connection


def get_execution_plan(query):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"EXPLAIN {query}")

    plan = [row[0] for row in cur.fetchall()]

    cur.close()
    conn.close()

    return plan


def parse_execution_plan(plan):

    execution_plan = "\n".join(plan)

    result = {
        "scan_type": None,
        "index_name": None,
        "startup_cost": None,
        "total_cost": None,
        "rows": None,
        "width": None,
        "recommendations": []
    }

    # Scan Type

    if "Index Scan" in execution_plan:
        result["scan_type"] = "Index Scan"

    elif "Seq Scan" in execution_plan:
        result["scan_type"] = "Sequential Scan"

    # Index Name

    match = re.search(r"Index Scan using (\S+)", execution_plan)

    if match:
        result["index_name"] = match.group(1)

    # Cost

    match = re.search(
        r"cost=(\d+\.\d+)\.\.(\d+\.\d+)",
        execution_plan
    )

    if match:
        result["startup_cost"] = float(match.group(1))
        result["total_cost"] = float(match.group(2))

    # Rows

    match = re.search(r"rows=(\d+)", execution_plan)

    if match:
        result["rows"] = int(match.group(1))

    # Width

    match = re.search(r"width=(\d+)", execution_plan)

    if match:
        result["width"] = int(match.group(1))

    return result
