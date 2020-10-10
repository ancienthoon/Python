import pygame as p
import random as r

p.init()

size = (800,400)

sc = p.display.set_mode(size)

p.display.set_caption("키보드 조작")

w = (255,255,255)
b = (0,0,0)
s = p.image.load("space.jpg")
s_rect = s.get_rect(left = 0, top = 0)
a = p.image.load("sol.jpg")
a_rect = a.get_rect(left = 10 , top = 0) 
y1 = p.image.load("y.jpg")
y1_rect = y1.get_rect(left = 700, top = 200)


font = p.font.SysFont('malgungothic',20) 
font1 = p.font.SysFont('malgungothic',50)

bo = p.image.load("b.png")


bg1 = s.copy()
s1_rect = bg1.get_rect(left = 800, top = 0)

x = 0
y = 0
y_c = 0
bg_x = 0
bg1_x = 800
en_x = 700
en_y = 0
score = 0
playing = True

while playing:

      for event in p.event.get():
            if event.type == p.QUIT:
                  playing = False
                  p.quit()
                  quit

            if event.type == p.KEYDOWN:
                  if event.key == p.K_w or event.key == p.K_s:
                        print()
                        y = -5
                  if event.key == p.K_s:
                        print()
                        y = 5
                 

            if event.type == p.KEYUP:
                  if event.key == p.K_w or event.key == p.K_s:
                        y = 0
                        
      a_rect.top += y            
      sc.fill(w)
      sc.blit(s,s_rect)
      sc.blit(bg1,s1_rect)
      s_rect.left -= 4
      s1_rect.left -= 4
      if s_rect.left <= -800:
            s_rect.left = 800
      if s1_rect.left <= -800:
            s1_rect.left = 800

      sc.blit(a,a_rect)
      if a_rect.top >= 350:
            y = 0
      if a_rect.top <= 0:
            y = 0

      sc.blit(y1,y1_rect) #left =x top = y
      y1_rect.left -= 9
      if y1_rect.left <= 0:
            y1_rect.left = 800
            y1_rect.top = r.randint(0,300)
            score += 1

      text = font.render('점수:{}'.format(score),True,(255,255,0))
      text1 = font1.render('GAME OVER',True,(0,255,255))
      sc.blit(text,(400,0))

      if a_rect.colliderect(y1_rect):
            sc.blit(bo,a_rect)
            sc.blit(text1,(300,150))
            playing = False 
      
      p.display.flip()
