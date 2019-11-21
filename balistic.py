import pygame
pygame.init()


def control(screen, GUN1, gun1, GUN2, gun2, xf, yf, ww, hh, h, color, jj, txt1, txt2):
    y = 0
    running = True
    velocity = [0, 0]
    rect = pygame.Rect(h, yf, 2000, 5)
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            elif e.type == pygame.KEYDOWN:
                if xf == gun1[0]:
                    if e.key == pygame.K_LEFT or e.key == pygame.K_a:
                        velocity[1] -= 10
                        velocity[0] -= 10
                    elif e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                        velocity[1] += 10
                        velocity[0] += 10
                elif xf == gun2[0]:
                    if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                        velocity[1] -= 10
                        velocity[0] += 10
                    elif e.key == pygame.K_LEFT or e.key == pygame.K_a:
                        velocity[1] += 10
                        velocity[0] -= 10
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
        pygame.draw.aaline(screen, (255, 255, 255), (xf + ww//2, yf + hh//2), (rect[0], rect[1]))
        pygame.draw.polygon(screen, (255, 255, 255), [[-2000, 1000], [-2000, 600], [400, 600], [450, 680], [480, 450], [530, 720], [670, 600],[2000, 600], [2000, 1000]])
        pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [400, 600], [450, 680], [530, 720], [670, 600], [2000, 600], [200000000, 1000]])
        pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [530, 720]])
        screen.blit(GUN1, gun1)
        screen.blit(GUN2, gun2)
        screen.blit(txt1, (0, 0))
        screen.blit(txt2, (1200, 0))
        pygame.display.update()
        print(rect)

# rect(710, -717, 2000, 5) red
# rect(516, -597, 2000, 5) blue
def bullet(A, screen, velocity, y, ground, GUN1, gun1, GUN2, gun2, jj, enemy, color, xf, yf, ww, hh, u, mountain, txt1, txt2):
    clock = pygame.time.Clock()
    FPS= 199
    WHITE = (255, 255, 255)
    image = pygame.Surface((8, 8))
    image .fill(WHITE)
    running = True
    velocity[0], velocity[1] = velocity[0]*u, velocity[1]*u

    while running:
        clock.tick(FPS)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        velocity[1] += y
        A.move_ip(*velocity)
        if ground.colliderect(A) or mountain.colliderect(A) or A[0] > 1366 or A[0] < 0:
            running = False
            print('gg')
        if enemy.colliderect(A):
            return -1
        print(A)

        ground = pygame.draw.polygon(screen, (0, 255, 0), [[-200000000, 1000], [-2000, 600], [400, 600], [450, 680], [530, 720], [670, 600], [2000, 600], [200000000, 1000]])
        mountain = pygame.draw.polygon(screen, (0, 255, 0), [[450, 680], [480, 300], [530, 720]])
        screen.blit(GUN1, gun1)
        screen.blit(GUN2, gun2)
        screen.blit(image, A)
        screen.blit(txt1, (0, 0))
        screen.blit(txt2, (1200, 0))
        pygame.display.update()
        print(running)
    return 0


def velocity(velocity1, x, y, gun0, gun2):
    gug = [0, 0]
    x1, y1 = velocity1[0], velocity1[1]
    if gun0 == gun2:
        if -654 < x < 1146:
            gug[0] = abs(((abs(x)-1146)*(x1*0.01)))*-1
            gug[1] = ((y - 573)*(y1*0.01))*-1
        elif 1141 <= x <= 1151:
            gug = [0, 20]
        elif -659 <= x <= -649:
            gug = [50, 0]
        else:
            gug = [0, 0]
    else:
        if 145 < x < 1995:
            gug[0] = ((x-140)*(x1*0.01))
            gug[1] = ((y - 573)*(y1*0.01))*-1
        elif 135 <= x <= 145:
            gug = [0, 20]
        elif 1995 <= x <= 2005:
            gug = [50, 0]
        else:
            gug = [0, 0]

    return gug


def gameover(player):
   screen = pygame.display.set_mode((1366, 768))
   screen.fill((77, 97, 167))
   font = pygame.font.Font(None, 90)
   font1 = pygame.font.Font(None, 60)
   b = 'GAME OVER'
   a =  'PLAYER{} WON'.format(player)
   txt = font.render(b, True, (0, 0, 0))
   txt1 = font1.render(a, True, (0, 0, 0))
   screen.blit(txt, (500, 329))
   screen.blit(txt1, (540, 380))
   pygame.display.update()
   running = True
   while running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               quit()
