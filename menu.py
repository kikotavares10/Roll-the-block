import pygame, sys
import botoes
from pygame import mixer
from pygame.locals import *
from jogo import *

pygame.init()

SCREEN = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("Menu")

def get_font(size):
    return pygame.font.Font("Gaming_font.ttf", size)        #fonte das letras

BG = pygame.image.load("Background.jpg")


#background sound
mixer.init()
mixer.music.load("SubwayDreams.mp3") 
volume = 0.5
pygame.mixer.music.set_volume(volume)
mixer.music.play(-1)                                  #para a música tocar em loop


def play():                                           #janela com os niveis
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        CHOOSE_TEXT = get_font(35).render("CHOOSE YOUR LEVEL", True, "White")
        CHOOSE_RECT = CHOOSE_TEXT.get_rect(center=(315, 70))
        SCREEN.blit(CHOOSE_TEXT, CHOOSE_RECT)


        
        LEVEL1_BUTTON=botoes.Button(image=None, pos=(200,275), 
                                    text_input="LEVEL1", font=get_font(50), base_color="White", hovering_color="Red") 
        
        LEVEL1_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL1_BUTTON.update(SCREEN)

        LEVEL2_BUTTON = botoes.Button(image=None, pos=(635,275), 
                                    text_input="LEVEL2", font=get_font(50), base_color="White", hovering_color="Red") 
        LEVEL2_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL2_BUTTON.update(SCREEN)

        LEVEL3_BUTTON = botoes.Button(image=None, pos=(1050,275), 
                                    text_input="LEVEL3", font=get_font(50), base_color="White", hovering_color="Red") 
        LEVEL3_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL3_BUTTON.update(SCREEN)

        LEVEL4_BUTTON=botoes.Button(image=None, pos=(200,400), 
                                    text_input="LEVEL4", font=get_font(50), base_color="White", hovering_color="Red") 
        
        LEVEL4_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL4_BUTTON.update(SCREEN)

        LEVEL5_BUTTON = botoes.Button(image=None, pos=(635,400), 
                                    text_input="LEVEL5", font=get_font(50), base_color="White", hovering_color="Red") 
        LEVEL5_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL5_BUTTON.update(SCREEN)

        LEVEL6_BUTTON = botoes.Button(image=None, pos=(1050,400), 
                                    text_input="LEVEL6", font=get_font(50), base_color="White", hovering_color="Red") 
        LEVEL6_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL6_BUTTON.update(SCREEN)

        LEVEL7_BUTTON=botoes.Button(image=None, pos=(200,525), 
                                    text_input="LEVEL7", font=get_font(50), base_color="White", hovering_color="Red") 
        
        LEVEL7_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL7_BUTTON.update(SCREEN)

        LEVEL8_BUTTON = botoes.Button(image=None, pos=(635,525), 
                                    text_input="LEVEL8", font=get_font(50), base_color="White", hovering_color="Red") 
        LEVEL8_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL8_BUTTON.update(SCREEN)

        LEVEL9_BUTTON = botoes.Button(image=None, pos=(1050,525), 
                                    text_input="LEVEL9", font=get_font(50), base_color="White", hovering_color="Red") 
        LEVEL9_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL9_BUTTON.update(SCREEN)


        PLAY_BACK = botoes.Button(image=None, pos=(1100, 650), text_input="BACK", 
                                   font=get_font(50), base_color="White", hovering_color="Red") 

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:                  #escolha do nivel através dos botões
                if LEVEL1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    tabuleiro1=[[0,0,0,0,0,0,0,0,0,0],      
                                [0,1,1,1,0,0,0,0,0,0],
                                [0,1,1,1,1,0,1,1,1,0],
                                [0,2,1,1,4,1,1,9,1,0],
                                [0,0,1,1,1,1,1,1,1,0],
                                [0,0,1,1,1,1,1,1,0,0],
                                [0,0,0,0,0,0,0,0,0,0]]
                    jogar(tabuleiro1)                               #abre o jogo com o tabuleiro especifico do nivel
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL2_BUTTON.checkForInput(PLAY_MOUSE_POS):

                    tabuleiro2=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0],
                                [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0],
                                [0,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0],
                                [0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0],
                                [0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0],
                                [0,1,2,1,0,0,1,1,1,1,1,1,1,1,1,1,0],
                                [0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0],
                                [0,0,0,0,0,0,1,9,1,0,0,1,1,1,1,1,0],
                                [0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,1,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
                    
                    jogar(tabuleiro2)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL3_BUTTON.checkForInput(PLAY_MOUSE_POS):

                    tabuleiro3=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0],
                                [0,1,1,1,1,0,0,1,1,1,0,0,1,1,0,0,0],
                                [0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0],
                                [0,1,2,1,1,0,0,0,0,0,0,0,1,1,9,1,0],
                                [0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
                    
                    jogar(tabuleiro3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL4_BUTTON.checkForInput(PLAY_MOUSE_POS):

                    tabuleiro4=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                                [0,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0],
                                [0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0],
                                [0,1,1,1,0,0,0,1,1,1,0,0,1,2,1,0],
                                [0,1,1,1,1,1,1,1,9,1,0,0,1,1,1,0],
                                [0,1,1,1,0,0,1,1,1,1,0,0,1,0,0,0],
                                [0,0,0,1,0,0,1,1,1,1,1,1,1,0,0,0],
                                [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
                                [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
                                [0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0]]
                    
                    
                    jogar(tabuleiro4)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL5_BUTTON.checkForInput(PLAY_MOUSE_POS):

                    tabuleiro5=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
                                [0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,0],
                                [0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0],
                                [0,2,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0],
                                [0,0,0,0,0,1,1,1,0,0,0,0,1,1,9,1,0],
                                [0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0],
                                [0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
                                [0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
                    
                    jogar(tabuleiro5)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL6_BUTTON.checkForInput(PLAY_MOUSE_POS):

                    tabuleiro6=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,0],
                                [0,1,1,1,1,0,0,1,1,1,1,51,51,1,1,1,0],
                                [0,1,1,5,1,0,0,1,1,1,1,0,0,1,1,1,0],
                                [0,1,1,1,1,0,0,1,1,1,1,0,0,1,9,1,0],
                                [0,1,2,1,1,51,51,1,1,1,1,0,0,1,1,1,0],
                                [0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
                    jogar(tabuleiro6)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL7_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    tabuleiro7=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,1,1,2,1,1,1,1,1,1,1,1,1,1,1,0],
                                [0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0],
                                [0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
                                [0,1,1,1,0,0,1,1,51,51,1,1,5,1,1,1,0],
                                [0,1,9,1,0,0,1,1,0,0,0,0,0,1,1,1,0],
                                [0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0],
                                [0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0],
                                [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
                    
                    jogar(tabuleiro7)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL8_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    tabuleiro8=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,1,4,1,1,1,1,1,1,0,0,0,0,0,0],
                                [0,0,0,4,4,0,1,1,0,1,1,0,0,0,0,0,0],
                                [0,4,1,9,4,0,1,1,1,1,1,0,0,0,0,0,0],
                                [0,1,1,1,0,0,1,4,4,0,4,1,4,4,0,0,0],
                                [0,2,1,4,1,0,0,0,0,0,1,1,1,4,4,4,0],
                                [0,0,0,4,1,0,0,0,0,0,4,1,4,4,0,0,0],
                                [0,0,0,4,1,0,0,0,4,4,1,0,0,4,4,4,0],
                                [0,0,0,4,4,1,0,1,4,4,4,4,4,4,0,0,0],
                                [0,0,0,0,4,4,4,4,4,4,0,0,0,4,0,0,0],
                                [0,0,0,0,0,4,4,4,0,0,0,0,0,4,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
                    jogar(tabuleiro8)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL9_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    tabuleiro9=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],      
                                [0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0],
                                [0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,1,0],
                                [0,1,2,1,1,1,1,1,1,1,1,0,0,1,9,1,0],
                                [0,1,1,1,0,0,0,0,1,1,5,0,0,1,1,1,0],
                                [0,1,1,4,0,0,0,0,1,1,1,0,0,1,1,1,0],
                                [0,0,1,4,51,0,0,0,1,0,0,0,0,0,0,0,0],
                                [0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
                    jogar(tabuleiro9)
                    
            

        pygame.display.update()
    
def options():                              # janela options
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(60).render("OPTIONS", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(300, 70))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        def volume():                       #janela do volume
            while True:
                VOLUME_MOUSE_POS = pygame.mouse.get_pos()

                SCREEN.blit(BG, (0, 0))

                VOLUME_TEXT = get_font(60).render("VOLUME", True, "White")
                VOLUME_RECT = VOLUME_TEXT.get_rect(center=(300, 70))

                SCREEN.blit(VOLUME_TEXT, VOLUME_RECT)

                VOLUME_BACK = botoes.Button(image=None, pos=(1100, 650), text_input="BACK", font=get_font(50), base_color="White", hovering_color="Red")  #botão "back" para voltar ao menu options

                VOLUME_BACK.changeColor(VOLUME_MOUSE_POS)
                VOLUME_BACK.update(SCREEN)

                PLUS_VOLUME = botoes.Button(image=None, pos=(725, 375), text_input="+", font=get_font(120), base_color="white", hovering_color="Red")  #botão para subir o volume
                PLUS_VOLUME.changeColor(VOLUME_MOUSE_POS)
                PLUS_VOLUME.update(SCREEN)

                MINUS_VOLUME = botoes.Button(image=None, pos=(575, 375), text_input="-", font=get_font(120), base_color="white", hovering_color="Red") #botão para diminuir o volume
                MINUS_VOLUME.changeColor(VOLUME_MOUSE_POS)
                MINUS_VOLUME.update(SCREEN)

                def increase():                           #função para aumentar o volume
                    global volume
                    volume = min(1.0, volume + 0.1)
                    pygame.mixer.music.set_volume(volume)
                def decrease():                           #função para diminuir o volume
                    global volume
                    volume = max(0.0, volume - 0.1)
                    pygame.mixer.music.set_volume(volume)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if VOLUME_BACK.checkForInput(VOLUME_MOUSE_POS):
                            options()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if MINUS_VOLUME.checkForInput(VOLUME_MOUSE_POS):              #quando pressionado o botão "-", diminui o volume da música de fundo
                            decrease()    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLUS_VOLUME.checkForInput(VOLUME_MOUSE_POS):               #quando pressionado o botão "+", aumenta o volume da música de fundo
                            increase()     
                pygame.display.update()

        def credits():                                  #janela dos créditos
            while True:
                CREDITS_MOUSE_POS = pygame.mouse.get_pos()

                SCREEN.blit(BG, (0, 0))

                CREDITS_TEXT = get_font(60).render("CREDITS", True, "White")
                CREDITS_RECT = CREDITS_TEXT.get_rect(center=(300, 70))                
                SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)

                MADE1_TEXT = get_font(55).render("MADE BY", True,"White")          #texto dos créditos dividido em três linhas
                MADE1_RECT = MADE1_TEXT.get_rect(center=(640, 325))
                SCREEN.blit(MADE1_TEXT, MADE1_RECT)
                MADE2_TEXT = get_font(55).render("FRANCISCO TAVARES", True,"White")
                MADE2_RECT = MADE2_TEXT.get_rect(center=(640, 400))
                SCREEN.blit(MADE2_TEXT, MADE2_RECT)
                MADE3_TEXT = get_font(55).render("RODRIGO BATISTA", True,"White")
                MADE3_RECT = MADE3_TEXT.get_rect(center=(640, 475))
                SCREEN.blit(MADE3_TEXT, MADE3_RECT)

                
                CREDITS_BACK = botoes.Button(image=None, pos=(1100, 650), text_input="BACK",                  #botão "back" para voltar ao menu options
                                              font=get_font(50), base_color="White", hovering_color="Red")
                CREDITS_BACK.changeColor(CREDITS_MOUSE_POS)
                CREDITS_BACK.update(SCREEN)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:        #retorna à janela options quando pressionamos o "back"
                        if CREDITS_BACK.checkForInput(CREDITS_MOUSE_POS):
                            options()
                pygame.display.update()

        VOLUME_BUTTON=botoes.Button(image=None, pos=(640,350), 
                                    text_input="VOLUME", font=get_font(75), base_color="white", hovering_color="Red")   #botão para ir para a janela "volume"
        VOLUME_BUTTON.changeColor(OPTIONS_MOUSE_POS)                            
        VOLUME_BUTTON.update(SCREEN)

        CREDITS_BUTTON=botoes.Button(image=None, pos=(640,500), 
                                    text_input="CREDITS", font=get_font(75), base_color="white", hovering_color="Red")  #botão para ir para a janela "options"
        CREDITS_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        CREDITS_BUTTON.update(SCREEN)

        OPTIONS_BACK = botoes.Button(image=None, pos=(1100, 650),                                              #botão para voltar ao menu inicial
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Red")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():                         
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VOLUME_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    volume()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDITS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    credits()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(60).render("MAIN MENU", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(300, 70))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        PLAY_BUTTON = botoes.Button(image=None, pos=(640, 300), 
                            text_input="PLAY", font=get_font(90), base_color="White", hovering_color="Red") #mudar esta cor, não faz grande contraste, como as das linhas a baixo
        OPTIONS_BUTTON = botoes.Button(image=None, pos=(640, 450), 
                            text_input="OPTIONS", font=get_font(90), base_color="White", hovering_color="Red")
        QUIT_BUTTON = botoes.Button(image=None, pos=(640, 600), 
                            text_input="QUIT", font=get_font(90), base_color="White", hovering_color="Red")

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #clicar no x do canto superior da janela
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS): #entra para a janela dos niveis
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS): #clicar no botão OPTIONS
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS): #clicar no QUIT e fechar o pygame
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()