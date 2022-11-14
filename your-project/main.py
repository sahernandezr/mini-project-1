import numpy as np
import os
import time

class Game():
    def __init__(self):
        self.has_winner = False
        self.possible_wins = [[1, 2, 3],[1, 4, 7],[1, 5, 9],[2, 5, 8],[3, 5, 7], [3, 6, 9],[4, 5, 6],[7, 8, 9]]
        
    def welcome(self):
        welcome = print("Welcome! Let's play Tic Tac Toe\n********************************\nPlay against a famous cat or mouse. You never know who will go first.")
        return 
    
    def instructions(self):
        text_instructions = print("\nYour goal: Form a straight line with three of your marks.\nInstructions: Type a number from 1 to 9 to claim that space in the grid.")
        return
    
    def start_game(self):
        os.system('cls')
        game.welcome()
        game.instructions()
        board.starting()
        time.sleep(1)
        player1.user_name()
        player2.opponent_name()
        session.who_goes_first(player1,player2)
    
    def repeat(self):
        want_again = input('Do you want to play again? (Y/N): ')
        print('**********************')
        if want_again.lower()=='y':
            board.printable_spaces = [' ',]*board.spaces
            board.available_spaces = [i+1 for i in range(board.spaces)]
            session.turns_played = 0
            player2.opponent_name()
            time.sleep(1)
            session.who_goes_first(player1,player2)
            player1.occupied_spaces = []
            player2.occupied_spaces = []
            session.has_winner = False
            session.play_mechanics()
        elif want_again.lower()=='n':
            print('Goodbye!')
        else:
            print('Please type Y if you want to play again or N if you want to stop playing')
            return self.repeat()
        
class Session():
    def __init__(self):
        self.has_winner = False
        self.turns_played = 0
        self.marks = ['X', 'O']
        self.first_player = ''
        
    def who_goes_first(self, player1, player2):
        selector_turn = np.random.randint(0,2)
        if selector_turn == 0:
            first_player=player1
            player1.mark = 'X'
            player2.mark = 'O'
            player1.goes_first=True
            player2.goes_first=False
            print(f"{player1.name} goes first and plays with {session.marks[0]}")
            print(f"{player2.name}'s mark is {session.marks[1]} and goes second")
            print('**********************')
        elif selector_turn == 1:
            first_player=player2
            player2.mark = 'X'
            player1.mark = 'O'
            player2.goes_first=True
            player1.goes_first=False
            print(f"{player2.name} goes first and plays with {session.marks[0]}")
            print(f"{player1.name}'s mark is {session.marks[1]} and goes second")
            print('**********************')
        return first_player, player1.mark, player2.mark
    
    def turns(self, turns_played):
        if self.turns_played == 0: #first move of the game
            if player1.goes_first:
                self.turns_played += 1
                return player1.user_choice()
            elif player2.goes_first:
                self.turns_played +=1
                return player2.opponent_choice()
        elif self.turns_played > 0 and self.turns_played%2 == 0:
            if player1.goes_first:
                self.turns_played += 1
                return player1.user_choice()
            elif player2.goes_first:
                self.turns_played +=1
                return player2.opponent_choice()
        elif self.turns_played > 0 and self.turns_played%2 == 1:
                if player1.goes_first:
                    self.turns_played += 1
                    return player2.opponent_choice()
                elif player2.goes_first:
                    self.turns_played +=1
                    return player1.user_choice()
            
    def play_mechanics(self):
        for i in range(0,9):
            session.turns(i)
            player1.check_winner(player1.occupied_spaces)
            player2.check_winner(player2.occupied_spaces)
            if session.has_winner:
                return game.repeat()
        if session.turns_played==9:
                print('We have a tie!')
                return game.repeat()
        
class Board():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.spaces = rows*columns
        self.printable_spaces = [' ',]*self.spaces
        self.available_spaces = [i+1 for i in range(self.spaces)]
        self.possible_spaces = [i+1 for i in range(self.spaces)]

    def display(self):
        separator = '+'.join(('---',)*self.columns)
        print(' '+' | '.join([self.printable_spaces[0], self.printable_spaces[1], self.printable_spaces[2]]))
        print(separator)
        print(' '+' | '.join([self.printable_spaces[3], self.printable_spaces[4], self.printable_spaces[5]]))
        print(separator)
        print(' '+' | '.join([self.printable_spaces[6], self.printable_spaces[7], self.printable_spaces[8]]))
        print('\n**********************')
        
    def starting(self):
        separator = '+'.join(('---',)*self.columns)
        print(f" {self.possible_spaces[0]} | {self.possible_spaces[1]} | {self.possible_spaces[2]}")
        print(separator)
        print(f" {self.possible_spaces[3]} | {self.possible_spaces[4]} | {self.possible_spaces[5]}")
        print(separator)
        print(f" {self.possible_spaces[6]} | {self.possible_spaces[7]} | {self.possible_spaces[8]}")
        print('\n**********************')
        
class Player():
    def __init__(self):
        self.name = ''
        self.goes_first = False
        #self.is_winner = False
        self.mark = ''
        self.occupied_spaces = []
             
    def check_winner(self, occupied_spaces): #compare occupied spaces of each player to possible wins. If there is a match, the player wins  
        if len(occupied_spaces)>2:
            for i in range(len(game.possible_wins)):
                if game.possible_wins[i][0] in self.occupied_spaces:
                    if game.possible_wins[i][1] in self.occupied_spaces:
                        if game.possible_wins[i][2] in self.occupied_spaces:
                            session.has_winner=True
                            print(f'We have a winner: {self.name}')
        return session.has_winner
        
class User(Player):
    def __init__(self):
        self.occupied_spaces = []
        #self.is_winner = bool
        
    def user_name(self):
        player_name = input('What is your name? ')
        self.name = player_name
        return self.name
    
    def user_choice(self):
        choice = input('Choose a space to put your mark: ')
        self.choice = choice
        if not choice.isdigit() or int(choice) not in board.possible_spaces: #To handle error if input is not a number
            print('You need to type a number between 1 and 9')
            return player1.user_choice()
        if int(choice) not in board.available_spaces: #To handle error if space is already occupied
            print('That space is already occupied. Choose another one')
            return player1.user_choice()
        if int(choice) in board.available_spaces:
            self.occupied_spaces.append(int(choice))
            board.available_spaces.remove(int(choice))
            board.printable_spaces[int(choice)-1]=self.mark
            os.system('cls')
            print(f'{self.name} chooses {self.choice}')
            return board.display(), board.available_spaces, self.occupied_spaces 
    
class Opponent(Player):
    def __init__(self):
        self.occupied_spaces = []
        #self.is_winner = bool
    
    def opponent_name(self):
        opponent_list = ['Tom', 'Wormtail', 'Garfield', 'Speedy', 'Tigger', 'Scratchy', 'Kitty', 'Itchy', 'Remy', 'Simba', 'Bianca', 'Mufasa', 'Gus Gus', 'Cheshire', 'Stuart', 'Crookshanks', 'Pinky', 'Jerry', 'Mickey', 'Minnie']
        opponent_selector = np.random.randint(0,len(opponent_list))
        opponent_name = opponent_list[opponent_selector]
        self.name = opponent_name
        return self.name
    
    def opponent_choice(self):
        time.sleep(1)
        random_selector = np.random.randint(len(board.available_spaces))
        pick = board.available_spaces[random_selector]
        self.choice = pick
        board.printable_spaces[self.choice-1] = self.mark
        self.occupied_spaces.append(self.choice)
        board.available_spaces.remove(self.choice)
        os.system('cls')
        print(f'{self.name} chooses {self.choice}')
        return board.display(), board.available_spaces, self.occupied_spaces  

game = Game()
session = Session()
board = Board(3,3)
player1 = User()
player2 = Opponent()

game.start_game()
session.play_mechanics()

