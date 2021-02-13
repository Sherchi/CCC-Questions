w = int(input())
n = int(input())
cars = 0
weight = [0,0,0]

for x in range(n):
    m = int(input())
    weight.append(m)
    
#     D:

for x in range(n):
    if (weight[x] + weight[x+1] + weight[x+2] + weight[x+3] <= w):
        cars += 1
    else:
        break

print(cars)



