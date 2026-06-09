import inspect

def simple_calculator(a, b, operation):
    """Performs a simple arithmetic operation.

    Args:
        a: The first number.
        b: The second number.
        operation: The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        The result of the operation.

    Raises:
        ValueError: If an invalid operation is provided or division by zero occurs.
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError(f"Invalid operation: {operation}. Supported operations are 'add', 'subtract', 'multiply', 'divide'.")

def demonstrate_ai_understanding():
    print("--- Demonstrating AI Code Generation and Understanding ---")

    # Scenario 1: AI generates code. We need to understand it.
    print("\nScenario 1: Understanding AI-generated code")
    print("Imagine an AI generated the following function:")
    print(inspect.getsource(simple_calculator))

    # AI might generate this call, but we need to know *why* it works.
    try:
        result_ai_call = simple_calculator(10, 5, 'multiply')
        print(f"AI-generated call: simple_calculator(10, 5, 'multiply') -> {result_ai_call}")
        # If the AI suggested 'power' instead of 'multiply', our understanding would catch the error.
    except ValueError as e:
        print(f"Error during AI-generated call: {e}")

    # Scenario 2: AI helps debug. Understanding the fundamentals is key.
    print("\nScenario 2: Understanding AI-assisted debugging")
    print("Let's introduce an error and see how understanding helps.")
    try:
        # AI might suggest this fix, but we need to know *why* it's a fix.
        problematic_call = simple_calculator(10, 0, 'divide')
        print(f"Problematic call: {problematic_call}")
    except ValueError as e:
        print(f"AI might suggest handling the error: {e}")
        print("Our understanding of division by zero allows us to validate AI's suggestions.")

    # Scenario 3: AI suggests improvements. Understanding guides the choice.
    print("\nScenario 3: Understanding AI-suggested improvements")
    print("An AI might suggest adding more operations or error handling.")
    print("Our fundamental knowledge helps us evaluate if these suggestions align with project requirements.")
    print("For instance, adding 'modulo' might be suggested, but we need to know its use case.")

    print("\nConclusion: AI is a powerful tool, but fundamental understanding remains crucial for effective use, debugging, and innovation.")

if __name__ == "__main__":
    demonstrate_ai_understanding()
