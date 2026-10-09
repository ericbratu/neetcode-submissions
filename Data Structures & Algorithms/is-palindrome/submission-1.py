class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstring = ''

        for i in s:
            if i.isalnum():
                newstring += i.lower()

        if newstring == newstring[::-1]:
            return True
        else:
            return False