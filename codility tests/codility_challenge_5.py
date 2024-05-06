"""
    Digital Sum Replacement 

    There is an array A that consists of N integers. In one move you can select a number from A and replace it by the sum of its digits. 
    One number can be selected multiple times. You can apply at most two moves. What is the minimum sum of the array you can achieve?
    Write a function:

    def solution(A)
    that, given an array A, returns the minimum sum of the array you can achieve after applying at most two moves.

    Examples:
    1. Given A = [1, 10, 12, 3], you can apply the move on the second and third elements. Then A = [1, 1, 3, 3] and the function should return 8.
    2. Given A = [2, 29, 3], you can apply the move twice on the second element. Then A = [2, 2, 3] and the function should return 7.
    3. Given A = [100, 101, 102, 103], you can apply the move on the first and second elements. Then A = [1, 2, 102, 103] and the function should return 208.
    4. Given A = [55], you can apply the move twice on the first element. Then A = [1] and the function should return 1.

    Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..50,000];
    each element of array A is an integer within the range [1..10,000].

"""

def solution(A):
    # define a helper function that 

    def find_sum(num):
        return sum([int(val) for val in str(num)])
    
    for _ in range(2):
        max_index = A.index(max(A))
        A[max_index] = find_sum(A[max_index])

    return sum(A)

print(solution([1, 10, 12, 3])) # 8
print(solution([2, 29, 3])) # 7
print(solution([100, 101, 102, 103])) # 208
print(solution([55])) # 1

