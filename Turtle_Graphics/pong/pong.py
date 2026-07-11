import turtle as t
from paddle import Paddle
from ball import Ball
import time 
from score import Scoreboard
screen=t.Screen()



screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
paddle1=Paddle()
paddle2=Paddle()
ball=Ball()
score=Scoreboard()
paddle1.create_paddle(x=370,y=0)
paddle2.create_paddle(x=-370,y=0)
screen.update()
screen.listen()
screen.onkey(key="Up",fun=paddle1.up)
screen.onkey(key="Down",fun=paddle1.down)
screen.onkey(key="w",fun=paddle2.up)
screen.onkey(key="s",fun=paddle2.down)
game_on=True


sleep=0.1
while game_on:
    screen.update()
    time.sleep(sleep)
    ball.move()
    
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_wall()

    if ball.distance(paddle1)<50 and ball.xcor()>340 or ball.distance(paddle2)<50 and ball.xcor()<-340:
        ball.bounce_paddle()
        
    
    if ball.xcor()>380:
        score.incr_lscore()
        ball.reset()
        
    if ball.xcor()<-380:
        score.incr_rscore()
        ball.reset()


        
        

screen.exitonclick()

