"""
    
    STEPWISE APPROACH
    1. 
"""

def solution(s, A):
    pyramid = A//2

    for i in range(1, A+1, 2):
        print(s * (i))


print(solution("a", 9))