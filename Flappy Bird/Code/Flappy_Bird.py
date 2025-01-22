import pygame,sys,random
#functions
def create_pillar(): #coodinates of top bottom
    random_pos=random.choice(pillar_height)
    bottom_pillar=pillar.get_rect(midtop=(590,random_pos))
    top_pillar=pillar.get_rect(midbottom=(590,random_pos-250))
    return bottom_pillar,top_pillar

def display_pillar(pillars): #blit
    for p in pillars:
        screen.blit(pillar,p)
        
def floor_mvt(): #2 floors
    screen.blit(floor,(floor_x,720))
    screen.blit(floor,(floor_x +570,720))

def move_pillars(pillars): #r to l pillar
    for p in pillars:
        p.centerx-=5
    return pillars

def collision_check(pillars):
    for p in pillars:
        if bird_rect.colliderect(p):
            return False
    if bird_rect.top<= -100 or bird_rect.bottom>=720:
        return False
    return True

def show_score(game):
    if game=='main':
        text='Score:'+str(int(score))
        score_show=font.render(text,True,(255,255,255))
        score_rect=score_show.get_rect(center=(285,200))
        screen.blit(score_show,score_rect)
    if game=='over':
        text='Score:'+str(int(score))
        score_show=font.render(text,True,(255,255,255)) #anti-aliased text=true
        score_rect=score_show.get_rect(center=(285,200))
        screen.blit(score_show,score_rect)

        high_text='High Score:'+str(int(high))
        high_show=font.render(high_text,True,(255,255,255))
        high_rect=high_show.get_rect(center=(285,250))
        screen.blit(high_show,high_rect)

def change_score(score,high):
    if score>high:
        high=score
    return high

#starting
pygame.init()
screen=pygame.display.set_mode((570,820)) 
time=pygame.time.Clock()
font=pygame.font.SysFont('Optima',40)

#variables
down_speed=0.15
bird_mvt=0
game_state=True
score,high=0,0
loop_state=False

#design loop
print('GAME MODES:')
print('For day enter 1')
print('For evening enter 2')
x=input('__')
while True:
    if x=='1':
        bg=pygame.image.load('PIX/back 1.png').convert()
        floor=pygame.image.load('PIX/F1.png').convert()
        loop_state=True
        break
    elif x=='2':
        bg=pygame.image.load('PIX/back 2.png').convert()
        floor=pygame.image.load('PIX/floor 2.png').convert()
        loop_state=True
        break
    else:
        x=input('Number not valid. Enter number 1 or 2:')
        
#images
bg=pygame.transform.scale2x(bg)
floor=pygame.transform.scale2x(floor)
floor_x=0
bird=pygame.transform.scale2x(pygame.image.load('PIX/bird.png'))
bird_rect=bird.get_rect(center=(175,410))
game_over=pygame.image.load('PIX/game over.png')
game_over_rect=game_over.get_rect(center=(285,410))
pillar=pygame.image.load('PIX/pillar.png')
pillar_list=[] # top bottom coodinates
spawn=pygame.USEREVENT # timer
pygame.time.set_timer(spawn,1200) 
pillar_height=[300,450,600]

# GAME LOOP
while loop_state==True:
    #events
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit() 

        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_SPACE:
                bird_mvt=0 #stop down 
                bird_mvt-=7

            if i.key==pygame.K_SPACE and game_state==False:
                game_state=True
                pillar_list.clear()
                bird_rect.center=(175,410)
                bird_mvt=0
                score=0

        if i.type==spawn:
            pillar_list.extend(create_pillar()) # get coodinates of top bottom

    #background
    screen.blit(bg,(0,0))

    #MAIN LOOP
    if game_state: 
        #bird
        bird_mvt+=down_speed
        bird_rect.centery+=bird_mvt 
        screen.blit(bird,bird_rect)
        #pillars
        pillar_list=move_pillars(pillar_list) # r to l
        display_pillar(pillar_list) #blit
        game_state=collision_check(pillar_list)
        score+=0.008333
        show_score('main')
    else:
        high=change_score(score,high)
        show_score('over')
        screen.blit(game_over,game_over_rect)
    
    #floor
    floor_x-=1
    floor_mvt()
    if floor_x<=-570:
        floor_x=0
    pygame.display.update()
    time.tick(120) 
