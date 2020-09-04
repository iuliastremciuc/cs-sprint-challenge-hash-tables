# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    cache = {}

    for f in files:
        path = f.split('/')[-1]
        # print(path)
        if path not in cache:
            cache[path] = 0
    # print(cache)
        for q in queries:
            if q in cache:
                cache[q] = 1
    # print(cache)
        for k in cache.items():
            if k[-1] > 0 and k[0] in path:
                
                result.append(f)
    

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
