class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token not in "+-/*":
                st.append(int(token))
            else:
                if token == "+":
                    r,l = st.pop(), st.pop()
                    st.append(l+r)
                elif token == "-":
                    r,l = st.pop(), st.pop()
                    st.append(l-r)
                elif token == "*":
                    r,l = st.pop(), st.pop()
                    st.append(l*r)
                elif token == "/":
                    r,l = st.pop(), st.pop()
                    # since the the rules mention that truncate towards 0 --> in negative numbers this is a problem as we truncate towards to -inf
                    # st.append(l//r)
                    if l/r < 0 and l/r != int(l/r):
                        st.append((l//r)+1)
                    else:
                        st.append(l//r)
        
        return st.pop()
