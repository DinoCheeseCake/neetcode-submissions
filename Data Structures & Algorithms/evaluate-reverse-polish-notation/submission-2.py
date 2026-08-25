class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token == "+":
                st.append(st.pop() + st.pop())
            elif token == "-":
                b = st.pop()
                a = st.pop()
                st.append(a - b)
            elif token == "*":
                st.append(st.pop() * st.pop())
            elif token == "/":
                b = st.pop()
                a = st.pop()
                st.append(int(a / b))
            else:
                st.append(int(token))

        return st[-1]