def generous_pay(lamb):
    """
    Function to get the number of henchmen getting paid if the commander is as generous as possible.
    :param lamb:
    :return: number of henchmen getting paid
    """
    # Rule 2 - A henchman will revolt if the person who ranks immediately above them gets more than double
    #     the number of LAMBs they do.
    # Because of this rule, this case becomes like a geometric series with common ratio=2.
    if lamb < 2:
        return lamb
    else:
        # Saving the number and sum of series as a list.
        l = [(1, 1)]
        while True:
            new = l[-1][0]*2
            l.append((new, l[-1][1]+new))
            if l[-1][1] > lamb:
                break
        l = l[:-1]
        final_sum = l[-1][1]
        remaining = lamb - final_sum
        if len(l) >= 2:
            # If the remaining amount follows rule 3, 1 more henchman can be paid.
            if remaining > l[-1][1] + l[-2][1]:
                return len(l) + 1
        return len(l)

def stingy_pay(lamb):
    """
    Function to get the number of henchmen getting paid if the commander is as stingy as possible.
    :param lamb:
    :return: number of henchmen getting paid
    """
    # Rule 3 - A henchman will revolt if the amount of LAMBs given to their next two subordinates combined is more
    # than the number of LAMBs they get.
    # Because of this rule, this case becomes like a Fibonacci series.
    if lamb <= 2:
        return lamb
    else:
        # Saving the number and sum of series as a list.
        fib = [(1, 1), (1, 2)]
        while True:
            num_1, sum_1 = fib[-1]
            num_2, _ = fib[-2]
            fib.append((num_1 + num_2, sum_1 + num_1 + num_2))
            final_sum = fib[-1][1]
            if final_sum > lamb:
                break
        fib = fib[:-1]
        return len(fib)

def solution(total_lambs):
    """
    Function to get the difference between the minimum and maximum number of henchmen who can share the LAMBs
    :param total_lambs:
    :return: difference
    """
    return stingy_pay(total_lambs) - generous_pay(total_lambs)
