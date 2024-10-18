import pygame, random
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Push it")
clock = pygame.time.Clock()



#player class
class player:
    def __init__(self):
        self.plr = pygame.Rect((400,250,20,20))
        
    
    def move(self):
        pygame.draw.rect(screen,(0,0,255),self.plr)
        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_w]:
            self.plr.move_ip(0,-3)
        if self.key[pygame.K_a]:
            self.plr.move_ip(-3,0)
        if self.key[pygame.K_s]:
            self.plr.move_ip(0,3)
        if self.key[pygame.K_d]:
            self.plr.move_ip(3,0)

block= pygame.Rect((300,250,20,20))
point = pygame.Rect((300,200,10,10))   
score = 0

#time and last score
sec = 60
ms = 60
l_sc = False
l_s = 0

def time_disp():
    global sec, ms, score, l_s, l_sc
    screen.blit(pygame.font.SysFont("comic sans",20).render(f"Time -> {sec}:{ms}",True,(0,0,0)),(500,10))
    if l_sc:
        screen.blit(pygame.font.SysFont("comic sans",20).render(f"Your last score was {l_s}",True,(0,0,0)),(480,460))

    ms -= 1
    if ms == -1:
        ms = 60
        sec -=1
        if sec == -1:
            sec = 60
            l_s = score
            score = 0
            l_sc = True


run = True

plr = player()

while run:
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(0,0,0),block)
    pygame.draw.rect(screen,(0,255,0),point)

    screen.blit(pygame.font.SysFont("comic sans",30).render(f"Score : {score}",True,(0,0,0)),(10,10))

    time_disp()

    if block.colliderect(point):
        score += 1
        point.y = random.randint(50,450)
        point.x = random.randint(10,680)

    plr.move()
    if block.colliderect(plr.plr):
        if plr.key[pygame.K_a]:
            block.move_ip(-4,0)
        if plr.key[pygame.K_w]:
            block.move_ip(0,-4)
        if plr.key[pygame.K_d]:
            block.move_ip(4,0)
        if plr.key[pygame.K_s]:
            block.move_ip(0,4)


    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(60)
pygame.quit()