#!/url/bin/python

# Filename: bowling.py 
# To run this code: python bowling.py ../data/test.csv

import sys 
import csv
import logging

class Bowling(object):
    """
    A class used to represent bowling games
    ...

    Attributes
    ----------
    cases : dict
        a tally dictionary that converts from string to integer for score calculations.
    table_content : dict
        main storage for the scores
    frame_id : int
        current frame for the game
    final_score_frame : int
        final score at each frame
    score_data : int
        final score data, assemebles all the game data to be printed out
    input_length : int
        length of each line of scoreboard from file

    Methods
    -------
    instructions()
        Prints the instruction for users to use the program
    read_csv()
        Read the csv data
    calculate_score()
        Calculate the score
    strike_frame_10()
        Calculate if strike frame is last frame
    strike()
        Calculate strike
    miss()
        Calculate when it's a miss
    partial_hit()
        Calculate the partial hits
    spare()
        Calculate spare
    score()
        Calculate total score
    bowling_game()
        Process each bowling game from the file
    print_table()
        Prints the bowling score chart in the CLI
    """
    def __init__(self):
        self.cases = {
            'X' : 10,
            '/' : 10,
            '-' : 0,
            '0' : 0,
            '1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9,
            '10': 10
        }
        self.table_content = dict().fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.frame_id = 1 			# Frame counter
        self.final_score_frame = 0		# Final Score
        self.input_length = 0
        self.score_data = []

    def instructions(self):
        message = ("""--------------------------------------------------------------------------\n"""
                    """To execude this code you have to write:\n"""
                    """$ python bowling.py <file>\n"""
                    """--------------------------------------------------------------------------""")
        return message

    def read_csv(self, filename):
        """ 
            Read CSV file from remote path.
            Args: filename(str): filename to read.
            Returns: The contents of CSV file.
            Raises: ValueError: Unable to read file
        """
        data = None
        try:
            with open(filename) as csv_file:
                data = csv.reader(csv_file, delimiter=',')
                for row in data:
                    self.score_data.append(list(map(str.strip, row)))      
        except IOError:
            logging.exception('')
        if not data:
            raise ValueError('No data available')

    def calculate_score(self):
        """
            Calculate scores
        """
        count = 0
        for score_board in self.score_data:
            count += 1
            self.bowling_game(score_board)
            self.print_table(count)

    def strike_frame_10(self, input_values, idx):
        if (idx+2 < self.input_length):
            self.final_score_frame += self.cases[input_values[idx]] + self.cases[input_values[idx+1]] + self.cases[input_values[idx+2]]
            if (input_values[idx+1] == '10'):
                score1 = 'X'
            else:
                score1 = input_values[idx+1]
            if (input_values[idx+2] == '10'):
                score2 = 'X'
            else:
                score2 = input_values[idx+2]
            self.table_content[self.frame_id]=('X', score1, score2, self.final_score_frame)
            self.frame_id += 1
        else:
            self.table_content[self.frame_id]=('X', '', '', self.final_score_frame)
            self.frame_id += 1

    def strike(self, input_values, idx):
        self.table_content[self.frame_id]=('X', ' ', ' ', self.final_score_frame)
        if (idx+2 < self.input_length):
            self.final_score_frame += self.cases[input_values[idx]] + self.cases[input_values[idx+1]] + self.cases[input_values[idx+2]]
            self.table_content[self.frame_id]=('X', ' ', ' ', self.final_score_frame)
            self.frame_id += 1
        else:
            self.table_content[self.frame_id]=('X', ' ', ' ', self.final_score_frame)
            self.frame_id += 1
        
    def miss(self, input_values, idx):
        # This means that this is the first throw of this frame
        if self.table_content[self.frame_id] == None:
            self.table_content[self.frame_id]=(self.cases[input_values[idx]], ' ', ' ', self.final_score_frame)

        else:
            self.final_score_frame += self.cases[input_values[idx-1]] + self.cases[input_values[idx]]
            self.table_content[frame_id]=(self.cases[input_values[idx-1]], self.cases[input_values[idx]], ' ', self.final_score_frame)
            self.frame_id += 1

    def partial_hit(self, input_values, idx):
        self.table_content[self.frame_id]=(self.cases[input_values[idx]], ' ', ' ', self.final_score_frame)

    def spare(self, input_values, idx):
        if self.cases[input_values[idx-1]] + self.cases[input_values[idx]] == 10:
            self.final_score_frame += self.cases[input_values[idx-1]] + self.cases[input_values[idx]] + self.cases[input_values[idx+1]]
            self.table_content[self.frame_id]=(self.cases[input_values[idx-1]], '/', ' ', self.final_score_frame)
            self.frame_id += 1
        elif self.cases[input_values[idx-1]] + self.cases[input_values[idx]] > 10:
            print( "Error: Looks like we have an extra pin in the roll, sorry!")
        else:
            self.final_score_frame += self.cases[input_values[idx-1]] + self.cases[input_values[idx]]
            self.table_content[self.frame_id]=(self.cases[input_values[idx-1]], self.cases[input_values[idx]], ' ', self.final_score_frame)
            self.frame_id += 1

    def score(self, input_values, idx):
        # This means that this is the first throw of this frame
        if self.table_content[self.frame_id] == None:
            self.partial_hit(input_values, idx)

        else:
            # We have a spare!
            self.spare(input_values, idx)

    def bowling_game(self, input_values):
        # Read all the arguments after bowling-scoreboard.py <numbers>
        self.input_length = len(input_values)
        try:

            # Let the game start!!
            self.frame_id = 1 			# Frame counter
            self.final_score_frame = 0		# Final Score

            # # Add the frame keys
            self.table_content = dict().fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

            # Then we have a game
            if self.input_length > 0:
                try:
                    for idx in range(0, self.input_length):
                        # We are under the limits of the game.
                        if self.frame_id <= 10 and self.final_score_frame <= 300:
                            # We are in frame 10 and we have a strike!
                            if self.frame_id == 10 and self.cases[input_values[idx]] == 10:
                                self.strike_frame_10(input_values, idx)
                            # We have a strike!
                            elif self.cases[input_values[idx]] == 10:
                                self.strike(input_values, idx)
                            # We have a miss!
                            elif self.cases[input_values[idx]] == 0:
                                self.miss(input_values, idx)
                            else:
                                self.score(input_values, idx)
                                
                    return self.table_content
                except IndexError as e:
                    # If he can't calculate the Bonus values means the game is not finished.
                    return self.table_content
            else:
                print( instructions())

        except KeyError:
            print( instructions())

        return None

    def print_table(self, count):
        try:
            # Print the table
            print( "")
            print( "----------------------------------------------------------------------------------------------------------------")
            print( "{:>57} - {:<37}".format("Bowling Game", count))
            print( "----------------------------------------------------------------------------------------------------------------")
            print( "{:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^11} | {:^8}".format('F1','F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'Score'))
            print( "----------------------------------------------------------------------------------------------------------------")
            for k,v in self.table_content.items():
                if v  == None:
                    r1, r2, r3, total = ('-', '-', '-', '-')
                else:
                    r1, r2, r3, total = v
                    score = total
                if k < len(self.table_content):
                    print( "{:^3} {:^3} |".format(r1, r2), end =" ")
                else:
                    print( "{:^3} {:^3} {:^3} | {:^7} ".format(r1, r2, r3, score), end =" ")
            print( "\n----------------------------------------------------------------------------------------------------------------")
            print( "")

        except TypeError:
            # "Can't" handle the 'X', '/' symbols."
            pass

if __name__ == '__main__':
    game = Bowling()
    game.read_csv(sys.argv[1])
    game.calculate_score() 