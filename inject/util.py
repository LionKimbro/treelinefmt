"""util.py  -- various general utility functions

find_dict(L, key, val)  -- return first dictionary with match
"""


def find_dict(L, key, val, default=None):
    """Find first matching dictionary in a list of dictionaries.

    :param L: list of dictionaries
    :type L: list of dictionaries
    :param key: key to match for value
    :type key: valid dictionary key to index on
    :param val: value to compare against
    :type val: any
    :return: the matched dictionary, or None (if nothing found)
    :rtype: dictionary or None
    """
    return next((D for D in L if D[key] == val), default)

