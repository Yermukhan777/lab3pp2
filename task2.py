# Grams to ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams


# Fahrenheit to Celsius
def fahrenheit_to_celsius(F):
    return (5/9) * (F - 32)


# Chickens and Rabbits puzzle
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2*chickens + 4*rabbits == numlegs:
            return chickens, rabbits
    return None


# Filter prime numbers
def filter_prime(nums):
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: return False
        return True
    return list(filter(lambda x: is_prime(x), nums))


# Permutations of string
from itertools import permutations
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]


# Reverse words
def reverse_sentence(s):
    return ' '.join(s.split()[::-1])


# has_33
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] == 3:
            return True
    return False


# spy_game
def spy_game(nums):
    code = [0, 0, 7]
    for n in nums:
        if n == code[0]:
            code.pop(0)
        if not code:
            return True
    return False


# Volume of sphere
def sphere_volume(r):
    return 4/3 * math.pi * r**3


# Unique list
def unique_list(lst):
    new = []
    for x in lst:
        if x not in new:
            new.append(x)
    return new


# Palindrome check
def is_palindrome(s):
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]


# Histogram
def histogram(lst):
    for n in lst:
        print('*' * n)


# Guess the number
import math
import random
def guess_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
