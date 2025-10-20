import pygame as pg
from sys import exit

pg.init()

widthWindow = 730
heightWindow = 500
FPS = 60
screen = pg.display.set_mode((widthWindow,heightWindow))
clock = pg.time.Clock()
bg_Music1 = pg.mixer.Sound("Audio/kahootChristmas.mp3")
bg_Music1.play()


spmColor = "#000000"
menyColor = "#000000"
scoreColor = "#FFD700"



backGsurf = pg.image.load("Bilder/christmasBG.jpg")
backGsurf = pg.transform.scale(backGsurf,(widthWindow,heightWindow))

menyFont = pg.font.Font("Fonts/Bebas_Neue/BebasNeue-Regular.ttf",60)
spmFont = pg.font.Font("Fonts/Nunito/Nunito-Italic-VariableFont_wght.ttf",30)

# menySurf = menyFont.render("MENY", True, menyColor)
# menyRect = menySurf.get_rect(midtop = (widthWindow/2,heightWindow/2-80))

menySmallSurf = spmFont.render("Trykk MELLOMROMSTASTEN for å starte", True,menyColor)
menySmallRect = menySmallSurf.get_rect(midtop = (widthWindow/2,heightWindow-260))

class text():
    #tekst er tekst (str), posRel er posisjon i forhold til surfacet (midtop eller bottomleft f.eks), posx og posy er pikselpos mellom (0-1000)
    def __init__(self,tekstInnhold,posx,posy):
        self.tekstInnhold = tekstInnhold
#         self.posRel = posRel
        self.posx = posx
        self.posy = posy
        self.spmSurf = spmFont.render(self.tekstInnhold, True, spmColor)
        self.spmRect = self.spmSurf.get_rect(midtop = (self.posx,self.posy))
    def returnRect(self):
        return self.spmRect
    def returnSurf(self):
        return self.spmSurf


altaListe = ["ok"]
altbListe = ["ok"]
altcListe = ["ok"]
altdListe = ["ok"]

spm1 = text("Hvor mange dollar i året tjener Mariah Carey i året?", widthWindow/2,10)
spm1Rect = spm1.returnRect()
spm1Surf = spm1.returnSurf()

alt1a = text("3 millioner", 250,250)
alt1aRect = alt1a.returnRect()
alt1aSurf = alt1a.returnSurf()


alt1b = text("5 millioner", widthWindow-250,250)
alt1bRect = alt1b.returnRect()
alt1bSurf = alt1b.returnSurf()

alt1c = text("10 millioner", 250,heightWindow-150)
alt1cRect = alt1c.returnRect()
alt1cSurf = alt1c.returnSurf()

alt1d = text("1 million", widthWindow-250,heightWindow-150)
alt1dRect = alt1d.returnRect()
alt1dSurf = alt1d.returnSurf()


spm2 = text("Hvem er den beste læreren på Nadderud", widthWindow/2,10)
spm2Rect = spm2.returnRect()
spm2Surf = spm2.returnSurf()

alt2a = text("Ikke Didrik", 250,250)
alt2aRect = alt2a.returnRect()
alt2aSurf = alt2a.returnSurf()

alt2b = text("Kanskje Didrik", widthWindow-250,250)
alt2bRect = alt2b.returnRect()
alt2bSurf = alt2b.returnSurf()

alt2c = text("Hvem er Didrik?", 250,heightWindow-150)
alt2cRect = alt2c.returnRect()
alt2cSurf = alt2c.returnSurf()

alt2d = text("Helt klart Didrik", widthWindow-250,heightWindow-150)
alt2dRect = alt2d.returnRect()
alt2dSurf = alt2d.returnSurf()



spm3 = text("Hva er verdens største øy?", widthWindow/2,10)
spm3Rect = spm3.returnRect()
spm3Surf = spm3.returnSurf()

alt3a = text("Afrika", 250,250)
alt3aRect = alt3a.returnRect()
alt3aSurf = alt3a.returnSurf()

alt3b = text("Grønnland", widthWindow-250,250)
alt3bRect = alt3b.returnRect()
alt3bSurf = alt3b.returnSurf()

alt3c = text("Australia", 250,heightWindow-150)
alt3cRect = alt3c.returnRect()
alt3cSurf = alt3c.returnSurf()

alt3d = text("Storbrittania", widthWindow-250,heightWindow-150)
alt3dRect = alt3d.returnRect()
alt3dSurf = alt3d.returnSurf()



spm4 = text("Hvilken film spiller Hugh Grant ikke i?", widthWindow/2,10)
spm4Rect = spm4.returnRect()
spm4Surf = spm4.returnSurf()

alt4a = text("Notting Hill", 250,250)
alt4aRect = alt4a.returnRect()
alt4aSurf = alt4a.returnSurf()

alt4b = text("Home Alone", widthWindow-250,250)
alt4bRect = alt4b.returnRect()
alt4bSurf = alt4b.returnSurf()

alt4c = text("Love Actually", 250,heightWindow-150)
alt4cRect = alt4c.returnRect()
alt4cSurf = alt4c.returnSurf()

alt4d = text("Bridget Jones", widthWindow-250,heightWindow-150)
alt4dRect = alt4d.returnRect()
alt4dSurf = alt4d.returnSurf()



spm5 = text("Hvilket land startet tradisjonen med juletrær?", widthWindow/2,10)
spm5Rect = spm5.returnRect()
spm5Surf = spm5.returnSurf()

alt5a = text("Bora Bora", 250,250)
alt5aRect = alt5a.returnRect()
alt5aSurf = alt5a.returnSurf()

alt5b = text("Storbrittania", widthWindow-250,250)
alt5bRect = alt5b.returnRect()
alt5bSurf = alt5b.returnSurf()

alt5c = text("Frankrike", 250,heightWindow-150)
alt5cRect = alt5c.returnRect()
alt5cSurf = alt5c.returnSurf()

alt5d = text("Tyskland", widthWindow-250,heightWindow-150)
alt5dRect = alt5d.returnRect()
alt5dSurf = alt5d.returnSurf()


spm6 = text("Hvor er det tradisjon å spise KFC til julen?", widthWindow/2,10)
spm6Rect = spm6.returnRect()
spm6Surf = spm6.returnSurf()

alt6a = text("USA", 250,250)
alt6aRect = alt6a.returnRect()
alt6aSurf = alt6a.returnSurf()

alt6b = text("Canada", widthWindow-250,250)
alt6bRect = alt6b.returnRect()
alt6bSurf = alt6b.returnSurf()

alt6c = text("Japan", 250,heightWindow-150)
alt6cRect = alt6c.returnRect()
alt6cSurf = alt6c.returnSurf()

alt6d = text("Mexico", widthWindow-250,heightWindow-150)
alt6dRect = alt6d.returnRect()
alt6dSurf = alt6d.returnSurf()


spmNummer = 0
score = 0

def drawQuiz(spmSurf,spmRect,altaSurf,altbSurf,altcSurf,altdSurf,altaRect,altbRect,altcRect,altdRect):
    global x
    pg.draw.rect(screen,"#FFD700", spmRect, border_radius=20)
    pg.draw.rect(screen,"#c0e8ec", altaRect,border_radius=20)
    pg.draw.rect(screen,"#c0e8ec", altbRect,border_radius=20)
    pg.draw.rect(screen,"#c0e8ec", altcRect,border_radius=20)
    pg.draw.rect(screen,"#c0e8ec", altdRect,border_radius=20)
    screen.blit(spmSurf,spmRect)
    screen.blit(altaSurf,altaRect)
    screen.blit(altbSurf,altbRect)
    screen.blit(altcSurf,altcRect)
    screen.blit(altdSurf,altdRect)
    if x == 0:
        altaListe.pop()
        altaListe.append(altaRect)
        altbListe.pop()
        altbListe.append(altbRect)
        altcListe.pop()
        altcListe.append(altcRect)
        altdListe.pop()
        altdListe.append(altdRect)
        x+=1
        if spmNummer == 0:
            score = 0


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            #importerer fra sys:
            exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            x=0
            spmNummer+=1
            
        mouse_pos = pg.mouse.get_pos()
        mouse_press = pg.mouse.get_pressed()
        if event.type == pg.MOUSEBUTTONDOWN and mouse_press[0]:
            
            for i in range(len(altaListe)):
                if altaListe[i].collidepoint(mouse_pos):
                    x=0
                    spmNummer+=1
                    if riktig == 1:
                        score+=1
                        print(score)
            for i in range(len(altbListe)):
                if altbListe[i].collidepoint(mouse_pos):
                    x=0
                    spmNummer+=1
                    if riktig == 2:
                        score+=1
                        print(score)
            for i in range(len(altcListe)):
                if altcListe[i].collidepoint(mouse_pos):
                    x=0
                    spmNummer+=1
                    if riktig == 3:
                        score+=1
                        print(score)
            for i in range(len(altdListe)):
                if altdListe[i].collidepoint(mouse_pos):
                    x=0
                    spmNummer+=1
                    if riktig == 4:
                        score+=1
                        print(score)
                    
        
            
    screen.blit(backGsurf,(0,0))
    
    if spmNummer == 1:
        x2 = 0
        if x2 == 0:
            score = 0
            x2+=1
        backGsurf = pg.image.load("Bilder/christmasBG1.png")
        backGsurf = pg.transform.scale(backGsurf,(widthWindow,heightWindow))
        #Hvilket alternativ som er riktig: (a=1,b=2,c=3 og d=4)
        riktig = 1
        pg.display.set_caption("Quiz")
        drawQuiz(spm1Surf,spm1Rect,alt1aSurf,alt1bSurf,alt1cSurf,alt1dSurf,alt1aRect,alt1bRect,alt1cRect,alt1dRect)
    if spmNummer == 2:
        backGsurf = pg.image.load("Bilder/christmasBG2.png")
        backGsurf = pg.transform.scale(backGsurf,(widthWindow,heightWindow))
        riktig = 4
        drawQuiz(spm2Surf,spm2Rect,alt2aSurf,alt2bSurf,alt2cSurf,alt2dSurf,alt2aRect,alt2bRect,alt2cRect,alt2dRect)
    if spmNummer == 3:
        backGsurf = pg.image.load("Bilder/christmasBG3.png")
        backGsurf = pg.transform.scale(backGsurf,(widthWindow,heightWindow))
        riktig = 2
        drawQuiz(spm3Surf,spm3Rect,alt3aSurf,alt3bSurf,alt3cSurf,alt3dSurf,alt3aRect,alt3bRect,alt3cRect,alt3dRect)
    if spmNummer == 4:
        backGsurf = pg.image.load("Bilder/christmasBG4.png")
        backGsurf = pg.transform.scale(backGsurf,(widthWindow,heightWindow))
        riktig = 2
        drawQuiz(spm4Surf,spm4Rect,alt4aSurf,alt4bSurf,alt4cSurf,alt4dSurf,alt4aRect,alt4bRect,alt4cRect,alt4dRect)
    if spmNummer == 5:
        backGsurf = pg.image.load("Bilder/christmasBG2.png")
        backGsurf = pg.transform.scale(backGsurf,(widthWindow,heightWindow))
        riktig = 4
        drawQuiz(spm5Surf,spm5Rect,alt5aSurf,alt5bSurf,alt5cSurf,alt5dSurf,alt5aRect,alt5bRect,alt5cRect,alt5dRect)
    if spmNummer == 6:
        backGsurf = pg.image.load("Bilder/christmasBG.jpg")
        backGsurf = pg.transform.scale(backGsurf,(widthWindow,heightWindow))
        riktig = 3
        drawQuiz(spm6Surf,spm6Rect,alt6aSurf,alt6bSurf,alt6cSurf,alt6dSurf,alt6aRect,alt6bRect,alt6cRect,alt6dRect)
    if spmNummer == 7:
        spmNummer = 0
    if spmNummer == 0:
        pg.display.set_caption("Meny")
        backGsurf = pg.image.load("Bilder/christmasBGmain.png")
        
        scoreTextSurf = menyFont.render(f"Poeng: {score}/6", True, scoreColor)
        scoreTextRect = scoreTextSurf.get_rect(midtop = (widthWindow/2,170))

        backGsurf = pg.transform.scale(backGsurf,(widthWindow,heightWindow))
#         screen.blit(menySurf,menyRect)
        screen.blit(menySmallSurf,menySmallRect)
        screen.blit(scoreTextSurf,scoreTextRect)
        
    
    clock.tick(FPS)
    pg.display.update()

    

    
    
    