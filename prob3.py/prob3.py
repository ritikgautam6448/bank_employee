def combo_strings(a, b):
    """
    Given two strings a and b, return a new string that is the concatenation of
    the shorter string followed by the longer string. If both strings are of
    equal length, return either one followed by the other.

    :param a: First string
    :param b: Second string
    :return: Concatenated string with shorter first
    """
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b