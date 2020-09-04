def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    if length <= 1:
        return None

    cache = {}
    pairs = []
   
    for i in range(length):
        cache[weights[i]] = i
    # print(cache)
    for i in range(length):
        diff = limit - weights[i] 
      
        if diff in cache:
         
            pairs.append([max(i, cache[diff]), min(i, cache[diff])])

    return pairs[0]

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
print(answer_4)

weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
print(answer_2)
