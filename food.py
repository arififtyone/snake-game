from turtle import Turtle
import random


class Food(Turtle): #food class has capabilities of Turtle class 

    def __init__(self): 
        super().__init__() # call the turtle's init method inside
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # creates 10x10 circle
        self.color("blue")
        self.speed("fastest") # don't need animation of food being created and move
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
