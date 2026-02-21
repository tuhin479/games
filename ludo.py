import random
dicerolling=True
while dicerolling:
    print(random.randint(1,6))
    playagain=input('do want to play this game[y/n]:')
    if playagain=='y':
        continue
    else:                           
            print('game over')
            break











