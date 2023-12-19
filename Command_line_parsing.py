import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help="Enter the first number", type=int, metavar="Num1") # The first number being passed as an argument
    parser.add_argument("--number2", help="Enter the second number", type=int, metavar="Num2") # The second number being passed as an argument
    parser.add_argument("--operation", help="Enter the operation which can be performed : addition, subtraction, multiplication, division & remainder", type=str, metavar="OPERATION",
                        choices=["Add", "Sub", "Div", "Remain"]) # The operation to be performed

    args = parser.parse_args()
    num1 = args.number1
    num2 = args.number2
    op = args.operation
    result = None


    if op.lower() == 'add' or op.lower() == 'addition':
        result = num1 + num2
    
    elif op.lower() == 'sub' or op.lower() == 'subtract':
        result = num1 - num2

    elif op.lower() == 'div' or op.lower() == 'division':
        result = num1 / num2   

    elif op.lower() == 'mul' or op.lower() == 'multiply':
        result = num1 * num2 

    elif op.lower() == 'remain' or op.lower() == 'remainder':
        result = num1 % num2
        
    print(f"The result of {num1} {op.lower()} {num2} = {result}")