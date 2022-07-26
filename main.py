# Press the green button in the gutter to run the script.
import Calculator

def do_something(tat, bayebaye, okbye):
    pass


def main():
    print("Give two values")
    x = int(input())
    y = int(input())
    print("Set operations like:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = int(input())

    if (operation > 4) and (operation < 1):
        print("Invalid choice of operation")
    elif operation == 1:
        res = Calculator.addition(x, y)
        print(res)
    elif operation == 2:
        res = Calculator.subtraction(x, y)
        print(res)
    elif operation == 3:
        res = Calculator.multiply(x, y)
        print(res)
    else:
        res = Calculator.divide(x, y)
        print(res)

    print("End of operation")
    saveme("End of test 3")


if __name__ == '__main__':
    main()
