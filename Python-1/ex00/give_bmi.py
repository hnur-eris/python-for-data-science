import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    h_arr = np.array(height)
    w_arr = np.array(weight)
    bmi_value = w_arr / h_arr ** 2
    return bmi_value.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise TypeError("All BMI values must be integers or floats.")

    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")

    return [b > limit for b in bmi]
