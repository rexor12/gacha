import math

RELATIVE_TOLERANCE = 1e-5

def isclose(a: float, b: float):
    return math.isclose(a, b, rel_tol=RELATIVE_TOLERANCE)