N = int(input())
L = input().split(" ")
heights = []
numbers = []
amount = []
length = 0
ways = 0


for x in range(1,N):
    for i in range(N-x):
        numbers.append(int(L[-x]) + int(L[i]))
        
for x in numbers:
    amount.append(numbers.count(x))

test = max(amount)
test1 = test

for x in range(len(amount)):
    if amount[x] == test1:
        test -= 1
    if test ==  0:
        ways += 1
        test = test1

length += test1

if N == 1:
    print(1, 1)
else:
    print(length, ways) 

