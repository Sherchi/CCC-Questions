main = []
branch = []
out = [0]
results = []
Y = False
T = int(input())
for x in range(T):
    main = []
    branch = []
    out = [0]
    nx = int(input())
    for y in range(nx):
        numbers = int(input())
        main.append(numbers) 
    for i in range(nx*nx):
        #Checks if the first number is 1
        if (main != [] and main[-1] == 1):
            out.append(main[-1])
            del main[-1]
        #if it isnt 1, check if it is 1 number above
        elif (main != [] and main[-1] == out[-1]+1):
            out.append(main[-1])
            del main[-1]
        #If it isnt 1 number above, send it to the branch if branch is empty
        elif (main != [] and not (branch)):
            branch.append(main[-1])
            del main[-1]
        
        elif (main != [] and main[-1] < branch[-1]):
            branch.append(main[-1])
            del main[-1]
        elif (main != [] and main[-1] > branch[-1]):
            Y = False
        else:
            Y = True
        if (branch != [] and branch[-1] == out[-1]+1):
            out.append(branch[-1])
            del branch[-1]
            
    if (Y == False):
        Y = False
    else:
        for n in range(nx+1):
            if(n == len(out)-1):
                break
            elif(out[n] == out[n+1]-1):
                Y = True
            else:
                Y = False
                break


            
    if (Y == True):
        results.append("Y")
        Y = False
    else:
        results.append("N")
        

for a in range(len(results)):
    print(results[a])

    
