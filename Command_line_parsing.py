import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help="Enter the first number", type=int, metavar="Num1") # The first number being passed as an argument
    parser.add_argument("number2", help="Enter the second number", type=int, metavar="Num2") # The second number being passed as an argument
    parser.add_argument("operation", help="Enter the operation to be performed", type=str, metavar="+, -, *, /, %") # The operation to be performed

    args = parser.parse_args()
    num1 = args.number1
    num2 = args.number2
    op = args.operation
    result = None


    if op == '+':
        result = num1 + num2
    
    elif op == '-':
        result = num1 - num2

    elif op == '/':
        result = num1 / num2   

    elif op == '*':
        result = num1 * num2 

    elif op == '%':
        result = num1 % num2
        
    print(f"The result of {num1} {op} {num2} = {result}")