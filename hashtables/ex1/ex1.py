weights = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21


def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    
    """
    
    map = {}

    for i in range(len(weights)):
        map[weights[i]] = i

    for i in range(len(weights)):
        lw = limit - weights[i]

        if lw in map:
            return ([max(i, map[lw]), min(i, map[lw])])

    return None


print(get_indices_of_item_weights(weights, length, limit))