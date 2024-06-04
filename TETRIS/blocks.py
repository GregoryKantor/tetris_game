from block import Block
from position import Position

class LBlock(Block):    #az L alaku elem függvénye, a zárójelbe kerül a parent (Block) class   
    def __init__(self):
        super().__init__(id = 1)    #meghívjuk a Block class init metódusát (a parent blokk)
                                    #azonosítót adunk neki id = 1
        self.cells = {
            0: [Position (0,2), Position(1,0), Position(1,1), Position(1,2)],   #első (azaz nulladik) sor, harmadik cella(azaz második)
                                                                                #második sor, első cellája és így tovább...
                                                                                #és kész is az L alakú elem
            1: [Position (0,1), Position(1,1), Position(2,1), Position(2,2)],                                                                  
            2: [Position (1,0), Position(1,1), Position(1,2), Position(2,0)],   # 0-1 között pedig a lehetséges forgatási pozíciók
            3: [Position (0,0), Position(0,1), Position(1,1), Position(2,1)]
        }
        self.move(0,3)

class JBlock(Block):     #a J (forditott L alakú) tetris elem definiálása
    def __init__(self):
        super().__init__(id = 2)   
                                    
        self.cells = {
            0: [Position (0,0), Position(1,0), Position(1,1), Position(1,2)],                                                              
            1: [Position (0,1), Position(0,2), Position(1,1), Position(2,1)],                                                                  
            2: [Position (1,0), Position(1,1), Position(1,2), Position(2,2)],   
            3: [Position (0,1), Position(1,1), Position(2,0), Position(2,1)]
        }
        self.move(0,3)

class IBlock(Block):     #az I (egyenes) tetris elem definiálása
    def __init__(self):
        super().__init__(id = 3)   
                                    
        self.cells = {
            0: [Position (1,0), Position(1,1), Position(1,2), Position(1,3)],                                                              
            1: [Position (0,2), Position(1,2), Position(2,2), Position(3,2)],                                                                  
            2: [Position (2,0), Position(2,1), Position(2,2), Position(2,3)],   
            3: [Position (0,1), Position(1,1), Position(2,1), Position(3,1)]
        }
        self.move(-1,3)

class OBlock(Block):     #az O tetris elem definiálása
    def __init__(self):
        super().__init__(id = 4)   
                                    
        self.cells = {      #mivel mind a 4 forgási állapot ugyanaz, ezért elég egyszer meghatározni
            0: [Position (0,0), Position(0,1), Position(1,0), Position(1,1)]                                                         
        }
        self.move(0,4)

class SBlock(Block):     #az S tetris elem definiálása
    def __init__(self):
        super().__init__(id = 5)   
                                    
        self.cells = {
            0: [Position (0,1), Position(0,2), Position(1,0), Position(1,1)],                                                              
            1: [Position (0,1), Position(1,1), Position(1,2), Position(2,2)],                                                                  
            2: [Position (1,1), Position(1,2), Position(2,0), Position(2,1)],   
            3: [Position (0,0), Position(1,0), Position(1,1), Position(2,1)]
        }
        self.move(0,3)

class TBlock(Block):     #a T tetris elem definiálása
    def __init__(self):
        super().__init__(id = 6)   
                                    
        self.cells = {
            0: [Position (0,1), Position(1,0), Position(1,1), Position(1,2)],                                                              
            1: [Position (0,1), Position(1,1), Position(1,2), Position(2,1)],                                                                  
            2: [Position (1,0), Position(1,1), Position(1,2), Position(2,1)],   
            3: [Position (0,1), Position(1,0), Position(1,1), Position(2,1)]
        }
        self.move(0,3)

class ZBlock(Block):     #a Z tetris elem definiálása
    def __init__(self):
        super().__init__(id = 7)   
                                    
        self.cells = {
            0: [Position (0,0), Position(0,1), Position(1,1), Position(1,2)],                                                              
            1: [Position (0,2), Position(1,1), Position(1,2), Position(2,1)],                                                                  
            2: [Position (1,0), Position(1,1), Position(2,1), Position(2,2)],   
            3: [Position (0,1), Position(1,0), Position(1,1), Position(2,0)]
        }
        self.move(0,3)
