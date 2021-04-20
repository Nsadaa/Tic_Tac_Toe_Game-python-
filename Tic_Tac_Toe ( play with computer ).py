from random import randrange

board = {"1":"","2":"","3":"",  #Dictionary For game board
         "4":"","5":"","6":"",
         "7":"","8":"","9":""}

board_keys = []  #

for key in board:
    board_keys.append(key)


def game_board(board):                                              #Create board
    print(board["1"] + " | " + board["2"] + " | " + board["3"])
    print("--+---+--")
    print(board["4"] + " | " + board["5"] + " | " + board["6"])
    print("--+---+--")
    print(board["7"] + " | " + board["8"] + " | " + board["9"])

def game():

    turn = 'x'
    count = 0

    for i in range(10):

        game_board(board)

        print("its your turn", turn , "move to which place")

        move = input("Enter place : ")    #get user input

        if board[move] == "":    # assume user input values for the dictionary key
            board[move] = turn
            count += 1

        else:
            print("Its Alredy Taken ", turn, "move to which place")
            continue


        if count >= 5:                                          # check user win or not
            if board["1"] == board["2"] == board["3"] != "":
                game_board(board)
                print("win by",turn)
                break

            elif board["4"] == board["5"] == board["6"] != "":
                game_board(board)
                print("win by", turn)
                break

            elif board["7"] == board["8"] == board["9"] != "":
                game_board(board)
                print("win by", turn)
                break

            elif board["1"] == board["4"] == board["7"] != "":
                game_board(board)
                print("win by", turn)
                break

            elif board["2"] == board["5"] == board["8"] != "":
                game_board(board)
                print("win by", turn)
                break

            elif board["3"] == board["6"] == board["9"] != "":
                game_board(board)
                print("win by", turn)
                break

            elif board["1"] == board["5"] == board["9"] != "":
                game_board(board)
                print("win by", turn)
                break

            elif board["3"] == board["5"] == board["7"] != "":
                game_board(board)
                print(" Congratulations win by", turn)
                break

        if count == 9:
            print("\ngame tied\n")
            break

#  computer input part.................

        print("\nits Computer Turn.....\n")
        xx = []                               #this set store random values
        random_count = 0        #this count the make condition for stop the wile loop
        if turn == "x":
            turn = "o"

            while random_count <=10:                # get random values
                xx.append(str(randrange(1,9)))
                random_count += 1

            for test_this in xx:            #assume random values to dictionary key & check wheather they are empty or not
                if board[test_this] == "":
                    board[test_this] = turn
                    del xx[:]          #cler set values for next checkings
                    random_count = 0   # clear variable value for next checkings
                    count += 1
                    break
                else:
                    continue

        else:
            turn = "x"

            while random_count <= 10:
                xx.append(randrange(1, 9))
                random_count += 1

            for vc in xx:
                if board[vc] == "":
                    board[vc] = turn
                    del xx[:]
                    random_count = 0
                    count += 1
                    break

                else:
                    continue

        if count >= 5:                                   #check computer move win or not
            if board["1"] == board["2"] == board["3"] != "":
                game_board(board)
                print("win by",turn)
                break

            elif board["4"] == board["5"] == board["6"] != "":
                game_board(board)
                print("win by", turn)
                break

            elif board["7"] == board["8"] == board["9"] != "":
                game_board(board)
                print("win by", turn)
                break

            elif board["1"] == board["4"] == board["7"] != "":
                game_board(board)
                print("win by", turn)
                break

            elif board["2"] == board["5"] == board["8"] != "":
                game_board(board)
                print("win by", turn)
                break

            elif board["3"] == board["6"] == board["9"] != "":
                game_board(board)
                print("win by", turn)
                break

            elif board["1"] == board["5"] == board["9"] != "":
                game_board(board)
                print("win by", turn)
                break

            elif board["3"] == board["5"] == board["7"] != "":
                game_board(board)
                print(" Congratulations win by", turn)
                break

        if turn=="o":   #change turn value for user ( turn = "x" )
            turn = "x"

        else:
            turn = "o"

        if count == 9:
            print("\nGame tied\n")
            break


    restart = input("Want to play again :") #check the input key and execute below code
    if restart =="y":
        for check_keys in board_keys:  #clear the board key values to start again the game
            board[check_keys] = ""


        game()  #run the game function again

    else:
        print("\nThank you Have a Nice Day.........")



game()  # calling game function to start the in the begining




