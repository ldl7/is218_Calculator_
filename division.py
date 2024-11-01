def div(a: float, b: float):
    if b == 0:
        # This part checks if 'b' is zero. If it is, we raise an error and stop the function.
        raise ValueError("Division by zero is not allowed.")  # This sends an error message when someone tries to divide by zero.
    return a / b  