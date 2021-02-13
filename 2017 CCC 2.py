N = int(input())
r = input().split(" ")
tide = []
order = []

for x in r:
    tide.append(int(x))
    
tides = sorted(tide)

if N == 1:
    for x in tides:
        print(x)
elif N % 2 == 0:
    for x in range(int(N/2)):
        order.append(tides[-x-1])
        order.append(tides[x])
    order.reverse()

    for x in order:
        print(x, end = " ")
else:
    for x in range(int(N/2) + 1):
        #order.append(tides[-x-1])
        order.append(tides[x])
        order.append(tides[-x-1])
    del order[-1]
    order.reverse()

    for x in order:
        print(x, end = " ")




