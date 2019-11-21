import pygame
import balistic as bl
pygame.init()

screen = pygame.display.set_mode((1366, 768))
clock = pygame.time.Clock()
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
x, y, ww, hh = 100, 573, 32, 32
x1, y1 = 1148, 573
xyr = [x, y, x1, y1]
hp1 = 3
hp2 = 3

rect = pygame.Rect((64, 500), (32, 32))

grect = pygame.Rect(-2000, 600, 4000, 2000)
ground = pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [400, 600], [450, 680], [530, 720], [670, 600], [2000, 600], [200000000, 1000]])
mountain = pygame.draw.polygon(screen,(0, 255,0), [[450, 680], [480, 300], [530, 720]])
gun1, gun2 = pygame.Rect((x, y), (ww, hh)), pygame.Rect((x1, y1), (ww, hh))
GUN1 = pygame.Surface((ww, hh))
GUN2 = pygame.Surface((ww, hh))
GUN1. fill((255, 0, 0))
GUN2. fill((0, 0, 255))
font = pygame.font.Font(None, 64)
u = 1
k = 0
y1 = 5
while True:
    txt1 = font.render(str(hp1), True, (0, 0, 0))
    txt2 = font.render(str(hp2), True, (0, 0, 0))
    velocity1 = [6, -6]
    A = pygame.Rect(list(rect))
    if k == 0:
        xf = xyr[0]
        yf = xyr[1]
        k = 1
        h = 2000
        jj = [x+(ww//2)+20, xyr[1]-(hh//2)]
        enemy = gun2
        color = (255, 0, 0)
        gun0 = gun1

    else:
        xf = xyr[2]
        yf = xyr[3]
        k = 0
        A[0] *= -1
        h = -654
        jj = [(x1-ww//2)-20, xyr[3]-(hh//2)]
        enemy = gun1
        color = (0, 0, 255)
        gun0 = gun2

    clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    A[0], A[1] = jj[0], jj[1]
    xx1, yy1, jj = bl.control(screen, GUN1, gun1, GUN2, gun2, xf, yf, ww, hh, h, color, jj, txt1, txt2)
    velocity2 = bl.velocity(velocity1, xx1, yy1, gun0, gun2)
    rta = bl.bullet(A, screen, velocity2, y1, ground, GUN1, gun1, GUN2, gun2, jj, enemy, color, xf, yf, ww, hh, u, mountain, txt1, txt2)
    if k == 1:
        hp2 += rta
    else:
        hp1 += rta

    ground = pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [400, 600], [450, 680], [530, 720], [670, 600], [2000, 600], [200000000, 1000]])
    mountain = pygame.draw.polygon(screen,(0, 255,0), [[450, 680], [480, 300], [530, 720]])
    screen.blit(txt1, (0, 0))
    screen. blit(txt2, (1200, 0))
    screen. blit(GUN1, gun1)
    screen. blit(GUN2, gun2)
    pygame.display.update()
    if hp1 == 0:
        bl.gameover(2)
    elif hp2 == 0:
        bl.gameover(1)
