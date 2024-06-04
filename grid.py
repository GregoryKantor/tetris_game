import pygame
from colors import Colors

class Grid:     #rajzolunk a négyzetrácsot
    def __init__(self):     #a self egy egyedenkénti attributum azonosító
        self.num_rows = 20      #sorok száma (20 négyzetrács(cella))
        self.num_cols = 10      #oszlopok száma (10 négyzetrács(cella))
        self.cell_size = 30     #egy négyzetrács 30 képpont szélességű
                                #listában hozunk létre listákat a cellák létrehozásához
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        #nem for ciklussal így nézne ki:
        """"
                [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #minden üres cella 0 értéket vesz fel
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #ha nem nulla akkor a megjelenítendő elem színe
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #ahány cellás az elem annyi ugyanolyan szám
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        """
        #létrehozzuk az elemek színeit (az üres cella színét is!!)
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows): #minden sort kinyomtat
            for column in range (self.num_cols): #oszloponként
                print(self.grid[row][column], end = " ") #új sorban
            print()
    
    #ez már nem is kell mert készült egy osztály a szineknek és importáltuk
    """"
    #a használt színekhez a kódok
    def get_cell_colors(self):
        dark_grey = (26, 31, 40) #ez lesz az üres cella
        green = (47,230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue =(13, 64, 216)

        #listában visszaadjuk az értékeket
        #a sorrend fontos mert a rácson a számok -> index-ekké válnak
        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]
    """

    def is_inside(self, row, column):   #megvizsgálja kimegy-e az elem a pályáról
                                        #sor és oszlop pozi >= 0 és < mint sorok/oszlopok száma
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False
    
    def is_empty(self, row, column):    #az ütközésekhez meg kell vizsgálni foglalt-e a cella
        if self.grid[row][column] == 0:
            return True
        return False
    
    def is_row_full(self, row): #megvizsgálja van-e üres cella a sorban (ez a teljes sorok miatt fontos)
        for column in range (self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):   #a cellákhoz 0 értéket rendel igy üresek lesznek
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows): #a törölt sor helyére kell tenni a kövit
        for column in range(self.num_cols): #átmásoljuk az új sorba az aktuális értékeket
            self.grid[row+num_rows][column] = self.grid[row][column] #ezzel leküldjük az aljára (az új értékekkel)
            self.grid[row][column] = 0 #és töröljük a régit

    def clear_full_rows(self):  #végig kell vizsgálni az összes sort (19-től 0-ig)h teli-e?
        completed = 0 #a kitöltött sor változója
        for row in range(self.num_rows-1, 0, -1): #a végén a -1-el visszafelé iterál
            if self.is_row_full(row):   #ha van teli meghivjuk a törlést és eltároljuk hány teli sor volt
                self.clear_row(row)
                completed += 1
            elif completed > 0: #ha ez igaz van teli sor és egy sorral lejebb visszük
                self.move_row_down(row, completed) 
        return completed    #ezt visszaadjuk kell majd a pontokhoz

    def reset(self): #rácstörtlés metódus ha vége a játéknak
        for row in range(self.num_rows): #végigiterál összes soron
            for column in range(self.num_cols): #összes oszlopon
                self.grid[row][column] = 0  #és nullára állítja az értékeket

    #rajzolás
    def draw(self, screen): #a screen változó a main.py-ban van ezért át kell adni
        #megkapjuk a cellák értékét:
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column] #a végig iterált értékeket hozzárendeljük
                                                    #a cell_value változóhoz
                cell_rect = pygame.Rect(column*self.cell_size + 1+10, row*self.cell_size + 1+10,  # gyakorlatilag x tengely és y tengely
                self.cell_size - 1, self.cell_size - 1)                                           # a +1 (a keret) és -1 (belül) a rácsok megjelenítéséhez kell
                                                                                                  # a +10 ahhoz kell,hogy ne az ablak sarkában legyen a pálya  
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect) #3 alap argumentum kell: (surface, color, rect)