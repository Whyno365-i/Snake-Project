import pyglet # noqa: F401
from pyglet import * # type: ignore
from pyglet.window import key
import random
import tkinter as tk
from tkinter import ttk

num_square= 0
high_score=0

def game():
    # noinspection PyAbstractClass
    class MyWindow(pyglet.window.Window):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            #window stuff
            self.set_location(x=450, y=70)
            self.batch= pyglet.graphics.Batch()

            #borders of game
            self.border_up = shapes.Rectangle(x=0, y=849, width=1000, height=100, color=(0, 0, 255), batch=self.batch)
            self.border_down = shapes.Rectangle(x=0, y=0, width=1000, height=49, color=(0, 0, 255), batch=self.batch)
            self.border_right = shapes.Rectangle(x=850, y=0, width=100, height=1000, color=(0, 0, 255), batch=self.batch)
            self.border_left = shapes.Rectangle(x=0, y=0, width=49, height=1000, color=(0, 0, 255), batch=self.batch)

            #player and player movement
            self.player = shapes.Rectangle(x=450, y=450, width=50, height=50, color=(0, 128, 0), batch=self.batch)
            self.player_blocks = []
            self.player_position = []
            self.player_postion = None
            self.speed= 50
            self.move_x= 0
            self.move_y= 0
            self.timer= 0
            self.x= -1

            #apple square
            apple_x= random.randrange(50, 801, 50)
            apple_y= random.randrange(50, 801, 50)
            self.apple= shapes.Rectangle(x= apple_x, y=apple_y, width=50, height=50, color= (255, 0, 0), batch=self.batch)


        def add_player_square(self):
            x_y2= self.player_position[self.x]
            x = x_y2[0]
            y = x_y2[1]
            self.player_blocks.append(shapes.Rectangle(x=x, y=y, width=50, height=50, color=(0, 128, 0), batch=self.batch))


        def on_key_press(self, symbol, modifiers):
            if symbol == key.LEFT and self.move_x != 1:
                self.move_x= -1
                self.move_y= 0

            elif symbol == key.RIGHT and self.move_x != -1:
                self.move_x= 1
                self.move_y= 0

            elif symbol == key.UP and self.move_y !=-1:
                self.move_x= 0
                self.move_y= 1

            elif symbol == key.DOWN and self.move_y != 1:
                self.move_x= 0
                self.move_y= -1


        def on_draw(self):
            # noinspection PyUnresolvedReferences
            window1.clear()
            self.batch.draw()


        def update(self, dt) -> None: # type: ignore
            global num_square, high_score

            if num_square > high_score:
                with open('C:\\Users\\PC\\OneDrive\\coding\\Coding files\\Snake Game\\high_score', 'w') as file:
                    file.write(str(num_square))
            #if player loses
            if self.player.y >= self.border_up.y:
                pyglet.app.exit()

            if self.player.x >= self.border_right.x:
                pyglet.app.exit()

            if self.player.y <= self.border_down.y:
                pyglet.app.exit()

            if self.player.x <= self.border_left.x:
                pyglet.app.exit()

            self.player_position.append(self.player.position)

            #player movement
            self.timer += dt

            if self.timer >= .1875:
                self.player.x += self.move_x * self.speed
                self.player.y += self.move_y * self.speed

                if num_square >= 1 and len(self.player_position) > 0:
                    x_y = self.player_position[-1]
                    block5= self.player_blocks[0]
                    block5.x = x_y[0]
                    block5.y = x_y[1]

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 2 and len(self.player_position) > 0:
                    x_y = self.player_position[-15]
                    block5= self.player_blocks[1]
                    block5.x = x_y[0]
                    block5.y = x_y[1]

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 3 and len(self.player_position) > 0:
                    x_y = self.player_position[-25]
                    block5= self.player_blocks[2]
                    block5.x = x_y[0]
                    block5.y = x_y[1]

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 4 and len(self.player_position) > 0:
                    x_y = self.player_position[-40]
                    block5= self.player_blocks[3]
                    block5.x = x_y[0]
                    block5.y = x_y[1]

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 5 and len(self.player_position) > 0:
                    x_y = self.player_position[-55]
                    block5= self.player_blocks[4]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -55

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()


                if num_square >= 6 and len(self.player_position) > 0:
                    x_y = self.player_position[-70]
                    block5= self.player_blocks[5]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -70

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 7 and len(self.player_position) > 0:
                    x_y = self.player_position[-80]
                    block5= self.player_blocks[6]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -80

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 8 and len(self.player_position) > 0:
                    x_y = self.player_position[-95]
                    block5= self.player_blocks[7]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -95

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 9 and len(self.player_position) > 0:
                    x_y = self.player_position[-105]
                    block5= self.player_blocks[8]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -105

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 10 and len(self.player_position) > 0:
                    x_y = self.player_position[-115]
                    block5= self.player_blocks[9]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -115
                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 11 and len(self.player_position) > 0:
                    x_y = self.player_position[-125]
                    block5= self.player_blocks[10]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -125

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 12 and len(self.player_position) > 0:
                    x_y = self.player_position[-135]
                    block5= self.player_blocks[11]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -135

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 13 and len(self.player_position) > 0:
                    x_y = self.player_position[-145]
                    block5= self.player_blocks[12]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -145

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 14 and len(self.player_position) > 0:
                    x_y = self.player_position[-155]
                    block5= self.player_blocks[13]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -155

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 15 and len(self.player_position) > 0:
                    x_y = self.player_position[-165]
                    block5= self.player_blocks[14]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -165

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 16 and len(self.player_position) > 0:
                    x_y = self.player_position[-175]
                    block5= self.player_blocks[15]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -175

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 17 and len(self.player_position) > 0:
                    x_y = self.player_position[-185]
                    block5= self.player_blocks[16]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -185

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 18 and len(self.player_position) > 0:
                    x_y = self.player_position[-195]
                    block5= self.player_blocks[17]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -195

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 19 and len(self.player_position) > 0:
                    x_y = self.player_position[-205]
                    block5= self.player_blocks[18]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -205

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 20 and len(self.player_position) > 0:
                    x_y = self.player_position[-225]
                    block5= self.player_blocks[19]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -225

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 21 and len(self.player_position) > 0:
                    x_y = self.player_position[-235]
                    block5= self.player_blocks[20]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -235

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 22 and len(self.player_position) > 0:
                    x_y = self.player_position[-245]
                    block5= self.player_blocks[21]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -245

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 23 and len(self.player_position) > 0:
                    x_y = self.player_position[-255]
                    block5= self.player_blocks[22]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -255

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 24 and len(self.player_position) > 0:
                    x_y = self.player_position[-265]
                    block5= self.player_blocks[23]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -265

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 25 and len(self.player_position) > 0:
                    x_y = self.player_position[-275]
                    block5= self.player_blocks[24]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -275

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 26 and len(self.player_position) > 0:
                    x_y = self.player_position[-285]
                    block5= self.player_blocks[25]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -285

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 27 and len(self.player_position) > 0:
                    x_y = self.player_position[-295]
                    block5= self.player_blocks[26]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -295

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 28 and len(self.player_position) > 0:
                    x_y = self.player_position[-305]
                    block5= self.player_blocks[27]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -305

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 29 and len(self.player_position) > 0:
                    x_y = self.player_position[-315]
                    block5= self.player_blocks[28]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -315

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 30 and len(self.player_position) > 0:
                    x_y = self.player_position[-325]
                    block5= self.player_blocks[29]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -325

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 31 and len(self.player_position) > 0:
                    x_y = self.player_position[-335]
                    block5= self.player_blocks[30]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -335

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 32 and len(self.player_position) > 0:
                    x_y = self.player_position[-345]
                    block5= self.player_blocks[31]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -345

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 33 and len(self.player_position) > 0:
                    x_y = self.player_position[-355]
                    block5= self.player_blocks[32]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -355

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 34 and len(self.player_position) > 0:
                    x_y = self.player_position[-365]
                    block5= self.player_blocks[33]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -365

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 35 and len(self.player_position) > 0:
                    x_y = self.player_position[-375]
                    block5= self.player_blocks[34]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -375

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 36 and len(self.player_position) > 0:
                    x_y = self.player_position[-385]
                    block5= self.player_blocks[35]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -385

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 37 and len(self.player_position) > 0:
                    x_y = self.player_position[-395]
                    block5= self.player_blocks[36]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -395

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 38 and len(self.player_position) > 0:
                    x_y = self.player_position[-405]
                    block5= self.player_blocks[37]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -405

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 39 and len(self.player_position) > 0:
                    x_y = self.player_position[-405]
                    block5= self.player_blocks[38]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -405

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 40 and len(self.player_position) > 0:
                    x_y = self.player_position[-415]
                    block5= self.player_blocks[39]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -415

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 41 and len(self.player_position) > 0:
                    x_y = self.player_position[-425]
                    block5= self.player_blocks[40]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -425

                if num_square >= 42 and len(self.player_position) > 0:
                    x_y = self.player_position[-435]
                    block5= self.player_blocks[41]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -435

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 43 and len(self.player_position) > 0:
                    x_y = self.player_position[-445]
                    block5= self.player_blocks[42]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -445

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 44 and len(self.player_position) > 0:
                    x_y = self.player_position[-455]
                    block5= self.player_blocks[43]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -455

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 45 and len(self.player_position) > 0:
                    x_y = self.player_position[-465]
                    block5= self.player_blocks[44]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -465

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 46 and len(self.player_position) > 0:
                    x_y = self.player_position[-475]
                    block5= self.player_blocks[45]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -475

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 47 and len(self.player_position) > 0:
                    x_y = self.player_position[-485]
                    block5= self.player_blocks[46]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -485

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 48 and len(self.player_position) > 0:
                    x_y = self.player_position[-495]
                    block5= self.player_blocks[47]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -495

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 49 and len(self.player_position) > 0:
                    x_y = self.player_position[-505]
                    block5= self.player_blocks[48]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -505

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 50 and len(self.player_position) > 0:
                    x_y = self.player_position[-515]
                    block5= self.player_blocks[49]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -515

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 51 and len(self.player_position) > 0:
                    x_y = self.player_position[-525]
                    block5= self.player_blocks[50]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -525

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 52 and len(self.player_position) > 0:
                    x_y = self.player_position[-535]
                    block5= self.player_blocks[51]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -535

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 53 and len(self.player_position) > 0:
                    x_y = self.player_position[-545]
                    block5= self.player_blocks[52]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -545

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 54 and len(self.player_position) > 0:
                    x_y = self.player_position[-555]
                    block5= self.player_blocks[53]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -555

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 55 and len(self.player_position) > 0:
                    x_y = self.player_position[-565]
                    block5= self.player_blocks[54]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -565

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 56 and len(self.player_position) > 0:
                    x_y = self.player_position[-575]
                    block5= self.player_blocks[55]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -575

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 57 and len(self.player_position) > 0:
                    x_y = self.player_position[-585]
                    block5= self.player_blocks[56]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -585

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 58 and len(self.player_position) > 0:
                    x_y = self.player_position[-595]
                    block5= self.player_blocks[57]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -595

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 59 and len(self.player_position) > 0:
                    x_y = self.player_position[-605]
                    block5= self.player_blocks[58]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -605

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 60 and len(self.player_position) > 0:
                    x_y = self.player_position[-615]
                    block5= self.player_blocks[59]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -615

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 61 and len(self.player_position) > 0:
                    x_y = self.player_position[-625]
                    block5= self.player_blocks[60]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -625

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 62 and len(self.player_position) > 0:
                    x_y = self.player_position[-635]
                    block5= self.player_blocks[61]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -635

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 63 and len(self.player_position) > 0:
                    x_y = self.player_position[-645]
                    block5= self.player_blocks[62]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -645

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 64 and len(self.player_position) > 0:
                    x_y = self.player_position[-655]
                    block5= self.player_blocks[63]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -655

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 65 and len(self.player_position) > 0:
                    x_y = self.player_position[-665]
                    block5= self.player_blocks[64]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -665

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 66 and len(self.player_position) > 0:
                    x_y = self.player_position[-675]
                    block5= self.player_blocks[65]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -675

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 67 and len(self.player_position) > 0:
                    x_y = self.player_position[-685]
                    block5= self.player_blocks[66]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -685

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 68 and len(self.player_position) > 0:
                    x_y = self.player_position[-695]
                    block5= self.player_blocks[67]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -695
                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 69 and len(self.player_position) > 0:
                    x_y = self.player_position[-705]
                    block5= self.player_blocks[68]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -705

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 70 and len(self.player_position) > 0:
                    x_y = self.player_position[-715]
                    block5= self.player_blocks[69]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -715

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 71 and len(self.player_position) > 0:
                    x_y = self.player_position[-725]
                    block5= self.player_blocks[70]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -725

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 72 and len(self.player_position) > 0:
                    x_y = self.player_position[-735]
                    block5= self.player_blocks[71]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -735

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 73 and len(self.player_position) > 0:
                    x_y = self.player_position[-745]
                    block5= self.player_blocks[72]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -745

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 74 and len(self.player_position) > 0:
                    x_y = self.player_position[-755]
                    block5= self.player_blocks[73]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -755

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 75 and len(self.player_position) > 0:
                    x_y = self.player_position[-765]
                    block5= self.player_blocks[74]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -765

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 76 and len(self.player_position) > 0:
                    x_y = self.player_position[-775]
                    block5= self.player_blocks[75]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -775

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 77 and len(self.player_position) > 0:
                    x_y = self.player_position[-785]
                    block5= self.player_blocks[76]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -785

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 78 and len(self.player_position) > 0:
                    x_y = self.player_position[-795]
                    block5= self.player_blocks[77]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -795

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 79 and len(self.player_position) > 0:
                    x_y = self.player_position[-805]
                    block5= self.player_blocks[78]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -805

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 80 and len(self.player_position) > 0:
                    x_y = self.player_position[-815]
                    block5= self.player_blocks[79]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -815

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 81 and len(self.player_position) > 0:
                    x_y = self.player_position[-825]
                    block5= self.player_blocks[80]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -825

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 82 and len(self.player_position) > 0:
                    x_y = self.player_position[-835]
                    block5= self.player_blocks[81]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -835

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 83 and len(self.player_position) > 0:
                    x_y = self.player_position[-845]
                    block5= self.player_blocks[82]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -845

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 84 and len(self.player_position) > 0:
                    x_y = self.player_position[-855]
                    block5= self.player_blocks[83]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -855

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 85 and len(self.player_position) > 0:
                    x_y = self.player_position[-865]
                    block5= self.player_blocks[84]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -865

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 86 and len(self.player_position) > 0:
                    x_y = self.player_position[-875]
                    block5= self.player_blocks[85]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -875

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 87 and len(self.player_position) > 0:
                    x_y = self.player_position[-885]
                    block5= self.player_blocks[86]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -885

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 88 and len(self.player_position) > 0:
                    x_y = self.player_position[-895]
                    block5= self.player_blocks[87]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -895

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 89 and len(self.player_position) > 0:
                    x_y = self.player_position[-905]
                    block5= self.player_blocks[88]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -905

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 90 and len(self.player_position) > 0:
                    x_y = self.player_position[-915]
                    block5= self.player_blocks[89]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -915

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 91 and len(self.player_position) > 0:
                    x_y = self.player_position[-925]
                    block5= self.player_blocks[90]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -925

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 92 and len(self.player_position) > 0:
                    x_y = self.player_position[-935]
                    block5= self.player_blocks[91]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -935

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 93 and len(self.player_position) > 0:
                    x_y = self.player_position[-945]
                    block5= self.player_blocks[92]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -945

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 94 and len(self.player_position) > 0:
                    x_y = self.player_position[-955]
                    block5= self.player_blocks[93]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -955

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 95 and len(self.player_position) > 0:
                    x_y = self.player_position[-965]
                    block5= self.player_blocks[94]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -965

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 96 and len(self.player_position) > 0:
                    x_y = self.player_position[-975]
                    block5= self.player_blocks[95]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -975

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 97 and len(self.player_position) > 0:
                    x_y = self.player_position[-985]
                    block5= self.player_blocks[96]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -985

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 98 and len(self.player_position) > 0:
                    x_y = self.player_position[-995]
                    block5= self.player_blocks[97]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -995

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 99 and len(self.player_position) > 0:
                    x_y = self.player_position[-1005]
                    block5= self.player_blocks[98]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -1005

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                if num_square >= 100 and len(self.player_position) > 0:
                    x_y = self.player_position[-1015]
                    block5= self.player_blocks[99]
                    block5.x = x_y[0]
                    block5.y = x_y[1]
                    self.x= -1015

                    if self.apple.x == block5.x and self.apple.y == block5.y:
                        self.apple.delete()
                        apple_x = random.randrange(50, 801, 50)
                        apple_y = random.randrange(50, 801, 50)
                        self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)

                    if self.player.x == block5.x and self.player.y == block5.y:
                        pyglet.app.exit()

                self.player_postion= self.player.position

                self.timer= 0.0



            if self.apple.x == self.player.x and self.apple.y == self.player.y:
                self.apple.delete()
                # apple square
                apple_x = random.randrange(50, 801, 50)
                apple_y = random.randrange(50, 801, 50)
                self.apple = shapes.Rectangle(x=apple_x, y=apple_y, width=50, height=50, color=(255, 0, 0), batch=self.batch)
                num_square += 1
                self.add_player_square()


    window1 = MyWindow(width=900, height=900, caption='Snake Game')
    pyglet.clock.schedule_interval(window1.update, 1 / 60)
    pyglet.app.run()



def home_screen():

        
    def main():
        home= Home()
        home.mainloop()

    class Home(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title('Home Screen')
            self.resizable(False, False)
            self.geometry('900x900+440+35')

            frame= Frame(self)
            frame.grid(row=0, column=0, sticky= 'nsew')
    
    class Frame_highscore(ttk.Frame):
        def __init__(self, parent):
            super().__init__(parent)
            self.grid(row=0, column=0, sticky='nsew')
            self.master.columnconfigure(0, weight=1)
            self.master.rowconfigure(0, weight=1)

            for c in range(3):
                self.columnconfigure(c, weight=1, uniform='group1')

            for r in range(6):
                self.rowconfigure(r, weight=1, uniform='group1')

            back_image= tk.PhotoImage(file='C:/Users/PC/OneDrive/coding/Coding files/personal/Snake Game/Background1.png')
            back_label= tk.Label(self, image= back_image)
            back_label.place(x=0, y=0, relwidth=1, relheight=1)
            back_label.image = back_image  # type: ignore

            label= tk.Label(self, text='High Score', font=('Arial', 40), bg='black', fg='white')
            label.grid(row=1, column=0, columnspan=3, padx=70, sticky='nsew')

            label2= tk.Label(self, text= f'High Score: {high_score}', font=('Arial', 40), bg='black', fg='white')
            label2.grid(row=2, column=0, columnspan=3, padx=70, sticky='nsew')

            self.back_button= tk.Button(self, text='Back', command=self.back_home)
            self.back_button.config(font=('Arial', 20), bg='blue', fg='white')
            self.back_button.grid(row=3, column=1, rowspan=1,sticky='nsew')

        def back_home(self):
            self.destroy()
            frame = Frame(self.master)
            frame.grid(row=0, column=0, sticky='nsew')
    
    class Frame(ttk.Frame):
        def __init__(self, parent):
            super().__init__(parent)
            self.grid(row=0, column=0, sticky='nsew')
            self.master.columnconfigure(0, weight=1)
            self.master.rowconfigure(0, weight=1)

            for c in range(3):
                self.columnconfigure(c, weight=1, uniform='group1')

            for r in range(6):
                self.rowconfigure(r, weight=1, uniform='group1')

            back_image= tk.PhotoImage(file='C:/Users/PC/OneDrive/coding/Coding files/personal/Snake Game/Background1.png')
            back_label= tk.Label(self, image= back_image)
            back_label.place(x=0, y=0, relwidth=1, relheight=1)
            back_label.image = back_image  # type: ignore


            label= tk.Label(self, text='Snake Game', font=('Arial', 40), bg='black', fg='white')
            label.grid(row=1, column=0, columnspan=3, padx=70, sticky='nsew')

            self.start_button= tk.Button(self, text='Start Game', command=self.start_game)
            self.start_button.config(font=('Arial', 20), bg='blue', fg='white')
            self.start_button.grid(row=2, column=1, rowspan=1,sticky='nsew')

            self.high_button= tk.Button(self, text='High Score', command=self.high_score)
            self.high_button.config(font=('Arial', 20), bg='green', fg='white')
            self.high_button.grid(row=3, column=1, rowspan=1, sticky='nsew')

            self.exit_button= tk.Button(self, text='Exit', command=self.end_game)
            self.exit_button.config(font=('Arial', 20), bg='red', fg='white')
            self.exit_button.grid(row=4, column=1, rowspan=1, sticky='nsew')

        def start_game(self):
            self.master.destroy()
            game()
        
        def end_game(self):
            self.master.destroy()
        
        def high_score(self):
            self.destroy()
            high_score_frame = Frame_highscore(self.master)
            high_score_frame.grid(row=0, column=0, sticky='nsew')




    main()


home_screen()
