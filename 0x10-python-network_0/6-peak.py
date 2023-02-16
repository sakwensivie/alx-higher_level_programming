#!/usr/bin/python3


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    """
    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return max(list_of_integers)

    mid = n // 2
    if list_of_integers[mid] < list_of_integers[mid-1]:
        # Search left half
        return find_peak(list_of_integers[:mid])
    elif list_of_integers[mid] < list_of_integers[mid+1]:
        # Search right half
        return find_peak(list_of_integers[mid+1:])
    else:
        # Found a peak
        return list_of_integers[mid]
