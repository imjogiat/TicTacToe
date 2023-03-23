#Class for creating the gamespace
# returns list of strings to be printed on terminal for game board

class GameSpace(object):
    def MakeGameSpace():
        #change to list of lists
        TopEntryRow="  |  |  "
        TopLineRow="--|--|--"
        MidEntryRow="  |  |  "
        MidLineRow=TopLineRow
        BotmEntryRow="  |  |  "
        TicTacToeSpace=[list(TopEntryRow),list(TopLineRow),list(MidEntryRow),list(MidLineRow),list(BotmEntryRow)]
        #list of list of characters for board. strings are immutable, list elements can be changed
        return TicTacToeSpace
        #return a list of lists
#Class for taking user input for each player and adding it to the board
#returns a list of strings with the updated board after the move, and each players last move
    def TakeUserInput(BoardList):
        GameTurn=0
        EndOfGame=False
        while EndOfGame==False:
            #Input to the function, BoardList is list of lists
            #input board is a list of strings
            #input squares:
            #BoardList[0][0], [0][3], [0][6], [2][0], [2][3], [2][6], [4][0], [4][3], [4][6]
            #aside: later on try to move this above the while loop
            InputSquares={"top left":[0,0], "top center":[0,3], "top right":[0,6], "middle left":[2,0], "center":[2,3], "middle right":[2,6], "bottom left":[4,0], "bottom center":[4,3], "bottom right":[4,6]}
            print("\nWhere would you like to place the x or o?\n(top left, top center, top right, \nmiddle left, center, middle right, \nbottom left, bottom center, bottom left)")
            Player1Move= str(input())
            if Player1Move.lower() not in InputSquares:
                print("\ninvalid entry, misspelled\n\n")
            
            else:
                InputRow=InputSquares[Player1Move.lower()][0]
                #InputRow is the integer for the row to input the user move
                InputColumn=InputSquares[Player1Move.lower()][1]
                #InputColumn is the integer for the column to input the user move
                #put an x on the spot corresponding to InputRow and InputColumn
                #if(GameTurn%2==0 and BoardList[InputRow][InputColumn]!="O"):
            if(GameTurn%2==0):
                if BoardList[InputRow][InputColumn]==" ":
                    BoardList[InputRow][InputColumn]="X" 
                    LastTurnPlayed="X"
                else:
                    print("\nThis is spot is already occupied, pick another")
                    GameTurn=GameTurn+1
                
            #elif (GameTurn%2!=0 and BoardList[InputRow][InputColumn]!="X"):
            elif(GameTurn%2!=0):
                if BoardList[InputRow][InputColumn]==" ":
                    BoardList[InputRow][InputColumn]="O"
                    LastTurnPlayed="O"
                else:
                    print("This is spot is already occupied, pick another")
                    GameTurn=GameTurn+1

             #print the board before checking victory
            for i in range(len(BoardList)):
                print("".join(BoardList[i]))
            #set LastPiecePlayed as X or O depending on what the last move wass
            #check if there are any victory combinations of the last character
            #victory combination are coordinates corresponding to 3 in a row of the LastPiecePlayed
            #victory combinations:
            #[0,0]+[0,3]+[0,6]  ----
            #[2][0]+[2][3]+[2][6] ----
            #[4][0]+[4][3]+[4][6] ----
            #[0][0]+[2][0]+[4][0] ----
            #[0][3]+[2][3]+[4][3] ----
            #[0][6]+[2][6]+[4][6] ----
            #[0][0]+[2][3]+[4][6] ----
            #[4][0]+[2][3]+[0][6] ----
            VictCondtn1=BoardList[0][0]==LastTurnPlayed and BoardList[0][3]==LastTurnPlayed and BoardList[0][6]==LastTurnPlayed
            VictCondtn2=BoardList[2][0]==LastTurnPlayed and BoardList[2][3]==LastTurnPlayed and BoardList[2][6]==LastTurnPlayed
            VictCondtn3=BoardList[4][0]==LastTurnPlayed and BoardList[4][3]==LastTurnPlayed and BoardList[4][6]==LastTurnPlayed
            VictCondtn4=BoardList[0][0]==LastTurnPlayed and BoardList[2][0]==LastTurnPlayed and BoardList[4][0]==LastTurnPlayed
            VictCondtn5=BoardList[0][3]==LastTurnPlayed and BoardList[2][3]==LastTurnPlayed and BoardList[4][3]==LastTurnPlayed
            VictCondtn6=BoardList[0][6]==LastTurnPlayed and BoardList[2][6]==LastTurnPlayed and BoardList[4][6]==LastTurnPlayed
            VictCondtn7=BoardList[0][0]==LastTurnPlayed and BoardList[2][3]==LastTurnPlayed and BoardList[4][6]==LastTurnPlayed
            VictCondtn8=BoardList[4][0]==LastTurnPlayed and BoardList[2][3]==LastTurnPlayed and BoardList[0][6]==LastTurnPlayed
                
            #if (VictCondtn1 or VictCondtn2 or VictCondtn3 or VictCondtn4 or VictCondtn5 or VictCondtn6 or VictCondtn7 or VictCondtn8):
            Victory=VictCondtn8 or VictCondtn1 or VictCondtn2 or VictCondtn3 or VictCondtn4 or VictCondtn5 or VictCondtn6 or VictCondtn7
            if Victory:    
                EndOfGame=True
                print("Congratulations, the player with",LastTurnPlayed,"wins!")
            #if condition to check for a draw
            #if all spaces on the board are occupied, if there are no coordinates with " "
            #if all of the spaces are not equal to " ". [0][0]and ....[4][6]
            DrawCondtn=BoardList[0][0]!=" " and BoardList[0][3]!=" " and BoardList[0][6]!=" " and BoardList[2][0]!=" " and BoardList[2][3]!=" " and BoardList[2][6]!=" " and BoardList[4][0]!=" " and BoardList[4][3]!=" " and BoardList[4][6]!=" "
            if DrawCondtn and (Victory==False):
                EndOfGame=True
                print("Game is drawn, no one wins")

            GameTurn=GameTurn+1

        return BoardList

MyGameSpaceBoard=GameSpace.MakeGameSpace()
#MyGameSpaceBoard is set to a list of lists, each list element is the row of the board
GameSpace.TakeUserInput(MyGameSpaceBoard)
#Input to Take User Input is a list of lists, function TakeUserInput prompts for input and updates the list of lists

#*******This segment prints the entire board as a string on command line
# #for loop to convert each element to string
#changes each element in the list to a string instead of an element list and prints it
# for i in range(len(MyGameSpaceBoard)):
#     print("".join(MyGameSpaceBoard[i]))
