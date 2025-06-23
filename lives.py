from turtle import Turtle

class Lives:
    def __init__(self,live):
        self.live=live
        self.lives=[]

    def create_live(self):
        for i in range(self.live):
            liv=Turtle(shape="circle")
            liv.color("white")
            liv.penup()
            liv.goto(-200+(i*30),240)
            self.lives.append(liv)

    def remove_live(self):
        if self.live>0:
            self.lives[self.live-1].hideturtle()
            self.live-=1
            return True
        else:
            return False

    def reset_lives(self):
        for liv in self.lives:
            liv.hideturtle()
        self.lives.clear()
        self.live = 3
        self.create_live()



