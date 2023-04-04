from vec import *
from typing import *
from human import *
import random
class Situation:
    #Model has to be preloaded
    def __init__(self, margin:int, position:Vector, vectorStack:list[Vector], Motors: tuple(float, float), Camera, Model, confidenceThreshold, nmsThreshold, speed):
        self.position = position
        self.VectorStack = vectorStack
        self.margin = margin
        self.Motors = Motors
        self.Camera = Camera
        self.Model = Model
        self.confidenceThreshold = confidenceThreshold
        self.nmsThreshold = nmsThreshold
        self.speed = speed
        self.currentVector = vectorStack[0]

    def updatePosition(self, x:float, y:float):
        self.position = Vector(x, y)
        #This function will be used by the thread that updates the position

    def removeFirstVector(self):
        self.VectorPath.pop(0)
        #This function is used to make the vector list act as a stack

    def resetPosition(self):
        self.position = Vector(0, 0)
        #This function is used to reset the position everytime a vector is finished

    def human_(self, frame):
        try:
            detect(frame, self.Model, self.confidenceThreshold, self.nmsThreshold)
        except:
            print("Error: Model has to be preloaded.")
            exit()
        #This function is made to simplify the coding when it comes to detecting humans. It also has error handling.
    def Heading(self):
        #returns current heading
        return 12
    def substitute(self, Vec):
        self.VectorStack[0] = Vec

#   The general way the loop works is to feed vectors one after the other. When one vector is finished the next one fed in.

    def start(self):
        while True:

            try:
                yn, frame = self.Camera.read()
            except:
                print("error: Camera is not well configured.")
                exit()
            #The try/except block allows for debug of the camera
            if(self.position == self.CurrentVector):
                self.resetPosition()
                self.removeFirstVector()
                #Checks if current vector is finished, if it is, it removes that vector from the stack and resets position.

            if(self.human_(frame) == True):
                self.Motors = [0, 0]
                continue
                #Stops robot if humans are in frame.

            if( 0<= abs(self.CurrentVector.angle() - self.Heading()) <= 1 ): #Checks if current heading and current vector have a big difference.
                if( pdiv(self.position, self.CurrentVector).nominal(self.margin)): #Checks if the robot is on the vector.
                    self.Motors = tuple(self.speed, self.speed)
                    continue
                else:
                    self.subsitute(substract(self.CurrentVector - self.position))
            else:
                one = abs(self.Heading() - self.CurrentVector.angle())
                two = 360 - one
                if (one > two):
                    three = two
                else:
                    three = one 


                if(self.Heading() > 180 and two == three):
                    self.Motors = [self.speed, 0]
                else:
                    self.Motors = [0, self.speed]   #all of this code basically directs the robot, in the good direction if the robot is not in the good heading

                


