import random

bot = random.choice([-1,0,1])
you = input("Enter the Choice:")

youdict = {"S" : 1, "W" : 0, "G" : -1}
reverseddict = {1 : "Snake", 0 : "Water", -1 : "Gun"}

your = youdict[you]

print(f"Your choice: {reverseddict[your]} \n Bot choice: {reverseddict[bot]}")

if bot == your:
    print("Its an draw")
    
else:
    if (bot == 1 and your == 0):
        print("Bot Wins")

    elif (bot == 1 and your == -1):
        print("You Win")
    
    elif (bot == 0 and your == 1):
        print("You Win")
    
    elif (bot == 0 and your == -1):
        print("Bot wins")
    
    elif (bot == -1 and your == 1):
        print("Bot Wins")
    
    elif (bot == -1 and your == 0):
        print("You Wins")
        
    else:
        print("Something Went Wrong")
        
    
    


