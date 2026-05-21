def two_sum(numbers, target):
    prevMap={}
    for i,n in enumerate(numbers):
        diff=target-n
        if diff in prevMap:
            return (prevMap[diff],i)
        prevMap[n]=i
    return