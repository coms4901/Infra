#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 23:13:45 2021

@author: maryam
"""
import random, math, numpy
import pyrosim
from robot import ROBOT

class INDIVIDUAL: #holds a robot and a simulator
    def __init__(self, i): #if you have the genome saved, then behavior of the robot is saved. 
        self.genome = numpy.random.random((4,8)) * 2 - 1 #genome matrix
        #print(self.genome)
        self.fitness = 0
        self.ID = i
    
    def Start_Evaluation(self, pb): #runs simulator for this one robot 
        self.sim = pyrosim.Simulator(play_paused=True, eval_time = 1000, play_blind = pb )
    
        self.robot = ROBOT( self.sim,  self.genome ) #create robot instance
    
        self.sim.start()
        
    def Compute_Fitness(self): #stores fitness value for this one robot in its simulator

        self.sim.wait_to_finish()
    
        y = self.sim.get_sensor_data( sensor_id = self.robot.P4 , svi = 1 ) #into the screen coordinates (y)
        self.fitness = y[-1] #final coordinate
    
        del self.robot
        del self.sim #deletes so deepcopy (child) doesn't retain those global variables; also throws error anyways
        
    def Mutate(self):
        geneToMutateJ = random.randint(0, 3)
        geneToMutateI = random.randint(0, 7)
        self.genome[geneToMutateJ,geneToMutateI] = random.gauss(self.genome[geneToMutateJ,geneToMutateI], math.fabs(self.genome[geneToMutateJ,geneToMutateI]))
        self.genome = numpy.clip(self.genome, -1, 1) #ensure weights is within range [-1, 1]
        
    def Print(self):
        print('[', self.ID, ' ', self.fitness, ']', end=' ')