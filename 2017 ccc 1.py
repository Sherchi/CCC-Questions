N = int(input())
swift = input().split(" ")
sema = input().split(" ")
days = [0]
p1 = 0
p2 = 0
for x in range(N):
    p1 += int(swift[x])
    p2 += int(sema[x])
    if p1 == p2:
        days.append(x+1)
        
print(max(days))
    
