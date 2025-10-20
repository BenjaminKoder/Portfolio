import pygame as pg
from sys import exit
import random as ran
import math as pl
filnavn = "lagringSkytSirkel.txt"
        
#Screen.blit funker ikke på sprites
class Character(pg.sprite.Sprite):
    def __init__(self):
        #arver sprite-klassen slik at den kan brukes i character-klassen også
        super().__init__()
        #convert_alpha() for å fjerne den svarte/hvite bakgrunnsfargen:
        
        #Animerer fuglen:
        self.character_walk = []
        for i in range(9):
            character_walk_1 = pg.image.load(f"Bilder/Parrot/tile00{i}.png")
            character_walk_1 = pg.transform.scale(character_walk_1,(51.5,45.1))
            self.character_walk.append(character_walk_1)
        self.character_index = 0
        self.character_jump = pg.image.load("Bilder/jump.png")
        
        self.image = self.character_walk[self.character_index]
        self.rect = self.image.get_rect(midbottom= (100,170))
        self.gravity = 0
        
    def character_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.rect.bottom >= 170:
            self.gravity = -10
    def apply_gravity(self):
        self.gravity +=0.4
        self.rect.y += self.gravity
        if self.rect.bottom >= 170:
            self.rect.bottom = 170
    def animation_state(self):
#         if self.rect.bottom < 170:
#             #jump-animasjon:
#             self.image = self.character_jump
#         #Dersom karakteren er på bakken:
#         else:
        #Per 10-ende frame bytter indexen fordi da blir indexen lik 1 mer enn før. På den siste framen i "animasjonen" character_walk byttes den tilbake til den første 
        self.character_index += 0.1
        if self.character_index >= len(self.character_walk):
            self.character_index=0
        self.image = self.character_walk[int(self.character_index)]
    def update(self):
        self.character_input()
        self.apply_gravity()
        self.animation_state()

def display_score():
    #pg.time.get_ticks() kalkulerer antall ticks siden vi kalte pg.init():
    currentTime = pg.time.get_ticks() - startTime
    time_surf = test_font.render(f"{currentTime/100:.0f}",True,"#ff0000")
    time_rect = time_surf.get_rect(topright=(widthWindow-10,10))
    pg.draw.rect(screen,"#c0e8ec", time_rect,border_radius=20)
    screen.blit(time_surf,time_rect)

def character_animation():
    global character_surface, character_index
    #skal spille gå-animasjon om spilleren er på bakken, og displaye jump-surfacet når spilleren ikke er på bakken:
    if character_rect.bottom < 292:
        #jump-animasjon:
        character_surface = character_jump
    #Dersom karakteren er på bakken:
    else:
        #Per 10-ende frame bytter indexen fordi da blir indexen lik 1 mer enn før. På den siste framen i "animasjonen" character_walk byttes den tilbake til den første 
        character_index += 0.1
        if character_index >= len(character_walk):
            character_index=0
        character_surface = character_walk[int(character_index)]    

#Må kalles for at pygame skal funke:
pg.init()

jump_Sound = pg.mixer.Sound("Audio/jump.wav")
jump_Sound.set_volume(0.5)

    


character_height = 65*1.2
character_width = 60*1.2
zombie_width = 80
zombie_height = 90
widthWindow = 800
heightWindow = 400

lagring = []
with open(filnavn,"r",encoding="utf-8-sig") as fil:
    for linje in fil:
        lagring.append(int(linje))
totalScore = lagring[0]
score = str(0)
liv_iStarten = lagring[1]
liv = str(liv_iStarten)
highscore = lagring[2]



#Lager en "gruppe"-konteiner med sprites, men med kun en sprite:
character = pg.sprite.GroupSingle()
#Adder fuglen inn i konteineren
character.add(Character())





life_color = "#00bf00"
score_color = "#bFa700"


#Setter display-surface med width 800 og hight 400:
screen = pg.display.set_mode((widthWindow,heightWindow))
#Setter navn på spillet:
pg.display.set_caption("Sirkelspillet")
clock = pg.time.Clock()

game_Active = False
startTime = 0


#font settes, først type font så størrelsen:
test_font = pg.font.Font("Fonts/Bebas_Neue/BebasNeue-Regular.ttf",50)
loadingScreenFont10 = pg.font.Font("Fonts/Press_Start_2P/PressStart2P-Regular.ttf",10)
loadingScreenFont30 = pg.font.Font("Fonts/Press_Start_2P/PressStart2P-Regular.ttf",30)
life_surface = test_font.render(liv, True, life_color)
life_rect = life_surface.get_rect(topleft = (10,10))


#Man kan kun ha et display-surface, det er det som vises. Man kan derimot ha uendelig med regular surfaces som ikke vises, disse kan f.eks legges på det displayed surface

#loader bildet til variabelen himmel_surface. Converter for da kan python lettere jobbe med bildene
himmel_surface = pg.image.load("Bilder/sky1.png").convert()
himmel_surface = pg.transform.scale(himmel_surface,(800,400))
bakke_surface = pg.image.load("Bilder/bakke1.png").convert()
bakke_surface = pg.transform.scale(bakke_surface,(800,230))
#når den skal rendere tekst-fonten må teksten skrives, om det er AA (smooth edges på teksten) og fargen må settes:
score_surface = test_font.render(score, True, score_color)
score_rect = score_surface.get_rect(midtop = (widthWindow/2,10))



#convert_alpha() for å fjerne den svarte/hvite bakgrunnsfargen:
character_walk_1 = pg.image.load("Bilder/player_walk_1.png").convert_alpha()
character_walk_2 = pg.image.load("Bilder/player_walk_2.png").convert_alpha()
character_walk = [character_walk_1,character_walk_2]
character_index = 0
character_jump = pg.image.load("Bilder/jump.png").convert_alpha()
#Tar et surface og tegner et rektangel rundt det, starter fra venstre hjørne her:
character_surface = character_walk[character_index]
character_rect = character_surface.get_rect(midbottom = (80, 292))
character_gravity = 0


logo_surf = pg.image.load("Bilder/target.png")
logo_surf = pg.transform.scale(logo_surf,(200,200))
logo_rect = logo_surf.get_rect(center=(widthWindow/2,heightWindow/2))



#sirkler:
circle_surf = pg.Surface((100,100))
diameter = ran.randint(70,100)
circle_rect = pg.Rect(ran.randint(0,widthWindow-20),ran.randint(0,heightWindow-20),diameter,diameter)


#loading-screen:
instruks_surf = loadingScreenFont10.render("Ikke treff Hank Hill, og skyt sirklene for poeng!", True,"#c0e8ec")
instruks_rect = instruks_surf.get_rect(center=(widthWindow/2,20))
tittel_surf = loadingScreenFont30.render("Sirkelspillet", True, "#000035")
tittel_rect = tittel_surf.get_rect(center=(widthWindow/2,70))
instruks2_surf = loadingScreenFont10.render("Fugl = ny rekord. Trykk SPACE for å begynne",True,"#c0e8ec")
instruks2_rect = instruks2_surf.get_rect(midbottom=(widthWindow/2,heightWindow-40))


hank_surface = pg.image.load("Bilder/hankhill.png")
hank_surface = pg.transform.scale(hank_surface,(zombie_width, zombie_height))
zombie_rect = hank_surface.get_rect(midbottom = (600,300))

# dale_surf = pg.image.load("Bilder/Dale_Gribble.png")
# jeff_surf = pg.image.load("Bilder/Jeff_Boomhauer.png")
# hank_surf = pg.image.load("Bilder/Hank_Hill_Standing.png")
# bill_surf = pg.image.load("Bilder/Bill_Dauterive.png")
# dale_surf = pg.transform.scale(dale_surf,(125,151.5))
# jeff_surf = pg.transform.scale(jeff_surf,(125,170))
# hank_surf = pg.transform.scale(hank_surf,(125,151.5))
# bill_surf = pg.transform.scale(bill_surf,(125,151.5))

zombie_speed = 2
character_speed = 1
x = 1
d = 0
rotation = 0
circle_color = "#ff0000"




#while-løkken kjøres i all evighet ettersom True aldri blir false
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            
            with open(filnavn, "w", encoding="utf-8-sig") as fil:
                fil.write(f"{totalScore}\n")
                fil.write(f"{liv_iStarten}\n")
                fil.write(f"{highscore:.0f}")
            
            #Motsatte av pg.init():
            pg.quit()
            #fra sys:
            exit()
        if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and character_rect.bottom >= 292:
                    #Hopp:
                    character_gravity = -10
                    jump_Sound.play()
        if game_Active:
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                mouse_press = pg.mouse.get_pressed()
                if circle_rect.collidepoint(mouse_pos) and mouse_press[0]:
                    x += 1
                    zombie_speed = pl.log2(x)*2+1
                    score = int(score) + 1
                    score = str(score)
                    score_surface = test_font.render(score, True, score_color)
                    score_rect = score_surface.get_rect(midtop = (widthWindow/2,10))
                    
                    zombie_rect.left = widthWindow
                    if d<60:
                        d+=5
                    diameter = ran.randint(70-d,90-d)
                    circle_rect = pg.Rect(ran.randint(20,widthWindow-20),ran.randint(20,heightWindow-20),diameter,diameter)
                    
                    r = lambda: ran.randint(0,235)
                    circle_color = '#%02X%02X%02X' % (r(),r(),r())
            
            
        #Restart:
        elif game_Active == False:
            #Resetter alle stats og progresjon ved trykk på start-knappen space:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                game_Active = True
                score = str(0)
                x=2
                zombie_speed = pl.log2(x)*2+1
                d=0
                rotation=0
                diameter = ran.randint(70-d,90-d)
                circle_rect = pg.Rect(ran.randint(20,widthWindow-20),ran.randint(20,heightWindow-20),diameter,diameter)
                zombie_rect.left = widthWindow
                score_surface = test_font.render(score, True, score_color)
                score_rect = score_surface.get_rect(midtop = (widthWindow/2,10))
                life_surface = test_font.render(str(liv), True, life_color)
                life_rect = life_surface.get_rect(topleft = (10,10))
                #Vil da resette tiden currentTime til 0 i display_score-funksjonen:
                startTime = pg.time.get_ticks()
                
                
    if game_Active:
        zombie_rect.left-=zombie_speed
        #blit står for block-image-transfer: (betyr å sette et surface oppå et annet surface (her display-surfacet))
        #posisjonen er (0,0), altså origo på display-surfacen
        screen.blit(himmel_surface,(0,0))
        screen.blit(bakke_surface,(0,200))
        #tegner en rektangel på display-surfacet screen i fargen gull
        pg.draw.rect(screen,"#c0e8ec", life_rect, border_radius=20)
        pg.draw.rect(screen,"#c0e8ec", score_rect,border_radius=20)
       
        screen.blit(life_surface,life_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(hank_surface,zombie_rect)
        
        display_score()

        #Spillerens tyngdekraft og forestilte "kontakt" med bakken:
        character_gravity += 0.4
        character_rect.y += character_gravity
        if character_rect.bottom >=292:
            character_rect.bottom = 292
        #Viser fuglen dersom det har gått 10 sek
        currentTime = (pg.time.get_ticks() - startTime)/100
        if currentTime > highscore:
            #Innebygd funksjon:
            character.draw(screen)
            character.update()
            
            
            
        screen.blit(character_surface,character_rect)
        #Animerer karakteren:
        character_animation()
        
        #Sprite har to metoder: draw og update
        
        
        #Ved kollidering med Zombien:
        if character_rect.colliderect(zombie_rect):
            pg.draw.line(screen,"red",(0,0),(800,400),10)
            pg.draw.line(screen,"red",(0,400),(800,0),10)
            liv =int(liv) - 1
            liv = str(liv)
            life_surface = test_font.render(liv, True, life_color)
            life_rect = life_surface.get_rect(topleft = (10,10))
        if int(liv) <= 0:
            game_Active = False
            totalScore = int(totalScore) + int(score)
            currentTime = (pg.time.get_ticks() - startTime)/100
            if currentTime > highscore:
                highscore = currentTime
        pg.draw.ellipse(screen,circle_color,circle_rect)
        
        #Setter posisjonen til karakteren til andre siden av vinduet dersom den går utenfor x-verdiene til vinduet
        if zombie_rect.right <= 0:
            zombie_rect.left = widthWindow
            
        if pg.key.get_pressed()[pg.K_r]:
            rotation+=2
        elif pg.key.get_pressed()[pg.K_e]:
            rotation-=2
            
        mouse_pos = pg.mouse.get_pos()
        cursor_surf = pg.transform.rotozoom(logo_surf,rotation,0.25)
        cursor_rect = cursor_surf.get_rect(center=(mouse_pos[0],mouse_pos[1]))
        screen.blit(cursor_surf,cursor_rect)
        
        
    #Typ loadingscreen:
    elif game_Active == False:
        screen.fill((74,109,142))
        screen.blit(hank_surface,(240,190))
        screen.blit(hank_surface,(390,180))
        screen.blit(hank_surface,(320,200))
        screen.blit(hank_surface,(480,210))
        screen.blit(logo_surf,logo_rect)
        screen.blit(instruks_surf,instruks_rect)
        screen.blit(instruks2_surf,instruks2_rect)
        screen.blit(tittel_surf, tittel_rect)
        
        liv = str(liv_iStarten)
        life_surface = test_font.render(f"liv: {liv}", True, life_color)
        life_rect = life_surface.get_rect(topleft = (10,10))
        totalScore_surf = test_font.render(f"{totalScore} kr",True,"#ffd700")
        totalScore_rect = totalScore_surf.get_rect(midleft=(20,heightWindow/2))
        highscore_surf = test_font.render(f"Rekord: {highscore:.0f}",True,"#ff0000")
        highscore_rect = highscore_surf.get_rect(midright=(widthWindow-20,heightWindow/2))
        
        pg.draw.rect(screen, "#8098ac",totalScore_rect,border_radius=20)
        pg.draw.rect(screen, "#90a8bc",highscore_rect,border_radius=20)
        pg.draw.rect(screen,"#a0b8cc", life_rect, border_radius=20)
        
        screen.blit(totalScore_surf,totalScore_rect)
        screen.blit(highscore_surf,highscore_rect)
        screen.blit(life_surface,life_rect)
        
            
    #Her skal alle elementene tegnes
    #Oppdaterer display-området fra variabelen "screen" hele tiden:
    pg.display.update()
    #Forteller while-løkken at den ikke skal kjøre mer enn 60 ganger i sekundet: (minimum fps kan ikke settes med en linje kode, men det er ikke noe å stresse med med enkle 2D-spill)
    clock.tick(60)