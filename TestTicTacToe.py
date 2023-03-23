class def_game_space(object):
    #_o|_o|_o
    #_x|_x|_x
    # o| x| o
    space7="_7|"
    space8="_8|"
    space9="_9 "
  

    space4="_4|"
    space5="_5|"
    space6="_6 "
    

    space1=" 1|"
    space2=" 2|"
    space3=" 3 "
    

    PLAYER1=""
    PLAYER2=""
    game_space={}
    game_space={7:space7, 8:space8, 9:space9, 4:space4, 5:space5, 6:space6, 1:space1, 2:space2, 3:space3}
    last_move=" "

    #Welcome screen, prompts for player names
    def welcome_players(self):

        print("Welcome to TicTacToe\nPlease use the number pad to choose a space on the game board\n")
        correct_players="no"
        self.display_game_space(self)

        while correct_players.lower()!="yes":
            print("Player 1, please enter your name\n")
            self.PLAYER1=str(input())
            print("\n-----------------------------------------------\nPlayer 2, please enter your name")
            self.PLAYER2=str(input())
            print("--------------------------------------------\nIs this correct? yes or no\n","Player1: ",self.PLAYER1,"\n Player2: ",self.PLAYER2)
            correct_players=str(input())
            print("\n")
    
        return None
    
    def display_game_space(self):

        #creates a dictionary where the potential user input is the number string and the element is the board space where x or o is placed
        
        # self.game_space={7:self.space7, 8:self.space8, 9:self.space9, 4:self.space4, 5:self.space5, 6:self.space6, 1:self.space1, 2:self.space2, 3:self.space3}

        # print(" \t",game_space[7],game_space[8],game_space[9],"\n","\t",game_space[4], game_space[5],game_space[6],"\t",game_space[1],game_space[2],game_space[3])
        print(" \t",self.game_space[7],self.game_space[8],self.game_space[9],"\n","\t",self.game_space[4], self.game_space[5],self.game_space[6],"\n","\t",self.game_space[1],self.game_space[2],self.game_space[3])
        # ,"\t",game_space[1], game_space[2],game_space[3])

        return None

    #prompts players for their moves and runs the game
    def players_move(self):

        game_turn=0
        player_turn=1
        game_over="n"

        while game_over!="y":
            #Condition to determine that it is player 1's turn
            if player_turn==1 and game_over!="y":
                print("\n\n","It is ",self.PLAYER1,"'s"," turn")
                self.display_game_space(self)
                print("\n",self.PLAYER1, "Please select a space (1-9) on the board for your X")
                space_number=int(input())

                if "o" in self.game_space[space_number]:
                    print("sorry this space is already chosen, choose another space")
                    player_turn=1
                #     space_confirm="y"    
                # else:    
                #     while space_confirm!="y":
                #         print(self.PLAYER1, "you have chosen space",space_number,"\n","Is this correct (y or n)?")
                #         space_confirm=str(input())

                #         if space_confirm != "y" and space_confirm !="n":
                #                 print("invalid entry")
                #         if space_confirm == "n":
                #                 print("selection cancelled")
                else:
                    self.game_space[space_number]= self.game_space[space_number][0:1]+"x"+self.game_space[space_number][2]
                    player_turn=2
                game_turn=game_turn+1

                #checks victory after player 1's move
                game_over=self.victorycheck(self)
                self.display_game_space(self)

            #Condition to determine that it is Player 2's turn
            if player_turn==2 and game_over!="y": 
                print("\n\n","It is ",self.PLAYER2,"'s"," turn")
                self.display_game_space(self)
                print(self.PLAYER2, "Please select a space (1-9) on the board for your O")
                space_number=int(input())

                if "x" in self.game_space[space_number][1]:
                    print("sorry this space is already chosen, choose another space")
                    player_turn=2
                #    space_confirm="y"
                # else:    
                #     while space_confirm!="y":
                #         print(self.PLAYER2, "you have chosen space",space_number,"\n","Is this correct (y or n)?")
                #         space_confirm=str(input())

                #         if space_confirm != "y" and space_confirm !="n":
                #                 print("invalid entry")
                #         if space_confirm == "n":
                #                 print("selection cancelled")
                else:
                    self.game_space[space_number]= self.game_space[space_number][0:1]+"o"+self.game_space[space_number][2]
                    player_turn=1
                game_turn=game_turn+1
                #self.display_game_space(self)

                #checks victory after player 2's move
                game_over=self.victorycheck(self)
                self.display_game_space(self)


            #Check if victory condition is met and game is over
            #game_over=self.victorycheck(self)
            #turn 1, player 1, turn 2, player 2- odd turns player 1, even turns player 2
            game_turn=game_turn+1

            #the shortest number of turns for any player to win is 6, in this case when game_turn ==5 or more
            # if game_turn==6 or game_turn>6:
            #     game_over="y"
            #     self.victorycheck(self)
            
            # game_over=self.victorycheck(self)

        return None

    #checks if a victory condition is met
    #returns y or n if 
    #check if an x or o is in the center then check if the same character is above and below, or left and right or top left and bottom right or top right and bottom left (4 conditions)
    #check if and x or o is across the top row, bottom row, left row or right row
    #
    def victorycheck(self):
        
        end_of_game="n"
        draw="n"

        #Check for draw
        # for i in self.game_space:
        #     if self.game_space[i]=="o" or self.game_space[i]=="x":
        #         draw="y"
        #         print("The game is drawn. No one wins")
        #     else:
        #         draw="n"
            

        #checks the center column and surrounding spots for three x's in a row
        if self.game_space[5][1] =="x": 
            if self.game_space[8][1] =="x" and self.game_space[2][1] =="x":
                end_of_game="y"
                print("The winner is: ",self.PLAYER1)
            
            if self.game_space[4][1] =="x" and self.game_space[6][1] =="x":
                end_of_game="y"
                print("The winner is: ",self.PLAYER1)
            
            if self.game_space[7][1] =="x" and self.game_space[3][1] =="x":
                end_of_game="y"
                print("The winner is: ",self.PLAYER1)

            if self.game_space[9][1] =="x" and self.game_space[1][1] =="x":
                end_of_game="y"
                print("The winner is: ",self.PLAYER1)

#------------------- check the outer rows for three x's in a row-------------------------------------
        if self.game_space[1][1]=="x":
            if self.game_space[4][1]=="x" and self.game_space[7][1]=="x":
                end_of_game="y"    
                print("The winner is: ",self.PLAYER1)
            
            if self.game_space[2][1]=="x" and self.game_space[3][1]=="x":
                end_of_game="y"    
                print("The winner is: ",self.PLAYER1)
        
        if self.game_space[9][1]=="x":
            if self.game_space[8][1]=="x" and self.game_space[7][1]=="x":
                end_of_game="y"    
                print("The winner is: ",self.PLAYER1)

            if self.game_space[6][1]=="x" and self.game_space[3][1]=="x":
                end_of_game="y"    
                print("The winner is: ",self.PLAYER1)

#--------------------------------------------------------------------------------------------------
        #checks for o's victory combos
        if self.game_space[5][1] =="o": 
            if self.game_space[8][1] =="o" and self.game_space[2][1] =="o":
                end_of_game="y"
                print("The winner is: ",self.PLAYER2)
            
            if self.game_space[4][1] =="o" and self.game_space[6][1] =="o":
                end_of_game="y"
                print("The winner is: ",self.PLAYER2)
            
            if self.game_space[7][1] =="o" and self.game_space[3][1] =="o":
                end_of_game="y"
                print("The winner is: ",self.PLAYER2)

            if self.game_space[9][1] =="o" and self.game_space[1][1] =="o":
                end_of_game="y"
                print("The winner is: ",self.PLAYER2)

        #check the outer rows for three o's in a row
        if self.game_space[1][1]=="o":
            if self.game_space[4][1]=="o" and self.game_space[7][1]=="o":
                end_of_game="y"    
                print("The winner is: ",self.PLAYER2)
            
            if self.game_space[2][1]=="o" and self.game_space[3][1]=="o":
                end_of_game="y"    
                print("The winner is: ",self.PLAYER2)
        
        if self.game_space[9][1]=="o":
            if self.game_space[8][1]=="o" and self.game_space[7][1]=="o":
                end_of_game="y"    
                print("The winner is: ",self.PLAYER2)

            if self.game_space[6][1]=="o" and self.game_space[3][1]=="o":
                end_of_game="y"    
                print("The winner is: ",self.PLAYER2)
        
        #Check for draw
        

        # self.display_game_space(self)
        # print("\n")

        return end_of_game

    

#display welcome screen and prompt for player names
tictacto_game_intro=def_game_space.welcome_players(def_game_space)

#display the game board 
# def_game_space.display_game_space(def_game_space)

#runs the game, prompting  for user input and updating the board
def_game_space.players_move(def_game_space)











