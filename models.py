from math import log10


def quantitative_factor(ref: float = 0.00, i: float = 0.00) -> float:
    """

    Compute a quantitative POS factor in a user POS search

    :param ref: the reference value of the factor (supplied by user)
    :param i: the current dynamic value of the factor (supplied by POS provider)
    :return: a float representing the match distance
    """

    if ref and i:
        sub = (ref, i)
        _min, _max = min(sub), max(sub)
        return log10(_min)/log10(_max)
    else:
        return 0.00

