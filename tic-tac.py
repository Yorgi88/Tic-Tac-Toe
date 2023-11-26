from tkinter import *
import random


# here we will make use of functional programming through the use of functions

def next_turn(row, column):
    global player

    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player

            # check if there is a winner
            if check_winner() is False:
                # then we switch players
                player = players[1]
                label.config(text=(players[1] + ' turn'))
            # we now check if there is a winner
            elif check_winner() is True:
                label.config(text=(players[0] + ' wins'))
            # if there is a tie
            elif check_winner() == 'Tie':
                label.config(text=('Tie!'))


        else:
            # if is not players[0] turn , then it will be 1's turn
            buttons[row][column]['text'] = player

            # check if there is a winner
            if check_winner() is False:
                # then we switch players
                player = players[0]
                label.config(text=(players[0] + ' turn'))
            # we now check if there is a winner
            elif check_winner() is True:
                label.config(text=(players[1] + ' wins'))
            # if there is a tie
            elif check_winner() == 'Tie':
                label.config(text=('Tie!'))


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg='green')
            buttons[row][1].config(bg='green')
            buttons[row][2].config(bg='green')

            return True
            # the vertical section next, or the column section
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":

            buttons[0][column].config(bg='green')
            buttons[1][column].config(bg='green')
            buttons[2][column].config(bg='green')
            return True
    # diagonal win conditions next
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":

        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":

        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='yellow')
        return "Tie"
    else:
        return False





#     as in no winner and no tie


# we need to check the text of each button in the row
# tis follows the format of [
# [0,0] [0,1] [0,2],
# [1,0] [1,1] [1,2],
# [2,0] [2,1] [2,2]
# ]

def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            #we will check the texts of each buttons
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + ' turn')
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg='#F0F0F0')


# def player_scores():
#     global firstPlayer1
#     global secondPlayer2
#
#     if players[0] and next_turn(row, column) is True:
#         firstPlayer1 += 1
#         return "Player1 score is: ", firstPlayer1
#     elif players[1] and next_turn(row, column) is True:
#         secondPlayer2 += 1
#         return  "Player2 score is", secondPlayer2





window = Tk()
window.title("Tic-Tac-Toe")
players = ["x", "o"]
player = random.choice(players)

# next we need buttons 9
buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# we will need a label to display whose turn it is
label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side='top')

# we create a reset button next
reset_button = Button(text="reset", font=('consolas', 20), command=new_game)  # from the new_game function we decalred
reset_button.pack(side='top')

# next we create a grid like display for our buttons
frame = Frame(window)
frame.pack()
# so next we use for loops to actually integrate the button with the 9 box grid
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

# since we have 3 rows and 3 columns







window.mainloop()

# this creates the interface for the game
