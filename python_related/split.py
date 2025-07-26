name = input("enter num:")
numlist = name.split()
a=[]
for i in range(len(numlist)):
    a.append(int(numlist[i]))
    #here a vale is getting stored in a[] list or we can say append
    #like a = [1,2,3,4,5,5,6]
#     print(a) ## change the place of this print you will get differet output
# print(a) ## change the place of this print you will get differet output
for number in a: #we a is taken as a input in number varible 
    if number % 2 == 0:
        print(number)