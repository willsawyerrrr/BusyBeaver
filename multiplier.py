# -*- coding: utf-8 -*-
"""
Test script for running a Turing machine unary multiplier

Usage: python multiplier.py input-string

Created on Fri Mar 29 21:57:42 2019

@author: shakes
"""
from turing_machine import TuringMachine
import sys

def main(input):
    #create the Turing machine
    multiplier = TuringMachine(
        {
            # we must initially place an input/output separator - 'x'
            # when initial state sees '0' or '1', skip over them
            ("q0", "0"): ("q0", "0", "R"),
            ("q0", "1"): ("q0", "1", "R"),

            # when the initial state reads the blank symbol, write input/output
            # separator - 'x'
            ("q0", "b"): ("begin", "x", "L"),

            # after placing input/output separator, move to the left to begin,
            # skipping any '0' or '1'
            ("begin", "0"): ("begin", "0", "L"),
            ("begin", "1"): ("begin", "1", "L"),

            # once the blank symbol to the left of the input has been read,
            # move right to begin calculations
            ("begin", "b"): ("dec", "b", "R"),

            # if preparing to decrement and we read a '0', begin cleaning up
            ("dec", "0"): ("clean", "0", "L"),

            # if we read a '1', decrement first argument and prepare to copy
            ("dec", "1"): ("p_copy", "b", "R"),

            # if preparing to copy and read argument separator, move right and
            # begin copying
            ("p_copy", "0"): ("copy", "0", "R"),

            # if preparing to copy, skip any read '1'
            ("p_copy", "1"): ("p_copy", "1", "R"),

            # if copying and read '1', convert to 'y' and prepare to paste
            ("copy", "1"): ("p_paste", "y", "R"),

            # if copying and read input/output separator, begin tidying
            ("copy", "x"): ("tidy", "x", "L"),

            # if preparing to paste, skip any read '1'
            ("p_paste", "1"): ("p_paste", "1", "R"),

            # if preparing to paste and read input/output separator, move right
            # and begin pasting
            ("p_paste", "x"): ("paste", "x", "R"),
            
            # if pasting, skip any read '1'
            ("paste", "1"): ("paste", "1", "R"),

            # if pasting and reach blank symbol, paste and move left until 'y'
            ("paste", "b"): ("find_y", "1", "L"),

            # if finding 'y' and read argument separator, all have been copied
            # begin tidying
            ("find_y", "0"): ("tidy", "0", "R"),

            # if finding 'y', skip any read '1' or 'x'
            ("find_y", "1"): ("find_y", "1", "L"),
            ("find_y", "x"): ("find_y", "x", "L"),

            # if found 'y', begin copying
            ("find_y", "y"): ("copy", "y", "R"),

            # if tidying and read argument separator, begin decrement/copy loop
            ("tidy", "0"): ("begin", "0", "L"),

            # if tidying and read 'y', convert to '1' and keep tidying to left
            ("tidy", "y"): ("tidy", "1", "L"),

            # if cleaning up and read 'x', clear 'x', halt and accept
            ("clean", "x"): ("qa", "b", "R"),

            # if cleaning up and read anything other than 'x', clear, keep
            # cleaning and move right
            ("clean", "0"): ("clean", "b", "R"),
            ("clean", "1"): ("clean", "b", "R"),
            ("clean", "b"): ("clean", "b", "R")
        },
        blank_symbol = "b"
    )

    # "step_limit = None" below allows the simulation to run until exhaustion
    multiplier.debug(input, step_limit = None)

if __name__ == "__main__":
    main(sys.argv[1])
