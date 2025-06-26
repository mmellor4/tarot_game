# button.py

import pygame
import textwrap

pygame.init()

# WINDOW SIZE
X = 700
Y = 700
screen = pygame.display.set_mode((X, Y))

# COLORS
bg_color = (0, 0, 0)
txt_color = (255, 255, 255)
selected_color = (0, 255, 0)

# FONT
font_size = 20
font = pygame.font.Font("fonts/pixel_font.ttf", font_size)


class Button():

    objects = []

    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False, name=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.name = name

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False
        self.clicked = False

        Button.objects.append(self)

    def process(self):
        if self.clicked:
            return

        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

                # flag button as clicked
                self.clicked = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])

        # only show the button if not clicked
        if not self.clicked:
            screen.blit(self.buttonSurface, self.buttonRect)

    @classmethod
    def clear_buttons(cls):
        cls.objects.clear()


def button_pressed():
    print('Button Pressed')
