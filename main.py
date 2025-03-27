# Complete Tic tac toe code 

win_combo = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] 

play1_loc_list = [] 
play2_loc_list = [] 

print("Welcome to Tic_tac_toe") 

board = ["1","2","3","4","5","6","7","8","9"] 

# Player names 
player1 = input("Enter the name of the first player: ") 
player2 = input("Enter the name of the second player: ") 

no_win = True 
turn = 1 

# Procedure 
def make_board(): 
    print(board[0], ":", board[1], ":", board[2]) 
    print(".........") 
    print(board[3], ":", board[4], ":", board[5]) 
    print(".........") 
    print(board[6], ":", board[7], ":", board[8]) 

# Calling the procedure 
make_board() 

while no_win: 

    while turn == 1 and no_win: 
        print("Hello", player1) 
        Xloc = int(input("Where do you want to place a cross (choose from 1-9): ")) 
        board[Xloc - 1] = "X" 
        loc_attempt = Xloc - 1 
        play1_loc_list.append(loc_attempt) 
        play1_loc_list.sort() 

        for i in range(0, len(win_combo)): 
            if win_combo[i] == play1_loc_list: 
                print(player1, " has won!") 
                no_win = False 

        make_board() 
        turn = 2 

    while turn == 2 and no_win: 
        print("Hello", player2) 
        Xloc = int(input("Where do you want to place a nought (choose from 1-9): ")) 
        board[Xloc - 1] = "0" 
        loc_attempt = Xloc - 1 
        play2_loc_list.append(loc_attempt) 
        play2_loc_list.sort() 

        for i in range(0, len(win_combo)): 
            if win_combo[i] == play2_loc_list: 
                print(player2, " has won!") 
                no_win = False 

        make_board() 
        turn = 1 