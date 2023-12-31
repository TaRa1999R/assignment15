
import arcade

class Snake ( arcade.Sprite ) :

    def __init__ ( self , game ) :
        super().__init__ ()
        self.width = 25
        self.height = 25
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.change_x = 0
        self.change_y = 0
        self.speed = 3
        self.color1 = arcade.color.PURPLE
        self.score = 0
        self.body = []
        self.color2 = arcade.color.BLACK

    
    def draw ( self ) :
        arcade.draw_rectangle_filled ( self.center_x , self.center_y , self.width , self.height , self.color1 )
        for i in range ( len(self.body) ) :
            body = self.body[i]
            if i % 4 < 2 :
                arcade.draw_rectangle_filled ( body["x"] , body["y"] , self.width , self.height , self.color1)
            else :
                arcade.draw_rectangle_filled ( body["x"] , body["y"] , self.width , self.height , self.color2 )


    def move ( self ) :
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

        self.body.append ( { "x" : self.center_x , "y" : self.center_y } )
        if len(self.body) > self.score :
            self.body.pop ( 0 )

    def eat ( self , food ) :
        self.score += food.score
        del food