def solution(n):
    """
    Function to get the minimum number of operations needed to transform the number of pellets to 1
    :param n:
    :return:
    """
    n = int(n)
    num_ops = 0
    while n!=1:
        if n%2 == 0:
            n = int(n/2)
            num_ops += 1
        elif (n+1) % 4 == 0:
            if n == 3:
                n -= 1
                num_ops += 1
            else:
                n += 1
                num_ops += 1
        else:
            n -= 1
            num_ops += 1
    return num_ops