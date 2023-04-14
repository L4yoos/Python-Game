import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((800, 900))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Pliki/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Pliki/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TETRIS = Button(image=None, pos=(400, 150),
                            text_input="TETRIS", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK = Button(image=None, pos=(400, 650),
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_TETRIS.changeColor(PLAY_MOUSE_POS)
        PLAY_TETRIS.update(SCREEN)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_TETRIS.checkForInput(PLAY_MOUSE_POS):
                    import gra
                    gra.rozpocznijgre()
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()


        pygame.display.update()
    
def autorzy():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        AUTORZY_TEXT = get_font(75).render("AUTORZY", True, "Black")
        AUTORZY_RECT = AUTORZY_TEXT.get_rect(center=(420, 150))
        SCREEN.blit(AUTORZY_TEXT, AUTORZY_RECT)

        KONRAD_TEXT = get_font(45).render("Konrad Dalecki", True, "Black")
        KONRAD_RECT = KONRAD_TEXT.get_rect(center=(400, 250))
        SCREEN.blit(KONRAD_TEXT, KONRAD_RECT)

        OPTIONS_BACK = Button(image=None, pos=(400, 650),
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MAIN_TEXT = get_font(100).render("MAIN", True, "#b68f40")
        MENU_TEXT = get_font(100).render("MENU", True, "#b68f40")
        MAIN_RECT = MAIN_TEXT.get_rect(center=(400, 100))
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 200))

        PLAY_BUTTON = Button(image=pygame.image.load("Pliki/Graj Rect.png"), pos=(400, 350),
                            text_input="GRAJ", font=get_font(75), base_color="#d7fcd4", hovering_color="#b68f40")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Pliki/Autorzy Rect.png"), pos=(400, 500),
                            text_input="AUTORZY", font=get_font(75), base_color="#d7fcd4", hovering_color="#b68f40")
        QUIT_BUTTON = Button(image=pygame.image.load("Pliki/Quit Rect.png"), pos=(400, 650),
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="#b68f40")

        SCREEN.blit(MAIN_TEXT, MAIN_RECT)
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    autorzy()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()