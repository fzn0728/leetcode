# -*- coding: utf-8 -*-
"""
Created on Thu May 26 19:46:09 2016

@author: Chandler
"""

import random
import matplotlib
import matplotlib.pyplot as plt

def rollDice():
    roll = random.randint(1,100)
    
    if roll == 100:
        return False
    elif roll<=50:
        return False
    elif 50<roll<100:
        return True
        
'''
Simple bettor, better same amount each time.
'''

def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    
    # Wager X
    wX = []
    
    # Value Y
    vY = []
    
    # Loop
    current_Wager = 1
    while current_Wager <= wager_count:
        if rollDice():
            value += wager
            wX.append(current_Wager)
            vY.append(value)
        else:
            value -= wager
            wX.append(current_Wager)
            vY.append(value)
        current_Wager +=1
    
    plt.plot(wX,vY)
    
    
'''
double better, if last time is loss, double the wager, if last time win then keep the same.
'''

def double_bettor(funds, initial_wager, wager_count):
    value = funds
    previous_Wager = initial_wager
    
    # Wager X
    wX = []
    
    # Value Y
    vY = []
    
    # Loop
    previous_Result = 'Win'
    current_Wager = 1
    while current_Wager <= wager_count:
        if previous_Result == 'Win':
            if rollDice():
                value += previous_Wager
                wX.append(current_Wager)
                vY.append(value)
                previous_Result = 'Win'
                print 'W-W'
            else:
                value -= previous_Wager
                wX.append(current_Wager)
                vY.append(value)
                previous_Result = 'Lose'
                print 'W-L'
        else:
            if rollDice():
                value += 2 * previous_Wager
                wX.append(current_Wager)
                vY.append(value)
                previous_Result = 'Win'
                previous_Wager = initial_wager
                print 'L-W'
            else:
                value -= 2 * previous_Wager
                wX.append(current_Wager)
                vY.append(value)
                previous_Result = 'Lose'
                print 'L-L'
            previous_Wager = 2 * previous_Wager
            print 'current wager is', previous_Wager
        current_Wager += 1
    # plot single path
    plt.plot(wX,vY)
# Doing N simulations
'''   
x = 0
while x < 100:
    simple_bettor(10000,100,100)
    x += 1
'''
'''
x = 0
while x <100:
    double_bettor(10000,100,100)
    x += 1
'''
double_bettor(10000,100,100)
plt.ylabel('Account value')
plt.xlabel('Wager Count')
plt.show

