#!/url/bin/python

# Filename: bowling.py 
# To run this code: python bowling.py ../data/test.csv

import sys 
import csv
import logging

class Bowling(object):
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
        self.tableContent = dict().fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.frameID = 1 			# Frame counter
        self.finalScoreFrame = 0		# Final Score


    def instructions(self):
        message = ("""--------------------------------------------------------------------------\n"""
                    """To execude this code you have to write:\n"""
                    """$ python bowling.py <file>\n"""
                    """--------------------------------------------------------------------------""")
        return message

    def read_csv(self, filename=sys.argv[1]):
        """ 
            Read CSV file from remote path.
            Args: filename(str): filename to read.
            Returns: The contents of CSV file.
            Raises: ValueError: Unable to read file
        """
        data = None
        count = 0
        try:
            with open(filename) as csv_file:
                data = csv.reader(csv_file, delimiter=',')
                for row in data:
                    count += 1
                    self.bowling_game(list(map(str.strip, row)))
                    self.print_table(count)
        except IOError:
            logging.exception('')
        if not data:
            raise ValueError('No data available')

    def strike_frame_10(self, inputValues, s, inputLength):
        if (s+2 < inputLength):
            self.finalScoreFrame += self.cases[inputValues[s]] + self.cases[inputValues[s+1]] + self.cases[inputValues[s+2]]
            if (inputValues[s+1] == '10'):
                score1 = 'X'
            else:
                score1 = inputValues[s+1]
            if (inputValues[s+2] == '10'):
                score2 = 'X'
            else:
                score2 = inputValues[s+2]
            self.tableContent[self.frameID]=('X', score1, score2, self.finalScoreFrame)
            self.frameID += 1
        else:
            self.tableContent[self.frameID]=('X', '', '', self.finalScoreFrame)
            self.frameID += 1

    def strike(self, inputValues, s, inputLength):
        self.tableContent[self.frameID]=('X', ' ', ' ', self.finalScoreFrame)
        if (s+2 < inputLength):
            self.finalScoreFrame += self.cases[inputValues[s]] + self.cases[inputValues[s+1]] + self.cases[inputValues[s+2]]
            self.tableContent[self.frameID]=('X', ' ', ' ', self.finalScoreFrame)
            self.frameID += 1
        else:
            self.tableContent[self.frameID]=('X', ' ', ' ', self.finalScoreFrame)
            self.frameID += 1
        
    def miss(self, inputValues, s, inputLength):
        # This means that this is the first throw of this frame
        if self.tableContent[self.frameID] == None:
            self.tableContent[self.frameID]=(self.cases[inputValues[s]], ' ', ' ', self.finalScoreFrame)

        else:
            self.finalScoreFrame += self.cases[inputValues[s-1]] + self.cases[inputValues[s]]
            tableContent[frameID]=(self.cases[inputValues[s-1]], self.cases[inputValues[s]], ' ', self.finalScoreFrame)
            self.frameID += 1

    def partial_hit(self, inputValues, s, inputLength):
        self.tableContent[self.frameID]=(self.cases[inputValues[s]], ' ', ' ', self.finalScoreFrame)

    def spare(self, inputValues, s, inputLength):
        if self.cases[inputValues[s-1]] + self.cases[inputValues[s]] == 10:
            self.finalScoreFrame += self.cases[inputValues[s-1]] + self.cases[inputValues[s]] + self.cases[inputValues[s+1]]
            self.tableContent[self.frameID]=(self.cases[inputValues[s-1]], '/', ' ', self.finalScoreFrame)
            self.frameID += 1
        elif self.cases[inputValues[s-1]] + self.cases[inputValues[s]] > 10:
            print "Error: Looks like we have an extra pin in the roll, sorry!"
        else:
            self.finalScoreFrame += self.cases[inputValues[s-1]] + self.cases[inputValues[s]]
            self.tableContent[self.frameID]=(self.cases[inputValues[s-1]], self.cases[inputValues[s]], ' ', self.finalScoreFrame)
            self.frameID += 1

    def score(self, inputValues, s, inputLength):
        # This means that this is the first throw of this frame
        if self.tableContent[self.frameID] == None:
            self.partial_hit(inputValues, s, inputLength)

        else:
            # We have a spare!
            self.spare(inputValues, s, inputLength)
            

    def bowling_game(self, inputValues):
        # Read all the arguments after bowling-scoreboard.py <numbers>
        inputLength = len(inputValues)
        try:

            # Let the game start!!
            self.frameID = 1 			# Frame counter
            self.finalScoreFrame = 0		# Final Score

            # # Add the frame keys
            self.tableContent = dict().fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

            # Then we have a game
            if inputLength > 0:
                try:
                    for s in range(0, inputLength):
                        # We are under the limits of the game.
                        if self.frameID <= 10 and self.finalScoreFrame <= 300:
                            # We are in frame 10 and we have a strike!
                            if self.frameID == 10 and self.cases[inputValues[s]] == 10:
                                self.strike_frame_10(inputValues, s, inputLength)
                            # We have a strike!
                            elif self.cases[inputValues[s]] == 10:
                                self.strike(inputValues, s, inputLength)
                            # We have a miss!
                            elif self.cases[inputValues[s]] == 0:
                                self.miss(inputValues, s, inputLength)
                            else:
                                self.score(inputValues, s, inputLength)
                                
                    return self.tableContent
                except IndexError as e:
                    # If he can't calculate the Bonus values means the game is not finished.
                    return self.tableContent
            else:
                print instructions()

        except KeyError:
            print instructions()

        return None

    def print_table(self, count):
        try:
            # Print the table
            print ""
            print "----------------------------------------------------------------------------------------------------------------"
            print "{:>57} - {:<37}".format("Bowling Game", count)
            print "----------------------------------------------------------------------------------------------------------------"
            print "{:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^11} | {:^8}".format('F1','F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'Score')
            print "----------------------------------------------------------------------------------------------------------------"
            for k,v in self.tableContent.iteritems():
                if v  == None:
                    r1, r2, r3, total = ('-', '-', '-', '-')
                else:
                    r1, r2, r3, total = v
                    score = total
                if k < len(self.tableContent):
                    print "{:^3} {:^3} |".format(r1, r2),
                else:
                    print "{:^3} {:^3} {:^3} | {:^7} ".format(r1, r2, r3, score)
            print "----------------------------------------------------------------------------------------------------------------"
            print ""

        except TypeError:
            # "Can't" handle the 'X', '/' symbols."
            pass

if __name__ == '__main__':
	Bowling().read_csv()