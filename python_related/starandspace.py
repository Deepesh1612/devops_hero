import time
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    spaces = ' ' * (rows - i)
    print (spaces)
    time.sleep(2)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
