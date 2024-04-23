def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    check if the letter.lower = to_swap lower
    check if letter is upper, switch to lower
    if letter is lower, switch to upper

    find the char and replace with lower
    .replace

    helloH
    aelloH
    aelloh
    Helloh

    return phrase.replace(to_swap.lower, to_swap.upper)
    """

    phrase_list = list(phrase)

    changed_list = []

    for char in phrase_list:
        if char.lower() == to_swap.lower():

            char = char.lower() if char == char.upper() else char.upper()

            changed_list.append(char)

    return "".join(changed_list)
