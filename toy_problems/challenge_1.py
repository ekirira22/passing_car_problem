import ipdb
# Scenario 1- [7, 15, 10, 8] should return 7
# Scenario 2 - [11, 10, 8, 12, 8, 10, 11] should return 6

# Pseudocode
# 1. Define a function solution(A) that receives boxes ✔️
# 2. Check if the sum total of all bricks is divisible by 10, return -1 if not ✔️
# 3. Define a second function brick_arranger() that will sort the  bricks and return moves ✔️
# 4. brick_arranger() receives bricks from solution(A) and checks:
#   a. if current box < 10 then 'steal' from the next box and register move ✔️
#   b. else if current box > 10 > previous box and prev box index is not out of range
#       add a brick to the left and register move ✔️
#   c. else if current box > 10 (left is not < 10) add a brick to the right and register move ✔️
#   d. else (box bricks are 10) shift the index position to move to the next box ✔️

def solution(A):
    # Check if each box can hold 10 bricks
    total_bricks = sum(A)
    no_of_boxes = len(A)
    if total_bricks != 10 * len(A):
        return -1

    # Keep track of the moves
    moves = 0
    # iterate over boxes
    for i in range(no_of_boxes):
        # check each brick for any deficit or excess
        if A[i] > 10:
            excess = A[i] - 10
            # if any excess move it to the next brick
            A[i] -= excess
            A[i+1] += excess
            moves += excess
        # do the same for deficit
        elif A[i] < 10:
            deficit = 10 - A[i]
            # if any deficit bring in difference from next box
            A[i] += deficit
            A[i+1] -= deficit
            moves += deficit
    return moves


print(solution([7, 15, 10, 8]))
print(solution([11, 10, 8, 12, 8, 10, 11]))
print(solution([7, 14, 10]))
print(solution([7, 3, 21, 10, 8, 12, 17, 10, 11, 1]))








