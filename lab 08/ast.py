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


def union(setA, setB):
    if not is_set(setA) or not is_set(setB):   #if there is one that is not a set, exclude 
        return False
    
    x = setA + setB

    result = make_set(x)
    
    return result

#test union function

print(union([1,2],[2,3]))
print(union([],[2,3]))
print(union([1,1,1],[2,3]))
