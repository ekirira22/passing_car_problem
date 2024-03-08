'''
    INPUTS
        1. An array of strings of length N
        2. An empty array in case of no pairs
    OUTPUT
        1. An array of integers, for either pair found and the position of the matching letter:
        2. An empty array if not matching string is found

    CONSTRAINTS

    REQUIREMENTS
        1. Write a function that takes an array of strings and returns matching pairs
        2.

    PSEUDOCODE
        ["abc", "bca", "dbe"]
        ["zzzz", "ferz", "zdsr", "fgtd"]

        1. Write a function loop that takes in an array
        3. Check the index position of pairs whose letters match
        4. Loop through the array, find matching pairs, return the result of that array
'''
import ipdb


def solution(S):

    for w_index in range(len(S)): # Loops through ["abc", "bca", "dbe"] 3 times
        for l_index in range(len(S[w_index])): # Loops through ["abc"] 3 times
            # for the first a check if it is equal to b at index 2 of S and d at index 3 of S
            for s_index in range(w_index + 1, len(S)):
                if S[w_index][l_index] == S[s_index][l_index]: # if a matching pair is found
                    return [w_index, s_index, l_index]
    return []


print(solution(["abc", "bca", "dbe"]))
print(solution(["bdafg", "ceagi"]))
print(solution(["zzzz", "ferz", "zdsr", "fgtd"]))
print(solution([ "gr", "sd", "rg"]))
