i = int(input("put number : ")) ##234
sum=0
while (i>0):
    sum=sum+i%10   # 0+234%10 = 0+4, 4+3
    print(sum)
    i=i//10
print(sum)