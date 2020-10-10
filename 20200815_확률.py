import pygame as p
import random as r

p.init()
w = (255,255,255)
size = (800,400)
sc = p.display.set_mode(size)
p.display.set_caption("게임판")
playing = True


b = p.image.load("1.png")
b_rect = b.get_rect(left = 700, top = 50)

c = p.image.load("20.png")
c_rect = c.get_rect(left = 700, top = 180)

m = p.image.load("100.png")
m_rect = m.get_rect(left = 700, top = 280)

re = p.image.load("re.png")
re_rect = re.get_rect(left = 0, top = 300)

bg = p.image.load("t.png")

money = 100000
font = p.font.SysFont("malgungothic",20)

box = 0

music = p.mixer.Sound("give.wav")

while playing:

       for event in p.event.get():
             if event.type == p.QUIT:
                   playing = False
                   p.quit()
                   quit()
             if event.type == p.MOUSEBUTTONDOWN:
                 if b_rect.collidepoint(event.pos):
                     box = r.choice([1,2,1,1,1])
                     if money <= 0:
                         print("돈부족!!")    
                         break   
                     if box == 1:
                         money += 200
                         music.play()
                     else:
                         money -= 100   
                 if c_rect.collidepoint(event.pos):
                     box = r.choice([1,2,2,2,1])
                     if money <= 0:
                         print("돈부족!!")    
                         break   
                     if box == 1:
                         money += 2000
                         music.play()
                     else:
                         money -= 1000   
                 if m_rect.collidepoint(event.pos):
                     box = r.choice([1,2,2,2,2])
                     if money <= 0:
                         print("돈부족!!")    
                         break   
                     if box == 1:
                         money += 20000
                         music.play()
                     else:
                         money -= 10000   
                 if re_rect.collidepoint(event.pos):
                     print("환전 아이콘 클릭")
                     money = money+1

                 
                    

       sc.fill(w)

       sc.blit(bg,(0,0))
       sc.blit(b,b_rect)
       sc.blit(c,c_rect)
       sc.blit(m,m_rect)
       sc.blit(re,re_rect)

       text = font.render("돈: {}".format(money),True,(255,0,255))
       sc.blit(text,(10,10)) 
       
       p.display.flip()
       
