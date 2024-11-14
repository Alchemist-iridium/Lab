#task 1
def product_of_digits(x):
    x=abs(x)
    if x < 10:
        return x
    else:
        # Recursive case: Multiply the last digit by the product of remaining digits
        return (x % 10) * product_of_digits(x // 10)

#test 1

print(product_of_digits(234))  # Output: 24
print(product_of_digits(12))   # Output: 2
print(product_of_digits(-12))  # Output: 2

#task 2

def array_to_string(a, index):
    # Base case: If index is at the last element, return that element as string
    if index == len(a) - 1:
        return str(a[index])
    else:
        # Recursive case: Return the current element and add comma + recursive call
        return str(a[index]) + "," + array_to_string(a, index + 1)

#test 2
print(array_to_string([1, 2, 3, 4], 0))  # Output: "1,2,3,4"
print(array_to_string([10, 20, 30], 0))  # Output: "10,20,30"

#task 3
def log(base, value):
    # Raise an error if base is <= 1 or value <= 0
    if base <= 1 or value <= 0:
        raise ValueError("Base must be greater than 1 and value must be greater than 0")
    
    # Base case: If value is less than base, return 0
    if value < base:
        return 0
    else:
        # Recursive case: Perform integer division and add 1 to the result
        return 1 + log(base, value // base)

#test 3
print(log(10, 123456))  # Output: 5
print(log(2, 64))       # Output: 6
print(log(10, 4567))    # Output: 3