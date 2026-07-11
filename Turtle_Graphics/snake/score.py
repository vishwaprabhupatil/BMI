from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(-10,275)
        self.color("white")
        self.write(arg=f"Score:{self.score}",move=False,align="center",font=("Arial",15,"normal"))   
        self.high_score=0
    
    def show_score(self):
        self.clear()
        self.write(arg=f"Score:{self.score} High score: {self.high_score}",move=False,align="center",font=("Arial",15,"normal"))
        
    def incr_score(self):
        self.score+=1
        self.show_score()
        
    # def end_score(self):
    #     self.clear()
    #     self.home()
    #     self.write(arg=f"GAME OVER!\n     Score:{self.score}",move=False,align="center",font=("Arial",30,"normal"))
        
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0
        self.show_score()
        
    