import random #import module random


def play_chicago():
    rounds = 2 #definition of round base
    points = 0 #base count of points
    print("Running playing Chicago")
    while rounds < 13:
        print("Round number ", rounds)
        #usage of random function to asign random numbers between 1 to 6
        first_dice = random.randint(1,6)
        second_dice = random.randint(1,6)
        print("Dice 1 number: ",first_dice)
        print("Dice 2 number: ", second_dice)
        if (first_dice+second_dice)==rounds:
            points+=1
            print("You won a point, your current points are: ",points)
        else:
            print("no points, your current points are: ", points)

        flag = input("Do you want to play again, enter 'yes' to continue: ").lower() #Flag if repeat the game or not lower case
        if flag == "yes":
            rounds+=1
        else:
            print("The game is over and your points are: ",points)
            return

    print("End of the Game")
    if rounds==13: #recap of total points after round 12
        print("Total point is: ", points)



play_chicago() #execution of function