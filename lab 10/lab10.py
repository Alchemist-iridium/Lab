# Task 1: Functional Programming version of CaesarCipher
from functools import partial

def encrypt_char(shift, char):
    if char == ' ':
        return ' '
    if char.isalpha():
        if 'A' <= char <= 'Z':
            char = chr(ord(char) + 32)  # Change uppercase to lowercase
        return chr((ord(char) - 97 + shift) % 26 + 97)  # Shift letters within the letter range
    else:
        return chr((ord(char) + shift) % 1114112)  # Shift non-letter characters

def decrypt_char(shift, char):
    if char == ' ':
        return ' '
    if char.isalpha():
        if 'A' <= char <= 'Z':
            char = chr(ord(char) + 32)  # Change uppercase to lowercase
        return chr((ord(char) - 97 - shift) % 26 + 97)  # Reverse the shift for letters
    else:
        return chr((ord(char) - shift) % 1114112)  # Reverse the shift for non-letter characters

def caesar_cipher(text, shift, encrypt=True):
    if encrypt:
        return ''.join(map(partial(encrypt_char, shift), text))
    else:
        return ''.join(map(partial(decrypt_char, shift), text))

# Test the functional Caesar cipher
print(caesar_cipher("hello WORLD!", 3, encrypt=True))  # Prints "khoor zruog$"
print(caesar_cipher("KHOOR zruog$", 3, encrypt=False))  # Prints "hello world!"
print(caesar_cipher("zzz", 6, encrypt=True))  # Prints "fff"
print(caesar_cipher("FFF", 6, encrypt=False))  # Prints "zzz"
print(caesar_cipher("FFF", -6, encrypt=True))  # Prints "zzz"


# Task 2: Decorator for Cache/Memoization
import time
from functools import lru_cache

# Decorator for memoization using lru_cache
def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

# Original recursive Fibonacci function
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)

# Decorated Fibonacci function with caching
@memoize
def recur_fibo_memoized(n):
    if n <= 1:
        return n
    else:
        return recur_fibo_memoized(n-1) + recur_fibo_memoized(n-2)

# Comparison of execution speed for n = 35
n = 35

# Measure the time taken by the original recursive Fibonacci function
start_time = time.time()
recur_fibo(n)
end_time = time.time()
print(f"Original recur_fibo({n}) took {end_time - start_time:.4f} seconds")

# Measure the time taken by the memoized Fibonacci function
start_time = time.time()
recur_fibo_memoized(n)
end_time = time.time()
print(f"Memoized recur_fibo_memoized({n}) took {end_time - start_time:.4f} seconds")
