def check_repeats(string, repeated):
    """
    Function to check if string 'string' is a repetition of the string 'repeated'
    Time Complexity: O(n) where n is the length of the 'string'
    :param string:
    :param repeated:
    :return: True if the repeats can be done, else False
    """
    if string[0] != repeated[0]:
        return False
    else:
        num_repeats = len(string)/len(repeated)
        if int(num_repeats) != num_repeats:
            return False
        else:
            for i in range(int(num_repeats)):
                if string[i*len(repeated):(i+1)*len(repeated)] != repeated:
                    return False
            return True


def solution(string):
    """
    Function to give the maximum number of equal parts in which the string can be divided
    with no left-overs.
    Time Complexity: O(n**2) where n is the length of the 'string'
    :param string: input string
    :return: number of equal parts
    """
    if len(string) == 0:
        return 0

    # initialise the repeated string with the first character
    repeated = string[:1]
    for i in range(1, len(string)):
        # If the remaining string is not a repetition of the 'repeated' string
        if not check_repeats(string[i:], repeated):
            # increase the span of the 'repeated' string
            repeated += string[i]
        else:
            return int(len(string)/len(repeated))
    return 1
