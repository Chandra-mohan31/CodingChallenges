class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i):
                if(nums[i]+nums[j] == target):
                    return i, j

##########################################


class Solution:
    def reverse(self, x: int) -> int:
        if(-2147483648 < x and x < 2147483647):
            revs_number = 0
            p = 1

            if(x < 0):
                x = x*-1
                p = -1

            while (x > 0):

                remainder = x % 10
                revs_number = (revs_number * 10) + remainder
                x = x // 10
            if(-2147483648 < revs_number and revs_number < 2147483647):
                return revs_number*p
            else:
                return 0
        else:
            return 0


###############################################

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        l = 201
        for i in strs:
            if len(i) < l:
                l = len(i)
        for i in range(l):
            check = True
            x = strs[0][i]
            for j in range(1, len(strs)):
                if x != strs[j][i]:
                    check = False
                    break
            if(check):
                s = s+x
            else:
                break
        return s

############################################################

class Solution:
    def isValid(self, s: str) -> bool:
        out = False;
        l = len(s)
        
        stack = []
        for i in range(l):
            if(s[i] in ["(","{","["]):
                stack.append(s[i])
            
            
            elif "(" in stack  and s[i]==")" and stack[len(stack) - 1] == "(":
                stack.pop()
            elif "[" in stack  and s[i]=="]":
                stack.pop()
            elif "{" in stack  and s[i]=="}":
                stack.pop()
            else:
                return False
            

        
        if(len(stack)==0):
            out = True
        return out

#############################################