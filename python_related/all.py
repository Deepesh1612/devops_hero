a=1
b=20
for i in range(a,b+1):
    if i > 1:
        is_prime = True
        for x in range (2,i):
            if  i % x == 0:
                    is_prime=False
                    break
        if is_prime:
            print(i)
# a = 1
# b = 20
# for num in range(a, b + 1):        # Use a new variable `num` instead of `i`
#     if num > 1:
#         is_prime = True
#         for i in range(2, num):    # Check divisibility from 2 to num-1
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num)
