def make_set(data):
    n = len(data)
    i = 0

    while i < len(data):
        x = data[i]
        j = i + 1
        while j < len(data):
            if data[j] == x:
                del(data[j])  # Delete the duplicate
            else:
                j += 1  # Only increment if no deletion occurs
        i += 1  # Increment the outer loop index

    return(data)

# Test the make set function
print("\ntest for make set function\n")
print("The set for the data is", make_set([1, 2, 3, 4, 4, 4, 5, 5]))


def is_set(data):
    if data == None:
        return False    # none returns false

    if len(data) == 0:
        return True     # empty returns true
    
    i = 0   # initialize i

    while i < len(data):
        x = data[i]
        j = i + 1
        while j < len(data):
            if data[j] == x:
                return False  # If there is a duplicate, return false
            else:
                j += 1  # go check next one
        i += 1  # Increment the outer loop index

    return True

# test is data function
print("\ntest for is set function\n")
print(is_set([1,2,3,4]))
print(is_set([5,5]))
print(is_set([]))
print(is_set(None))


def union(setA, setB):
    if not is_set(setA) or not is_set(setB):   #if there is one that is not a set, exclude 
        return False
    
    x = setA + setB

    result = make_set(x)
    
    return result

#test union function
print("\ntest for union function\n")
print(union([1,2],[2,3]))
print(union([],[2,3]))
print(union([1,1,1],[2,3]))


def intersection(setA, setB):
    if not is_set(setA) or not is_set(setB):   #if there is one that is not a set, exclude 
        return False

    result = [] #initialize the result set
    for item in setA:
        if item in setB and item not in result:
            result.append(item)
    return result

#test for intersection
print("\ntest for intersection function\n")
print(intersection((1,2),[2,3]))
print(intersection([],[2,3]))
print(intersection([1,1,1],[2,3]))