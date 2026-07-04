def analyze_query(query):
    recommendations = []

    query_lower = query.lower()

    if "select *" in query_lower:
        recommendations.append(
            "Avoid using SELECT *. Fetch only the required columns."
        )

    if "where" in query_lower:
        recommendations.append(
            "Consider creating indexes on columns used in WHERE clauses."
        )

    if "order by" in query_lower:
        recommendations.append(
            "Ensure ORDER BY columns are indexed."
        )

    if "like '%" in query_lower:
        recommendations.append(
            "Leading wildcard searches may prevent index usage."
        )

    if not recommendations:
        recommendations.append(
            "No optimization suggestions for this query."
        )

    return recommendations
