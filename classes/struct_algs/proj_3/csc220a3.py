"""
This module imports the ArrayStack class from the array_stack module.
This provides the push, pop, and checks if the stack is empty.
"""
from array_stack import ArrayStack

def do_operation(value_stack, operator_stack):
    """ Perform a single operation.
        Pop operands from value_stack,
        Pop operator from operator_stack,
        Push result back to value_stack.
        Input: value_stack - the value stack
               operator_stack - the operator stack
        Output: None
    """
    operand2 = value_stack.pop()
    operand1 = value_stack.pop()
    operator = operator_stack.pop()
    if operator == '+':
        value_stack.push(operand1 + operand2)
    elif operator == '-':
        value_stack.push(operand1 - operand2)
    else: # operator == '*'
        value_stack.push(operand1 * operand2)

def get_precedence(operator):
    """ Get the precedence of an operator.
        Input: operator - the operator
        Output: the precedence of the operator
    """
    operators = '*+-$'
    precedences = [2, 1, 1, 0]
    return precedences[operators.index(operator)]

def repeat_operations(value_stack, operator_stack, reference_operator):
    """ Repeat performing operators.
        Input: value_stack - the value stack
               operator_stack - the operator stack
               reference_operator - the reference operator
        Output: None
    """
    while len(value_stack) > 1 and \
            get_precedence(reference_operator) <= get_precedence(operator_stack.top()):
        do_operation(value_stack, operator_stack)

def evaluate(expression):
    """ Evaluates expression using two stacks: one for values and one for operators.
        Input (str): The arithmetic expression.
        Output: The result of the expression.
    """
    # Create a stack for values
    value_stack = ArrayStack()
    # Create a stack for operators
    operator_stack = ArrayStack()
    # Push an end token with lowest precedence onto operator stack
    operator_stack.push('$')
    # Iterate over each token in expression
    for token in expression:
        # If a digit, push onto value stack
        if token.isdigit():
            value_stack.push(int(token))
        else:
            # If operator, perform operations until reaching operator with lower precedence
            repeat_operations(value_stack, operator_stack, token)
            # Push current operator onto operator stack
            operator_stack.push(token)
    # Perform remaining operations until end token
    repeat_operations(value_stack, operator_stack, '$')
    # Return result
    return value_stack.top()
