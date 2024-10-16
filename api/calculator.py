class RPNCalculator:
    def calculate(self, expression: str) -> float:
        operators = ['+', '-', '*', '/']
        stack = []
        entries = expression.split()
        for entry in entries:
            if entry.replace('.', '', 1).isdigit():
                stack.append(float(entry))
            elif entry in operators:
                if len(stack) < 2:
                    raise ValueError("Insufficient values in the expression.")
                b = stack.pop()
                a = stack.pop()
                result = self.apply_operator(a, b, entry)
                stack.append(result)
            else:
                raise ValueError(f"Unknown entry: {entry}")

        if len(stack) != 1:
            raise ValueError("The user input has too many values.")

        return stack[0]
    
    def apply_operator(self, a:float, b: float, operator: str):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return a / b
        else:
            raise ValueError(f"Invalid operator: {operator}")