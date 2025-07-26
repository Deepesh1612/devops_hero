i=5
for n in range(0,i+1):
    spaces = '-' * (i-n)
    # print (spaces,"|" )
    strik = '*' * ( 2*n - 1 )
    print (spaces + strik)


a = int(input("bhai input dal:"))
for i in range(a):
    # print (i)
    # a=a-1
    # print(a)
    # print(' ')
    spaces= " " * (a-i)##here suppose a=5 and first i value will be 0 so a-i means 5-0=5
    #print(spaces)
    strk= '*' * (i*2-1) ##2multiple by i
    #print(strk) 
    print(spaces + strk)
