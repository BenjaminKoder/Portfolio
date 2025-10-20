import pygame as pg
from sys import exit
import random as ran
import math as pl
#Må kalles for at pygame skal funke:
pg.init()

character_height = 65*1.2
character_width = 60*1.2
zombie_width = 80
zombie_height = 90
widthWindow = 800
heightWindow = 400

score = 0
score = str(score)
liv = 170
liv = str(liv)


#Setter display-surface med width 800 og hight 400:
screen = pg.display.set_mode((widthWindow,heightWindow))
#Setter navn på spillet:
pg.display.set_caption("Skyt sirkelen")
clock = pg.time.Clock()



#font settes, først type font så størrelsen:
test_font = pg.font.Font("Fonts/Bebas_Neue/BebasNeue-Regular.ttf",50)
life_surface = test_font.render(liv, True, "black")
life_rect = life_surface.get_rect(topleft = (10,10))

#Man kan kun ha et display-surface, det er det som vises. Man kan derimot ha uendelig med regular surfaces som ikke vises, disse kan f.eks legges på det displayed surface
#Et regular surface som kan displayes slik som screen over:
#test_surface = pg.Surface((100,200))
#test_surface.fill("yellow")

#loader bildet til variabelen himmel_surface. Converter for da kan python lettere jobbe med bildene
himmel_surface = pg.image.load("Bilder/sky1.png").convert()
himmel_surface = pg.transform.scale(himmel_surface,(800,400))
bakke_surface = pg.image.load("Bilder/bakke1.png").convert()
bakke_surface = pg.transform.scale(bakke_surface,(800,230))
#når den skal rendere tekst-fonten må teksten skrives, om det er AA (smooth edges på teksten) og fargen må settes:
score_surface = test_font.render(score, True, "black")
score_rect = score_surface.get_rect(midtop = (widthWindow/2,10))




#convert_alpha() for å fjerne den svarte/hvite bakgrunnsfargen:
character_surface = pg.image.load("Bilder/terraria-character.png").convert_alpha()
character_surface = pg.transform.scale(character_surface, (character_width,character_height))
#Tar et surface og tegner et rektangel rundt det, starter fra venstre hjørne her:
character_rect = character_surface.get_rect(midbottom = (80, 292))

#sirkelspill:
circle_surf = pg.Surface((100,100))
diameter = ran.randint(70,100)
circle_rect = pg.Rect(ran.randint(0,widthWindow-20),ran.randint(0,heightWindow-20),diameter,diameter)




zombie_surface = pg.image.load("Bilder/terraria-zombie.png")
zombie_surface = pg.transform.scale(zombie_surface,(zombie_width, zombie_height))
zombie_rect = zombie_surface.get_rect(midbottom = (600,300))

zombie_speed = 2
character_speed = 1
skudd = 30
x = 1
d = 0
circle_color = "#ff0000"

#while-løkken kjøres i all evighet ettersom True aldri blir false
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            #Motsatte av pg.init():
            pg.quit()
            #fra sys:
            exit()
#         #Sjekker om musen flytter seg:
#         if event.type == pg.MOUSEMOTION:
#             if character_rect.collidepoint(zombie_rect):
#                  print("collision")
#         if event.type == pg.mouse.get_pressed():
#             skudd-=1
#             print(skudd)
        #Skudd treffer zombien?:
#        if event.type == pg.MOUSEBUTTONDOWN:
#             skudd-=1
#             print(skudd)
#             mouse_pos = pg.mouse.get_pos()
#             if zombie_rect.collidepoint(mouse_pos):
#                 #Sjekker om venstre tast er nedtrykket:
#                 if pg.mouse.get_pressed()[0] == True:
#                     zombie_rect.left = widthWindow
        if event.type == pg.MOUSEBUTTONDOWN:
            skudd -= 1
            print(skudd)
            mouse_pos = pg.mouse.get_pos()
            mouse_press = pg.mouse.get_pressed()
            if circle_rect.collidepoint(mouse_pos) and mouse_press[0]:
                x += 1
                zombie_speed = pl.log(x)*2+1
                print(zombie_speed)
                score = int(score) + 1
                score = str(score)
                score_surface = test_font.render(score, True, "black")
                score_rect = score_surface.get_rect(midtop = (widthWindow/2,10))
                
                zombie_rect.left = widthWindow
                if d<60:
                    d+=5
                diameter = ran.randint(70-d,90-d)
                circle_rect = pg.Rect(ran.randint(20,widthWindow-20),ran.randint(20,heightWindow-20),diameter,diameter)
                
                r = lambda: ran.randint(0,235)
                print('#%02X%02X%02X' % (r(),r(),r()))
                circle_color = '#%02X%02X%02X' % (r(),r(),r())
                
    zombie_rect.left-=zombie_speed
    #     print(character_rect.left)
    #print(zombie_rect)

    #blit står for block-image-transfer: (betyr å sette et surface oppå et annet surface (her display-surfacet))
    #posisjonen er (0,0), altså origo på display-surfacen
    screen.blit(himmel_surface,(0,0))
    screen.blit(bakke_surface,(0,200))
    #tegner en rektangel på display-surfacet screen i fargen gull
#     pg.draw.rect(screen,"Gold", life_rect)
    pg.draw.rect(screen,"red", life_rect)
    pg.draw.rect(screen,"Gold", score_rect,border_radius=20)
    pg.draw.rect(screen,"Black", score_rect,1,20)
   
    screen.blit(score_surface,score_rect)
    screen.blit(zombie_surface,zombie_rect)
    screen.blit(character_surface,character_rect)


    
    #pg.draw.circle(screen,"red", circle_rect,20)
    #pg.draw.line(screen,"red",(0,0),(800,400),10)
    #pg.draw.line(screen,"red",(0,400),(800,0),10)
    
    if character_rect.colliderect(zombie_rect):
        pg.draw.line(screen,"red",(0,0),(800,400),10)
        pg.draw.line(screen,"red",(0,400),(800,0),10)
        liv =int(liv) - 1
        print(liv)
        liv = str(liv)
        life_surface = test_font.render(liv, True, "#00ff00")
        life_rect = life_surface.get_rect(topleft = (10,10))
    if int(liv) < 0:
        pg.quit()
        exit()
    pg.draw.ellipse(screen,circle_color,circle_rect)
    
    
    
    
    
    
    #Setter posisjonen til karakteren til andre siden av vinduet dersom den går utenfor x-verdiene til vinduet
    if zombie_rect.right <= 0:
        zombie_rect.left = widthWindow
        
    #Sjekker om de kolliderer, da er verdien enten True eller False
#     if character_rect.colliderect(zombie_rect):
#         print("collision")

    
    
            
    #Her skal alle elementene tegnes
    #Oppdaterer display-området fra variabelen "screen" hele tiden:
    pg.display.update()
    #Forteller while-løkken at den ikke skal kjøre mer enn 60 ganger i sekundet: (minimum fps kan ikke settes med en linje kode, men det er ikke noe å stresse med med enkle 2D-spill)
    clock.tick(60)
    