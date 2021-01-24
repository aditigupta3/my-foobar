def solution(l):
    """
    Function to find the largest number that can be made from some or all of these digits in l and is divisible by 3.
    :param l: list
    :return:
    """
    l = sorted(l, reverse=True)
    sum_ = sum(l)
    to_remove = list() # to carry the numbers that need to be removed

    # If the remainder upon division by 3 is 1
    if sum_ % 3 == 1:
        # remove the smallest number which gives the same remainder
        for i, int_ in enumerate(reversed(l)):
            if int_ % 3 == 1:
                to_remove.append(len(l)-i-1)
                break
        # if no such number found,
        if len(to_remove) == 0:
            # remove the smallest 2 numbers which give the remainder 2
            for i, int_ in enumerate(reversed(l)):
                if int_ % 3 == 2:
                    to_remove.append(len(l)-i-1)
                    if len(to_remove) == 2:
                        break
            if len(to_remove) < 2:
                return 0

    # If the remainder upon division by 3 is 1
    elif sum_ % 3 == 2:
        # remove the smallest number which gives the same remainder
        for i, int_ in enumerate(reversed(l)):
            if int_ % 3 == 2:
                to_remove.append(len(l)-i-1)
                break
        # if no such number found,
        if len(to_remove) == 0:
            # remove the smallest 2 numbers which give the remainder 1
            for i, int_ in enumerate(reversed(l)):
                if int_ % 3 == 1:
                    to_remove.append(len(l)-i-1)
                    if len(to_remove) == 2:
                        break
            if len(to_remove) < 2:
                return 0

    largest = 0
    for i, int_ in enumerate(l):
        if i not in to_remove:
            largest = largest*10 + int_
    return largest
