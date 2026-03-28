def calculate_confidence(output):
    score = 0.5

    if output and len(output) > 20:
        score += 0.2

    if "error" not in output.lower():
        score += 0.2

    return min(score, 1.0)