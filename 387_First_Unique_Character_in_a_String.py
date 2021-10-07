#Question:	Given a string s, find the first non-repeating character in it 
#			and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        for i in range(0,len(s)):
            chars[s[i]] = -1 if s[i] in chars else i
        result = [chars[ch] for ch in chars if not chars[ch] == -1]
        return result[0] if result else -1
                
        