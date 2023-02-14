#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:36:32 2023

@author: tjards
"""

# import stuff
# ------------
import random
import time

# main function
# ------------
def main():
    print('Me: Are you ready yet?')
    i = random.randint(1,30)
    while i > 0:
        print('Avocado: No, not yet.')
        time.sleep(0.5)
        i -=1
        print('Me: How about now?')
    print('Avocado: OK, now.')
    print('Avocado: Too late.')

# terminal call
# -------------
if __name__ == "__main__":  
    main()