#a különböző tetris elemekhez létrehozunk egy alap osztályt
#majd mindegyiknek lesz egy "child" osztálya amibe örökli az alaposztály jellemzőit

from colors import Colors   #szín class import
import pygame
from position import Position   #pozició class import

class Block:
    def __init__(self, id):
        self.id = id    #egyedi azonosító (a class egy tagja) a különböző formákhoz
        self.cells = {}     #az elemek forgatáshoz kell egy 4x4es rács ami dict lesz
        self.cell_size = 30     #egy cella mérete ugyanugy 30 px
        self.row_offset = 0     #a tetris elemek mozgásáért felelős mert a kezdő sarok pontot változtataj majd
        self.column_offset = 0  #
        self.rotation_state = 0     #forgási állapot meghatározása
        self.colors = Colors.get_cell_colors()  #meghívtuk  a colors.py-ból a Colors classt

    def move(self, rows, columns):  #ezzel mindig eggyel eltoljuk az elemek mögötti minirácsot (tiles)
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):   #kiszámolja a cellák mozgatás utáni új (foglalt cellás) pozícióját
        tiles = self.cells[self.rotation_state]
        moved_tiles = []    #a mozgatott minirácsokat itt tároljuk
        for position in tiles:  #az összes tile-on végig kell mennünk hogy mik a pozijuk és hozzáadni a mozgást
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles
    
    def rotate(self):   #ha a forgatás eléri az utolsó forgási lehetőséget a dict indexe legyen 0
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state < 0:
            self.rotation_state = len(self.cells) - 1

    #tetris elemek rajzolása
    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()     #a forgási állapotok pozícióját kéri le
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size,    #hasonlóan mint a rácsozás kirajzolásánál (grid.py)
                offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)     
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)           #igazítani kell mindig az ép.elemek mozgási helyzetét a rácshoz