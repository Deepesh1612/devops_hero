def name(a,b):
    return a+b
def surname(c,d):
    return c-d
def com(q,w):
    return q*w
choice= str(input ("A o B= "))
n1=int(input("first=" ))
n2=int(input("second=" ))

if choice == "A":
    print(name(n1,n2))
elif choice == "B":
    print(surname(n1,n2))
else:
    print("nothing")
    print(com(name(n1,n2),surname(n1,n2)))
    