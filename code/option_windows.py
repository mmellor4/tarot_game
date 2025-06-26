# option_windows.py

import pygame
import textwrap
from button import *

pygame.init()
# WINDOW SIZE
X = 700
Y = 700

# COLORS
bg_color = (0, 0, 0)
txt_color = (255, 255, 255)
selected_color = (0, 255, 0)

# FONT
font_size = 20
font = pygame.font.Font("fonts/pixel_font.ttf", font_size)


def render_wrapped_text(text, surface, font, max_width, y_pos):
    # Wrap text and render it on screen
    wrapped_text = textwrap.wrap(text, width=30)
    line_height = font.get_height() + 5

    for idx, line in enumerate(wrapped_text):
        render_text = font.render(line, True, txt_color)
        x_pos = (max_width - render_text.get_width()) // 2
        surface.blit(render_text, (x_pos, y_pos + idx * line_height))

    return y_pos + len(wrapped_text) * line_height


def option1_window():
    Button.clear_buttons()
    Button(20, 20, 100, 50, 'Quit', quit_game, name="QUIT")
    game_screen = pygame.display.set_mode((X, Y))
    game_screen.fill(bg_color)
    text = "You chose Option 1"
    y_pos = Y // 4
    render_wrapped_text(text, game_screen, font, X, y_pos)
    pygame.display.flip()


def option2_window():
    Button.clear_buttons()
    Button(20, 20, 100, 50, 'Quit', quit_game, name="QUIT")
    game_screen = pygame.display.set_mode((X, Y))
    game_screen.fill(bg_color)
    text = "You chose Option 2"
    y_pos = Y // 4
    render_wrapped_text(text, game_screen, font, X, y_pos)
    pygame.display.flip()


def quit_game():
    pygame.quit()
    exit()
