
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    n1=float(input("Enter a number: "))
    for symbol in operations_dict:
        print(symbol)

    continue_cal=True
    while continue_cal:
        op_symbol=input("Pick an operation")
        n2=float(input("Enter an another no.:"))
        calculator_function=operations_dict[op_symbol] 
        output=calculator_function(n1,n2)
        print(f"{n1} {op_symbol} {n2} ={output}")  

        should_continue=input(f"Enter 'y' to continue calculation with {output} or 'n'to start new calculation or 'x'to exit")
        if should_continue=='y':
            n1=output
        elif should_continue=='n':
            continue_cal=False
            
            calculator()
        else:
            continue_cal=False
            print("thankyou using")
calculator()
