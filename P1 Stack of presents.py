n = int(input())
presents1 = []
amount = 0
b = 0

for x in range(n):
    i = int(input())
    presents1.append(i)
    
presents2 = sorted(presents1)


bot = presents2[-1]

if (n == 1):
    print (1)
else:

    for c in range(n):
        bot -= presents2[c]
        amount += 1
        if (bot < 0):
            break



            
print(amount-1)    

