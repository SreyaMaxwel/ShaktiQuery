def analyze_query(query):

    recommendations = []

    q = query.lower()

    if "select *" in q:
        recommendations.append(
            "Avoid SELECT *. Retrieve only required columns."
        )

    if "where" in q:
        recommendations.append(
            "Consider indexing columns used in WHERE clauses."
        )

    if "order by" in q:
        recommendations.append(
            "Ensure ORDER BY columns are indexed."
        )

    if "like '%" in q:
        recommendations.append(
            "Leading wildcard searches may cause full table scans."
        )

    return recommendations
