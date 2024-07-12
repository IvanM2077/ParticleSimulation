import Infraestructure
from Vector import *
from Infraestructure import *
from random import *
from math import *

class particle(Vector):
    def __init__(self,radius):
        self.x,self.y = RandomPosition()
        self.vx=0
        self.vy=0
        self.ax=0
        self.ay=0
        self.color=RandomColor()
        self.radius=radius
    def Update(self):
        #Para x
        self.x = self.x + self.vx * dt
        #Para vy
        self.vy= self.vy - gravity * dt
        #Para y
        self.y = self.y + self.vy * dt - 0.5* gravity*dt^2

    def CheckCollisionsWalls(self):
        if(self.y+self.radius>=width):
            self.y=width-self.radius
            self.vy = self.vy*-1
        if(self.y+self.radius<=0):
            self.y=0+self.radius
            self.vy = self.vy*-1






