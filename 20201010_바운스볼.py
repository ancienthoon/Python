import pygame as p

p.init()
w = (255,255,255)
size = (1000,600)
sc = p.display.set_mode(size)
p.display.set_caption("bounce_ball")
playing = True

ball = p.image.load("ball.png")
b_rect = ball.get_rect(left=490,top=290)
b_x = 0
b_y = 3
clock = p.time.Clock()

while playing:
       #수정됨
       
       clock.tick(60)  
       for event in p.event.get():
              if event.type == p.QUIT:
                   playing = False
                   p.quit()
                   quit()

       sc.fill(w)
       sc.blit(ball,b_rect)
       b_rect.top += b_y
       b_y = b_y + 1
       if b_rect.top >= 590:
              b_y = -20
              
       p.display.flip()
       
