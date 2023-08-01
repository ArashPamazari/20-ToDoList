import arcade
from turtle import width
import random


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class Game(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width, height, "snake game")
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake(width ,height )
        self.apple = Apple(width,height)
        self.Golabi = Golabi(width,height)
        self.PU = PU(width,height)

        arcade.schedule(self.ai_move, 2.0)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('Score : ' + str(self.snake.score), 2, 480, arcade.color.BLACK, 14, 1000, 'left')
        self.snake.draw()
        self.apple.draw()
        self.Golabi.draw()
        self.PU.draw()

        if self.snake.score < 0 or self.snake.center_x <= 0 or self.snake.center_x >= SCREEN_WIDTH or self.snake.center_y <= 0 or self.snake.center_y >= SCREEN_WIDTH:
            arcade.draw_text('GAME OVER', 150, 250, arcade.color.RED, font_size=12)
            arcade.exit()

    def ai_move(self,delta_time ):
        # تصادفی حرکت کنیم:
        directions = [(0, 5), (0, -5), (5, 0), (-5, 0)]  # بالا، پایین، راست، چپ
        move_x, move_y = random.choice(directions)

        # محدودیت حرکت در میدان:
        new_x = self.snake.center_x + move_x * self.snake.speed
        new_y = self.snake.center_y + move_y * self.snake.speed

        if 0 <= new_x <= SCREEN_WIDTH and 0 <= new_y <= SCREEN_HEIGHT:
            self.snake.change_x = move_x
            self.snake.change_y = move_y
        pass
    
    

    
    def on_update(self, delta_time: float):
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.apple.apple):
            apple = 1
            self.apple = Apple(self.width, self.height)
            self.snake.eat(apple)

        if arcade.check_for_collision(self.snake, self.PU.PU):
            pu = 2
            self.PU = PU(self.width, self.height)
            self.snake.eat(pu)

        if arcade.check_for_collision(self.Golabi.Golabi, self.snake):
            golabi = 3
            self.Golabi = Golabi(self.width, self.height)
            self.snake.eat(golabi)





    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1






class Snake(arcade.Sprite):
    def __init__(self,width , height):
        super().__init__()
        self.width = 16
        self.height = 16
        self.speed = 1
        self.color_1 = arcade.color.GREEN
        self.color_2 = arcade.color.DARK_GREEN
        self.change_x = 0
        self.change_y = 0
        self.score = 0
        self.center_x = width // 2
        self.center_y = height // 2
        self.body = []

    def eat(self, eat):
        if eat == 1:
            self.score += 1
        elif eat == 2:
            self.score -= 1
        elif eat == 3:
            self.score += 2

    def move(self):
        self.body.append((self.center_x, self.center_y))
        if len(self.body) > self.score:
            self.body.pop(0)
        if self.change_x > 0:
            self.center_x += self.speed
        elif self.change_x < 0:
            self.center_x -= self.speed
        elif self.change_y > 0:
            self.center_y += self.speed
        elif self.change_y < 0:
            self.center_y -= self.speed

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color_1)
        for i in range(len(self.body)):
            if i % 2 == 0:
                arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color_1)
            else:
                arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color_2)





class Apple(arcade.Sprite):
    def __init__(self, width , height ):
        super().__init__()
        self.image = "A.jpg"
        self.apple = arcade.Sprite(self.image, 0.1)
        self.apple.center_x = random.randint(10, width - 10)
        self.apple.center_y = random.randint(10, height - 10)

    def draw(self):
        self.apple.draw()





class Golabi (arcade.Sprite):
    def __init__(self, width , height):
        super().__init__()
        self.image = "Golabi.jpg"
        self.Golabi = arcade.Sprite(self.image, 0.11)
        self.Golabi.center_x = random.randint(10, width - 10)
        self.Golabi.center_y = random.randint(10, height - 10)

    def draw(self):
        self.Golabi.draw()





class PU (arcade.Sprite):
    def __init__(self, width , height):
        super().__init__()
        self.image = "pu.jpg"
        self.PU = arcade.Sprite(self.image, 0.1)
        self.PU.center_x = random.randint(10, width - 10)
        self.PU.center_y = random.randint(10, height - 10)

    def draw(self):
        self.PU.draw()




width = 500
height = 500

mygame = Game(width , height)
arcade.run()