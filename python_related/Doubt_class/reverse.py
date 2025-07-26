number=int(input("put number :"))
reverse=0
while  number > 0:
    rem= number % 10
    print("rem",rem)
    reverse= reverse * 10 + rem
    print("reverse",reverse)
    number= number//10
    print("number",number)
    print('')
print("reverse num",reverse)
