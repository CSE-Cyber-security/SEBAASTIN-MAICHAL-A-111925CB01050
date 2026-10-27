"""
Simple command-line calculator.

Run:
    python calculator.py
"""

def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    if operator == "%":
        if num2 == 0:
            raise ZeroDivisionError("Cannot calculate remainder with zero.")
        return num1 % num2
    if operator == "**":
        return num1 ** num2
    raise ValueError("Unsupported operator.")


def main():
    print("=" * 32)
    print("       PYTHON CALCULATOR")
    print("=" * 32)
    print("Operations: +  -  *  /  %  **")
    print("Type q at the first prompt to quit.")

    while True:
        first = input("\nEnter first number: ").strip()
        if first.lower() == "q":
            print("Calculator closed. Goodbye!")
            break

        try:
            num1 = float(first)
            operator = input("Enter operator (+, -, *, /, %, **): ").strip()
            num2 = float(input("Enter second number: ").strip())
            result = calculate(num1, operator, num2)
            # Display whole-number results without an unnecessary .0.
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            print(f"Result: {result}")
        except ValueError as error:
            print(f"Input error: {error}")
        except ZeroDivisionError as error:
            print(f"Math error: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nCalculator closed. Goodbye!")
            break


if __name__ == "__main__":
    main()
