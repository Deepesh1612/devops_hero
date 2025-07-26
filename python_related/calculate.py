choice = input("add/sub/divide/mul=" )
a = int(input("a="))
b = int(input("b="))
 
if choice == "add":
    op = a + b
    print ("output =", op)
elif choice == "sub":
    op = a - b
    print ("output =", op )
elif choice == "divide":
    op = a / b
    print ("output =", op)
    print(type(op))
elif choice == "mul":
    op = a * b
    print ("output =", op)
else:
    print ("output worng", op)
    