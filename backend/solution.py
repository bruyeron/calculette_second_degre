import math

def solution_sec_degree(a: int, b:int, c:int) -> dict:
    """
    Resolution de l'equation du second degre avec a, b et c des entiers
    """

    if not all(isinstance(coef, int) and not isinstance(coef, bool) for coef in (a,b,c)):
        raise TypeError("Les coefficients doivent etre positif (a, b et c).")

    if a == 0:
        raise ValueError("'a' ne peux pas etre nul.")

    delta = (b ** 2) - (4 * a * c)

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return {
            "delta": delta,
            "status": "Delta positif",
            "message": "Deux solutions réelles distinctes.",
            "roots": [x1, x2],
        }

    if delta == 0:
        x0 = -b / (2 * a)
        return {
            "delta": delta,
            "status": "Delta egale a zero",
            "message": "Une solution réelle unique.",
            "roots": [x0],
        }

    return {
        "delta": delta,
        "status": "Delta negative",
        "message": "Pas de solution réelle",
        "roots": [],
    }