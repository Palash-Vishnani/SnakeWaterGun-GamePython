import random
var3=0
var4=0
print("Let's Play The Game Of Snake, Water and Gun!!!")
list1=["Snake","Water","Gun"]
x=10
print("You have total 10 lifes")
while(True):
    if x==0:
        print("Game Over!!")
        print("Your Score:",var3,"vs","Pc Score:",var4)
        if var3>var4:
            print("Congratulations! You Won against Pc")
            break
        elif var3<var4:
            print("Pc Won..Try again later :( ")
            break
        else:
            print("Its a Tie")
            break
    var1 = random.choice(list1)
    var2=int(input("Enter a number of your choice:\n1.Snake\n2.Water\n3.Gun\n"))
    if var1=="Snake" and var2==1:
        print("Pc Chose: Snake")
        print("It's a tie try again!!")
        print("Lifes Remaining: ",x)
        continue
    elif var1=="Water" and var2==2:
        print("Pc Chose: Water")
        print("It's a tie try again!!")
        print("Lifes Remaining: ", x)
        continue
    elif var1=="Gun" and var2==3:
        print("Pc Chose: Gun")
        print("It's a tie try again!!")
        print("Lifes Remaining: ", x)
        continue
    elif var1=="Snake" and var2==2:
        print("Pc Chose: Snake")
        var4=var4+1
        print("Pc won try again!!")
        x = x - 1
        print("Lifes Remaining: ", x)
        continue
    elif var1=="Snake" and var2==3:
        print("Pc Chose: Snake")
        var3=var3+1
        print("You won play again!!")
        x = x - 1
        print("Lifes Remaining: ", x)
        continue
    elif var1=="Water" and var2==1:
        print("Pc Chose: Water")
        var3=var3+1
        print("You won play again!!")
        x = x - 1
        print("Lifes Remaining: ", x)
        continue
    elif var1=="Water" and var2==3:
        print("Pc Chose: Water")
        var4=var4+1
        print("Pc won try again!!")
        x = x - 1
        print("Lifes Remaining: ", x)
        continue
    elif var1=="Gun" and var2==1:
        print("Pc Chose: Gun")
        var4=var4+1
        print("Pc won try again!!")
        x = x - 1
        print("Lifes Remaining: ", x)
        continue
    elif var1=="Gun" and var2==2:
        print("Pc Chose: Gun")
        var3=var3+1
        print("You won play again!!")
        x = x - 1
        print("Lifes Remaining: ", x)
        continue
    else:
        print("Invalid Input..Try Again")
        continue
    