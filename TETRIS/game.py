from grid import Grid
from blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()  #meghívjuk a rács classt, ezután az összes tetris elemet
                            #hogy véletlenszerűen kerüljenek be
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()  #aktuális építőelem
        self.next_block = self.get_random_block() #kövi építőelem
        self.game_over = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")  #forgatáshoz hangeffekt
        self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")   #teli sornál hangeffekt
        self.game_over_sound = pygame.mixer.Sound("Sounds/game_over.ogg")
        
        pygame.mixer.music.load("Sounds/music.ogg") #a mappa ahol vannak a zenefájlok
        pygame.mixer.music.play(-1)   #a -1 azt jelenti, hogy végtelenítve játsza a music.ogg-ot
        pygame.mixer.music.set_volume(0.1)    

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100   #100 pont egy teli sornál
        elif lines_cleared == 2:
            self.score += 300   #300 p 2 teli sornál
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 1000
        self.score += move_down_points  #minden lefeléhaladásnál 1 pont

    def get_random_block(self):
        if len(self.blocks) == 0:   #ha kiürül töltse be újra az építő elemeket
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)  #kiválaszt egy elemet random
        self.blocks.remove(block)   #utána el is távolitjuk a kiválasztott elemet, hogy ne ismétlődjön
        return block

    def move_left(self):
        self.current_block.move(0,-1)   #eggyel balra megy az építőkocka
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,1)    #ha kimenne a pályáról vagy ütközne visszalépteti

    def move_right(self):
        self.current_block.move(0,1)   #eggyel jobbra megy az építőkocka
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,-1)

    def move_down(self):
        self.current_block.move(1,0)   #eggyel lejebb megy az építőkocka
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1,0)
            self.lock_block()
    
    def lock_block(self):   #ha leér az aljára rögziteni kell az ép.elemet
        tiles = self.current_block.get_cell_positions() #rögzitjük a minirácsok poziját
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block    #kell az uj elem ami érkezik
        self.next_block = self.get_random_block() #ráadásul véletlenszerűen
        rows_cleared = self.grid.clear_full_rows()  #a lefelé plusz 1 ponthoz kellett ez változóként
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        if self.block_fits() == False:  #a block_fits-ben az is_empty nézi h üres-e a cella
            self.game_over = True   #ha nem akkor vége a játéknak
            self.game_over_sound.play()     
    
    def reset(self):
        self.grid.reset()   #be kell töltődjenek úra az ép.elemek
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block() #kellenek új random elemek
        self.next_block = self.get_random_block()
        self.score = 0

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False  or self.block_fits() == False:
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()
    
    def block_inside(self):
        tiles = self.current_block.get_cell_positions() #az összes minirácsot meg kell vizsgálni
                                                        #nincs-e kívül a pályán
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    
    def draw(self, screen):
        self.grid.draw(screen)  #kirajzolja a rácsot
        self.current_block.draw(screen, 11, 11) #kirajzolja a kezdő elemet
        
        if self.next_block.id == 3: #ha a kövi elem a minirács miatt nem középen van oldalt
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)
