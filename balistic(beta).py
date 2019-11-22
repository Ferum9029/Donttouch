import pygame
import random
pygame.init()

mode = 0


def menu(mode):
   screen = pygame.display.set_mode((1366, 768))
   name = pygame.image.load('guns-of-bAm-png-1.png')
   pygame.display.set_caption('Guns of BAm')
   h = 0
   screen.fill((77, 97, 167))
   font = pygame.font.Font(None, 58)
   first = 'PLAY'
   second = 'ARCADE'
   third = 'EXIT'
   circle = 'SQUARE:'
   bot = 'BOT'
   duel = 'DUEL'
   dueltxt = font.render(duel, True, (0, 0, 0))
   txt1 = font.render(first, True, (0, 0, 0))
   txt2 = font.render(second, True, (0, 0, 0))
   txt3 = font.render(third, True, (0, 0, 0))
   txtcircle = font.render(circle, True, (0, 0, 0))
   bottxt = font.render(bot, True, (0, 0, 0))
   rect1, rect2, rect3 = pygame.Rect(10, 15, 100, 40), pygame.Rect(10, 95, 168, 40), pygame.Rect(10, 135, 97, 40)
   duelrect = pygame.Rect(10, 55, 97, 40)
   print(duelrect)
   pygame.draw.line(screen, (255, 0, 0), (116, 589), (710, -717), 8)
   pygame.draw.circle(screen, (77, 97, 167), (116, 589), 1000, 950)
   pygame.draw.line(screen, (0, 0, 255), (1164, 589), (516, -597), 8)
   pygame.draw.circle(screen, (77, 97, 167), (1164, 589), 1000, 950)
   lxl = '1234'
   pygame.draw.circle(screen, (255, 0, 0), (116, 605), 32)
   pygame.draw.circle(screen, (0, 0, 255), (1164, 605), 32)
   botrect2 = pygame.draw.rect(screen, (0, 0, 0), (1330, 175, 26, 26), 3)
   botrect3 = pygame.draw.rect(screen, (0, 0, 0), (1304, 175, 26, 26), 3)
   botrect4 = pygame.draw.rect(screen, (0, 0, 0), (1278, 175, 26, 26), 3)
   botrect5 = pygame.draw.rect(screen, (0, 0, 0), (1252, 175, 26, 26), 3)
   pygame.draw.rect(screen, (77, 97, 167), (1251, 174, 106, 28))


   pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
   pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
   level1 = font.render((lxl[0]),True, (0, 0, 0))
   level2 = font.render((lxl[1]), True, (0, 0, 0))
   level3 = font.render((lxl[2]), True, (0, 0, 0))
   level4 = font.render((lxl[3]), True, (0, 0, 0))
   screen.blit(txt1, rect1)
   screen.blit(txt2, rect2)
   screen.blit(txt3, rect3)
   screen.blit(dueltxt, duelrect)
   screen.blit(txtcircle, (1173, 15))
   screen. blit(bottxt, (1173, 95))
   screen. blit(name, (481, 0))
   circlerect = pygame.draw.rect(screen, (0, 0, 0), (1330, 55, 26, 26), 3)
   screen.blit(bottxt, (1173, 95))
   botrect = pygame.draw.rect(screen, (0, 0, 0), (1330, 135, 26, 26), 3)
   running = True
   pygame.display.update()
   while running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               quit()
           elif event.type == pygame.MOUSEBUTTONDOWN:
               if rect1.collidepoint(event.pos) and mode == 0:
                   mode = 1
                   running = False
               elif circlerect.collidepoint(event.pos) and mode != 2:
                   mode = 2
                   screen.fill((77, 97, 167))
                   pygame.draw.line(screen, (255, 0, 0), (116, 589), (710, -717), 8)
                   pygame.draw.circle(screen, (77, 97, 167), (116, 589), 1000, 950)
                   pygame.draw.line(screen, (0, 0, 255), (1164, 589), (516, -597), 8)
                   pygame.draw.circle(screen, (77, 97, 167), (1164, 589), 1000, 950)
                   pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
                   pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
                   pygame.draw.lines(screen, (0, 0, 0), False, [[1330, 68], [1343, 81], [1356, 55]], 4)
                   pygame.Rect(-2000, 600, 4000, 2000)
                   pygame.Rect((100, 573), (32, 32))
                   pygame.Rect((1148, 573), (32, 32))
                   GUN1 = pygame.Surface((32, 32))
                   GUN2 = pygame.Surface((32, 32))
                   GUN1.fill((255, 0, 0))
                   GUN2.fill((0, 0, 255))
                   gun1, gun2 = pygame.Rect((100, 573), (32, 32)), pygame.Rect((1148, 573), (32, 32))
                   screen.blit(GUN1, gun1)
                   screen.blit(GUN2, gun2)
                   screen.blit(txt1, rect1)
                   screen.blit(txt2, rect2)
                   screen.blit(txt3, rect3)
                   screen.blit(name, (481, 0))
                   screen.blit(txtcircle, (1173, 15))
                   screen.blit(bottxt, (1173, 95))
                   screen.blit(bottxt, (1173, 95))
                   botrect = pygame.draw.rect(screen, (0, 0, 0), (1330, 135, 26, 26), 3)
                   circlerect = pygame.draw.rect(screen, (0, 0, 0), (1330, 55, 26, 26), 3)
                   screen.blit(dueltxt, duelrect)
                   pygame.display.update()
               elif circlerect.collidepoint(event.pos) and mode == 2:
                   screen.fill((77, 97, 167))
                   pygame.draw.line(screen, (255, 0, 0), (116, 589), (710, -717), 8)
                   pygame.draw.circle(screen, (77, 97, 167), (116, 589), 1000, 950)
                   pygame.draw.line(screen, (0, 0, 255), (1164, 589), (516, -597), 8)
                   pygame.draw.circle(screen, (77, 97, 167), (1164, 589), 1000, 950)
                   pygame.draw.circle(screen, (255, 0, 0), (116, 605), 32)
                   pygame.draw.circle(screen, (0, 0, 255), (1164, 605), 32)
                   pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
                   pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
                   screen.blit(txt1, rect1)
                   screen.blit(txt2, rect2)
                   screen.blit(txt3, rect3)
                   screen.blit(txtcircle, (1173, 15))
                   screen.blit(bottxt, (1173, 95))
                   screen.blit(bottxt, (1173, 95))
                   screen.blit(name, (481, 0))
                   screen.blit(dueltxt, duelrect)
                   botrect = pygame.draw.rect(screen, (0, 0, 0), (1330, 135, 26, 26), 3)

                   circlerect = pygame.draw.rect(screen, (0, 0, 0), (1330, 55, 26, 26), 3)
                   mode = 0
                   pygame.display.update() #нен № #Ne
               elif rect2.collidepoint(event.pos) and mode != 2:
                   mode = 3
                   running = False
               elif rect3.collidepoint(event.pos):
                   quit()
               elif rect1.collidepoint(event.pos) and mode == 2:
                   running = False
               elif botrect.collidepoint(event.pos) and mode == 2:
                   mode = 4
                   pygame.draw.lines(screen, (0, 0, 0), False, [[1330, 148], [1343, 161], [1356, 135]], 4)
                   botrect2 = pygame.draw.rect(screen, (0, 0, 0), (1330, 175, 26, 26), 3)
                   botrect3 = pygame.draw.rect(screen, (0, 0, 0), (1304, 175, 26, 26), 3)
                   botrect4 = pygame.draw.rect(screen, (0, 0, 0), (1278, 175, 26, 26), 3)
                   botrect5 = pygame.draw.rect(screen, (0, 0, 0), (1252, 175, 26, 26), 3)
                   screen.blit(level1, (1252, 215))
                   screen.blit(level2, (1278, 215))
                   screen.blit(level3, (1304, 215))
                   screen.blit(level4, (1330, 215))
                   pygame.display.update()
               elif botrect2.collidepoint(event.pos) and mode == 4:
                   pygame.draw.rect(screen, (77, 97, 167), (1252, 175, 78, 26))
                   botrect2 = pygame.draw.rect(screen, (0, 0, 0), (1330, 175, 26, 26), 3)
                   pygame.draw.lines(screen, (0, 0, 0), False, [[1330, 188], [1343, 201], [1356, 175]], 4)
                   botrect3 = pygame.draw.rect(screen, (0, 0, 0), (1304, 175, 26, 26), 3)
                   botrect4 = pygame.draw.rect(screen, (0, 0, 0), (1278, 175, 26, 26), 3)
                   botrect5 = pygame.draw.rect(screen, (0, 0, 0), (1252, 175, 26, 26), 3)
                   h = 4
                   pygame.display.update()
               elif botrect3.collidepoint(event.pos) and mode == 4:
                   pygame.draw.rect(screen, (77, 97, 167), (1252, 175, 78, 26))
                   botrect2 = pygame.draw.rect(screen, (0, 0, 0), (1330, 175, 26, 26), 3)
                   botrect3 = pygame.draw.rect(screen, (0, 0, 0), (1304, 175, 26, 26), 3)
                   pygame.draw.lines(screen, (0, 0, 0), False, [[1304, 188], [1317, 201], [1330, 175]], 4)
                   botrect4 = pygame.draw.rect(screen, (0, 0, 0), (1278, 175, 26, 26), 3)
                   botrect5 = pygame.draw.rect(screen, (0, 0, 0), (1252, 175, 26, 26), 3)
                   h = 3
                   pygame.display.update()
               elif botrect4.collidepoint(event.pos) and mode == 4:
                   pygame.draw.rect(screen, (77, 97, 167), (1252, 175, 78, 26))
                   botrect2 = pygame.draw.rect(screen, (0, 0, 0), (1330, 175, 26, 26), 3)
                   botrect3 = pygame.draw.rect(screen, (0, 0, 0), (1304, 175, 26, 26), 3)
                   botrect4 = pygame.draw.rect(screen, (0, 0, 0), (1278, 175, 26, 26), 3)
                   botrect5 = pygame.draw.rect(screen, (0, 0, 0), (1252, 175, 26, 26), 3)
                   pygame.draw.lines(screen, (0, 0, 0), False, [[1278, 188], [1291, 201], [1304, 175]], 4)
                   h = 2
                   pygame.display.update()
               elif botrect5.collidepoint(event.pos) and mode == 4:
                   pygame.draw.rect(screen, (77, 97, 167), (1252, 175, 78, 26))
                   botrect2 = pygame.draw.rect(screen, (0, 0, 0), (1330, 175, 26, 26), 3)
                   botrect3 = pygame.draw.rect(screen, (0, 0, 0), (1304, 175, 26, 26), 3)
                   botrect4 = pygame.draw.rect(screen, (0, 0, 0), (1278, 175, 26, 26), 3)
                   botrect5 = pygame.draw.rect(screen, (0, 0, 0), (1252, 175, 26, 26), 3)
                   pygame.draw.lines(screen, (0, 0, 0), False, [[1252, 188], [1265, 201], [1278, 175]], 4)
                   h = 1
                   pygame.display.update()
               elif mode == 4 and h != 0 and rect1.collidepoint(event.pos):
                   running = False
               elif botrect.collidepoint(event.pos) and mode == 4:
                   h = 0
                   mode = 2
                   pygame.draw.rect(screen, (77, 97, 167), (1250, 173, 126, 94))
                   pygame.draw.rect(screen, (77, 97, 167), (1328, 134, 32, 32))
                   botrect = pygame.draw.rect(screen, (0, 0, 0), (1330, 135, 26, 26), 3)
                   pygame.display.update()
               elif mode == 0 and botrect.collidepoint(event.pos):
                   mode = 5
                   pygame.draw.lines(screen, (0, 0, 0), False, [[1330, 148], [1343, 161], [1356, 135]], 4)
                   botrect2 = pygame.draw.rect(screen, (0, 0, 0), (1330, 175, 26, 26), 3)
                   botrect3 = pygame.draw.rect(screen, (0, 0, 0), (1304, 175, 26, 26), 3)
                   botrect4 = pygame.draw.rect(screen, (0, 0, 0), (1278, 175, 26, 26), 3)
                   botrect5 = pygame.draw.rect(screen, (0, 0, 0), (1252, 175, 26, 26), 3)
                   screen.blit(level1, (1252, 215))
                   screen.blit(level2, (1278, 215))
                   screen.blit(level3, (1304, 215))
                   screen.blit(level4, (1330, 215))
                   pygame.display.update()
               elif botrect2.collidepoint(event.pos) and mode == 5:
                   pygame.draw.rect(screen, (77, 97, 167), (1250, 173, 200, 30))
                   botrect2 = pygame.draw.rect(screen, (0, 0, 0), (1330, 175, 26, 26), 3)
                   pygame.draw.lines(screen, (0, 0, 0), False, [[1330, 188], [1343, 201], [1356, 175]], 4)
                   botrect3 = pygame.draw.rect(screen, (0, 0, 0), (1304, 175, 26, 26), 3)
                   botrect4 = pygame.draw.rect(screen, (0, 0, 0), (1278, 175, 26, 26), 3)
                   botrect5 = pygame.draw.rect(screen, (0, 0, 0), (1252, 175, 26, 26), 3)
                   h = 4
                   pygame.display.update()
               elif botrect3.collidepoint(event.pos) and mode == 5:
                   pygame.draw.rect(screen, (77, 97, 167), (1250, 173, 200, 30))
                   botrect2 = pygame.draw.rect(screen, (0, 0, 0), (1330, 175, 26, 26), 3)
                   botrect3 = pygame.draw.rect(screen, (0, 0, 0), (1304, 175, 26, 26), 3)
                   pygame.draw.lines(screen, (0, 0, 0), False, [[1304, 188], [1317, 201], [1330, 175]], 4)
                   botrect4 = pygame.draw.rect(screen, (0, 0, 0), (1278, 175, 26, 26), 3)
                   botrect5 = pygame.draw.rect(screen, (0, 0, 0), (1252, 175, 26, 26), 3)
                   h = 3
                   pygame.display.update()
               elif botrect4.collidepoint(event.pos) and mode == 5:
                   pygame.draw.rect(screen, (77, 97, 167), (1250, 173, 200, 30))
                   botrect2 = pygame.draw.rect(screen, (0, 0, 0), (1330, 175, 26, 26), 3)
                   botrect3 = pygame.draw.rect(screen, (0, 0, 0), (1304, 175, 26, 26), 3)
                   botrect4 = pygame.draw.rect(screen, (0, 0, 0), (1278, 175, 26, 26), 3)
                   botrect5 = pygame.draw.rect(screen, (0, 0, 0), (1252, 175, 26, 26), 3)
                   pygame.draw.lines(screen, (0, 0, 0), False, [[1278, 188], [1291, 201], [1304, 175]], 4)
                   h = 2
                   pygame.display.update()
               elif botrect5.collidepoint(event.pos) and mode == 5:
                   pygame.draw.rect(screen, (77, 97, 167), (1250, 173, 200, 30))
                   botrect2 = pygame.draw.rect(screen, (0, 0, 0), (1330, 175, 26, 26), 3)
                   botrect3 = pygame.draw.rect(screen, (0, 0, 0), (1304, 175, 26, 26), 3)
                   botrect4 = pygame.draw.rect(screen, (0, 0, 0), (1278, 175, 26, 26), 3)
                   botrect5 = pygame.draw.rect(screen, (0, 0, 0), (1252, 175, 26, 26), 3)
                   pygame.draw.lines(screen, (0, 0, 0), False, [[1252, 188], [1265, 201], [1278, 175]], 4)
                   h = 1
                   pygame.display.update()
               elif botrect.collidepoint(event.pos) and mode == 5:
                   h = 0
                   mode = 0
                   pygame.draw.rect(screen, (77, 97, 167), (1250, 173, 152, 94))
                   pygame.draw.rect(screen, (77, 97, 167), (1328, 134, 32, 32))
                   botrect = pygame.draw.rect(screen, (0, 0, 0), (1330, 135, 26, 26), 3)
                   pygame.display.update()
               elif rect1.collidepoint(event.pos) and mode == 5:
                   running = False
               elif mode == 5 and h != 0 and rect1.collidepoint(event.pos):
                   running = False
               elif rect2.collidepoint(event.pos) and mode == 2:
                   mode = 6
                   running = False
               elif duelrect.collidepoint(event.pos) and mode != 2:
                   mode = 7
                   running = False
               elif duelrect.collidepoint(event.pos) and mode == 2:
                   mode = 8
                   running = False
   if mode == 1:
       gamecircle()
   elif mode == 2:
       game()
   elif mode == 3:
       gamecircleArcade()
   elif mode == 4:
       gameBOT(h)
   elif mode == 5:
       gameBOTcircle(h)
   elif mode == 6:
       gameArcade()
   elif mode == 7:
       duelgame()
   elif mode == 8:
       gameduelsq()

def controlcircle(screen, GUN1, gun1, GUN2, gun2, xf, yf, ww, hh, h, color, jj, txt1, txt2, x, y, x1, y1):
    clock = pygame.time.Clock()
    running = True
    velocity = [0, 0]
    rect = pygame.Rect(h, yf, 2000, 5)
    shift = False
    mnozh = 10
    while running:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
                elif (e.key == pygame.K_LSHIFT or e.key == pygame.K_RSHIFT) and shift == False:
                    mnozh = 100
                    shift = True
                elif (e.key == pygame.K_LSHIFT or e.key == pygame.K_RSHIFT) and shift == True:
                    mnozh = 10
                    shift = False
                elif xf == gun1[0]:
                    if e.key == pygame.K_LEFT or e.key == pygame.K_a:
                        velocity[1] -= mnozh
                        velocity[0] -= mnozh
                    elif e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                        velocity[1] += mnozh
                        velocity[0] += mnozh
                elif xf == (gun2[0] + (ww//2)):
                    if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                        velocity[1] -= mnozh
                        velocity[0] += mnozh
                    elif e.key == pygame.K_LEFT or e.key == pygame.K_a:
                        velocity[1] += mnozh
                        velocity[0] -= mnozh
                if e.key == pygame.K_RETURN or e.key == pygame.K_SPACE:
                    return rect[0], rect[1], jj
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP or pygame.K_DOWN:
                    velocity[1] = 0
                    velocity[0] = 0
        rect.move_ip(*velocity)
        screen.fill((14, 150, 180))
        pygame.draw.line(screen, color, (xf + ww // 2, yf + hh // 2), (rect[0], rect[1]), ww // 3)
        pygame.draw.circle(screen, (14, 150, 180), (xf + ww // 2, yf + hh // 2), 2000, 1950)
        pygame.draw.aaline(screen, (255, 255, 255), (xf + ww // 2, yf + hh // 2), (rect[0], rect[1]))
        pygame.draw.circle(screen, (14, 150, 180), (xf + ww // 2, yf + hh // 2), 2000, 1650)
        pygame.draw.circle(screen, (255, 0, 0), (x + (ww // 2), y + hh), 32)
        pygame.draw.circle(screen, (0, 0, 255), (x1 + (ww // 2), y + hh), 32)
        pygame.draw.polygon(screen, (14, 150, 180), [[-2000, 1000], [-2000, 600], [400, 600], [450, 680], [480, 450], [530, 720], [670, 600],[2000, 600], [2000, 1000]])
        pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
        pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
        screen.blit(txt1, (0, 0))
        screen. blit(txt2, (1277, 0))
        pygame.display.update()
        #print(gun1, gun2, xf, yf)

# rect(710, -717, 2000, 5) red
# rect(516, -597, 2000, 5) blue


def bulletcircle(A, screen, velocity, y, ground, gun1, gun2, enemy, u, mountain, txt1, txt2, x, yyy, x1, y1, ww, hh):
    clock = pygame.time.Clock()
    FPS= 30
    WHITE = (255, 255, 255)
    image = pygame.Surface((8, 8))
    image .fill(WHITE)
    back = pygame.Surface((16, 16))
    back.fill((14, 150, 180))
    running = True
    velocity[0], velocity[1] = velocity[0]*u, velocity[1]*u
    while running:
        clock.tick(FPS)/1000
        K = [A[0], A[1]]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
        velocity[1] += y
        A.move_ip(*velocity)
        pygame.draw.circle(screen, (255, 0, 0), (x + (ww // 2), yyy + hh), 32)
        pygame.draw.circle(screen, (0, 0, 255), (x1 + (ww // 2), y1 + hh), 32)
        mountain = pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
        ground = pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
        screen.blit(image, A)
        screen.blit(txt1, (0, 0))
        screen. blit(txt2, (1277, 0))
        if ground.colliderect(A) or mountain.colliderect(A) or A[0] > 1366 or A[0] < 0:
            running = False
        if enemy.colliderect(A):
            return -1
        pygame.display.update()
        screen.blit(back, K)

    return 0


def velocity(velocity1, x, y, gun0, gun2):
    gug = [0, 0]
    x1, y1 = velocity1[0], velocity1[1]
    if gun0 == gun2:
        if -654 < x < 1146:
            gug[0] = int(abs(((abs(x)-1146)*(x1*0.01)))*-1)
            gug[1] = int(((y - 573)*(y1*0.01))*-1)
        elif 1141 <= x <= 1151:
            gug = [0, 20]
        elif -659 <= x <= -649:
            gug = [-50, 0]
        else:
            gug = [0, 0]
    else:
        if 145 < x < 1995:
            gug[0] = int(((x-140)*(x1*0.01)))
            gug[1] = int(((y - 573)*(y1*0.01))*-1)
        elif 135 <= x <= 145:
            gug = [0, 20]
        elif 1995 <= x <= 2005:
            gug = [50, 0]
        else:
            gug = [0, 0]
    return gug


def gameover(player):
   screen = pygame.display.set_mode((1366, 768))
   pygame.display.set_caption('Guns of BAm')
   screen.fill((77, 97, 167))
   font = pygame.font.Font(None, 92)
   font1 = pygame.font.Font(None, 58)
   b = 'GAME OVER'
   a =  'PLAYER{} WON'.format(player)
   menutr = 'MENU'
   txt = font.render(b, True, (0, 0, 0))
   txt1 = font1.render(a, True, (0, 0, 0))
   menutxt = font1.render(menutr, True, (0, 0, 0))
   menurect = pygame.Rect(626, 455, 114, 40)
   screen.blit(txt, (489, 252))
   screen.blit(txt1, (539, 314))
   screen.blit(menutxt, (626, 455))
   t = pygame.draw.rect(screen, (0, 0, 0), (617, 446, 132, 49), 3)
   pygame.display.update()
   #print(txt, txt1, menutxt)
   running = True
   while running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               quit()
           elif event.type == pygame.MOUSEBUTTONDOWN:
               if t.collidepoint(event.pos):
                   menu(mode)


def gamecircle():

    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption('Guns of BAm')
    clock = pygame.time.Clock()
    FPS = 60

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    x, y, ww, hh = 100, 573, 32, 32
    x1, yyy1 = 1148, 573
    xyr = [x, y, x1, yyy1]
    hp1 = 3
    hp2 = 3

    rect = pygame.Rect((64, 500), (32, 32))

    grect = pygame.Rect(-2000, 600, 4000, 2000)
    mountain = pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
    ground = pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
    gun1, gun2 = pygame.draw.circle(screen, (255, 0, 0), (x + ww, y + hh), 32), pygame.draw.circle(screen, (0, 0, 255), (x1 + (ww // 2), yyy1 + hh), 32)
    GUN1 = pygame.Surface((ww, hh))
    GUN2 = pygame.Surface((ww, hh))
    GUN1. fill((255, 0, 0))
    GUN2. fill((0, 0, 255))
    font = pygame.font.Font(None, 64)
    u = 1
    k = 0
    y1 = 5
    running = True
    while running:
        hpa1 = '{}HP'.format(hp1)
        hpa2 = '{}HP'.format(hp2)
        txt1 = font.render(hpa1, True, (195, 60, 0))
        txt2 = font.render(hpa2, True, (195, 60, 0))
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
        A[0], A[1] = jj[0], jj[1]
        xx1, yy1, jj = controlcircle(screen, GUN1, gun1, GUN2, gun2, xf, yf, ww, hh, h, color, jj, txt1, txt2, x, y, x1, yyy1)
        velocity2 = velocity(velocity1, xx1, yy1, gun0, gun2)
        rta = bulletcircle(A, screen, velocity2, y1, ground,  gun1, gun2, enemy, u, mountain, txt1, txt2, x, y, x1, yyy1, ww, hh)
        if k == 1:
            hp2 += rta
        elif k == 0:
            hp1 += rta
        pygame.draw.circle(screen, (255, 0, 0), (x + (ww // 2), y + hh), 32)
        pygame.draw.circle(screen, (0, 0, 255), (x1 + (ww // 2), yyy1 + hh), 32)
        mountain = pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
        ground = pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
        screen.blit(txt1, (0, 0))
        screen. blit(txt2, (1277, 0))
        pygame.display.update()
        if hp1 == 0:
            gameover(2)
        elif hp2 == 0:
            gameover(1)


def control(screen, GUN1, gun1, GUN2, gun2, xf, yf, ww, hh, h, color, jj, txt1, txt2):
    y = 0
    clock = pygame.time.Clock()
    running = True
    velocity = [0, 0]
    rect = pygame.Rect(h, yf, 2000, 5)
    shift = False
    mnozh = 10
    while running:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
                elif (e.key == pygame.K_LSHIFT or e.key == pygame.K_RSHIFT) and shift == False:
                    mnozh = 100
                    shift = True
                elif (e.key == pygame.K_LSHIFT or e.key == pygame.K_RSHIFT) and shift == True:
                    mnozh = 10
                    shift = False
                elif xf == gun1[0]:
                    if e.key == pygame.K_LEFT or e.key == pygame.K_a:
                        velocity[1] -= mnozh
                        velocity[0] -= mnozh
                    elif e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                        velocity[1] += mnozh
                        velocity[0] += mnozh
                elif xf == gun2[0]:
                    if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                        velocity[1] -= mnozh
                        velocity[0] += mnozh
                    elif e.key == pygame.K_LEFT or e.key == pygame.K_a:
                        velocity[1] += mnozh
                        velocity[0] -= mnozh
                if e.key == pygame.K_RETURN or e.key == pygame.K_SPACE:
                    return rect[0], rect[1], jj
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP or pygame.K_DOWN:
                    velocity[1] = 0
                    velocity[0] = 0
        rect.move_ip(*velocity)
        screen.fill((14, 150, 180))
        pygame.draw.line(screen, color, (xf + ww // 2, yf + hh // 2), (rect[0], rect[1]), ww // 3)
        pygame.draw.circle(screen, (14, 150, 180), (xf + ww // 2, yf + hh // 2), 2000, 1950)
        pygame.draw.aaline(screen, (255, 255, 255), (xf + ww // 2, yf + hh // 2), (rect[0], rect[1]))
        pygame.draw.circle(screen, (14, 150, 180), (xf + ww // 2, yf + hh // 2), 2000, 1650)
        pygame.draw.polygon(screen, (14, 150, 180), [[-2000, 1000], [-2000, 600], [400, 600], [450, 680], [480, 450], [530, 720], [670, 600],[2000, 600], [2000, 1000]])
        pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
        pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])

        screen.blit(GUN1, gun1)
        screen.blit(GUN2, gun2)
        screen.blit(txt1, (0, 0))
        screen. blit(txt2, (1277, 0))
        pygame.display.update()
        #print(rect)


def bullet(A, screen, velocity, y, GUN1, gun1, GUN2, gun2, enemy, u, txt1, txt2):
    clock = pygame.time.Clock()
    FPS= 30
    WHITE = (255, 255, 255)
    image = pygame.Surface((8, 8))
    image .fill(WHITE)
    back = pygame.Surface((16, 16))
    back.fill((14, 150, 180))
    running = True
    velocity[0], velocity[1] = velocity[0]*u, velocity[1]*u
    while running:
        clock.tick(FPS)/1000
        K = [A[0], A[1]]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
        velocity[1] += y
        A.move_ip(*velocity)
        #print(A)
        mountain = pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
        ground = pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
        screen.blit(GUN1, gun1)
        screen.blit(GUN2, gun2)
        screen.blit(image, A)
        screen.blit(txt1, (0, 0))
        screen. blit(txt2, (1277, 0))
        if ground.colliderect(A) or mountain.colliderect(A) or A[0] > 1366 or A[0] < 0:
            running = False
        if enemy.colliderect(A):
            return -1
        pygame.display.update()
        screen.blit(back, K)
        #print(running)
    return 0


def game():

    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption('Guns of BAm')
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
    mountain = pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
    ground = pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
    gun1, gun2 = pygame.Rect((x, y), (ww, hh)), pygame.Rect((x1, y1), (ww, hh))
    GUN1 = pygame.Surface((ww, hh))
    GUN2 = pygame.Surface((ww, hh))
    GUN1. fill((255, 0, 0))
    GUN2. fill((0, 0, 255))
    font = pygame.font.Font(None, 64)
    u = 1
    k = 0
    y1 = 5
    running = True
    while running:
        hpa1 = '{}HP'.format(hp1)
        hpa2 = '{}HP'.format(hp2)
        txt1 = font.render(hpa1, True, (195, 60, 0))
        txt2 = font.render(hpa2, True, (195, 60, 0))
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
        A[0], A[1] = jj[0], jj[1]
        xx1, yy1, jj = control(screen, GUN1, gun1, GUN2, gun2, xf, yf, ww, hh, h, color, jj, txt1, txt2)
        velocity2 = velocity(velocity1, xx1, yy1, gun0, gun2)
        rta = bullet(A, screen, velocity2, y1, GUN1, gun1, GUN2, gun2, enemy, u, txt1, txt2)
        if k == 1:
            hp2 += rta
        elif k == 0:
            hp1 += rta

        mountain = pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
        ground = pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
        screen.blit(txt1, (0, 0))
        screen. blit(txt2, (1277, 0))
        screen. blit(GUN1, gun1)
        screen. blit(GUN2, gun2)
        pygame.display.update()
        if hp1 == 0:
            gameover(2)
        elif hp2 == 0:
            gameover(1)


def MyRand(h):
    b = random.randint(1, 1 + h)
    print(b)
    if b > 1:
        u = [(random.randrange(506, 556, 10)), 0]
        g = u[0] + 654
        g //= 10
        g = 573 - g * 10
        u[1] = g
    elif b == 2:
        u = [(random.randrange(346, 496, 10)), 0]
        g = u[0] + 654
        #g //= 10
        g = 573 - g#*10
        u[1] = g
    elif b == 1:
        u = [(random.randrange(556, 946, 10)), 0]
        #x+ y- right
        g = u[0] + 654
        #g //= 10
        g = 573 - g #* 10
        u[1] = g
    return u


def controlBOT(xb, yb, xbf, ybf, txt1, txt2, GUN1, GUN2, gun1, gun2, screen):
    if -654 == xb:
        return
    else:
        rect = pygame.Rect(-654, 573, 2000, 5)
        running = True
        while running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    quit()
            if rect[0] >= xb:
                running = False
            elif rect[0] // 100 != 0:
                velocity = [+100, -100]
                rect.move_ip(*velocity)
            else:
                velocity = [+10, -10]
                rect.move_ip(*velocity)
            screen.fill((14, 150, 180))
            pygame.draw.line(screen, (0, 0, 255), (xbf, ybf), (rect[0], rect[1]), 8)
            pygame.draw.circle(screen, (14, 150, 180), (xbf, ybf), 2000, 1950)
            pygame.draw.polygon(screen, (14, 150, 180), [[-2000, 1000], [-2000, 600], [400, 600], [450, 680], [480, 450], [530, 720], [670, 600], [2000, 600], [2000, 1000]])
            pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
            pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])

            screen.blit(GUN1, gun1)
            screen.blit(GUN2, gun2)
            screen.blit(txt1, (0, 0))
            screen.blit(txt2, (1277, 0))
            pygame.display.update()


def gameBOT(CHANCHE):

    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption('Guns of BAm')
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

    pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
    pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
    gun1, gun2 = pygame.Rect((x, y), (ww, hh)), pygame.Rect((x1, y1), (ww, hh))
    GUN1 = pygame.Surface((ww, hh))
    GUN2 = pygame.Surface((ww, hh))
    GUN1. fill((255, 0, 0))
    GUN2. fill((0, 0, 255))
    font = pygame.font.Font(None, 64)
    u = 1
    k = 0
    y1 = 5
    running = True
    while running:
        clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
        hpa1 = '{}HP'.format(hp1)
        hpa2 = '{}HP'.format(hp2)
        txt1 = font.render(hpa1, True, (195, 60, 0))
        txt2 = font.render(hpa2, True, (195, 60, 0))
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
            A[0], A[1] = jj[0], jj[1]
            xx1, yy1, jj = control(screen, GUN1, gun1, GUN2, gun2, xf, yf, ww, hh, h, color, jj, txt1, txt2)
            velocity2 = velocity(velocity1, xx1, yy1, gun0, gun2)
        else:
            uber = MyRand(CHANCHE)
            xb, yb = uber[0], uber[1]
            uber.append(2000)
            uber.append(5)
            jj = [(x1 - ww // 2) - 20, xyr[3] - (hh // 2)]
            A[0], A[1] = jj[0], jj[1]
            controlBOT(xb, yb, 1164, 589, txt1, txt2, GUN1, GUN2, gun1, gun2, screen)
            velocity2 = velocity(velocity1, xb, yb, [15, 2], [15, 2])
            enemy = gun1
            k = 0
        rta = bullet(A, screen, velocity2, y1, GUN1, gun1, GUN2, gun2, enemy, u, txt1, txt2)
        if k == 1:
            hp2 += rta
        elif k == 0:
            hp1 += rta

        pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
        pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
        screen.blit(txt1, (0, 0))
        screen. blit(txt2, (1277, 0))
        screen. blit(GUN1, gun1)
        screen. blit(GUN2, gun2)
        pygame.display.update()
        if hp1 == 0:
            gameover(2)
        elif hp2 == 0:
            gameover(1)



def gameBOTcircle(CHANCHE):

    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption('Guns of BAm')
    clock = pygame.time.Clock()
    FPS = 60

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    x, y, ww, hh = 100, 573, 32, 32
    x1, yyy1 = 1148, 573
    xyr = [x, y, x1, yyy1]
    hp1 = 3
    hp2 = 3

    rect = pygame.Rect((64, 500), (32, 32))

    grect = pygame.Rect(-2000, 600, 4000, 2000)
    mountain = pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
    ground = pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
    gun1, gun2 = pygame.draw.circle(screen, (255, 0, 0), (x + ww, y + hh), 32), pygame.draw.circle(screen, (0, 0, 255), (x1 + (ww // 2), yyy1 + hh), 32)
    GUN1 = pygame.Surface((ww, hh))
    GUN2 = pygame.Surface((ww, hh))
    GUN1.fill((255, 0, 0))
    GUN2.fill((0, 0, 255))
    font = pygame.font.Font(None, 64)
    u = 1
    k = 0
    y1 = 5
    running = True
    while running:
        clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
        hpa1 = '{}HP'.format(hp1)
        hpa2 = '{}HP'.format(hp2)
        txt1 = font.render(hpa1, True, (195, 60, 0))
        txt2 = font.render(hpa2, True, (195, 60, 0))
        velocity1 = [6, -6]
        A = pygame.Rect(list(rect))
        if k == 0:
            xf = xyr[0]
            yf = xyr[1]
            k = 1
            h = 2000
            jj = [x+(ww//2)+20, xyr[1]-(hh//2)]
            enemy = gun2
            gun0 = gun1
            A[0], A[1] = jj[0], jj[1]
            xx1, yy1, jj = controlcircle(screen, GUN1, gun1, GUN2, gun2, xf, yf, ww, hh, h, (255, 0, 0), jj, txt1, txt2, x, y, x1, yyy1)
            velocity2 = velocity(velocity1, xx1, yy1, gun0, gun2)
        else:
            uber = MyRand(CHANCHE)
            xb, yb = uber[0], uber[1]
            uber.append(2000)
            uber.append(5)
            jj = [(x1 - ww // 2) - 20, xyr[3] - (hh // 2)]
            A[0], A[1] = jj[0], jj[1]
            controlBOTcircle(xb, yb, 1164, 589, txt1, txt2, GUN1, GUN2, gun1, gun2, screen)
            velocity2 = velocity(velocity1, xb, yb, [15, 2], [15, 2])
            enemy = gun1
            k = 0
        rta = bulletcircle(A, screen, velocity2, y1, ground,  gun1, gun2, enemy, u, mountain, txt1, txt2, x, y, x1, yyy1, ww, hh)
        if k == 1:
            hp2 += rta
        elif k == 0:
            hp1 += rta

        pygame.draw.circle(screen, (255, 0, 0), (x + (ww // 2), y + hh), 32)
        pygame.draw.circle(screen, (0, 0, 255), (x1 + (ww // 2), yyy1 + hh), 32)
        mountain = pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
        ground = pygame.draw.polygon(screen, (0, 255, 0),
                                     [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720],
                                      [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
        screen.blit(txt1, (0, 0))
        screen.blit(txt2, (1277, 0))
        pygame.display.update()
        if hp1 == 0:
            gameover(2)
        elif hp2 == 0:
            gameover(1)


def controlBOTcircle(xb, yb, xbf, ybf, txt1, txt2, GUN1, GUN2, gun1, gun2, screen):
    if -654 == xb:
        return
    else:
        rect = pygame.Rect(-654, 573, 2000, 5)
        running = True
        while running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    quit()
            if rect[0] >= xb:
                running = False
            elif rect[0] // 100 != 0:
                velocity = [+100, -100]
                rect.move_ip(*velocity)
            else:
                velocity = [+10, -10]
                rect.move_ip(*velocity)
            screen.fill((14, 150, 180))
            pygame.draw.line(screen, (0, 0, 255), (xbf, ybf), (rect[0], rect[1]), 8)
            pygame.draw.circle(screen, (14, 150, 180), (xbf, ybf), 2000, 1950)
            pygame.draw.circle(screen, (255, 0, 0), (116, 605), 32)
            pygame.draw.circle(screen, (0, 0, 255), (1164, 605), 32)
            pygame.draw.polygon(screen, (14, 150, 180), [[-2000, 1000], [-2000, 600], [400, 600], [450, 680], [480, 450], [530, 720], [670, 600], [2000, 600], [2000, 1000]])
            pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
            pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])


            screen.blit(txt1, (0, 0))
            screen.blit(txt2, (1277, 0))
            pygame.display.update()


def gamecircleArcade():
    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption('Guns of BAm')
    clock = pygame.time.Clock()
    FPS = 60
    font1 = pygame.font.Font(None, 32)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    x, y, ww, hh = 100, 573, 32, 32
    x1, yyy1 = 1148, 573
    xyr = [x, y, x1, yyy1]
    hp1 = 3
    hp2 = 3
    kol1 = 0
    kol2 = 0
    rect = pygame.Rect((64, 500), (32, 32))

    grect = pygame.Rect(-2000, 600, 4000, 2000)
    mountain = pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
    ground = pygame.draw.polygon(screen, (0, 255, 0),
                                 [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720],
                                  [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
    gun1, gun2 = pygame.draw.circle(screen, (255, 0, 0), (x + ww, y + hh), 32), pygame.draw.circle(screen, (0, 0, 255),
                                                                                                   (x1 + (ww // 2),
                                                                                                    yyy1 + hh), 32)
    GUN1 = pygame.Surface((ww, hh))
    GUN2 = pygame.Surface((ww, hh))
    GUN1.fill((255, 0, 0))
    GUN2.fill((0, 0, 255))
    font = pygame.font.Font(None, 64)
    u = 1
    k = 0
    y1 = 5
    running = True
    while running:
        hpa1 = '{}HP'.format(hp1)
        hpa2 = '{}HP'.format(hp2)
        moves1 = '{}MOVES'.format(3-kol1)
        moves2 = '{}MOVES'.format(3-kol2)
        txt1 = font.render(hpa1, True, (195, 60, 0))
        txt2 = font.render(hpa2, True, (195, 60, 0))
        movetxt1 = font1.render(moves1, True, (60, 195, 0))
        movetxt2 = font1.render(moves2, True, (60, 195, 0))
        velocity1 = [6, -6]
        A = pygame.Rect(list(rect))
        if k == 0:
            xf = xyr[0]
            yf = xyr[1]
            kolx = kol1
            k = 1
            h = 2000
            jj = [xyr[0] + (ww // 2) + 20, xyr[1] - (hh // 2)]
            enemy = gun2
            color = (255, 0, 0)
            gun0 = gun1

        else:
            xf = xyr[2]
            yf = xyr[3]
            kolx = kol2
            k = 0
            A[0] *= -1
            h = -654
            jj = [(xyr[2] - ww // 2) - 20, xyr[3] - (hh // 2)]
            enemy = gun1
            color = (0, 0, 255)
            gun0 = gun2

        clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
        A[0], A[1] = jj[0], jj[1]
        xx1, yy1, jj, yap = controlcircleArcade(screen, GUN1, gun1, GUN2, gun2, xf, yf, ww, hh, h, color, jj, txt1, txt2, xyr[0], xyr[1], xyr[2], xyr[3], kolx, movetxt1, movetxt2)
        if yap == 0:
            velocity2 = velocity(velocity1, xx1, yy1, gun0, gun2)
            rta = bulletcircle(A, screen, velocity2, y1, ground, gun1, gun2, enemy, u, mountain, txt1, txt2, xyr[0], xyr[1], xyr[2], xyr[3], ww, hh)
            if k == 1:
                hp2 += rta
            elif k == 0:
                hp1 += rta
        elif yap == 1 and k == 1:
            print(xyr[0])
            xyr[0] = movementArcade(xyr[0], xyr[1], 0, 510)
            kol1 += 1
            print(xyr[0])
        elif yap == 1 and k == 0:
            print(xyr[2])
            xyr[2] = movementArcade(xyr[2], xyr[3], 670, 1366)
            kol2 += 1
            print(xyr[2])
        pygame.draw.circle(screen, (255, 0, 0), (xyr[0] + (ww // 2), xyr[1] + hh), 32)
        pygame.draw.circle(screen, (0, 0, 255), (xyr[2] + (ww // 2), xyr[3] + hh), 32)
        mountain = pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
        ground = pygame.draw.polygon(screen, (0, 255, 0),
                                     [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720],
                                      [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
        screen.blit(txt1, (0, 0))
        screen.blit(txt2, (1277, 0))
        screen.blit(movetxt1, (0, 40))
        screen.blit(movetxt2, (1272, 40))
        pygame.display.update()
        if hp1 == 0:
            gameover(2)
        elif hp2 == 0:
            gameover(1)


def controlcircleArcade(screen, GUN1, gun1, GUN2, gun2, xf, yf, ww, hh, h, color, jj, txt1, txt2, x, y, x1, y1, kolx, movetxt1, movetxt2):
    clock = pygame.time.Clock()
    running = True
    velocity = [0, 0]
    rect = pygame.Rect(h, yf, 2000, 5)
    shift = False
    mnozh = 10
    while running:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
                elif (e.key == pygame.K_LSHIFT or e.key == pygame.K_RSHIFT) and shift == False:
                    mnozh = 100
                    shift = True
                elif (e.key == pygame.K_LSHIFT or e.key == pygame.K_RSHIFT) and shift == True:
                    mnozh = 10
                    shift = False
                elif xf == gun1[0]:
                    if e.key == pygame.K_LEFT or e.key == pygame.K_a:
                        velocity[1] -= mnozh
                        velocity[0] -= mnozh
                    elif e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                        velocity[1] += mnozh
                        velocity[0] += mnozh
                elif xf == (gun2[0] + (ww // 2)):
                    if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                        velocity[1] -= mnozh
                        velocity[0] += mnozh
                    elif e.key == pygame.K_LEFT or e.key == pygame.K_a:
                        velocity[1] += mnozh
                        velocity[0] -= mnozh
                if e.key == pygame.K_RETURN or e.key == pygame.K_SPACE:
                    return rect[0], rect[1], jj, 0
                elif (e.key == pygame.K_TAB or e.key == pygame.K_KP0) and kolx != 3:
                    return rect[0], rect[1], jj, 1
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP or pygame.K_DOWN:
                    velocity[1] = 0
                    velocity[0] = 0
        rect.move_ip(*velocity)
        screen.fill((14, 150, 180))
        pygame.draw.line(screen, color, (xf + ww // 2, yf + hh // 2), (rect[0], rect[1]), ww // 3)
        pygame.draw.circle(screen, (14, 150, 180), (xf + ww // 2, yf + hh // 2), 2000, 1950)
        pygame.draw.aaline(screen, (255, 255, 255), (xf + ww // 2, yf + hh // 2), (rect[0], rect[1]))
        pygame.draw.circle(screen, (14, 150, 180), (xf + ww // 2, yf + hh // 2), 2000, 1650)
        pygame.draw.circle(screen, (255, 0, 0), (x + (ww // 2), y + hh), 32)
        pygame.draw.circle(screen, (0, 0, 255), (x1 + (ww // 2), y + hh), 32)
        pygame.draw.polygon(screen, (14, 150, 180),
                            [[-2000, 1000], [-2000, 600], [400, 600], [450, 680], [480, 450], [530, 720], [670, 600],
                             [2000, 600], [2000, 1000]])
        pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
        pygame.draw.polygon(screen, (0, 255, 0),
                            [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720],
                             [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
        screen.blit(txt1, (0, 0))
        screen.blit(txt2, (1277, 0))
        screen.blit(movetxt1, (0, 40))
        screen.blit(movetxt2, (1272, 40))
        pygame.display.update()
        # print(gun1, gun2, xf, yf)


def movementArcade(x, y, xg, xg1):
    running = True
    i = 0
    print(x, xg, xg1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    x -= 32
                    i = 1
                    running = False
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x += 32
                    i = 1
                    running = False
        if x < xg:
            x += 32
        elif x > xg1:
            x -= 32
        if i == 1:
            return int(x)


def gameArcade():
    font1 = pygame.font.Font(None, 32)
    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption('Guns of BAm')
    clock = pygame.time.Clock()
    FPS = 60

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    x, y, ww, hh = 100, 573, 32, 32
    x1, y1 = 1148, 573
    xyr = [x, y, x1, y1]
    hp1 = 3
    hp2 = 3
    kol1 = 0
    kol2 = 0
    rect = pygame.Rect((64, 500), (32, 32))

    grect = pygame.Rect(-2000, 600, 4000, 2000)
    mountain = pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
    ground = pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
    GUN1 = pygame.Surface((ww, hh))
    GUN2 = pygame.Surface((ww, hh))
    GUN1. fill((255, 0, 0))
    GUN2. fill((0, 0, 255))
    font = pygame.font.Font(None, 64)
    u = 1
    k = 0
    y1 = 5
    running = True
    while running:
        gun1, gun2 = pygame.Rect((xyr[0], xyr[1]), (ww, hh)), pygame.Rect((xyr[2], xyr[3]), (ww, hh))
        hpa1 = '{}HP'.format(hp1)
        hpa2 = '{}HP'.format(hp2)
        moves1 = '{}MOVES'.format(3 - kol1)
        moves2 = '{}MOVES'.format(3 - kol2)
        txt1 = font.render(hpa1, True, (195, 60, 0))
        txt2 = font.render(hpa2, True, (195, 60, 0))
        movetxt1 = font1.render(moves1, True, (60, 195, 0))
        movetxt2 = font1.render(moves2, True, (60, 195, 0))
        velocity1 = [6, -6]
        A = pygame.Rect(list(rect))
        if k == 0:
            xf = xyr[0]
            yf = xyr[1]
            kolx = kol1
            k = 1
            h = 2000
            jj = [xyr[0]+(ww//2)+20, xyr[1]-(hh//2)]
            enemy = gun2
            color = (255, 0, 0)
            gun0 = gun1

        else:
            xf = xyr[2]
            yf = xyr[3]
            k = 0
            kolx = kol2
            A[0] *= -1
            h = -654
            jj = [(xyr[2]-ww//2)-20, xyr[3]-(hh//2)]
            enemy = gun1
            color = (0, 0, 255)
            gun0 = gun2

        clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
        A[0], A[1] = jj[0], jj[1]
        xx1, yy1, jj, yap = controlArcade(screen, GUN1, gun1, GUN2, gun2, xf, yf, ww, hh, h, color, jj, txt1, txt2,  xyr[0], xyr[1], xyr[2], xyr[3], kolx, movetxt1, movetxt2)
        if yap == 0:
            velocity2 = velocity(velocity1, xx1, yy1, gun0, gun2)
            rta = bullet(A, screen, velocity2, y1, GUN1, gun1, GUN2, gun2, enemy, u, txt1, txt2)
            if k == 1:
                hp2 += rta
            elif k == 0:
                hp1 += rta
        elif yap == 1 and k == 1:
            print(xyr[0])
            xyr[0] = movementArcade(xyr[0], xyr[1], 0, 510)
            kol1 += 1
            print(xyr[0])
        elif yap == 1 and k == 0:
            print(xyr[2])
            xyr[2] = movementArcade(xyr[2], xyr[3], 670, 1366)
            kol2 += 1
            print(xyr[2])
        mountain = pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
        ground = pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])
        screen.blit(txt1, (0, 0))
        screen.blit(txt2, (1277, 0))
        screen.blit(movetxt1, (0, 40))
        screen.blit(movetxt2, (1272, 40))
        screen. blit(GUN1, gun1)
        screen. blit(GUN2, gun2)
        pygame.display.update()
        if hp1 == 0:
            gameover(2)
        elif hp2 == 0:
            gameover(1)


def controlArcade(screen, GUN1, gun1, GUN2, gun2, xf, yf, ww, hh, h, color, jj, txt1, txt2, x, y, x1, y1, kolx, movetxt1, movetxt2):
    y = 0
    clock = pygame.time.Clock()
    running = True
    velocity = [0, 0]
    rect = pygame.Rect(h, yf, 2000, 5)
    shift = False
    mnozh = 10
    while running:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
                elif (e.key == pygame.K_LSHIFT or e.key == pygame.K_RSHIFT) and shift == False:
                    mnozh = 100
                    shift = True
                elif (e.key == pygame.K_LSHIFT or e.key == pygame.K_RSHIFT) and shift == True:
                    mnozh = 10
                    shift = False
                elif xf == gun1[0]:
                    if e.key == pygame.K_LEFT or e.key == pygame.K_a:
                        velocity[1] -= mnozh
                        velocity[0] -= mnozh
                    elif e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                        velocity[1] += mnozh
                        velocity[0] += mnozh
                elif xf == gun2[0]:
                    if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                        velocity[1] -= mnozh
                        velocity[0] += mnozh
                    elif e.key == pygame.K_LEFT or e.key == pygame.K_a:
                        velocity[1] += mnozh
                        velocity[0] -= mnozh
                if e.key == pygame.K_RETURN or e.key == pygame.K_SPACE:
                    return rect[0], rect[1], jj, 0
                elif (e.key == pygame.K_TAB or e.key == pygame.K_KP0) and kolx != 3:
                    return rect[0], rect[1], jj, 1
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP or pygame.K_DOWN:
                    velocity[1] = 0
                    velocity[0] = 0
        rect.move_ip(*velocity)
        screen.fill((14, 150, 180))
        pygame.draw.line(screen, color, (xf + ww // 2, yf + hh // 2), (rect[0], rect[1]), ww // 3)
        pygame.draw.circle(screen, (14, 150, 180), (xf + ww // 2, yf + hh // 2), 2000, 1950)
        pygame.draw.aaline(screen, (255, 255, 255), (xf + ww // 2, yf + hh // 2), (rect[0], rect[1]))
        pygame.draw.circle(screen, (14, 150, 180), (xf + ww // 2, yf + hh // 2), 2000, 1650)
        pygame.draw.polygon(screen, (14, 150, 180), [[-2000, 1000], [-2000, 600], [400, 600], [450, 680], [480, 450], [530, 720], [670, 600],[2000, 600], [2000, 1000]])
        pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [510, 320], [530, 720]])
        pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [380, 600], [400, 680], [510, 680], [530, 720], [590, 720], [670, 600], [2000, 600], [200000000, 1000]])

        screen.blit(GUN1, gun1)
        screen.blit(GUN2, gun2)
        screen.blit(txt1, (0, 0))
        screen.blit(txt2, (1277, 0))
        screen.blit(movetxt1, (0, 40))
        screen.blit(movetxt2, (1272, 40))
        pygame.display.update()
        #print(rect)


def controlcircle1(screen, GUN1, gun1, GUN2, gun2, xf, yf, ww, hh, h, color, jj, txt1, txt2, x, y, x1, y1):
    clock = pygame.time.Clock()
    running = True
    velocity = [0, 0]
    rect = pygame.Rect(h, yf, 2000, 5)
    shift = False
    mnozh = 10
    while running:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
                elif (e.key == pygame.K_LSHIFT or e.key == pygame.K_RSHIFT) and shift == False:
                    mnozh = 100
                    shift = True
                elif (e.key == pygame.K_LSHIFT or e.key == pygame.K_RSHIFT) and shift == True:
                    mnozh = 10
                    shift = False
                elif xf == gun1[0]:
                    if e.key == pygame.K_LEFT or e.key == pygame.K_a:
                        velocity[1] -= mnozh
                        velocity[0] -= mnozh
                    elif e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                        velocity[1] += mnozh
                        velocity[0] += mnozh
                elif xf == (gun2[0] + (ww//2)):
                    if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                        velocity[1] -= mnozh
                        velocity[0] += mnozh
                    elif e.key == pygame.K_LEFT or e.key == pygame.K_a:
                        velocity[1] += mnozh
                        velocity[0] -= mnozh
                if e.key == pygame.K_RETURN or e.key == pygame.K_SPACE:
                    return rect[0], rect[1], jj
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP or pygame.K_DOWN:
                    velocity[1] = 0
                    velocity[0] = 0
        rect.move_ip(*velocity)
        screen.fill((14, 150, 180))
        pygame.draw.line(screen, color, (xf + ww // 2, yf + hh // 2), (rect[0], rect[1]), ww // 3)
        pygame.draw.circle(screen, (14, 150, 180), (xf + ww // 2, yf + hh // 2), 2000, 1950)
        pygame.draw.aaline(screen, (255, 255, 255), (xf + ww // 2, yf + hh // 2), (rect[0], rect[1]))
        pygame.draw.circle(screen, (14, 150, 180), (xf + ww // 2, yf + hh // 2), 2000, 1650)
        pygame.draw.circle(screen, (255, 0, 0), (x + (ww // 2), y + hh), 32)
        pygame.draw.circle(screen, (0, 0, 255), (x1 + (ww // 2), y + hh), 32)
        pygame.draw.polygon(screen, (14, 150, 180), [[-2000, 900], [-2000, 600], [2000, 600], [2000, 900]])
        pygame.draw.polygon(screen, (0, 255, 0), [[-2000, 900], [-2000, 600], [2000, 600], [2000, 900]])
        screen.blit(txt1, (0, 0))
        screen. blit(txt2, (1277, 0))
        pygame.display.update()
        #print(gun1, gun2, xf, yf)


def bulletcircle1(A, screen, velocity, y, ground, gun1, gun2, enemy, u, txt1, txt2, x, yyy, x1, y1, ww, hh):
    clock = pygame.time.Clock()
    FPS= 30
    WHITE = (255, 255, 255)
    image = pygame.Surface((8, 8))
    image .fill(WHITE)
    back = pygame.Surface((16, 16))
    back.fill((14, 150, 180))
    running = True
    velocity[0], velocity[1] = velocity[0]*u, velocity[1]*u
    while running:
        clock.tick(FPS)/1000
        K = [A[0], A[1]]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
        velocity[1] += y
        A.move_ip(*velocity)
        pygame.draw.circle(screen, (255, 0, 0), (x + (ww // 2), yyy + hh), 32)
        pygame.draw.circle(screen, (0, 0, 255), (x1 + (ww // 2), y1 + hh), 32)
        ground = pygame.draw.polygon(screen, (0, 255, 0), [[-2000, 900], [-2000, 600], [2000, 600], [2000, 900]])
        screen.blit(image, A)
        screen.blit(txt1, (0, 0))
        screen. blit(txt2, (1277, 0))
        if ground.colliderect(A) or A[0] > 1366 or A[0] < 0:
            running = False
        if enemy.colliderect(A):
            return -1
        pygame.display.update()
        screen.blit(back, K)

    return 0


def duelgame():

    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption('Guns of BAm')
    clock = pygame.time.Clock()
    FPS = 60

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    x, y, ww, hh = 100, 573, 32, 32
    x1, yyy1 = 1148, 573
    xyr = [x, y, x1, yyy1]
    hp1 = 1
    hp2 = 1

    rect = pygame.Rect((64, 500), (32, 32))

    grect = pygame.Rect(-2000, 600, 4000, 2000)
    mountain = pygame.draw.polygon(screen, (0, 255, 0), [[-2000, 900], [-2000, 600], [2000, 600], [2000, 900]])
    ground = pygame.draw.polygon(screen, (0, 255, 0), [[-2000, 900], [-2000, 600], [2000, 600], [2000, 900]])
    gun1, gun2 = pygame.draw.circle(screen, (255, 0, 0), (x + ww, y + hh), 32), pygame.draw.circle(screen, (0, 0, 255), (x1 + (ww // 2), yyy1 + hh), 32)
    GUN1 = pygame.Surface((ww, hh))
    GUN2 = pygame.Surface((ww, hh))
    GUN1. fill((255, 0, 0))
    GUN2. fill((0, 0, 255))
    font = pygame.font.Font(None, 64)
    k = 0
    u = 1
    y1 = 0
    running = True
    while running:
        rta = 0
        clock.tick(FPS) / 1000
        hpa1 = '{}HP'.format(hp1)
        hpa2 = '{}HP'.format(hp2)
        txt1 = font.render(hpa1, True, (195, 60, 0))
        txt2 = font.render(hpa2, True, (195, 60, 0))
        velocity2 = [0, 0]
        A = pygame.Rect(list(rect))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
                elif event.key == pygame.K_SPACE:
                    hp2 = 0
                    velocity2 = [6, 0]
                    image = pygame.Surface((8, 8))
                    irect = pygame.Rect(x, y, 8, 8)
                    irect.move_ip(*velocity2)
                    screen. blit(image, irect)
                elif event.key == pygame.K_RETURN:
                    hp1 = 0
                    velocity2  = [-6, 0]
                    image = pygame.Surface((8, 8))
                    irect = pygame.Rect(x, y, 8, 8)
                    irect.move_ip(*velocity2)
                    screen.blit(image, irect)
        screen. fill((14, 150, 180))
        pygame.draw.line(screen, (255, 0, 0), (140, 550), (190, 550), 8)
        pygame.draw.circle(screen, (14, 150, 180), (x + ww // 2, y - hh // 2), 2000, 1650)
        pygame.draw.circle(screen, (14, 150, 180), (x1 + ww // 2, yyy1 - hh // 2), 2000, 1650)
        pygame.draw.circle(screen, (255, 0, 0), (x + (ww // 2), y + hh), 32)
        pygame.draw.circle(screen, (0, 0, 255), (x1 + (ww // 2), yyy1 + hh), 32)
        pygame.draw.line(screen, (255, 0, 0), (110, 590), (190, 590), 8)
        pygame.draw.line(screen, (0, 0, 255), (x1 + ww // 2, yyy1 + hh // 2), ((x1 + ww // 2) - 70, yyy1 + hh // 2), 8)

        ground = pygame.draw.polygon(screen, (0, 255, 0), [[-2000, 900], [-2000, 600], [2000, 600], [2000, 900]])
        screen.blit(txt1, (0, 0))
        screen. blit(txt2, (1277, 0))
        pygame.display.update()
        if hp1 == 0:
            gameover(2)
        elif hp2 == 0:
            gameover(1)


def control1(screen, GUN1, gun1, GUN2, gun2, xf, yf, ww, hh, h, color, jj, txt1, txt2):
    y = 0
    clock = pygame.time.Clock()
    running = True
    velocity = [0, 0]
    rect = pygame.Rect(h, yf, 2000, 5)
    shift = False
    mnozh = 10
    while running:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
                elif (e.key == pygame.K_LSHIFT or e.key == pygame.K_RSHIFT) and shift == False:
                    mnozh = 100
                    shift = True
                elif (e.key == pygame.K_LSHIFT or e.key == pygame.K_RSHIFT) and shift == True:
                    mnozh = 10
                    shift = False
                elif xf == gun1[0]:
                    if e.key == pygame.K_LEFT or e.key == pygame.K_a:
                        velocity[1] -= mnozh
                        velocity[0] -= mnozh
                    elif e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                        velocity[1] += mnozh
                        velocity[0] += mnozh
                elif xf == gun2[0]:
                    if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                        velocity[1] -= mnozh
                        velocity[0] += mnozh
                    elif e.key == pygame.K_LEFT or e.key == pygame.K_a:
                        velocity[1] += mnozh
                        velocity[0] -= mnozh
                if e.key == pygame.K_RETURN or e.key == pygame.K_SPACE:
                    return rect[0], rect[1], jj
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP or pygame.K_DOWN:
                    velocity[1] = 0
                    velocity[0] = 0
        rect.move_ip(*velocity)
        screen.fill((14, 150, 180))
        pygame.draw.line(screen, color, (xf + ww // 2, yf + hh // 2), (rect[0], rect[1]), ww // 3)
        pygame.draw.circle(screen, (14, 150, 180), (xf + ww // 2, yf + hh // 2), 2000, 1950)
        pygame.draw.aaline(screen, (255, 255, 255), (xf + ww // 2, yf + hh // 2), (rect[0], rect[1]))
        pygame.draw.circle(screen, (14, 150, 180), (xf + ww // 2, yf + hh // 2), 2000, 1650)
        pygame.draw.polygon(screen, (14, 150, 180), [[-2000, 900], [-2000, 600], [2000, 600], [2000, 900]])
        pygame.draw.polygon(screen, (0, 255, 0), [[-2000, 900], [-2000, 600], [2000, 600], [2000, 900]])
        screen.blit(GUN1, gun1)
        screen.blit(GUN2, gun2)
        screen.blit(txt1, (0, 0))
        screen. blit(txt2, (1277, 0))
        pygame.display.update()
        #print(rect)


def bullet1(A, screen, velocity, y, GUN1, gun1, GUN2, gun2, enemy, u, txt1, txt2, ground):
    clock = pygame.time.Clock()
    FPS= 30
    WHITE = (255, 255, 255)
    image = pygame.Surface((8, 8))
    image .fill(WHITE)
    back = pygame.Surface((16, 16))
    back.fill((14, 150, 180))
    running = True
    velocity[0], velocity[1] = velocity[0]*u, velocity[1]*u
    while running:
        clock.tick(FPS)/1000
        K = [A[0], A[1]]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
        velocity[1] += y
        A.move_ip(*velocity)
        #print(A)
        pygame.draw.polygon(screen, (0, 255, 0), [[-2000, 900], [-2000, 600], [2000, 600], [2000, 900]])
        screen.blit(GUN1, gun1)
        screen.blit(GUN2, gun2)
        screen.blit(image, A)
        screen.blit(txt1, (0, 0))
        screen. blit(txt2, (1277, 0))
        if ground.colliderect(A) or A[0] > 1366 or A[0] < 0:
            running = False
        if enemy.colliderect(A):
            return -1
        pygame.display.update()
        screen.blit(back, K)
        #print(running)
    return 0


def gameduelsq():

    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption('Guns of BAm')
    clock = pygame.time.Clock()
    FPS = 60

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    x, y, ww, hh = 100, 573, 32, 32
    x1, y1 = 1148, 573
    xyr = [x, y, x1, y1]
    hp1 = 2
    hp2 = 2

    rect = pygame.Rect((64, 500), (32, 32))

    grect = pygame.Rect(-2000, 600, 4000, 2000)
    mountain = pygame.draw.polygon(screen, (0, 255, 0), [[-2000, 900], [-2000, 600], [2000, 600], [2000, 900]])
    ground = pygame.draw.polygon(screen, (0, 255, 0), [[-2000, 900], [-2000, 600], [2000, 600], [2000, 900]])
    gun1, gun2 = pygame.Rect((x, y), (ww, hh)), pygame.Rect((x1, y1), (ww, hh))
    GUN1 = pygame.Surface((ww, hh))
    GUN2 = pygame.Surface((ww, hh))
    GUN1. fill((255, 0, 0))
    GUN2. fill((0, 0, 255))
    font = pygame.font.Font(None, 64)
    u = 1
    k = 0
    y1 = 5
    running = True
    while running:
        hpa1 = '{}HP'.format(hp1)
        hpa2 = '{}HP'.format(hp2)
        txt1 = font.render(hpa1, True, (195, 60, 0))
        txt2 = font.render(hpa2, True, (195, 60, 0))
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu(mode)
        A[0], A[1] = jj[0], jj[1]
        xx1, yy1, jj = control1(screen, GUN1, gun1, GUN2, gun2, xf, yf, ww, hh, h, color, jj, txt1, txt2)
        velocity2 = velocity(velocity1, xx1, yy1, gun0, gun2)
        rta = bullet1(A, screen, velocity2, y1, GUN1, gun1, GUN2, gun2, enemy, u, txt1, txt2, ground)
        if k == 1:
            hp2 += rta
        elif k == 0:
            hp1 += rta

        pygame.draw.polygon(screen, (0, 255, 0), [[-2000, 900], [-2000, 600], [2000, 600], [2000, 900]])
        screen.blit(txt1, (0, 0))
        screen. blit(txt2, (1277, 0))
        screen. blit(GUN1, gun1)
        screen. blit(GUN2, gun2)
        pygame.display.update()
        if hp1 == 0:
            gameover(2)
        elif hp2 == 0:
            gameover(1)
mode = menu(mode)
