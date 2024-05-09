import time
import random




totalcpuchoice = ["r","p","s"]





while True:
    
    userinput = input("Please pick rock, paper, or sissors by either typing it out or by typing R, P, or S: ").lower()
    computernumber = random.randint(0,2)
    cpufinalchoice = totalcpuchoice[computernumber]
    
    print("......")
    time.sleep(0.60)    
    print(cpufinalchoice)

    if userinput == "r" or userinput == "rock":
        if cpufinalchoice == "r" or cpufinalchoice == "rock":
            print("You Tied")
        elif cpufinalchoice == "p" or cpufinalchoice == "paper":
            print("You Lose!!")
        elif cpufinalchoice == "s" or cpufinalchoice == "scissors":
            print("You Win")

    elif userinput == "p" or userinput == "paper":
        if cpufinalchoice == "r" or cpufinalchoice == "scissors":
            print("You Win!!")
        elif cpufinalchoice == "p" or cpufinalchoice == "paper":
            print("You Tie!!")
        elif cpufinalchoice == "s" or cpufinalchoice == "rock":
            print("You Lose")

    elif userinput == "s" or userinput == "scissors":
        if cpufinalchoice == "r" or cpufinalchoice == "rock":
            print("You Lose")
        elif cpufinalchoice == "p" or cpufinalchoice == "paper":
            print("You Win!!")
        elif cpufinalchoice == "s" or cpufinalchoice == "scissors":
            print("You Tie")
            play_again = input("Play again? (y/n or yes/no): ").lower()
            if play_again.lower() != "n" and play_again.lower() !=  "no":
                    continue
            else:
                break
        

    else:
        print("That isn't an option, Try again!")
        play_again = input("Play again? (y/n or yes/no): ").lower()
        if play_again.lower() != "n" and play_again.lower() !=  "no":
                continue
        else:
            break


