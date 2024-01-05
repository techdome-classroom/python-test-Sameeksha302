class Solution():
    def isValid(self,s):
        stack = []
        for ch in s:
            if ch in ('(', '{', '['):
                stack.append(ch)
            else:
                if stack and ((stack[-1] == '(' and ch == ')') or
                            (stack[-1] == '{' and ch == '}') or
                            (stack[-1] == '[' and ch == ']')):
                    stack.pop()
                else:
                    return False
        return not stack

exp = input("Enter the expression : ")
# creating an instance of the Solution class
solution = Solution()
# call the isValid method with a string argument that will be taken as input from user
result = solution.isValid(exp)
print(result)


  

