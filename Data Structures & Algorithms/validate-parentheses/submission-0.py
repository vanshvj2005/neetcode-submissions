class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(len(s)):
            if s[i] == '{' or s[i] == '[' or s[i] == '(':
                st.append(s[i])
            elif s[i] == '}' or s[i] == ']' or s[i] == ')':
                if len(st) == 0:
                    return False
                if (s[i] == '}' and st[-1] != '{' ) or (s[i] == ')' and st[-1] != '(' ) or (s[i] == ']' and st[-1] != '[' ):
                    return False
                st.pop()
        return len(st) == 0
            
                
