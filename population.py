#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 08:03:49 2021

@author: maryam
"""
from individual import INDIVIDUAL

class POPULATION: #stores multiple individuals for parallelization
    def __init__(self, popSize):
        self.p = {}
        
        for i in range(0,popSize):
            self.p[i] = INDIVIDUAL(i)
    
    def Evaluate(self, pb=True): #runs each of the indivisual's evaluate method
        for i in self.p:
            self.p[i].Start_Evaluation(pb)
            
        for i in self.p:
            self.p[i].Compute_Fitness()
            
    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()
            
    def ReplaceWith(self, other): #replace parent with better fit children 
        for i in self.p:
            if ( self.p[i].fitness < other.p[i].fitness ):
                self.p[i] = other.p[i]
        
    def Print(self): #prints each of the indidividual's genonomes
        for i in self.p:
            self.p[i].Print()
        print()