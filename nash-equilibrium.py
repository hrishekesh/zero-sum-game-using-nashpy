#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 18:22:57 2019

@author: hrishekesh.shinde
"""

import nashpy as nash
import numpy as np

valid_input = True
while valid_input:
    print('Enter 4 values for a zero sum game:')
    user_input_values = input()
    game_val = []
    game = []
    try:
        user_input_values = user_input_values.split(',')
        for val in user_input_values:
            game_val.append(float(val))
            game.append([float(val), -1*float(val)])
        if (sum(game_val) == 0 and len(game_val) == 4):
            valid_input = False
        else:
            raise Exception('Invaild Input')
    except:
        print('Invalid input. Please try again')

game_A = np.array(game[:2])
game_B = np.array(game[2:])
nash_game = nash.Game(game_A, game_B)
print('The game is:')
print(game)

nash_equilibria_se = nash_game.support_enumeration()
print('Solution using support enumeration')
for eq in nash_equilibria_se:
    print(eq)
    
nash_equilibria_ve = nash_game.vertex_enumeration()
print('Solution using vertex enumeration')
for eq in nash_equilibria_ve:
    print(eq)
    
nash_equilibria_lh = nash_game.lemke_howson(initial_dropped_label=0)
print('Solution using Lemke Howson Algorithm')
for eq in nash_equilibria_lh:
    print(eq)

valid_prob = True
while valid_prob:
    print('Enter repetition probability value between 0 and 1:')
    prob = input()
    try:
        prob = float(prob)
        if prob <= 1 and prob > 0:
            valid_prob = False
        else:
            raise Exception('Invalid probability value')
    except:
        print('Invalid probability value entered. Please try again.')

valid_move = True
while valid_move:
    print('Choice A: ', game[0])
    print('Choice B: ', game[1])
    print('Enter your move A or B:')
    player_choice = input()
    if player_choice in ['a', 'A', 'b', 'B']:
        valid_move = False
        if player_choice == 'a' or player_choice == 'A':
            player_choice = np.array([prob,1-prob])
        else:
            player_choice = np.array([1-prob,prob])
    else:
        print('Invalid move. Please try again.')
        
print('Selected choice is ', player_choice)
print('Available computer choices are:')
print('Choice A: ', game[2])
print('Choice B: ', game[3])

selected_computer_choice = 'A'
utility_A = 0
utility_B = 0
index = 0
for available_computer_choice in [[prob,1-prob], [1-prob,prob]]:
    available_computer_choice = np.array(available_computer_choice)
    computer_utility_value = nash_game[player_choice, available_computer_choice][1]
    if index == 0:
        utility_A = computer_utility_value
    elif index == 1:
        utility_A = computer_utility_value
    index += 1
    
if utility_A >= utility_B:
    print('Selected choice by computer is A')
else:
    print('Selected choice by computer is B')
    

    
