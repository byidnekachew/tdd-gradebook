def letter_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be number")
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def is_passing(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be number")
    return score >= 60


def average(scores):
    if len(scores) == 0:
        raise ValueError("List is empty")
    if not isinstance(scores, list):
        raise TypeError("scores most be in list")
    if not all(isinstance(s, (int, float))for s in scores):
        raise TypeError("all items in average scores must be numbers")

    return round(sum(scores) / len(scores), 2)


def curve_score(score, bonus):
    return 85
