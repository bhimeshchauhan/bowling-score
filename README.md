Bowling
======================================


======================================

                         ! ! ! !
                      ." ! ! !  /
                    ."   ! !   /
                  ."     !    /
                ."           /
              ."     o      /
            ."             /
          ."              /
        ."               /
      ."      . '.      /
    ."      '     '    /
  ."                  / 
."                   /
.       0 |          
.       |/
.      /|
.      / |

======================================


### Problem description
Create a program, which, given a valid sequence of rolls for one line of American Ten-Pin Bowling, 
produces the total score for the game.

#### Scoring
* Each game, or “line” of bowling, includes ten turns, or “frames” for the bowler.
* In each frame, the bowler gets up to two tries to knock down all the pins.
* If in two tries, he fails to knock them all down, his score for that frame is the total number of pins knocked down in his two tries.
* If in two tries he knocks them all down, this is called a “spare” and his score for the frame is ten plus the number of pins knocked down on his next throw (in his next turn).
* If on his first try in the frame he knocks down all the pins, this is called a “strike”. His turn is over, and his score for the frame is ten plus the simple total of the pins knocked down in his next two rolls.
* If he gets a spare or strike in the last (tenth) frame, the bowler gets to throw one or two more bonus balls, respectively. These bonus throws are taken as part of the same turn. If the bonus throws knock down all the pins, the process does not repeat: the bonus throws are only used to calculate the score of the final frame.
* The game score is the total of all frame scores.

More info on the rules at: https://www.topendsports.com/sport/tenpin/scoring.htm

#### Clues
What makes this game interesting to score is the lookahead in the scoring for strike and spare. At the time we throw a strike or spare, we cannot calculate the frame score: we have to wait one or two frames to find out what the bonus is.

#### Input
The game should be able to read a file containing a comma separated list of rolls, taking the reference to the file as a command line argument, as a starting point. 
You don't need to cater for invalid input, it is not part of the scope of this task.

Example input:

    2, 3, 5, 4, 9, 1, 2, 5, 3, 2, 4, 2, 3, 3, 4, 6, 10, 3, 2

#### Output

##### Strikes and spares
For output, a strike is denoted as `X` and the last roll in a spare is denoted as `/`. A miss (a gutter ball) is denoted as a `-`

##### Format
The game should print a game summary and the score for the game in the following format
 
    | f1 | f2 | f3 | f4 | f5 | f6 | f7 | f8 | f9 | f10   |
    |roll1[, roll2]|roll1[, roll2]|...|roll1[, roll2][, roll3]|
    score: score

Example output 1:

    | f1 | f2 | f3 | f4 | f5 | f6 | f7 | f8 | f9 | f10   |
    |-, 3|5, -|9, /|2, 5|3, 2|4, 2|3, 3|4, /|X   |X, 2, 5|
    score: 103
    
Example output 2:    
       
    | f1 | f2 | f3 | f4 | f5 | f6 | f7 | f8 | f9 | f10   |
    |7, 1|5, /|2, 7|4, /|-, 5|8, /|8, 1|4, 3|2, 4|5, 2   |
    score: 91
    
#### Testing
The solution should include tests.

#### Programming language
You have different options for the programming language and these are the current preferred languages: Java, Kotlin, Python, C#, Ruby, Javascript or Typescript.

#### Delivery
Source code and a description of how to build and run the program. Remember to specify build/run 
requirements of the local environment.  