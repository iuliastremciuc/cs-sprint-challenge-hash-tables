def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    
    result = []
    for array in arrays:
        for a in array:
            if a not in cache:
                cache[a] = 1
            else:
                cache[a] += 1
    # print(cache)  
    k = len(arrays)
    for key, value in cache.items():
        if value == k:
            result.append(key)
  

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
