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

# Button class derived from https://thepythoncode.com/code/make-a-button-using-pygame-in-python


class Button:
    objects = []

    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, name=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.onclickFunction = onclickFunction
        self.name = name

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
        }

        self.surface = pygame.Surface((width, height))
        self.text = font.render(buttonText, True, (20, 20, 20))

        Button.objects.append(self)

    def draw(self, screen):
        mousePos = pygame.mouse.get_pos()
        color = self.fillColors['hover'] if self.rect.collidepoint(mousePos) else self.fillColors['normal']
        self.surface.fill(color)

        self.surface.blit(
            self.text,
            (self.rect.width // 2 - self.text.get_width() // 2,
             self.rect.height // 2 - self.text.get_height() // 2)
        )

        screen.blit(self.surface, self.rect)

    @classmethod
    def handle_event(cls, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in cls.objects:
                if button.rect.collidepoint(event.pos):
                    if button.onclickFunction:
                        button.onclickFunction()
                    break  # Stop after the first button is clicked

    @classmethod
    def draw_all(cls, screen):
        for button in cls.objects:
            button.draw(screen)

    @classmethod
    def clear_buttons(cls):
        cls.objects.clear()



def button_pressed():
    print('Button Pressed')
