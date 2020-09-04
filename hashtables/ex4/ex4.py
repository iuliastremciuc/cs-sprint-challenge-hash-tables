def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for i in a:
        if i not in cache and i != 0:        
            cache[i] = 0
        if -i in cache:
            
            # if i != 0:
            result.append(abs(i))
        
    # print(cache)            

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
