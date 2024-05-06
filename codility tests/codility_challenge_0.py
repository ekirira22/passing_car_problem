'''
    PSEUDOCODE ::
    1. Define a function that takes in a list of crossing cars that are either zeros or ones ✔️
    2. Define a variable crossing_pairs that keeps track of crossing cars
    3. Create a for loop that loops through the list, if a car is 0 any 1's found after it will register as a pair
    4. Return the crossing pairs
'''
import ipdb


def solution_one(A):
    crossing_pairs = 0

    for car in range(len(A)):
        index = car + 1
        while True:
            try:
                if A[car] == 0 and A[index] == 1:
                    crossing_pairs += 1
                    index += 1
                elif A[car] == 1 and A[index] == 0:
                    index += 1
                else:
                    index += 1
            except IndexError:
                break

    return crossing_pairs


print(solution_one([0, 1, 0, 1, 1, 1]))


def solution_two(A):
    sE = 0
    s = 0
    for i in range(0, len(A)):
        if A[i] == 0:
            sE += 1
        elif A[i] == 1:
            s += sE
    return s


print(solution_two([0, 1, 0, 1, 1, 1]))
