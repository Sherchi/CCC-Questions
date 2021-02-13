#a is the steps forwards for Nikky
#b is the steps backwards for Nikky
#c is the steps forwards for Byron
#d is the steps backwards for Byron
#s is Total Steps allowed for both.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

#How many steps each one of them took forwards and backwards.
ASteps = 0
BSteps = 0
CSteps = 0
DSteps = 0


NikkyDist = 0
ByronDist = 0
#Goes in reverse because I wanted to see how many steps I had left
#during Troubleshooting
for i in range(s-1, -1, -1):

#Reseting the amount of steps going forwards and backwards for Nikky
    if (b == -1):
        a = ASteps -1
        ASteps = 0
        b = BSteps -1
        BSteps = 0
#Reseting the amount of steps going forwards and backwards for Byron        
    if (d == -1):
        c = CSteps -1
        CSteps = 0
        d = DSteps -1
        DSteps = 0
#Steps Forwards for Nikky
    if (a > -1):
        NikkyDist += 1
        a -= 1
        ASteps += 1
        
#Steps backwards for Nikky
    if (a <= 0 and b > -1):
        NikkyDist -= 1
        b -= 1
        BSteps += 1

#Steps forwards for Byron    
    if (c > -1):
        ByronDist += 1
        c -= 1
        CSteps += 1

#Steps backwards for Byron
    if (c <= 0 and d > -1):
        ByronDist -= 1
        d -= 1
        DSteps += 1
        
#Print the result.
if (NikkyDist > ByronDist):
    print("Nikky")
elif (ByronDist > NikkyDist):
    print("Byron")
else:
    print("Tied")

                #####Looking at my own code hurts me.#####
    #####Please don't be like me and use 10 million if statements. D:#####


