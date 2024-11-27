# Function to give precedence of character according to standard BODMAS rules
def prec(c):
    if c == '*' or c == '/':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

# Function that converts an infix expression to postfix expression for easier evaluation
def infix_to_postfix(s):
    result = []
    stack = []
    number = []
    operator = []
    n = len(s)

    i = 0
    while i < n:
        c = s[i]
        if c.isdigit() or c == '.':
            j = i + 1
            while j < n and (s[j].isdigit() or s[j] == '.'):
                j += 1
            result.append(s[i:j])
            number.append(s[i:j])
            i = j
        elif c == '(':
            stack.append(c)
            i += 1
        elif c == ')':
            if not stack:
                return "Invalid expression"
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            if stack:
                stack.pop()
            else:
                return "Invalid expression"
            i += 1
        elif c in ['+', '-', '*', '/']:
            if c == '-':
                if i == 0 or s[i-1] == '(':
                    result.append("0")
            while stack and (prec(s[i]) < prec(stack[-1]) or (prec(s[i]) == prec(stack[-1]))):
                result.append(stack.pop())
            stack.append(c)
            operator.append(c)
            i += 1
        else:
            return "Invalid expression"
        if len(number) > len(operator) + 1:
            return "Invalid expression"

    while stack:
        result.append(stack.pop())

    return result

# Function that evaluates a postfix expression
def evaluate_postfix(exp):
    stack = []
    for token in exp:
        if token not in ['+', '*', '-', '/']: 
            try:
                stack.append(float(token))
            except:
                return "Invalid expression"
        else:
            if stack:
                operand2 = stack.pop()
            else:
                return "Invalid expression"
            if stack:
                operand1 = stack.pop()
            else:
                return "Invalid expression"
            if not (type(operand1) == float and type(operand2) == float):
                return "Invalid expression"
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                if operand2 == 0:
                    return "Undefined value"
                result = operand1 / operand2
            stack.append(result)
    
    if len(stack) == 1:
        return stack.pop()
    else:
        return "Invalid expression"

# Basic I/O
print ("Welcome to calculator! Please enter your expression:")
exp = input()
exp = exp.replace(" ", "")

# Calling the functions
post = infix_to_postfix(exp)
answer = evaluate_postfix(post)

print(answer)