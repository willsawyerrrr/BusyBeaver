# -*- coding: utf-8 -*-
"""
Busy beaver Turing machine with 4 states.

Created on Sat Mar 30 13:55:25 2019

@author: shakes
"""
from double_sided import TuringMachine


#create the Turing machine
bbeaver = TuringMachine(
    {
        # Write transitions like ('q0', '1'): ('q1', '0', 'R')
        ("a", "0"): ("d", "1", "L"),
        ("a", "1"): ("h", "1", "L"),

        ("b", "0"): ("b", "1", "R"),
        ("b", "1"): ("c", "1", "R"),

        ("c", "0"): ("h", "0", "L"),
        ("c", "1"): ("d", "0", "L"),

        ("d", "0"): ("b", "0", "R"),
        ("d", "1"): ("h", "0", "R"),

    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)

bbeaver.debug('00000000000000', step_limit=1000)    # results in a single '1'
