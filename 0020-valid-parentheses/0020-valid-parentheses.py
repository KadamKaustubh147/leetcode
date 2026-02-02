class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        # diff = ord('(') - ord(')') 

        for c in s:
            if c in ("(", "[", "{"):
                st.append(c)
            else:
                if not st:
                    return False
                    break
                if c == ")" and st[-1] == "(":
                    st.pop()
                elif c == "]" and st[-1] == "[":
                    st.pop()
                elif c == "}" and st[-1] == "{":
                    st.pop()
                else:
                    break
        
        return True if not st else False