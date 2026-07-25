def calculate_health_score(query, plan_info):

    score = 100

    query_lower = query.lower()

    # Penalize SELECT *
    if "select *" in query_lower:
        score -= 10

    # Penalize Sequential Scan
    if plan_info["scan_type"] == "Sequential Scan":
        score -= 30

    # Reward Index Scan
    elif plan_info["scan_type"] == "Index Scan":
        score += 10

    # Penalize expensive plans
    if plan_info["total_cost"]:

        if plan_info["total_cost"] > 100:
            score -= 20

        elif plan_info["total_cost"] > 50:
            score -= 10

    # Penalize queries without WHERE clause
    if "where" not in query_lower:
        score -= 10

    score = max(0, min(100, score))

    return score
