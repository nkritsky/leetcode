#
# Description: https://leetcode.com/problems/longest-common-prefix/
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        c = 0
        for i,v in enumerate(strs[0]):
            print (strs[0][i])
# doing try/except to catch the out-of-index errors
            try:
                temp = strs[0][i]
                for s in strs:
                    if (s[i] != temp):
                        return(strs[0][:c])
                c = c+1
            except:
                return(strs[0][:c])
        if (c == 0):
            return ("")
        else:
            return(strs[0][:c])
                
                    
