#Question:	Given a string s, find the first non-repeating character in it 
#			and return its index. If it does not exist, return -1.
#Author: Jiawen Liu

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = [0 for i in range(0,26)]
        index_stack = []
        val_stack = []
        for i in range(0, len(s)):
            if visited[ord(s[i]) - 97] == 0:
                visited[ord(s[i]) - 97] = 1
                index_stack.append(i)
                val_stack.append(s[i])
            else:
                if s[i] in val_stack:
                    index_stack.pop(val_stack.index(s[i]))
                    val_stack.remove(s[i])
        if len(val_stack) == len(s):
            return 0
        elif len(val_stack) == 0:
            return -1
        else:
            return index_stack[0]
                
        