import os

spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}


def draw_board(spot):
    print(f" {spot[1]} | {spot[2]} | {spot[3]}")
    print(f"---|---|---")
    print(f" {spot[4]} | {spots[5]} | {spot[6]}")
    print(f"---|---|---")
    print(f" {spot[7]} | {spot[8]} | {spot[9]}")


def check_turn(tur):
    if tur % 2 == 0:
        return 'O'
    return 'X'


def check_for_win(spot):
    if (spot[1] == spot[2] == spot[3]) or (spot[4] == spot[5] == spot[6]) or (spot[7] == spot[8] == spot[9]):
        return True
    if (spot[1] == spot[4] == spot[7]) or (spot[2] == spot[5] == spot[8]) or (spot[3] == spot[6] == spot[9]):
        return True
    if (spot[1] == spot[5] == spot[9]) or (spot[3] == spot[5] == spot[7]):
        return True
    return False


print('Welcome to "Tic Tac Toe" Game😁')
playing = True
turn = 0

while playing:
    # Reset the screen
    # os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    print(f"Player {str((turn % 2) + 1)}'s Turn: Pick your spot or press 'Q' to Quit.")
    #  Get Input from Player
    choice = input()
    if choice.lower() == 'q':
        playing = False
    # Check weather the player has given the number from 1-9
    elif str.isdigit(choice) and int(choice) in spots:
        # Check weather that is taken or not
        if not spots[int(choice)] in {'X', 'O'}:
            turn += 1
            spots[int(choice)] = check_turn(turn)
        else:
            print("Take spot is taken")
    else:
        print("Please, Enter the numbers from 1 to 9")
    if check_for_win(spots):
        print(f"Player {2 if (turn % 2) == 0 else 1} Wins🎊🎉")
        playing = False
    elif turn > 8:
        print("Match is Draw")
        playing = False

print("Thanks For Playing")
