name = input("Type your name ")
print("welcome",name, "to this adventure ")

answer = input("You were travelling in your car in the mountains and your car broke down you can travel in two directions right or left type right or left to go in that direction ")
if answer == "left":
    answer = input("you found a river you can follow it to reach the city choose follow ")
    if answer == "follow":
        answer = input("YOU WIN ")
elif answer == "right":
    answer = input("you travel denser into the forest now you and see a tiger choose run to run away and choose fight to fight the tiger ")
    if answer =="run":
        answer =input("The tiger catches upto you and you die ") 
    elif answer =="fight":  
        answer = input("the tiger overpowers you and you die ")  
    else:
        print("you freeze in fear seeing the tiger and the tiger enjoys you as a lunch")    
else:
    print("not a valid option")   