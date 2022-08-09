""" for list a length n, return b length n where b[i]=a[i-1]+a[i]+a[i+1].  if out of range, i=0"""

def solution(n, a):
    b = [None]*n
    for i in range(n):
        if i <= 0:
            b[i] = a[i] + a[i+1]
        elif i >= n-1:
            b[i] = a[i-1] + a[i]
        else:
            b[i] = a[i-1] + a[i] + a[i+1]
    return b

#TEST CASE
a = [4, 0, 1, -2, 3]
print(solution(5, a))


"""Given a string shift each vowel to the position of the next vowel in the string. The last vowel should be shifted to the position of the first vowel of the string.
Note: The list of vowels is: "a", "e", "i", "o", "u".
Example
For message = "codesignal", the output should be solution(message) = "cadosegnil".
Explanation:
The given string "codesignal" contains the following vowels: message[1] = "o", message[3] = "e", message[5] = "i", message[8] = "a".
message[1] = "o" is moved to the position of the next vowel - message[3].
message[3] = "e" is moved to the position of the next vowel - message[5];
message[5] = "i" is moved to the position of the next vowel - message[8];
message[8] = "a" is the last vowel, so it is moved to the position of the first vowel in the string - message[1];
Finally, the resulting string becomes "cadosegnil". """

def solution2(message):
    pass

"""
A robot responds to two commands, U or D, that tell it to move one step up (U) or one step down (D) on a vertical line.
You're given a string commands representing a series of U and D commands. After responding to all the commands in order, the robot will stop. Your task is to determine whether the robot will stop above or below its starting position:
If the robot will stop above its starting position, return "U".
If the robot will stop at its starting position, return an empty string.
If the robot will stop below its starting position, return "D".
Example
For commands = "UDDUDD", the output should be solution(commands) = "D".
After executing the first two commands, the robot will return to its starting position.
Similarly, after executing the third and fourth commands, the robot will return to its starting position.
After executing the last two commands, the robot will stop 2 steps below its starting position, so the answer is "D".
For commands = "DDUDDDUUUU", the output should be solution(commands) = "".
After executing all the commands, the robot will return to its starting position, so you should return an empty string.
"""

def solution(commands):
    pass

"""
2 Sum: Given a list and a target value return the index of the two numbers that will add to the target value
"""
def two_sum(nums, target):
        for i in range(len(nums)):              #first loop
            for j in range(i + 1, len(nums)):   #second loop starting at i+1
                if nums[j] == target - nums[i]: #check if j loop value = target- loop value
                    return [i, j]

# this solution has runtime of O(n^2) because of the nested loops.

#TEST
nums = [1, 4, 6, 8, 22]
print(two_sum(nums, 9))

#ALTERNATE SOLUTION WITH HASHMAP#
#Hashmap is a dictionary that uses index as value and the list item as key
#This solution has a runtime of O(n)

def two_sum_hashmap(nums, target):
    hashmap = {}                #dictionary
    for i in range(len(nums)):
        hashmap[nums[i]] = i    #loop to add to dictionary value: index
    for i in range(len(nums)):
        complement = target - nums[i]   # look for complement (the value that is target-num)
        if complement in hashmap and hashmap[complement] != i:  # if num can be doubled for target, do not return the num twice
            return [i, hashmap[complement]]

#TEST
nums = [1, 4, 6, 8, 22]
print(two_sum_hashmap(nums, 9))