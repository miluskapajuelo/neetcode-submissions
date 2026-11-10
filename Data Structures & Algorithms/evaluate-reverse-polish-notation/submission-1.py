class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  

        for i in tokens:
            if i == "+":
                last = stack.pop()
                secondlast = stack.pop()
                stack.append(int(last) + int(secondlast))
            elif i == "-":
                last = stack.pop()
                secondlast = stack.pop()
                stack.append(int(secondlast) - int(last) )
                
            elif i == "*":
                last = stack.pop()
                secondlast = stack.pop()
                stack.append(int(last) * int(secondlast))
            elif i == "/":            
                last = stack.pop()
                secondlast = stack.pop()
                stack.append(int(int(secondlast) / int(last)))
            else:
                stack.append(int(i))
        return stack[0]