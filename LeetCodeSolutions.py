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
        out = False
        l = len(s)

        stack = []
        for i in range(l):
            if(s[i] in ["(", "{", "["]):
                stack.append(s[i])

            elif "(" in stack and s[i] == ")" and stack[len(stack) - 1] == "(":
                stack.pop()
            elif "[" in stack and s[i] == "]":
                stack.pop()
            elif "{" in stack and s[i] == "}":
                stack.pop()
            else:
                return False

        if(len(stack) == 0):
            out = True
        return out

#############################################
#    public static List<Integer> gradingStudents(List<Integer> grades) {
#         List<Integer> roundedGrades = new ArrayList<Integer>();
#         int t,x;
#         for(int i=0;i<grades.size();i++){
#             // System.out.println(grades.get(i));

#             // roundedGrades.add(grades.get(i));
#             x = grades.get(i);
#             t = x;
#             while (t%5!=0)
#                 t++;
#             // System.out.println(t);
#             if(t-x<3 && x>=38)
#             roundedGrades.add(t);
#             else
#             roundedGrades.add(x);
#             }
#         return roundedGrades;
#     }

# }

######################################################


class Solution:
    def maxArea(self, height: List[int]) -> int:
        large_area = 0

        for i in range(0, len(height)):
            for j in range(i, len(height)):
                large_area = max(large_area, min(
                    height[i], height[j]) * (j - i))
                # if(large_area < height[i]*abs(i-j)):
                #     large_area = height[i]*abs(i-j)

        return large_area
#####################################

# public class Solution {
#     public int maxArea(int[] height) {
#         int maxarea = 0, l = 0, r = height.length - 1;
#         while (l < r) {
#             maxarea = Math.max(maxarea, Math.min(height[l], height[r]) * (r - l));
#             if (height[l] < height[r])
#                 l++;
#             else
#                 r--;
#         }
#         return maxarea;
#     }
# }

######################################################


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx = 0
        l = 0
        r = len(height)-1
        while(l < r):
            maxx = max(min(height[r], height[l])*abs(r-l), maxx)
            if height[r] > height[l]:
                l = l+1
            else:
                r = r-1
        return maxx

################################################
#         comb = list(combinations(nums, 3))
#         ans = []
        
#         for i in comb:
#             i = list(i)
#             i.sort()
#             if(sum(i) == 0 and i not in ans):
#                 ans.append(i)
        
#         return ans

