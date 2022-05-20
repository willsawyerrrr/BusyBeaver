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
            #Write your transition rules here as entries to a Python dictionary
            #For example, the key will be a pair (state, character)
            #The value will be the triple (next state, character to write, move head L or R)
            #such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
            #then transition to state q1, write a 0 and move head right.

            # rd    represents the "read symbol" state
            # mv_r  represents the "move right" state
            # mv_r  represents the "move left" state
            ("rd", "0"): ("qa", "0", "R"),
            ("rd", "1"): ("mv_r", "x", "R"),
            ("mv_r", "0"): ("mv_r", "0", "R"),
            ("mv_r", "1"): ("mv_r", "1", "R"),
            ("mv_r", "b"): ("mv_l", "1", "L"),
            ("mv_l", "0"): ("mv_l", "0", "L"),
            ("mv_l", "1"): ("mv_l", "1", "L"),
            ("mv_l", "x"): ("rd", "x", "R")
        },
        start_state = "rd",
        blank_symbol = "b"
    )

    adder.debug(input)

if __name__ == "__main__":
    main(sys.argv[1])
