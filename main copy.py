import pygame
import random
import math


pygame.init()


witdh=800
height=600
FPS=30
black= (0,0,0)
white=(0,0,0)

number_enemies= 8
score=0

player_x_change=5

bullet_x_change = 0
bullet_y_change = 15
bullet_state = "ready"

"""alien_x_change =5
alien_y_change = 40
alienx_random= random.randint(0,witdh)
alieny_random= random.randint(50,150)"""

alien_x_change =[]
alien_y_change = []
alienx_random= []
alieny_random= []
alien_img=[]



clock= pygame.time.Clock()
#Icono
icon = pygame.image.load("ufo.png")
pygame.display.set_icon( icon )

pygame.display.set_caption( "Space invaders @Alejandro Merlina" )

#Pantalla
display_surface= pygame.display.set_mode((witdh,height))


#Fondo de pantalla
bg= pygame.image.load("fedex.jfif")
bg=pygame.transform.scale(bg,(witdh,height))


#Añadir imagenes

player= pygame.image.load("player.png")
bullet= pygame.image.load("tomato.png")
bullet=pygame.transform.scale(bullet,(60,60))
alien=pygame.image.load("alien33.png")

#Crear rectangulos (hitbox)
player_rect= player.get_rect()
bullet_rect= bullet.get_rect()
alien_rect= alien.get_rect()

#posicionar  nuestros rectangulos
player_rect.x= witdh/2
player_rect.y= height-64
player_rect.center =((witdh/2,height-64))

for i in range( number_enemies):

    alien_img.append(pygame.image.load("alien33.png"))
    alienx_random.append (random.randint(0,witdh))
    alieny_random.append (random.randint(50,150))
    alien_x_change.append(5)
    alien_y_change.append(40)
    



#Posicion en x de la bala
posicion_player=player_rect.x


bullet_rect_x= posicion_player
bullet_rect_y= (height-64)

def is_collision(alienx_random,alieny_random,bullet_rect_x,bullet_rect_y):

    distancia=math.sqrt((alienx_random - bullet_rect_x)**2 + (alieny_random - bullet_rect_y)**2)

    if distancia<27:
        return True
    else:
        return False

running = True


while running:

    display_surface.blit(bg,(0,0))  
    
    alien_rect.x +=alien_x_change[i]

    #For cada i en la lista hara esto

    """if alien_rect.left<=0:
        alien_x_change*= -1
        alien_rect.y += alien_y_change

    elif alien_rect.right>=witdh:
        alien_x_change*= -1
        alien_rect.y += alien_y_change"""

    #primer tipo de colision
        
    

    keys= pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_rect.left>= 0:
        player_rect.x -= player_x_change

    if keys[pygame.K_RIGHT] and player_rect.right<=witdh:
        player_rect.x += player_x_change


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_SPACE:
                
                if bullet_state == "ready":
                   
                    bullet_rect_x= player_rect.x
                    bullet_state = "fire"
               


    if bullet_state == "fire":
        
        #bullet_rect_x= posicion_player
        display_surface.blit(bullet,(bullet_rect_x , bullet_rect_y))
        bullet_rect_y -= bullet_y_change 


    if bullet_rect_y <=0:
        bullet_rect_y= (height-64)
        bullet_state="ready"


    """if bullet_rect.colliderect(alien_rect):

        score +=1
        print(score)
        alienx_random= random.randint(0,witdh)
        alieny_random= random.randint(50,150)
        bullet_rect_x= player_rect.x
        bullet_rect_y= (height-64)
        bullet_state= "ready"""
    
    #colision
    #verificar avriables
    


    for i in range(number_enemies):

        alienx_random[i] += alien_x_change[i]

        if alienx_random[i]<= 0:
            alien_x_change[i] *= -1

            alien_y_change[i]+= alien_y_change[i]


        elif alienx_random [i] >= witdh:

            alien_x_change[i] *= -1

        collision = is_collision(alienx_random[i],alieny_random[i],bullet_rect_x,bullet_rect_y)

        if collision==True:

            bullet_rect_y= (height-64)
            bullet_state = "ready"
            score +=1
            print(score)
            alienx_random[i]= random.randint(0,witdh)
            alieny_random[i]= random.randint(50,150)
            
   
        display_surface.blit(alien_img[i],(alienx_random[i],alieny_random[i]))

        
             
    display_surface.blit(player,player_rect)
    
    




    pygame.display.update()
    clock.tick(FPS)



