
import pygame
from pygame.locals import *
from sys import exit
from pprint import pprint
import time
import copy
import numpy as np
from collections import deque
import menu




def jogar(tabuleiro):
    
    lista_ponte=[]
                                 #Esta parte regista as posições dos caminhos ocultos
    bloco_final=tabuleiro


    for i in range (len(tabuleiro)): 
        for j in range (len(tabuleiro[i])):
            if tabuleiro[i][j]==51:
                lista_ponte.append((i,j))
                tabuleiro[i][j]=0
                print(lista_ponte)
                

    Num_linhas=len(tabuleiro)
    Num_colunas=len(tabuleiro[0])
    bloco=np.zeros((Num_linhas,Num_colunas),dtype=int)

    historico=[]

    RETANGULO = (255, 0, 0)             #Cores dos vários objetos para a parte gráfica
    META = (255, 255, 0)
    QUADRADO_PRETO = (0, 0, 0)
    BOTAO= (0,255,0)
    VIDRO= (173,216,230)
    BOTAO_ATIVO= (0,100,0)
    COR_FUNDO = (183,124,235)
    COR_TABULEIRO = (0, 0, 255)


    Tamanho_celula = 50
    Largura = 1280
    Altura = 700

            
    def posicao_inicial(bloco,tabuleiro):                                 #Obter a posição inicial do bloco
            for i in range (len(tabuleiro)):
                for j in range(len(tabuleiro[i])):
                    if tabuleiro[i][j]==2:
                        bloco[i][j]=2
                        return (i,j)
            return False
        
    def atualizar_vencedor(bloco,tabuleiro):                             #Verificar se a condição para vencer é cumprida
            for i in range (len(bloco)):
                for j in range (len(bloco[i])):
                    if bloco[i][j]==2:
                        if tabuleiro[i][j]==9:
                            return True
            return False
        
    def botao_pesado(bloco,tabuleiro):                                   #Verificar se a condição para ativar o bloco é cumprida (se sim mostra o caminho oculto)
            for i in range (len(bloco)):
                for j in range (len(bloco[i])):
                    if bloco[i][j]==2:
                        if tabuleiro[i][j]==5:
                            for h in lista_ponte:
                                tabuleiro[h[0]][h[1]]=1
                                tabuleiro[i][j]=6
            return True
        
    def chao_vidro(bloco,tabuleiro):                                    #Verificar se o bloco está "em pé" num chão de vidro 
            for i in range (len(bloco)):
                for j in range (len(bloco[i])):
                    if bloco[i][j]==2:
                        if tabuleiro[i][j]==4:
                            return False
            return True
            
            
    def move_vertical(bloco,tabuleiro,direcao):                  #Movimento para quando o bloco está de pé
            for i in range(len(tabuleiro)):
                for j in range(len(tabuleiro[i])):
                    if bloco[i][j] == 2:
                        if direcao == "w":
                            bloco[i-1][j] = 3
                            bloco[i-2][j] = 3
                            bloco[i][j] = 1
                            return bloco
                        elif direcao == "s":
                            bloco[i+1][j] = 3
                            bloco[i+2][j] = 3
                            bloco[i][j] = 1
                            return bloco
                        elif direcao == "a":
                            bloco[i][j-1] = 3
                            bloco[i][j-2] = 3
                            bloco[i][j] = 1
                            return bloco
                        elif direcao == "d":
                            bloco[i][j+1] = 3
                            bloco[i][j+2] = 3
                            bloco[i][j] = 1
                            return bloco
        
    def move_horizontal_1(bloco,tabuleiro,direcao): #Deitado na vertical
            for i in range(len(tabuleiro)):
                for j in range(len(tabuleiro[i])):
                    if bloco[i][j]==3:
                        if direcao == "w":
                            bloco[i-1][j]=2
                            bloco[i][j]=1
                            bloco[i+1][j]=1
                            atualizar_vencedor(bloco,tabuleiro)
                            botao_pesado(bloco,tabuleiro)
                            return bloco
                        elif direcao == "s":
                            bloco[i+2][j]=2
                            bloco[i+1][j]=1
                            bloco[i][j]=1
                            atualizar_vencedor(bloco,tabuleiro)
                            botao_pesado(bloco,tabuleiro)
                            return bloco
                        elif direcao == "a":
                            bloco[i][j-1]=3
                            bloco[i+1][j-1]=3
                            bloco[i][j]=1
                            bloco[i+1][j]=1
                            return bloco
                        elif direcao == "d":
                            bloco[i][j+1]=3
                            bloco[i+1][j+1]=3
                            bloco[i][j]=1
                            bloco[i+1][j]=1
                            return bloco
            
    def move_horizontal_2(bloco,tabuleiro,direcao): #Deitado na horizontal
            for i in range(len(tabuleiro)):
                for j in range(len(tabuleiro[i])):
                    if bloco[i][j]==3:
                        if direcao == "w":
                            bloco[i-1][j]=3
                            bloco[i-1][j+1]=3
                            bloco[i][j]=1
                            bloco[i][j+1]=1
                            return bloco
                        elif direcao == "s":
                            bloco[i+1][j]=3
                            bloco[i+1][j+1]=3
                            bloco[i][j]=1
                            bloco[i][j+1]=1
                            return bloco
                        elif direcao == "a":
                            bloco[i][j-1]=2
                            bloco[i][j]=1
                            bloco[i][j+1]=1
                            atualizar_vencedor(bloco,tabuleiro)
                            botao_pesado(bloco,tabuleiro)
                            return bloco
                        elif direcao == "d":
                            bloco[i][j+2]=2
                            bloco[i][j+1]=1
                            bloco[i][j]=1
                            atualizar_vencedor(bloco,tabuleiro)
                            botao_pesado(bloco,tabuleiro)
                            return bloco
        
    def ver_move_vertical(bloco,tabuleiro,direcao):                  #Verifica se é possivel fazer esse movimento
            for i in range(len(tabuleiro)):
                for j in range(len(tabuleiro[i])):
                    if bloco[i][j] == 2:
                        if direcao == "w":
                            if tabuleiro[i-1][j] == 0 or tabuleiro[i-2][j]==0:
                                return False
                            else:
                                return True
                        elif direcao == "s":
                            if tabuleiro[i+1][j] == 0 or tabuleiro[i+2][j]==0:
                                return False
                            else:
                                return True
                        elif direcao == "a":
                            if tabuleiro[i][j-1] == 0 or tabuleiro[i][j-2]==0:
                                return False
                            else:
                                return True
                        elif direcao == "d":
                            if tabuleiro[i][j+1] == 0 or tabuleiro[i][j+2]==0:
                                return False
                            else:
                                return True
            return False
        
    def ver_move_horizontal_1(bloco,tabuleiro,direcao): 
            for i in range(len(tabuleiro)):
                for j in range(len(tabuleiro[i])):
                    if bloco[i][j]==3:
                        if direcao == "w":
                            if tabuleiro[i-1][j]==0:
                                return False
                            else:
                                return True
                        elif direcao == "s":
                            if tabuleiro[i+2][j]==0:
                                return False
                            else:
                                return True
                        elif direcao == "a":
                            if tabuleiro[i][j-1]==0 or tabuleiro[i+1][j-1]==0:
                                return False
                            else:
                                return True
                        elif direcao == "d":
                            if tabuleiro[i][j+1]==0 or tabuleiro[i+1][j+1]==0:
                                return False
                            else:
                                return True
            return False
            
    def ver_move_horizontal_2(bloco,tabuleiro,direcao):
            for i in range(len(tabuleiro)):
                for j in range(len(tabuleiro[i])):
                    if bloco[i][j]==3:
                        if direcao == "w":
                            if tabuleiro[i-1][j]==0 or tabuleiro[i-1][j+1]==0:
                                return False
                            else:
                                return True
                        elif direcao == "s":
                            if tabuleiro[i+1][j]==0 or tabuleiro[i+1][j+1]==0:
                                return False
                            else:
                                return True
                        elif direcao == "a":
                            if tabuleiro[i][j-1]==0:
                                return False
                            else:
                                return True
                        elif direcao == "d":
                            if tabuleiro[i][j+2]==0:
                                return False
                            else:
                                return True
            return False
        
    def estado_bloco(bloco,tabuleiro):                    #Avalia o estado do bloco para saber qual movimento usar
            for i in range (len(tabuleiro)):
                for j in range (len(tabuleiro[i])):
                    if bloco[i][j]==2:
                        return "Vertical"
                    elif bloco[i][j]==3:
                        if bloco[i][j+1]==3:
                            return "Horizontal2"
                        else:
                            return "Horizontal1"
                        
                        
    def start(bloco,tabuleiro):
            movimentos=0                              #Contador dos movimentos
            
            pygame.init()                             #Inicia o pygame
            tela = pygame.display.set_mode((Largura, Altura))   #Abre a janela comas dimensões
            pygame.display.set_caption("Jogo")        #Altera o nome da janela
            clock = pygame.time.Clock()               #Não sei bem o que isto faz mas está lá no moodle
            
            font=pygame.font.SysFont(None,25)         #Fonte para escrever o fim de jogo e vitoria
            
            fimdejogo=False                           #Necessário para terminar o jogo
                    
            tela.fill(COR_TABULEIRO)                  #Preenche a tela com a COR_TABULEIRO (que é azul)
            
            posicao_inicial(bloco,tabuleiro)              #Atualiza a posição inicial na matriz do bloco  
            
            while True:
                for lin in range(1,Num_linhas-1):
                    for col in range(Num_colunas):
                        
                        #Desenha os traços brancos à volta dos quadrados (basicamente é a grelha)
                        if tabuleiro[lin][col] !=0:
                            pygame.draw.rect(tela, (255,255,255), (int(col * Tamanho_celula + Tamanho_celula)-5, int(lin * Tamanho_celula + Tamanho_celula/ 2)-5, 55,55))
                        
                        cor = COR_TABULEIRO #Começa com azul porque caso seja 0 na matriz para pintar de azul
                        
                        if tabuleiro[lin][col] == 9:          #Pinta de amarelo caso seja a meta
                            cor= META
                        if tabuleiro[lin][col] == 1 or tabuleiro[lin][col] == 2:     #  Pinta de preto caso seja 1 (Tambem coloquei o 2 para atualizar 
                            cor= QUADRADO_PRETO                                                            #  senão ficava sempre um retangulo vermelho na posição inicial)
                        if tabuleiro[lin][col] == 5:         #Pinta da cor do botão desativado
                            cor= BOTAO
                        if tabuleiro[lin][col] == 6:         #Pinta da cor do botão ativo
                            cor= BOTAO_ATIVO
                        if tabuleiro[lin][col] == 4:         #Pinta da cor do chao de vidro
                            cor= VIDRO
                        
                        pygame.draw.rect(tela, cor, (int(col * Tamanho_celula + Tamanho_celula), int(lin * Tamanho_celula + Tamanho_celula/ 2), 45,45))
                cor= RETANGULO
                for lin in range(1,Num_linhas-1):
                    for col in range(Num_colunas):
                        #Quando está de pé
                        if bloco[lin][col] == 2:            
                            pygame.draw.rect(tela, cor, (int(col * Tamanho_celula + Tamanho_celula), int(lin * Tamanho_celula + Tamanho_celula/ 2), 45,45))
                        #Quando está deitado vertical
                        if bloco[lin][col] == 3 and bloco[lin+1][col]==3:
                            pygame.draw.rect(tela, cor, (int(col * Tamanho_celula + Tamanho_celula), int(lin * Tamanho_celula + Tamanho_celula/ 2), 45,95))
                        #Quando está deitado horizontal
                        if bloco[lin][col] == 3 and bloco[lin][col+1]==3:
                            pygame.draw.rect(tela, cor, (int(col * Tamanho_celula + Tamanho_celula), int(lin * Tamanho_celula + Tamanho_celula/ 2), 95,45))

                while fimdejogo:                             #Para poder terminar o jogo quando o jogador tenta mover o bloco para o vazio
                    tela.fill((255,255,255))
                    texto=font.render("Fim de jogo, clique S para sair",True,(255,0,0))
                    tela.blit(texto, (int(Largura / 2 - texto.get_width() / 2), int(Altura / 2 - texto.get_height() / 2)))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            exit()
                            fimdejogo=False
                        if event.type == pygame.KEYDOWN:
                            if event.key ==pygame.K_s:      #Clicar S para sair do jogo e fechá-lo
                                menu.main_menu()
                                exit()
                                fimdejogo=False        
                
                if atualizar_vencedor(bloco,tabuleiro):            #Tela de vitória
                    tela.fill((255,255,255))
                    texto1=font.render("Vitória!!",True,(0,0,0))
                    texto2=font.render(f"Movimentos: {movimentos}", True, (0,0,0))
                    texto3=font.render("Clique S para sair",True,(0,0,0))
                    tela.blit(texto1, (int(Largura / 2 - texto1.get_width() / 2), int(Altura / 9 - texto1.get_height() / 2)))
                    tela.blit(texto2, (int(Largura / 2 - texto2.get_width() / 2), int(Altura / 6 - texto2.get_height() / 2)))
                    tela.blit(texto3, (int(Largura / 2 - texto3.get_width() / 2), int(Altura / 3 - texto3.get_height() / 2)))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key ==pygame.K_s:
                                menu.main_menu()
                                exit()
                
                botao_pesado(bloco,tabuleiro)            # Vê se o bloco cumpre os requisitos para ativar o botão
                
                estado = estado_bloco(bloco,tabuleiro)   # Atualiza o estado do bloco
                
                atualiza_fimjogo=chao_vidro(bloco,tabuleiro)        #Chao de vidro
                if atualiza_fimjogo==False:
                    fimdejogo=True
                
                for event in pygame.event.get():
                    if event.type == QUIT:           #Terminar o jogo quando o jogador clica no X
                        pygame.quit()                #Encerra o pygame
                        exit()                       #Encerra o programa
                    if event.type == KEYDOWN:
                        movimentos+=1
                        if event.key == K_w:
                            if estado == "Vertical":
                                if ver_move_vertical(bloco,tabuleiro,"w"):     #Verifica se é possível exxecutar esse movimento
                                    move_vertical(bloco,tabuleiro,"w")         #Se for, ele executa
                                    nova=copy.deepcopy(bloco)
                                    historico.append(nova)
                                else:
                                    fimdejogo=True
                                pprint(bloco)
                            elif estado == "Horizontal1":
                                if ver_move_horizontal_1(bloco,tabuleiro,"w"):
                                    move_horizontal_1(bloco,tabuleiro,"w")
                                    nova=copy.deepcopy(bloco)
                                    historico.append(nova)
                                else:
                                    fimdejogo=True
                                pprint(bloco)
                            elif estado == "Horizontal2":
                                if ver_move_horizontal_2(bloco,tabuleiro,"w"):
                                    move_horizontal_2(bloco,tabuleiro,"w")
                                    nova=copy.deepcopy(bloco)
                                    historico.append(nova)
                                else:
                                    fimdejogo=True
                                pprint(bloco)
                        elif event.key == K_s:
                            if estado == "Vertical":
                                if ver_move_vertical(bloco,tabuleiro,"s"):
                                    move_vertical(bloco,tabuleiro,"s")
                                    nova=copy.deepcopy(bloco)
                                    historico.append(nova)
                                else:
                                    fimdejogo=True
                                pprint(bloco)
                            elif estado == "Horizontal1":
                                if ver_move_horizontal_1(bloco,tabuleiro,"s"):
                                    move_horizontal_1(bloco,tabuleiro,"s")
                                    nova=copy.deepcopy(bloco)
                                    historico.append(nova)
                                else:
                                    fimdejogo=True
                                pprint(bloco)
                            elif estado == "Horizontal2":
                                if ver_move_horizontal_2(bloco,tabuleiro,"s"):
                                    move_horizontal_2(bloco,tabuleiro,"s")
                                    nova=copy.deepcopy(bloco)
                                    historico.append(nova)
                                else:
                                    fimdejogo=True
                                pprint(bloco)
                        elif event.key == K_a:
                            if estado == "Vertical":
                                if ver_move_vertical(bloco,tabuleiro,"a"):
                                    move_vertical(bloco,tabuleiro,"a")
                                    nova=copy.deepcopy(bloco)
                                    historico.append(nova)
                                else:
                                    fimdejogo=True
                                pprint(bloco)
                            elif estado == "Horizontal1":
                                if ver_move_horizontal_1(bloco,tabuleiro,"a"):
                                    move_horizontal_1(bloco,tabuleiro,"a")
                                    nova=copy.deepcopy(bloco)
                                    historico.append(nova)
                                else:
                                    fimdejogo=True
                                pprint(bloco)
                            elif estado == "Horizontal2":
                                if ver_move_horizontal_2(bloco,tabuleiro,"a"):
                                    move_horizontal_2(bloco,tabuleiro,"a")
                                    nova=copy.deepcopy(bloco)
                                    historico.append(nova)
                                else:
                                    fimdejogo=True
                                pprint(bloco)
                        elif event.key == K_d:
                            if estado == "Vertical":
                                if ver_move_vertical(bloco,tabuleiro,"d"):
                                    move_vertical(bloco,tabuleiro,"d")
                                    nova=copy.deepcopy(bloco)
                                    historico.append(nova)
                                else:
                                    fimdejogo=True
                                pprint(bloco)
                            elif estado == "Horizontal1":
                                if ver_move_horizontal_1(bloco,tabuleiro,"d"):
                                    move_horizontal_1(bloco,tabuleiro,"d")
                                    nova=copy.deepcopy(bloco)
                                    historico.append(nova)
                                else:
                                    fimdejogo=True
                                pprint(bloco)
                            elif estado == "Horizontal2":
                                if ver_move_horizontal_2(bloco,tabuleiro,"d"):
                                    move_horizontal_2(bloco,tabuleiro,"d")
                                    nova=copy.deepcopy(bloco)
                                    historico.append(nova)
                                else:
                                    fimdejogo=True
                                pprint(bloco)                
                
                pygame.display.flip()
                



    start(bloco,tabuleiro)