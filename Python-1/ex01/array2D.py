import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        if not isinstance(family, list) \
             or not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("Input must be a list and 2 integer")
        if not all(len(i) == len(family[0]) for i in family):
            raise AssertionError("All elements must have the same length")
    except AssertionError as e:
        print(e)
        exit()
    arr = np.array(family)
    print(f"My shape is : {arr.shape}")
    print(f"My new shape is : {arr[start:end].shape}")
    return arr[start:end].tolist()
