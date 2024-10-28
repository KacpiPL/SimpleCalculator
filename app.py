"""
A simple Flask application to perform basic arithmetic calculations.

This module defines a Flask app with a single endpoint that performs
addition, subtraction, multiplication, and division based on the
provided query parameters.
"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/calculate')
def calculate():
    """Perform a mathematical operation based on the provided parameters.

    Query parameters:
    - op: The operation to perform ('sum', 'subtract', 'multiply', 'divide').
    - arg1: The first integer argument.
    - arg2: The second integer argument.

    Returns:
    A string representation of the calculation result.
    """
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)
    if op == 'sum':
        result = arg1 + arg2
        operation = '+'
    elif op == 'subtract':
        result = arg1 - arg2
        operation = '-'
    elif op == 'multiply':
        result = arg1 * arg2
        operation = '*'
    elif op == 'divide':
        if arg2 != 0:
            result = arg1 / arg2
            operation = '/'
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation. Please use 'sum', 'subtract', 'multiply', or 'divide'."

    return f"{arg1} {operation} {arg2} = {result}"


if __name__ == '__main__':
    app.run()
