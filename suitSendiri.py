class Suit:
    
    def __init__(self): 
        """ The beginning of the Rock, Paper, Scissors game :)"""
        self.players_score = 0
        self.computers_score = 0
        print("...Rock...")
        print("...Paper...")
        print("...Scissors...")

    def GamePlay(self): 
        """ One set of gameplay in order """
        print(self.PlayerMoves())
        print(self.Scoring())
        print(f"Player's score : {s.players_score}")
        return f"Computer's {s.computers_score} "
        
    def PlayerMoves(self): 
        """ The player makes his/her move """
        move_set = ['rock' , 'paper' , 'scissors']
        players_move = input("Make your move : ")
        self.players_move = players_move
        while players_move not in move_set:
            print("PLease answer me with rock or paper or scissors")
            players_move = input("Make your move : ")
            if players_move in move_set:
                break
        print(f"{players_move} is the player's move")
        from random import choice
        comps_move = choice(move_set)
        self.comps_move = comps_move
        return (f"{comps_move} is the computer's move") 

    def Scoring(self): 
        """ System to determine who wins """
        if self.players_move == self.comps_move:
            return "It's a tie"
        elif self.players_move == "rock":
            if self.comps_move == "paper":
                self.computers_score += 1
                return "Computer wins"
            else:
                self.players_score += 1
                return "Player wins"
        elif self.players_move == "paper":
            if self.comps_move == "scissors":
                self.computers_score += 1
                return "Computer wins"
            else:
                self.players_score += 1
                return "Player wins"       
        elif self.players_move == "scissors":
            if self.comps_move == "rock":
                self.computers_score += 1
                return "Computer wins"
            else:
                self.players_score += 1
                return "Player wins"
    
    def WannaContinue(self): 
        """ System to determine wether the player wants to continue or not """
        answer = input("Do you want to continue(y/n) : ")
        while answer == "y":
            print(self.GamePlay())
            answer = input("Do you want to continue(y/n) : ")
            if answer == 'no':
                break 
        return "Thank you for playing with me"

s = Suit()
print(s.PlayerMoves())
print(s.Scoring())
print(f"Player's score : {s.players_score}")
print(f"Computer's {s.computers_score} ")
print(s.WannaContinue())