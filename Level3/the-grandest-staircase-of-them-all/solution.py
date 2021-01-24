def solution(n):
    """
    Function to give the number of unique staircases that can be built from exactly 'n' bricks using DP
    :param n: the number of bricks to be used
    :return: the number of unique staircases
    """
    counts = [[0 for i in range(n)] for k in range(n)]
    # matrix 'counts' stores the number of unique staircases that can be built using (i+1) bricks that have at most
    # (k+1) bricks in the highest step.
    for k in range(n):
        for i in range(n):
            if i==0:
                if k == 0:
                    counts[k][i] = 1
            else:
                if k > i:
                    new_counts = counts[k-i-1][i-1]
                elif k==i:
                    new_counts = 1
                else:
                    new_counts = 0
                counts[k][i] = counts[k][i-1] + new_counts
    return counts[-1][-1]-1