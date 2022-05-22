# -*- coding: utf-8 -*-
"""
Busy beaver Turing machine with 5 states.

Created on Sat Mar 30 13:55:25 2019

@author: shakes
"""
from double_sided import TuringMachine


#create the Turing machine
bbeaver = TuringMachine(
    {
        ("a", "0"): ("e", "1", "L"),
        ("a", "1"): ("h", "1", "R"),

        ("b", "0"): ("d", "1", "L"),
        ("b", "1"): ("e", "1", "R"),

        ("c", "0"): ("b", "0", "L"),
        ("c", "1"): ("b", "1", "R"),

        ("d", "0"): ("c", "1", "R"),
        ("d", "1"): ("e", "0", "L"),

        ("e", "0"): ("c", "1", "R"),
        ("e", "1"): ("a", "1", "L")
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)

bbeaver.debug('00000000000000', step_limit=1000)
