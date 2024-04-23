def multiply_even_numbers(nums):
    """Multiply the even numbers.

        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48

        >>> multiply_even_numbers([3, 4, 5])
        4

    If there are no even numbers, return 1.

        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    total = 1

    # loop through all the numbers
    for num in nums:
        # check if the number is even
        if num % 2 == 0:
            total *= num
    # if it is, multiply to a running total

    # return the total

    return total
