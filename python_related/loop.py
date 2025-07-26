import time
for i in range(2):
    print(i)
    time.sleep(3)
    j = i
    while j < 5:
        j += 1
        print(j)
        time.sleep(3)
        
