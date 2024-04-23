def partition(lst, fn):
    """Partition lst by predicate.

     - lst: list of items
     - fn: function that returns True or False

     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0

        >>> def is_string(el):
        ...     return isinstance(el, str)

        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]

        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    true_lst = []
    false_lst = []

    # given a list, run the function on every value within the list
    for elem in lst:
        if fn(elem) is True:
            true_lst.append(elem)
        elif fn(elem) is False:
            false_lst.append(elem)

    return [true_lst, false_lst]

    # if the return is True, put it in a true list

    # if return is False, put it in false list

    # put both lists in a final list
