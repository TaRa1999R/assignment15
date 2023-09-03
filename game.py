
import arcade
from snake import Snake
import food

class Game ( arcade.Window ) :

    def __init__ ( self ) :
        super().__init__ ( width = 500 , height = 500 , title = " Super Snake 🐍🍎 " )
        self.snake = Snake ( self )
        self.apple = food.Apple ( self )
        self.pear = food.Pear ( self )
        self.poop = food.Poop ( self )
        self.game_mode = None
        self.background = arcade.load_texture ( "image\image game over.png" )
        self.start = False

    
    def on_draw ( self ) :
        arcade.start_render ()

        score_text = f"Score : {self.snake.score}"

        if self.game_mode == "game_over" :
            arcade.set_background_color ( arcade.color.BLACK )
            arcade.draw_lrwh_rectangle_textured ( 0 , 0 , self.width , self.height , self.background )
            arcade.draw_text ( score_text , ( self.width // 2 ) - 90 , 35 , arcade.color.PINK_PEARL , 25 )

        else :
            arcade.set_background_color ( arcade.color.KHAKI )

            self.snake.draw ()
            self.apple.draw ()
            self.pear.draw ()
            self.poop.draw ()

            arcade.draw_text ( score_text , 20 , self.height - 25 , arcade.color.DARK_BROWN , 15)

        arcade.finish_render ()

    
    def on_key_release ( self , symbol , modifiers ) :
        if symbol == arcade.key.UP and self.snake.change_y == 0 :
            self.snake.change_x = 0
            self.snake.change_y = 1

        elif symbol == arcade.key.DOWN and self.snake.change_y == 0 :
            self.snake.change_x = 0
            self.snake.change_y = -1

        elif symbol == arcade.key.RIGHT and self.snake.change_x == 0 :
            self.snake.change_x = 1 
            self.snake.change_y = 0
        
        elif symbol == arcade.key.LEFT and self.snake.change_x == 0 :
            self.snake.change_x = -1
            self.snake.change_y = 0

    
    def on_update ( self , delta_time ) :
        self.snake.move ()

        if arcade.check_for_collision ( self.snake , self.apple ) :
            self.start = True
            self.snake.eat ( self.apple )
            self.apple = food.Apple ( self )

        if arcade.check_for_collision ( self.snake , self.pear ) :
            self.start = True
            self.snake.eat ( self.pear )
            self.pear = food.Pear ( self )

        if arcade.check_for_collision ( self.snake , self.poop ) :
            self.start = True
            self.snake.eat ( self.poop )
            self.poop = food.Poop ( self )

        if self.snake.center_x < 10 or self.snake.center_x > self.width - 10 :
            self.game_mode = "game_over"
        
        if self.snake.center_y < 10 or self.snake.center_y > self.height - 10 :
            self.game_mode = "game_over"

        if self.snake.score <= 0 and self.start == True :
            self.game_mode = "game_over"

        for i in range ( 0 , len(self.snake.body)-1 ) :
            body = self.snake.body [i]
            if self.snake.center_x == body["x"] and self.snake.center_y == body["y"] :
                self.game_mode = "game_over"
        
        
game = Game ()
arcade.run ()