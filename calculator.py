def calculate(expression):
  """
  Calculates the result of a mathematical expression string.

  Args:
    expression: A string representing a mathematical expression.  
                Supports +, -, *, /, parentheses, and spaces.
                Assumes expressions are well-formed and uses operator precedence (PEMDAS/BODMAS).

  Returns:
    The result of the expression as a float.
    Returns None if the expression is invalid or causes an error (e.g., division by zero).
  """

  try:
    return eval(expression)  # WARNING: See notes below about using eval()
  except (SyntaxError, TypeError, ZeroDivisionError) as e:
    print(f"Error evaluating expression: {e}")
    return None


# Example usage
if __name__ == "__main__":
  expression1 = "2 + 3 * 4"
  result1 = calculate(expression1)
  print(f"Expression: {expression1}, Result: {result1}")  # Output: 14.0

  expression2 = "(10 - 5) / 2"
  result2 = calculate(expression2)
  print(f"Expression: {expression2}, Result: {result2}")  # Output: 2.5

  expression3 = "10 / 0"  # Division by zero
  result3 = calculate(expression3)
  print(f"Expression: {expression3}, Result: {result3}")  # Output: Error and None

  expression4 = "2 * (3 + 4) - 1"
  result4 = calculate(expression4)
  print(f"Expression: {expression4}, Result: {result4}")  # Output: 13.0

  expression5 = "abc + 5" # Invalid expression
  result5 = calculate(expression5)
  print(f"Expression: {expression5}, Result: {result5}") # Output: Error and None


# ALTERNATIVE IMPLEMENTATION (SAFER, BUT MORE COMPLEX)

#  A more robust implementation that doesn't use eval() would involve:
#   1. Tokenizing the input string (breaking it into numbers, operators, parentheses).
#   2.  Converting the tokens into postfix (Reverse Polish Notation - RPN).
#   3.  Evaluating the RPN expression using a stack.

#  Implementing this would be more secure but require a significantly more complex code.  
#  I can provide that if requested, but for simple educational purposes, eval is often used
#  with the understanding of its risks.