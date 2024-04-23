def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}

        loop through every letter in phrase
        if it exists, add 1
        else, set it equal to 1

        value in dictionary || 0
        +1


    """

    dict = {}

    for ltr in phrase:
        dict[ltr] = dict.get(ltr, 0)+1

    return dict
