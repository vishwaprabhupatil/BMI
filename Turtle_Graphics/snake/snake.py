import turtle as t

UP=90
DOWN=270
LEFT=180
RIGHT=0
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]

class Snake():
    def __init__(self):
        
        self.snakes=[]
        self.create_snake()
        self.head=self.snakes[0]
        
        
    def create_snake(self):    
        for square in STARTING_POSITION:
            self.add_body(square)
    
    
    def add_body(self,position):
        kachwa=t.Turtle(shape="square",undobuffersize=20)
        kachwa.color("white")
        kachwa.penup()
        kachwa.goto(position)    
        self.snakes.append(kachwa)
        
    def extend(self):
        self.add_body(self.snakes[-1].position())
            
    def move(self):
        for snake in range(len(self.snakes)-1,0,-1):
            newx=self.snakes[snake-1].xcor()
            newy=self.snakes[snake-1].ycor() 
            self.snakes[snake].goto(newx,newy)
        self.snakes[0].forward(20)
    
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
        
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
        
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)    
    
    def reset(self):
        for seg in self.snakes:
            seg.goto(1000,1000)
        
        self.snakes.clear()
        self.create_snake()
        self.head=self.snakes[0]
   