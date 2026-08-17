class Solution:
    def isPalindrome(self, s: str) -> bool:

        goodstring = ''

        for i in s:
            if i.isalnum():
                goodstring += i.lower()

        if goodstring == goodstring[::-1]:
            return True
        return False