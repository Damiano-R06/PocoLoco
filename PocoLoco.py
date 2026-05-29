#Poco Loco Dice Game

import random

#Creating number to dice

dice_pics = {
    1: [
        " ----- ",
        "|     |",
        "|  o  |",
        "|     |",
        " ----- "
    ],
    2: [
        " ----- ",
        "| o   |",
        "|     |",
        "|   o |",
        " ----- "
    ],
    3: [
        " ----- ",
        "| o   |",
        "|  o  |",
        "|   o |",
        " ----- "
    ],
    4: [
        " ----- ",
        "| o o |",
        "|     |",
        "| o o |",
        " ----- "
    ],
    5: [
        " ----- ",
        "| o o |",
        "|  o  |",
        "| o o |",
        " ----- "
    ],
    6: [
        " ----- ",
        "| o o |",
        "| o o |",
        "| o o |",
        " ----- "
    ]
}
rules ='''
POCO LOCO: RULES & INSTRUCTIONS\n
RULES:
1. Objective: Be the first player to lose all your chips.
2. Chips: Each player starts with any amount of chips that you choose.
3. Gameplay is turn-based, played over rounds, until one player has no chips left.\n
SETUP:
- Player order is randomized at the start of each round.\n
GAMEPLAY:
1. Whoever is first in order has the opportunity to roll up to three times in the round.
2. If your not first to roll you can only roll as many times as the player before you.
3. Dice are ranked from best to worst:
   - PoCo!: 4, 5, 6
   - Three-of-a-kind (e.g., 6, 6, 6 or 1, 1, 1)
   - Loco!: 1, 2, 3
   - All other rolls: Score based on:
     - 1 = 100, 6 = 60, 2 = 2, 3 = 3, 4 = 4, 5 = 5
4. Players after you can roll as many times as you did.\n
SCORING:
- At the end of the round, determine the highest and lowest rolls.
- Chips are given to the lowest-scoring player as follows:
  - 1 chip: Winner's roll is a point total.
  - 2 chips: Winner rolled Loco! (1, 2, 3).
  - 3 chips: Winner rolled three-of-a-kind.
  - 4 chips: Winner rolled PoCo! (4, 5, 6).\n
TIE-BREAKING:
- Ties for highest or lowest rolls are broken randomly.
GAME END:
- The first player to lose all their chips wins.
- If no one has 0 chips, another round begins.'''


help = input('Type "y" if you would like to know the rules. ')
if help == 'y':
    print(rules)




chips = int(input("How many chips: "))
player_name = input('What is your name? ')

#93-
bot_name = ["Alice", "Bob", "Charlie", "John", "Eva", "Frank", "Grace", "Hannah", "Isaac", "Jack", "Murph"]
name = random.randint(0,len(bot_name)-1)
C1 = bot_name[name]
bot_name.pop(name)

name = random.randint(0,len(bot_name)-1)
C2 = bot_name[name]
bot_name.pop(name)

name = random.randint(0,len(bot_name)-1)
C3 = bot_name[name]
bot_name.pop(name)

players = [player_name, C1, C2, C3]
print(f"Hi {player_name}, your opponents will be {C1}, {C2} and {C3}")

chipcount = {player_name: chips, C1: chips, C2: chips, C3: chips}
rounds = 1
game = True


    



def dice_roll(user):
    roll = []
    for i in range(3):
        roll.append(random.randint(1,6))
    roll.sort()

    for i in range(5):
        print()
        for j in range(3):
            test = dice_pics[roll[j]]
            print(test[i], end=" ")
    print("")
    if roll == [1,2,3]:
        print('Score: Loco!')
        input('Press enter to continue: ')
        print('----------------------------')
        user.append(300)
    elif roll == [4,5,6]:
        print('Score: Poco!')
        input('Press enter to continue: ')
        print('----------------------------')
        user.append(400)
    elif roll[0] == roll[1] == roll[2]:
        print('Score: Three-of-a-kind!')
        input('Press enter to continue: ')
        print('----------------------------')
        user.append(300 + roll[0])
    else:
        x = 0
        for i in range(3):
            if roll[i-1] == 1:
                x += 99
            if roll[i-1] == 6:
                x += 54
        print(f'Score: {sum(roll) + x}')
        user.append(sum(roll) + x)


def game_loop():

    starting_order = [1,2,3,4]    

    player_pos = random.randint(1,4)
    starting_order.remove(player_pos)

    C1_pos = starting_order[random.randint(0,len(starting_order)-1)]
    starting_order.remove(C1_pos)

    C2_pos = starting_order[random.randint(0,len(starting_order)-1)]
    starting_order.remove(C2_pos)

    C3_pos = starting_order[random.randint(0,len(starting_order)-1)]
    starting_order.remove(C3_pos)
    #this can be simplified but for the sake of simplicity it is not

    #testing values, remove string
    rollp = [player_name]
    roll1 = [C1]
    roll2 = [C2]
    roll3 = [C3]

    order = {player_pos:rollp, C1_pos:roll1, C2_pos:roll2, C3_pos:roll3}

    turn = 3
    
    for i in range(len(order)):
        input('Press enter to continue: ')
        print('----------------------------')
        print(f"Player {order[i+1][0]}'s turn: ")
        if order[i+1] != rollp:
            turn = loop(order[i+1],turn,1)
        else:
            turn = loop(order[i+1],turn,0)
    score(order)

# Loop to set the amount of turns for the round
def loop(user,turn, ai_check):
    if turn == 1:
        availble_turn = 0
# availble_turn keeps track of how many turns were used
    availble_turn = 1
    for i in range(turn):
        dice_roll(user)
        if turn == i + 1:
            break
        elif choice(ai_check, user) == "n": 
            break
        
        availble_turn += 1
    if availble_turn == 0:
        availble_turn = turn
    return availble_turn


def choice(ai_check, user):
    if ai_check == 0:
        valid = True
        while valid:
            choice = input('Would you like to roll again? y/n: ')
            if choice == "y":
                user.pop(-1)
                return "y"
            elif choice == "n":
                return "n"
            else:
                print("Invalid input")
                valid = True
    else:
        current_score = user[-1]  # AI's current score
        
        # AI's decision logic based on the current score:
        #Checks chances to improve their score
        if current_score < 100:
            user.pop(-1)  
            print(f"{user[0]} rolled again.\n")
            return "y"
        elif 100 <= current_score < 300:
            chance = random.random()
            if chance < 0.5:  # 50% chance to reroll
                user.pop(-1)
                print(f"{user[0]} rolled again.\n")
                return "y"
            else:
                print(f"{user[0]} decided to keep their current score.\n")
                return "n"
        else:
            print(f"{user[0]} decided to keep their current score.\n")
            return "n"


def score(getscore):
    score = []
    priority = []
    for i in range(len(getscore)):
        score.append(getscore[i + 1])
    for i in range(4):
        x = getscore[i+1]
        priority.append(x[-1])
    priority.sort(reverse=True)
#Tiebreaker/determine winner:
    tie_w = []
    tie_l = []
#For ties (winner)
    if priority[0] == priority[1]:
        for i in getscore:
            if getscore[i][1] == priority[0]:
                tie_w.append(getscore[i][0])
                for i in range(4):
                    if score[i][1] == priority[0]:
                        winner = score[i][0]
                        a1 = i    
        print(f'There was a tie in the winners between {" and ".join(tie_w)} random tiebreaker enabled.')
        winner = tie_w[random.randint(0,len(tie_w)-1)]

#Normal(winner)
    else:
        for i in range(4):
            if score[i][1] == priority[0]:
                winner = score[i][0]
                a1 = i    
#For ties (loser)   
    if priority[-1] == priority[-2]:
        for i in getscore:
            if getscore[i][1] == priority[-1]:
                tie_l.append(getscore[i][0])
        #print(f'There was a tie in the losers between {' and '.join(tie_l)}, random tiebreaker enabled.')
        print(f'There was a tie in the losers between {" and ".join(tie_l)}, random tiebreaker enabled.')
        loser = tie_l[random.randint(0,len(tie_l)-1)]
#Normal (loser)   
    else:
        for i in range(4):
            if score[i][1] == priority[-1]:
                loser = score[i][0]
   


    print("Winner:", winner)
    print('Loser:', loser,'\n')

#Win cases. 

    if score[a1][1] == 400:
        loss = 4  
    elif 300 < score[a1][1] < 400:
        loss = 3
    elif score[a1][1] == 300:
        loss = 2
    else:
        loss = 1
    
    chipcount[player_name] -= loss
    chipcount[C1] -= loss
    chipcount[C2] -= loss
    chipcount[C3] -= loss
    chipcount[loser] += 3*loss + loss

    print('Chipcounts after the round:')
    for i in players:
        print(f"{i}: {chipcount[i]}")
    print('')


while game:

    staff = input('Press enter to start the next round, type "exit" to stop the game or type "help" for the rules again. ')
    if staff == 'exit':
        game = False
        break
    if staff == 'help':
        print(rules)
        input('Press enter to contiue the game. ')

    print('+',6*"-"+len(str(rounds))*'-',"+" )
    print(f'| Round {rounds} |')
    print('+',6*"-"+len(str(rounds))*'-',"+" )

    print('Current Chipcounts:')
    for i in players:
        print(f"{i}: {chipcount[i]}")
    print('')

    game_loop()

    rounds += 1
    winners = []
    for i in chipcount.keys():
        if chipcount[i] <= 0:
            winners.append(i)
            game = False
    if game == False:
        print('')
        print("------------------")
        print('Game Over\n')
        #print(f"Congrats to {" and ".join(winners)} for winning.\n")
        print(f"Congrats to {' and '.join(winners)} for winning.\n")

        print("Final chipcount:")
        for i in chipcount.keys():
            if chipcount[i] < 0:
                print(f"{i}: 0")
            else:
                print(f"{i}: {chipcount[i]}")
            


