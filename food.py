
import random
import arcade

class Food ( arcade.Sprite ) :
    def __init__ ( self , game , image ) :
        super().__init__ ( image )
        self.width = 25
        self.height = 25
        self.center_x = random.randint ( 5 , game.width - 5 )
        self.center_y = random.randint ( 5 , game.height - 5 )
        self.change_x = 0
        self.change_y = 0


class Apple ( Food ) :
    def __init__ ( self , game ) : 
        super().__init__ ( game , "image/apple.png" )
        self.score = 1


class Pear ( Food ) :
    def __init__ ( self , game ) :
        super().__init__ ( game , "image/pear.png" )
        self.score = 2


class Poop ( Food ) :
    def __init__ ( self , game ) :
        super().__init__ ( game , "image/poop.png" )
        self.score = -1