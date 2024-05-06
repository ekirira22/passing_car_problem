import math
import random
import string

import ipdb


# Scenario 1 - N(3) - "fig", "pea", "ckw"
# Scenario 2 - N(30) - "aabbcc...oo"

# Pseudocode
# 1. Create a function solution(A) that receives an integer N ✔️
# 2. Create a list that holds all alphabets from 'a' - 'z' in a tuple rand_letters() ✔️
# 3. Find the number of occurrences possible based on integer N and find the limit of your list ✔️
# 4. While list is true for the length of the N, append the result to a new list ✔️
# 5. Join the chars of new list and return the result ✔️
# 6. If input was an odd number, pop out the last letter ✔️


def solution(N):
    # get random letters and store in a tuple that is much faster
    alphabets = list(string.ascii_lowercase)
    random.shuffle(alphabets)
    rand_letters = tuple(alphabets)
    letters = []

    if N <= 26:
        pass

    return letters


while True:
    user_input = int(input("Pick any number (0 to quit): \n"))
    if user_input == 0:
        break
    print(solution(user_input))
