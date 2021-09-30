#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 01:41:57 2021

@author: maryam
"""

from individual import INDIVIDUAL
import pickle

f = open('robot.p','rb') #reconstructs the best individual
best = pickle.load(f)
f.close()

best.Evaluate(False)
print(best.fitness)

