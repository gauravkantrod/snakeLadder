import random


def start():
    #key represents the mouth of snake and value represents the tail of snake
    snake = {7:2, 13:9, 22:5, 40:27, 57:9, 72: 4, 99:91}

    #Key represents the start of ladder and calue represents the end of ladder
    ladder = {5:17, 10:23, 26:50, 49: 60, 59: 71, 80: 91}

    numberOfPlayers = int(input("Enter number of players -- "))
    playerScore = {}
    for player in range(1, numberOfPlayers+1):
        playerScore['player_'+str(player)] = 0
        
    # Flag to terminate while loop condition
    winner = False
    while not winner:
        for player in range(1, numberOfPlayers+1):
            print(f"Player {player}'s turn!")
            # Random number is generated between 1 to 6 to mimik dice.
            throwDice = random.randint(1,6)
            if (playerScore['player_'+str(player)] + throwDice) <= 100:
                playerScore['player_'+str(player)] += throwDice

                # To check if the position of player is a key in snake dictionary
                goBack = snake.get(playerScore['player_'+str(player)])
                # To check if the position of player is a key in ladder dictionary
                goFurther = ladder.get(playerScore['player_'+str(player)])

                # If players position is at snakes mouth bring that player to snakes tail position
                if goBack:
                    playerScore['player_'+str(player)] = goBack
                elif goFurther:
                    # If players position is at start of ladder bring that player to end of ladder position
                    playerScore['player_'+str(player)] = goFurther
                
            # If any of the player's reach at home/100 first declare that player winner.
            if playerScore['player_'+str(player)] == 100:
                winner = True
                print('*'*100)
                print(playerScore)
                print('*'*100)
                print(f"Player {player} is winner!!")
                # Break necessary as its while loop as it will go further to complete the loop.
                break;


start()