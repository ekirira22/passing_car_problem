import ipdb
'''
    INPUTS, OUTPUTS, CONSTRAINTS, REQUIREMENTS
    INPUTS
        a. Input of list of length (N)
        b. Each element in A denoted as A[i]
    OUTPUTS
        a. max num of two pairs with equal sum
        b. If not -1
    CONSTRAINTS
        a. Length of list A : work within length
        b. Each element has to be integers
    REQUIREMENTS
        a. A function that will take in A as input and return maximum sum of two pairs in list
        b. Sum of digits of each element taken into consideration
        c. If no such -1
        d. Function to handle constraints

    PSEUDOCODE


'''

# Pseudocode
# 1. Create a function solution(A) that will receive a list of numbers ✔️
# 2. Loop through the list add the digits of individual numbers and append to list_buffer[] ✔️
# 3. Check if list_buffer[] has unique values (checkUniqueOrDuplicate()) and return -1 if values are unique,
#       proceed if duplicates exist ✔️
# 4. Check if list_buffer[] had duplicates (checkUniqueOrDuplicate()) and return indices of duplicate numbers ✔️
# 5. Add the sum of the numbers from A and append to a max_sum[] ✔️
# 6. Find the maximum number in max_sum and return that value. ✔️


# create a helper function that takes a number and returns the sum of the digits
def digitSum(num):
    return sum(int(digit) for digit in str(num))


def solution(A):
    # return should be a maximum sum
    # if no pair return -1
    max_sum = -1
    digit_sum = {}
    # iterate over the array to get the max sum for the pairs
    for num in A:
        sum_of_digits = digitSum(num)
        # store the above sum to the dictionary reference
        if sum_of_digits in digit_sum:
            # calculate sum of two numbers with equal digit sums
            # we use max here as a comparator to compare current max_sum and current sum
            max_sum = max(max_sum, num + digit_sum[sum_of_digits])
            pass
        else:
            # store sum in dict if it doesn't exist
            digit_sum[sum_of_digits] = num
        # ipdb.set_trace()

    return max_sum


print(solution([51, 32, 43]))
print(solution([42, 33, 60]))
print(solution([51, 71, 17, 42]))


# Previous Solution # Still Works

# indices = []
# def solution(A):
#     list_buffer = []
#     sum_totals = []
#     for i in range(len(A)):
#         # Set counter to keep track of digit sums
#         count = 0
#         for char in str(A[i]):
#             count += int(char)
#         list_buffer.append(count)
#
#     # Checks if list is unique or duplicate
#     if checkduplicate(list_buffer) == 'unique':
#         return -1
#
#     # We need to return an array of the sum of numbers in A
#     for i in range(len(list_buffer)):
#         # [6,8,8,6]
#         find_indices(list_buffer, list_buffer[i], start=0)
#         # ipdb.set_trace()
#
#     # Get indices pairs, append total of pairs to sum
#     start = 0
#     while True:
#         try:
#             total = A[indices[start]] + A[indices[start + 1]]
#             sum_totals.append(total)
#             start += 2
#         except IndexError:
#             break
#
#     return max(sum_totals)
#
#
# def checkduplicate(list_buffer):
#     # set does not allow duplicates
#     list_set = set(list_buffer)
#     if len(list_set) == len(list_buffer):
#         return 'unique'
#
#
# def find_indices(list_buffer, value, start):
#     global indices
#     while True:
#         try:
#             index = list_buffer.index(value, start)
#             start = index + 1
#             indices.append(index)
#             # ipdb.set_trace()
#         except ValueError:
#             break
#
#
# print(solution([33, 71, 17, 42]))

