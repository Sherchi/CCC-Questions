n = int(input())
aHP = 100
dHP = 100
for x in range(n):
    roll = input()
    numbers = roll.split()
    a = int(numbers[0])
    d = int(numbers[1])
    if (a > d):
        dHP -= a
    elif (a < d):
        aHP -= d
print (aHP)
print (dHP)
