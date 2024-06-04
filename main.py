import pygame, sys
from game import Game
from colors import Colors

print("Welcome in the Tetris Game! \nControls: Left/Right/Down \nRotate: Space")

pygame.init()   #inicializáljuk a pygame-et

title_font = pygame.font.Font(None, 40) #alapért. betű, 40es méret a pontok kiírásához
score_surface = title_font.render("Score", True, Colors.white) #amitkiír, engedélyezés, betűtípus
                                                               #a Colors class-ból (colors.py)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER \n NEW:\n   ANY KEY!", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)  #(x,y, milyen széles, milyen magas)
next_rect = pygame.Rect(320,215, 170, 180)  #háttér a soron következő elem kirajzolásáshoz

screen = pygame.display.set_mode((500, 620))    #lérehozzuk az ablakot
pygame.display.set_caption("Tetris Game")   #ablak neve

clock = pygame.time.Clock()     #ezzel szabályozzuk a sebességet majd
                                #nagy C-vel kezdd! :)

game = Game()

GAME_UPDATE = pygame.USEREVENT  #egyéni eseményhez rendelt változó,ahhoz h lelassítsuk a sebességet
pygame.time.set_timer(GAME_UPDATE, 200) #200 m.sec-ként frissitk

while True:
    for event in pygame.event.get():    #mindig végigvizsgálja a event-eket
        if event.type == pygame.QUIT:
            pygame.quit()               #kilép a loop-ból
            sys.exit()
        if event.type == pygame.KEYDOWN:    #ellenőrzi h lenyomtak-e egy billentyűt és nincs game over
            if game.game_over == True: #ha vége a játéknak is lenyomnak egy billentyűt
                game.game_over = False #engedje ujra a játékot
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:  
                game.move_left()    #meghivja a game.py-ból a megfelelő mozgató metódust
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1) #lefelé haladáskor kapsz egy pontot
            if event.key == pygame.K_SPACE and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()    #ha az esemény = GAME_UPDATE és ha nincs game over
                                #meghivja a move_down funkciót        

        score_value_surface = title_font.render(str(game.score), True, Colors.white) #a pont integer ugyh str-é alakitjuk

        screen.fill(Colors.dark_blue)      #az ablakot sötétkékkel tölti ki
        screen.blit(score_surface, (365, 20, 50, 50)) #a score felirat (x,y, milyen széles, milyen magas)
        screen.blit(next_surface, (375, 180, 50, 50)) #next felirat
        if game.game_over == True:  #csak akkor irja ki ha vége a játéknak
            screen.blit(game_over_surface, (320, 450, 50, 50))

        pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)  #a 0,10 a lekerekített sarkokhoz kell
        #a pontszámok mindig változnak és így mindig középre kerülnek \/ \/ \/
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
        pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)   #kövi elem mögötti háttér
        game.draw(screen)

        pygame.display.update() #az objektumokon végrehajtott változást érzékeli
        clock.tick(60) # a fő ciklus 60szor fog lefutni /sec -> ezért tűnik ugy mintha mozognának

