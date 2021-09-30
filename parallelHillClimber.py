#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 03:56:50 2021

@author: maryam
"""

import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
import random, copy
from individual import INDIVIDUAL
import pickle
from population import POPULATION
from sys import exit

parents = POPULATION(10)
parents.Evaluate()
#exit()
parents.Print()

for i in range(1, 200):
    children = copy.deepcopy(parents)
    children.Mutate()
    children.Evaluate()
    parents.ReplaceWith(children)
    print(i, end=' ')
    parents.Print()

parents.Evaluate(False)