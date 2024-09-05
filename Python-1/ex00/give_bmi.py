import numpy as np


def control(height: list, weight: list):
    if height.__class__ .__name__ != "list" or \
         weight.__class__ .__name__ != "list":
        raise ValueError("Both height and weight must be lists.")
    if not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("All height values must be integers or floats.")

    if not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("All weight values must be integers or floats.")

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    try:
        control(height, weight)
    except TypeError as e:
        print(e)
        exit()
    except ValueError as e:
        print(e)
        exit()

    h_arr = np.array(height)
    w_arr = np.array(weight)
    bmi_value = w_arr / h_arr ** 2
    return bmi_value.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        if not all(isinstance(b, (int, float)) for b in bmi):
            raise TypeError("All BMI values must be integers or floats.")

        if not isinstance(limit, int):
            raise TypeError("Limit must be an integer.")
    except TypeError as e:
        print(e)
        exit()
    return [b > limit for b in bmi]
