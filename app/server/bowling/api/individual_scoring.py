#!/url/bin/python

# Filename: bowling.py 
# To run this code: python bowling.py ../data/test.csv

import sys 
import csv
import logging

class ScoreBowling(object):
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
    return_data()
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
        self.result = []

    def calculate_score(self, data):
        """
            Calculate scores
        """
        self.bowling_game(data)
        self.result.append(self.table_content)

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
            print('ERROR1')
        return None

    def return_data(self):
        return {'result': self.result, 'score': self.final_score_frame}

    def get_score(self, data):
        self.calculate_score(data) 