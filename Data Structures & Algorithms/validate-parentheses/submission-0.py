class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_dict = {
            "]":'[',
            "}":'{',
            ")":'('
            }
        stack = []

        for bracket in s:
            if bracket in bracket_dict:
                if not stack:
                    return False
                last_bracket = stack.pop()
                if last_bracket!= bracket_dict[bracket]:
                    return False
                

            else:
                stack.append(bracket)
            
        if stack:
            return False
        else:
            return True



