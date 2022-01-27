import random
number=[]
attempts=0
def Number():
    for i in range (4):
        x=random.randrange(0,9)
        number.append(x)
def playgames():
    global attempts
    attempts+=1
    cows=0
    bulls=0
    print(number)
    choice=input("please enter 4 digit number")
    guess=[]
    for i in range(4):
        guess.append(int(choice[i]))
    for i in range(4):
        for j in range(4):
            if (guess[i])==number[j]:
                cows+=1
    for x in range(4):
        if guess[x]==number[x]:
            bulls+=1
    print("bulls",bulls)
    print("cow",cows)
    if bulls==4:
        print("you won after",attempts,"attempts")
    if bulls!=4:
        playgames()
Number()
playgames()



