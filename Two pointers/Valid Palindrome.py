""""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""
import re

def isPalindrome(s):
    s = str(re.sub('[^a-zA-Z0-9]',"",s))
    s = s.lower()
    if len(s) == 0:
        return True
    i=0
    j=len(s)-1
    while i<j:
        if s[i]==s[j]:
            i+=1
            j-=1
        else:
            return False
    return True


s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))