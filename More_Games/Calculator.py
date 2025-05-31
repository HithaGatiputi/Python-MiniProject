def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1/n2

operations = {
 "+":add,
 "-":sub,
 "*":mul,
 "/":div
}
def calculator():
    num1 = float(input("What is the first number?\n"))

    for operator in operations:
        print(operator)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the second number?\n"))
        function = operations[operation_symbol]
        ans = function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {ans}")

        proceed = input("Type 'y' to continue calculating with {ans} OR type 'n' to start calculation with new numbers OR type 'e' to exit: ")
        if proceed == "y" :
            num1 = ans
        elif proceed == "n" :
            calculator()
        else:
            print("Thank You")
        break

calculator()