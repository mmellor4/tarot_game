# main.py
from pygame_menu import themes
from button import *
from option_windows import *
import pygame_menu

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


# display wrapped text
def render_wrapped_text(text, surface, font, max_width, y_pos):
    # width
    wrapped_text = textwrap.wrap(text, width=30)
    # padding
    line_height = font.get_height() + 5

    for idx, line in enumerate(wrapped_text):
        render_text = font.render(line, True, txt_color)
        # center text
        x_pos = (max_width - render_text.get_width()) // 2
        surface.blit(render_text, (x_pos, y_pos + idx * line_height))

    return y_pos + len(wrapped_text) * line_height


def game_window():
    # global bool to end loop in main menu
    global game_started

    game_screen = pygame.display.set_mode((X, Y))

    game_screen.fill(bg_color)

    Button(20, 20, 100, 50, 'Quit', quit_game, name="QUIT")

    text1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    text2 = "Choose your path."

    # show text on the screen
    # y pos determines where text starts in the y coord
    y_pos = Y // 8
    # y pos + 20 to add spacing between each line of text
    y_pos = render_wrapped_text(text1, game_screen, font, X, y_pos + 20)
    y_pos = render_wrapped_text(text2, game_screen, font, X, y_pos + 20)

    Button(100, y_pos + 20, 200, 50, 'Option 1', option1_window, name="opt1")
    Button(350, y_pos + 20, 200, 50, 'Option 2', option2_window, name="opt2")

    pygame.display.flip()

    # once the game screen is loaded, set game_started to True to stop the menu
    game_started = True


def loading_game():
    # LOADING SCREEN
    mainmenu._open(loading)
    pygame.time.set_timer(update_loading, 30)


# MAIN MENU

# menu options
mainmenu = pygame_menu.Menu('Game Demo', X, Y, theme=themes.THEME_DARK)
mainmenu.add.button('Start', loading_game)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

# loading bar
loading = pygame_menu.Menu('Loading Game...', X, Y, theme=themes.THEME_DARK)
loading.add.progress_bar("Progress", progressbar_id="1", default=0, width=200, )

# menu arrow
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))

update_loading = pygame.USEREVENT + 0

# game state bool
game_started = False

# main game loop
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == update_loading:
            # update progress bar
            progress = loading.get_widget("1")
            progress.set_value(progress.get_value() + 1)

            # check if the progress bar is full
            if progress.get_value() == 100:
                # stop timer to prevent further updates
                pygame.time.set_timer(update_loading, 0)
                # call game window
                game_window()

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if not game_started:
        # if game not started, continue menu display loop
        if mainmenu.is_enabled():
            mainmenu.update(events)
            mainmenu.draw(screen)
        elif loading.is_enabled():
            loading.update(events)
            loading.draw(screen)

    elif game_started:
        # if game has started, show the game window and stop displaying menu
        for obj in Button.objects:
            obj.process()



    pygame.display.update()
