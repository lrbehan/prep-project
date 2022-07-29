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
Finally, the resulting string becomes "cadosegnil".
