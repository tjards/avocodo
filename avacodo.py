#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:36:32 2023

@author: tjards
"""

#avocodo
import random
import time

def main():

    print('Me: Are you ready yet?')
    
    i = random.randint(1,10)
    
    while i > 0:
        time.sleep(1)
        print('Avocado: No, not yet.')
        i -=1
        if i == 1:
            print('Avocado:OK, now.')
            break
        print('Me: How about now?')
    print('Avocado: Too late.')


if __name__ == "__main__":
    
    main()