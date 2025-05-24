from calculator import ScientificCalculator
from art import logo


def main():
    calc = ScientificCalculator()
    print(logo)
    print("Scientific Calculator (type 'exit' to quit)")
    print("Special commands: history, clear_history, mem_store, mem_recall")

    while True:
        expr = input("\nEnter expression: ").strip()

        if expr.lower() == 'exit':
            break
        elif expr.lower() == 'history':
            print("\n=== Calculation History ===")
            print(calc.show_history())
            continue
        elif expr.lower() == 'clear_history':
            print(calc.clear_history())
            continue

        result = calc.calculate(expr)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()