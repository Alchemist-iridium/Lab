# Task 1: zipmap(key_list: list, value_list: list, override=False)

def zipmap(key_list: list, value_list: list, override=False):
    # If key_list is longer, append None to value_list to match lengths
    value_list.extend([None] * (len(key_list) - len(value_list)))
    
    if not override and len(key_list) != len(set(key_list)):
        return {}  # Return an empty dictionary if there are duplicate keys and override is False

    # Use map and dict to create the result
    key_value_pairs = map(lambda x, y: (x, y), key_list, value_list)
    return dict(key_value_pairs)

# Examples
print(zipmap(['a', 'b', 'c', 'd', 'e', 'f'], [1, 2, 3, 4, 5, 6]))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(zipmap([1, 2, 3, 2], [4, 5, 6, 7], True))  # {1: 4, 2: 7, 3: 6}
print(zipmap([1, 2, 3], [4, 5, 6, 7, 8]))  # {1: 4, 2: 5, 3: 6}
print(zipmap([1, 3, 5, 7], [2, 4, 6]))  # {1: 2, 3: 4, 5: 6, 7: None}

# Task 2: group_by(<f>, target_list: list)

def group_by(f, target_list: list):
    result = {}
    for item in target_list:
        key = f(item)  # Apply the function to each element to determine the group key
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result

# Examples
print(group_by(len, ["hi", "dog", "me", "bad", "good"]))  # {2: ["hi", "me"], 3: ["dog", "bad"], 4: ["good"]}

# Task 3: Implementing filter() using reduce()
from functools import reduce

def filter_with_reduce(predicate, target_list: list):
    return reduce(lambda acc, x: acc + [x] if predicate(x) else acc, target_list, [])

# Example
print(filter_with_reduce(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
print(filter_with_reduce(lambda x: len(x) > 3, ["hi", "hello", "world", "Python", "is", "great"]))  # ["hello", "world", "Python", "great"]
