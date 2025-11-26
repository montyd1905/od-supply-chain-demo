from typing import List
import math
from math import log10


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate great-circle distance between two points on Earth.
    Returns distance in kilometers.
    """
    R = 6371.0  # Earth radius in km

    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Correct Haversine formula
    a = (math.sin(dlat/2)**2 +
         math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def quantitative_factor(ref: float = 0.00, i: float = 0.00) -> float:
    """

    Compute a quantitative POS factor in a user POS search

    :param ref: the reference value of the factor (supplied by user)
    :param i: the current dynamic value of the factor (supplied by POS provider)
    :return: a float representing the match distance
    """

    if ref and i:
        if ref != i:
            sub = (ref, i)
            _min, _max = min(sub), max(sub)
            return log10(_min)/log10(_max)
        else:
            return 1.00
    else:
        return 0.00


def categorical_factor(ref: str, i: str) -> int:
    """

    Compute a categorical (binary) POS factor in a user POS search

    :param ref: the reference value of the factor (supplied by user)
    :param i: the current dynamic value of the factor (supplied by POS provider)
    :return: an int (1 or 0) representing the boolean match
    """

    if ref and i:
        return int(ref == i)
    else:
        return 0


def sum_qf(ref_arr: List[float], i_arr: List[float]) -> float:
    """

    Gives the sum of quantitative factors of a user search

    :param ref_arr: array of user quantitative inputs
    :param i_arr: array of corresponding POS quantitative inputs
    :return: single float representing the quantitative match component of POS quality
    """

    return sum(map(lambda _: quantitative_factor(*_), zip(ref_arr, i_arr)))


def sum_cf(ref_arr: List[str], i_arr: List[str]) -> int:
    """

    Gives the sum of categorical factors of a user search

    :param ref_arr: array of user categorical inputs
    :param i_arr: array of corresponding POS categorical inputs
    :return: single integer representing the categorical match component of POS quality
    """

    return sum(map(lambda _: categorical_factor(*_), zip(ref_arr, i_arr)))

