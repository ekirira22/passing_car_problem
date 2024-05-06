"""
    A one day long training session will be conducted during the next 10 days. 
    there are n number of employees will to attend it. 

    Each employee provides a list of which of the next 10 days that they will be able to participate in the training. 
    The preference are presented as an array of strings . 
    E[K] is a string of digits ('0'-'9') representing the days the k-th employee is able to attend the training. 

    The dates in which the training will take place are yet to be scheduled. 
    What is the maximum number of employees that can attend during at least one of the two scheduled days. 

    In python write the function that given an array E consisting of N strings denoting the available days for each employee, 
    will return the max number of employees that during at least one of the two scheduled days.

    e..g given 
    print(solution(["039", "4", "14", "32", "", "34", "7"])) # 5
    print(solution(["801234567", "180234567", "0", "189234567", "891234567", "98", "9"])) # 7
    print(solution(["5421", "245", "1452", "0345", "53", "354"])) # 6
    
    It can be achieved for example by running trainings on day 3 and 4 , 
    this way employees number 0,1,2,3,and 5 will attend the training. 
    Give the solution and pseudocode steps. 

    STEPS::
    1. 

"""

# When dealing with schedule try thinking of dictionaries

# E[k] - Represents the employees days of attendance
"""
    key     :       value
    0               {0}
    1       :       {2}
    2               {3}
    3       :       {0,3,5}
    4               {1,2,5}
    5       :       {}
    6               {}
    7       :       {6}
    8               {}
    9       :       {0}
"""

def solution(E):
    # initialize our availability dictionary
    availability = {str(day) : set() for day in range(10)}
    # populate our availability dictionary
    for index, days in enumerate(E):
        for day in days:
            availability[day].add(index)
            
    # Find the best two days manually
    max_attendance = float('-inf')
    days = list(availability.keys())
    # Gets a list of all keys in dictionary
    for i in range(len(days)):
        for j in range(i+1, len(days)):
            day1, day2 = days[i], days[j]
            # calculate no. of unique employees that can attend either day1 or day2
            combined_attendance = len(availability[day1].union(availability[day2]))
            max_attendance = max(max_attendance, combined_attendance)

    return max_attendance 
    
print(solution(["039", "4", "14", "32", "", "34", "7"])) # 5
print(solution(["801234567", "180234567", "0", "189234567", "891234567", "98", "9"])) # 7
print(solution(["5421", "245", "1452", "0345", "53", "354"])) # 6