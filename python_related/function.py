def add(a,b):
    print(a+b)
def sub(c,d):
    print(c-d)
def div(q,w):
    print(q/w)
choice = input("put add or sub:" )
n1 = int(input("frt= "))
n2 = int(input("sec= "))
if choice == 'add':
    add(n1,n2)
elif choice == 'sub':
    sub(n1,n2)
elif choice == 'div':
    div(n1,n2)
