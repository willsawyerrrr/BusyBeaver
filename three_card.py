# -*- coding: utf-8 -*-
"""
Busy beaver Turing machine with 3 states.

Created on Sat Mar 30 13:55:25 2019

@author: shakes
"""
from double_sided import TuringMachine


#create the Turing machine
bbeaver = TuringMachine(
    {
        ("a", "0"): ("b", "1", "R"),
        ("a", "1"): ("c", "0", "R"),

        ("b", "0"): ("h", "0", "L"),
        ("b", "1"): ("a", "1", "L"),
        
        ("c", "0"): ("a", "1", "L"),
        ("c", "1"): ("h", "0", "R")
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)

bbeaver.debug('00000000000000', step_limit=1000)    # results in a single '1'
