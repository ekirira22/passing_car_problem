"""
    INPUT
    OUTPUT
    CONSTRAINTS

    PSEDOCODE
    1. 
"""

def solution(A):
    if not A:
        return 0
    
    h = {}
    max_val = float('-inf')
    
    for num in A:
        h[num] = h.get(num, 0) + 1
        max_val = max(max_val, num)
    
    res = 1
    for key, value in h.items():
        if key == max_val:
            continue
        res += min(2, value)
    
    return res

print(solution([2]))
print(solution([1,2]))
print(solution([2, 6, 3, 2, 4, 1]))
print(solution([2, 3, 3, 2, 2, 2, 1]))