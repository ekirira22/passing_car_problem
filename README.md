# Phase 3 - Python Code Challenge

## Python Fundamentals
Authors: Eric Kirira Maranga && Diana Tuei

The following code challenges are meant to drill in fundamental concepts of python programming

### Codility Challenge 0
There is a list of N Cars (numbered from 0 to N−1) arranged in a row. The cars are represented in a binary fashion where
0 represents cars going east and 1 represents cars going left. Implement a function that returns the total number of
crossing cars in the most modular way possible.
Write a function solution(A); that, given a list A of N cars, returns the minimum number of crossing cars

Examples:

        1. For A = [0, 1, 0, 1, 1], the function should return 5.
        2. For A = [0, 1, 0, 1, 1, 1], the function should return 7. 
        3. For A = [0,1], the function should return 1.

### Codility Challenge 1

You are given an array S consisting of N strings. Every string is of the same length M. 
Your task is to find a pair of strings in array S, such that there exists a position in which both of the strings have the same letter.
Both the index in array S and the positions in the strings are numbered from zero. 
For example, given S = ["abc", "bca", "dbe"], string 0 ("abc") and string 2 ("dbe") have the same letter 'b' in position 1. 
On the other hand, for strings "abc" and "bca" there does not exist a position in which they have the same letter. 

Write a function: solution(A) that, given a zero-indexed array S of N strings, returns an array describing a pair of strings 
from S which share a common letter at some index. 

    If there is no such pair, the function should return an empty array. 
    If there is more than one correct answer, the function can return any of them. 
The result should be represented as an array containing `three integers`. 
The first two integers are the indexes in S of the strings belonging to the pair. 
The third integer is the position of the common letter. 

For S=[ "abc", "bca", "dbe"], as above, the result array should be represented as [0,2,1]. 
Another correct answer is [2,0,1], as the order of indexes of strings does not matter. 

Examples: 

    1. Given: S=[ "abc", "bca", "dbe"], your function may return [0,2,1] as described above. there is no such pair, the function should return an empty array. 
        If there is more than one correct answer, the function can return any of them. The result should be represented as an array containing three integers. 
        The first two integers are the indexes in S of the strings belonging to the pair. The third integer is the position of the common letter. 

        For S = ["abc", "bca", "dbe"], as above, the result array should be represented as [0,2,1]. Another correct answer is [2,0,1], as the order of 
        indexes of strings does not matter. Examples: 1. Given: S=[ "abc", "bca", "dbe"], your function may return [0,2,1] as described above.

    2. Given: S = ["zzzz", "ferz", "zdsr", "fgtd", your function may return [0,1,3]. Both "zzzz" and "ferz" have ' z ' in position 3. 
        The function may also return [1,3,0], which would reflect strings "ferz", "fgtd" and letter 'F. 

    3. Given A=[ "gr", "sd", "rg"] your function should return D. There is no pair of strings that fulfils the criteria.

    4. Given A= ["bdafg", "ceagi"], your function may return [0,1,2]. 

Write an efficient algorithm for the following assumptions: -

    N is an integer within the range [1,.,30,000}h - 
    M is an integer within the range 11,2,000k - 
    each element of S consists only of lowercase English - N∗M≦30,000.

### Codility Challenge 2




