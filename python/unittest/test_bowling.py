#!/usr/bin/python
# File name: test_bowling.py
# This is the unit test file for the bowling score calculation

import unittest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from bowling import Bowling
import pytest

def test_no_file():
    """
        should throw IOError when no file is present 
    """
    with pytest.raises(IOError):
        Bowling().read_csv(filename = 'incorrectfile.csv')

def test_data_extraction():
    """
        should read correct data 
    """
    assert_data = [['2', '3', '5', '4', '9', '1', '2', '5', '3', '2', '4', '2', '3', '3', '4', '6', '10', '3', '2'], ['10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10'], ['2', '3', '5', '4', '10', '10'], ['10', '10', '10']]
    game = Bowling()
    result = game.read_csv(filename = '../data/test.csv')
    assert game.score_data == assert_data

def test_score_calculation():
    """
        should print correct result for the last data
    """
    assert_data = {1: ('X', ' ', ' ', 30), 2: ('X', ' ', ' ', 30), 3: ('X', ' ', ' ', 30), 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None}
    game = Bowling()
    assert_score = 30
    game.read_csv(filename = '../data/test.csv')
    result  = game.calculate_score()
    assert game.final_score_frame == assert_score
    assert game.table_content == assert_data

def test_strike_calculation():
    """
        should print correct result for the last data
    """
    assert_data = {1: ('X', ' ', ' ', 30), 2: ('X', ' ', ' ', 60), 3: ('X', ' ', ' ', 90), 4: ('X', ' ', ' ', 120), 5: ('X', ' ', ' ', 150), 6: ('X', ' ', ' ', 180), 7: ('X', ' ', ' ', 210), 8: ('X', ' ', ' ', 240), 9: ('X', ' ', ' ', 270), 10: ('X', 'X', 'X', 300)}
    assert_score = 300
    game = Bowling()
    game.read_csv(filename = '../data/test_strike.csv')
    result  = game.calculate_score()
    assert game.table_content == assert_data
    assert game.final_score_frame == assert_score

def test_spare_calculation():
    """
        should print correct result for the last data
    """
    assert_data = {1: (2, 3, ' ', 5), 2: (5, 4, ' ', 14), 3: (9, '/', ' ', 26), 4: (2, 5, ' ', 33), 5: (3, 2, ' ', 38), 6: (4, 2, ' ', 44), 7: (3, 3, ' ', 50), 8: (4, '/', ' ', 70), 9: ('X', ' ', ' ', 85), 10: (3, 2, ' ', 90)}
    assert_score = 90
    game = Bowling()
    game.read_csv(filename = '../data/test_spare.csv')
    result  = game.calculate_score()
    assert game.table_content == assert_data
    assert game.final_score_frame == assert_score


def test_empty_calculation():
    """
        should raise error for value not present in the file
    """
    with pytest.raises(ValueError):
        Bowling().read_csv(filename = '../data/test_empty.csv')