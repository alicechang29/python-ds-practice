def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
    counter = {}
    for elem in word:
        if elem.lower() in counter:
            counter[elem.lower()] += 1
        else:
            counter[elem.lower()] = 1

    return counter.get(letter.lower(), 0)

    # return word.lower().count()
    # how count fn works: iterable.count(element)
