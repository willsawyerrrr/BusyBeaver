# -*- coding: utf-8 -*-
"""
Test script for running a Turing machine unary adder

Usage: python adder.py input-string

Created on Fri Mar 29 21:57:42 2019

@author: shakes
"""
from turing_machine import TuringMachine
import sys

def main(input):
    print(input)
    #create the Turing machine
    adder = TuringMachine(
        {
            # if we read a '0' from the input string, halt and accept
            ("rd", "0"): ("qa", "0", "R"),

            # if we read a '1' from the input string, begin moving right
            ("rd", "1"): ("mv_r", "x", "R"),

            # if moving right and we read a '0' or '1', continue moving right
            ("mv_r", "0"): ("mv_r", "0", "R"),
            ("mv_r", "1"): ("mv_r", "1", "R"),

            # if moving right and we read a blank symbol, write a 1 and begin moving left
            ("mv_r", "b"): ("mv_l", "1", "L"),
            
            # if moving left and we read a '0' or '1', keep moving left
            ("mv_l", "0"): ("mv_l", "0", "L"),
            ("mv_l", "1"): ("mv_l", "1", "L"),
 
            # if moving left and we read an 'x', move right and read from the input string again
            ("mv_l", "x"): ("rd", "x", "R")
        },
        start_state = "rd",     # rd    represents read from input string
        blank_symbol = "b"
    )

    adder.debug(input)

if __name__ == "__main__":
    main(sys.argv[1])
