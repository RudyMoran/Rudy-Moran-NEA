import pygame as py
import pygame.display

py.init()
tabsize = (1400, 800)
tab = py.display.set_mode(tabsize)
py.display.set_caption("Escape")
x = 50
y = 50
w = 50
h = 64
v = 10
on = True


class Character(pygame.sprite.Sprite):
    def __init__(self):
        self.look = py.Surface((int(25), int(50)))
        self.look.fill((0, 0, 0))
        self.rect = self.look.get_rect()

def play(x, y, h, v, taby, tabx):
    k = py.key.get_pressed()
    if k[py.K_a] and x > v:
        x = x - v
    if k[py.K_s] and y < taby - v:
        y = y + v
    if k[py.K_d] and x < tabx - v:
        x = x + v
    if k[py.K_w] and y > v:
        y = y - v
    tab.fill((255, 255, 255))
    py.draw.rect(tab, (76, 70, 152), (x, y, w, h))
    py.display.update()


def startGame():
  x = 50
  y = 50
  w = 50
  h = 64
  v = 10
  on = True
  tabx = 1400
  taby = 800
  player = py.draw.rect(tab,(0,0,0), (x,y,w,h))
  while on == True:
    #py.display.update()
    k = py.key.get_pressed()
    if k[py.K_a] and x > v:
        x = x - v
    if k[py.K_s] and y < taby - v:
        y = y + v
    if k[py.K_d] and x < tabx - v:
        x = x + v
    if k[py.K_w] and y > v:
        y = y - v
    #tab.fill((255, 255, 255))
    py.display.update()
    player = py.draw.rect(tab,(0,0,0), (x,y,w,h))



py.font.init()
myfont = py.font.SysFont("newcourier", 48)


def menu(tab, myfont):
    tab.fill((255, 255, 255))
    play_button = py.draw.rect(tab, (80, 80, 80), (550, 250, 300, 100))
    play_text = myfont.render("START GAME", False, (0, 0, 0))
    tab.blit(play_text, (590, 280))
    other_button = py.draw.rect(tab, (80, 80, 80), (550, 450, 300, 100))
    other_text = myfont.render("EXIT GAME", False, (0,0,0))
    tab.blit(other_text,(600,480))
    py.display.update()

    if event.type == py.MOUSEBUTTONDOWN:
        click = event.pos
        if play_button.collidepoint(click):
            print('THIS IS WHERE THE GAME STARTS')
            tab.fill((255, 255, 255))
            startGame()
            

        if other_button.collidepoint(click):
            print("NOT YET")


while on:
    #py.time.delay(100)
    for event in py.event.get():
        if event.type == py.QUIT:
            on = False
        menu(tab, myfont)

py.quit()


