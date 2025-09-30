import random


def play_chicago():
    rounds = 2
    points = 0
    print("Running playing Chicago")
    while rounds < 13:
        print("Round number ", rounds)
        first_dice = random.randint(1,6)
        second_dice = random.randint(1,6)
        print("Dice 1 number: ",first_dice)
        print("Dice 2 number: ", second_dice)
        if (first_dice+second_dice)==rounds:
            points+=1
            print("You won a point, your current points are: ",points)
        else:
            print("no points, your current points are: ", points)

        flag = input("Do you want to play again, enter 'yes' to continue: ").lower() #Flag if repeat the game or not
        if flag == "yes":
            rounds+=1
        else:
            print("The game is over and your points are: ",points)
            return

    print("End of the Game")
    if rounds==13: #recap of total points after round 12
        print("Total point is: ", points)



play_chicago()