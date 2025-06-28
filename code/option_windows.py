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


def start_game_window():
    Button.clear_buttons()

    # global bool to end loop in main menu
    global game_started

    game_screen = pygame.display.set_mode((X, Y))

    game_screen.fill(bg_color)

    chariot = pygame.image.load("rider-waite-tarot/major_arcana_chariot.png")
    chariot = pygame.transform.scale(chariot, (200, 346))
    screen.blit(chariot, (250, 300))

    Button(20, 20, 100, 50, 'Quit', quit_game, name="QUIT")

    text1 = "You begin in a maze, a fork in the path in front of you."
    text2 = "Choose your path."

    # show text on the screen
    # y pos determines where text starts in the y coord
    y_pos = Y // 8
    # y pos + 20 to add spacing between each line of text
    y_pos = render_wrapped_text(text1, game_screen, font, X, y_pos + 20)
    y_pos = render_wrapped_text(text2, game_screen, font, X, y_pos + 20)

    Button(100, y_pos + 20, 200, 50, 'Right', choiceA_window, name="CHOICE_A")
    Button(350, y_pos + 20, 200, 50, 'Left', choiceB_window, name="CHOICE_B")

    pygame.display.flip()

    # once the game screen is loaded, set game_started to True to stop the menu
    game_started = True


def choiceA_window():
    Button.clear_buttons()
    Button(20, 20, 100, 50, 'Quit', quit_game, name="QUIT")

    game_screen = pygame.display.set_mode((X, Y))
    game_screen.fill(bg_color)

    chariot = pygame.image.load("rider-waite-tarot/major_arcana_star.png")
    chariot = pygame.transform.scale(chariot, (200, 346))
    screen.blit(chariot, (250, 320))

    text = "Room A. Choose again."

    y_pos = Y // 4
    render_wrapped_text(text, game_screen, font, X, y_pos)

    Button(100, y_pos + 40, 200, 50, 'Left', choiceC_window, name="CHOICE_C")
    Button(350, y_pos + 40, 200, 50, 'Right', choiceH_window, name="CHOICE_H")

    pygame.display.flip()


def choiceB_window():
    Button.clear_buttons()
    Button(20, 20, 100, 50, 'Quit', quit_game, name="QUIT")
    game_screen = pygame.display.set_mode((X, Y))
    game_screen.fill(bg_color)

    chariot = pygame.image.load("rider-waite-tarot/major_arcana_sun.png")
    chariot = pygame.transform.scale(chariot, (200, 346))
    screen.blit(chariot, (250, 320))
    text = "Room B. Choose again."

    y_pos = Y // 4
    render_wrapped_text(text, game_screen, font, X, y_pos)

    Button(100, y_pos + 40, 200, 50, 'Left', choiceD_window, name="CHOICE_D")
    Button(350, y_pos + 40, 200, 50, 'Right', choiceE_window, name="CHOICE_E")

    pygame.display.flip()


def choiceC_window():
    Button.clear_buttons()
    Button(20, 20, 100, 50, 'Quit', quit_game, name="QUIT")

    game_screen = pygame.display.set_mode((X, Y))
    game_screen.fill(bg_color)

    chariot = pygame.image.load("rider-waite-tarot/major_arcana_hermit.png")
    chariot = pygame.transform.scale(chariot, (200, 346))
    screen.blit(chariot, (250, 320))
    text = "Room C. Choose again."

    y_pos = Y // 4
    render_wrapped_text(text, game_screen, font, X, y_pos)

    Button(100, y_pos + 40, 200, 50, 'Left', choiceJ_window, name="CHOICE_J")
    Button(350, y_pos + 40, 200, 50, 'Right', choiceD_window, name="CHOICE_D")

    pygame.display.flip()


def choiceD_window():
    Button.clear_buttons()
    Button(20, 20, 100, 50, 'Quit', quit_game, name="QUIT")

    game_screen = pygame.display.set_mode((X, Y))
    game_screen.fill(bg_color)

    chariot = pygame.image.load("rider-waite-tarot/major_arcana_strength.png")
    chariot = pygame.transform.scale(chariot, (200, 346))
    screen.blit(chariot, (250, 320))
    text = "Room D. Choose again."

    y_pos = Y // 4
    render_wrapped_text(text, game_screen, font, X, y_pos)

    Button(100, y_pos + 40, 200, 50, 'Left', choiceG_window, name="CHOICE_G")
    Button(350, y_pos + 40, 200, 50, 'Right', choiceH_window, name="CHOICE_H")

    pygame.display.flip()


def choiceE_window():
    Button.clear_buttons()
    Button(20, 20, 100, 50, 'Quit', quit_game, name="QUIT")

    game_screen = pygame.display.set_mode((X, Y))
    game_screen.fill(bg_color)

    chariot = pygame.image.load("rider-waite-tarot/major_arcana_moon.png")
    chariot = pygame.transform.scale(chariot, (200, 346))
    screen.blit(chariot, (250, 320))
    text = "Room E. Choose again."

    y_pos = Y // 4
    render_wrapped_text(text, game_screen, font, X, y_pos)

    Button(100, y_pos + 40, 200, 50, 'Left', game_over, name="GAME_OVER")
    Button(350, y_pos + 40, 200, 50, 'Right', choiceI_window, name="CHOICE_I")

    pygame.display.flip()

'''
def choiceF_window():
    Button.clear_buttons()
    Button(20, 20, 100, 50, 'Quit', quit_game, name="QUIT")

    game_screen = pygame.display.set_mode((X, Y))
    game_screen.fill(bg_color)
    text = "Room E. Choose again."

    y_pos = Y // 4
    render_wrapped_text(text, game_screen, font, X, y_pos)

    Button(100, y_pos + 40, 200, 50, 'Left', choiceJ_window(), name="CHOICE_J")
    Button(350, y_pos + 40, 200, 50, 'Right', choiceI_window, name="CHOICE_I")

    pygame.display.flip()
'''


def choiceG_window():
    Button.clear_buttons()
    Button(20, 20, 100, 50, 'Quit', quit_game, name="QUIT")

    game_screen = pygame.display.set_mode((X, Y))
    game_screen.fill(bg_color)

    chariot = pygame.image.load("rider-waite-tarot/major_arcana_world.png")
    chariot = pygame.transform.scale(chariot, (200, 346))
    screen.blit(chariot, (250, 320))
    text = "Room G. Choose again."

    y_pos = Y // 4
    render_wrapped_text(text, game_screen, font, X, y_pos)

    Button(100, y_pos + 40, 200, 50, 'Left', choiceC_window, name="CHOICE_C")
    Button(350, y_pos + 40, 200, 50, 'Right', game_over, name="GAME_OVER")

    pygame.display.flip()


def choiceH_window():
    Button.clear_buttons()
    Button(20, 20, 100, 50, 'Quit', quit_game, name="QUIT")

    game_screen = pygame.display.set_mode((X, Y))
    game_screen.fill(bg_color)

    chariot = pygame.image.load("rider-waite-tarot/major_arcana_justice.png")
    chariot = pygame.transform.scale(chariot, (200, 346))
    screen.blit(chariot, (250, 320))
    text = "Room H. Choose again."

    y_pos = Y // 4
    render_wrapped_text(text, game_screen, font, X, y_pos)

    Button(100, y_pos + 40, 200, 50, 'Left', end_window, name="END")
    Button(350, y_pos + 40, 200, 50, 'Right', choiceG_window, name="CHOICE_G")

    pygame.display.flip()


def choiceI_window():
    Button.clear_buttons()
    Button(20, 20, 100, 50, 'Quit', quit_game, name="QUIT")

    game_screen = pygame.display.set_mode((X, Y))
    game_screen.fill(bg_color)

    chariot = pygame.image.load("rider-waite-tarot/major_arcana_empress.png")
    chariot = pygame.transform.scale(chariot, (200, 346))
    screen.blit(chariot, (250, 320))
    text = "Room I. Choose again."

    y_pos = Y // 4
    render_wrapped_text(text, game_screen, font, X, y_pos)

    Button(100, y_pos + 40, 200, 50, 'Left', choiceC_window, name="CHOICE_C")
    Button(350, y_pos + 40, 200, 50, 'Right', choiceG_window, name="CHOICE_G")

    pygame.display.flip()


def choiceJ_window():
    Button.clear_buttons()
    Button(20, 20, 100, 50, 'Quit', quit_game, name="QUIT")

    game_screen = pygame.display.set_mode((X, Y))
    game_screen.fill(bg_color)

    chariot = pygame.image.load("rider-waite-tarot/major_arcana_fool.png")
    chariot = pygame.transform.scale(chariot, (200, 346))
    screen.blit(chariot, (250, 320))
    text = "Room J. Choose again."

    y_pos = Y // 4
    render_wrapped_text(text, game_screen, font, X, y_pos)

    Button(100, y_pos + 40, 200, 50, 'Left', choiceE_window, name="CHOICE_E")
    Button(350, y_pos + 40, 200, 50, 'Right', choiceH_window, name="CHOICE_H")

    pygame.display.flip()


def end_window():
    Button.clear_buttons()
    # Button(20, 20, 100, 50, 'Quit', quit_game, name="QUIT")

    game_screen = pygame.display.set_mode((X, Y))
    game_screen.fill(bg_color)

    chariot = pygame.image.load("rider-waite-tarot/major_arcana_fortune.png")
    chariot = pygame.transform.scale(chariot, (200, 346))
    screen.blit(chariot, (250, 340))
    text = "You've escaped the maze"

    y_pos = Y // 4
    render_wrapped_text(text, game_screen, font, X, y_pos)

    Button(200, y_pos + 40, 300, 50, 'Play Again?', start_game_window, name="AGAIN")
    Button(250, y_pos + 100, 200, 50, 'Quit', quit_game, name="QUIT")

    pygame.display.flip()


def game_over():
    Button.clear_buttons()
    # Button(20, 20, 100, 50, 'Quit', quit_game, name="QUIT")

    game_screen = pygame.display.set_mode((X, Y))
    game_screen.fill(bg_color)

    chariot = pygame.image.load("rider-waite-tarot/major_arcana_death.png")
    chariot = pygame.transform.scale(chariot, (200, 346))
    screen.blit(chariot, (250, 340))
    text = "You died"

    y_pos = Y // 4
    render_wrapped_text(text, game_screen, font, X, y_pos)

    Button(200, y_pos + 40, 300, 50, 'Play Again?', start_game_window, name="AGAIN")
    Button(250, y_pos + 100, 200, 50, 'Quit', quit_game, name="QUIT")

    pygame.display.flip()


def quit_game():
    pygame.quit()
    exit()
