import pygame
import sys
from random import randint
from time import sleep
import os
import pygame.font
pygame.init()
largura = 882
altura = 513

tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

musica_de_fundo= pygame.mixer.music.load("musicadefundo.ogg")
pygame.mixer.music.play(-1)

pontos = 0
fonte= pygame.font.SysFont('arial',40,True, True)

fundo = pygame.image.load("QuadroNegro.jpg")
fruta1 = pygame.image.load("banana(1).png")
fruta2 = pygame.image.load("goiaba (1).png")
fruta3 = pygame.image.load("laranja.png")
fruta4 = pygame.image.load("pera (1).png")
fruta5 = pygame.image.load("uva (1).png")

palavra1 = pygame.image.load("banana.png")
palavra2 = pygame.image.load("goiaba.png")
palavra3 = pygame.image.load("laranj.png")
palavra4 = pygame.image.load("pera.png")
palavra5 = pygame.image.load("uva.png")
palavra6 = pygame.image.load("abacate(1).png")
palavra7 = pygame.image.load("maça (2).png")
Alfaletrar = pygame.image.load("Alfaletrar.png")
branco = (255, 255, 255)
preto = (0, 0, 0)

posicaoX = 200
posicaoY = 280
movimentoX = 0
movimentoY = 0
velocidade = 5
roleta = [fruta1,fruta2,fruta3,fruta4,fruta5]
palavraselecao = [palavra1, palavra2,palavra3,palavra4]
palavraselecao2 = [palavra5, palavra6,palavra7]
indice = 0

Alfaletrarlargura = 936
Alfaletraraltura = 542
AlfaletrarPosicaoX = 360
AlfaletrarPosicaoY = 10
velocidadeaAlfaletrar = 5
def clicoubotao(x, y, posxmaior, posxmenor, posymaior, posymenor):
    if posxmaior > x > posxmenor and posymaior > y > posymenor:
        clicoubotao = True
        return clicoubotao

def clicoupalavra(condicao, palavraselecao, posx, posy):
    if condicao == True:
        mostrartela((f'{palavraselecao}press.png'), posx, posy)
        condicao = False
        return condicao
    else:
        mostrartela(tela, carregarimagem(f'{roleta}.png'), posx-6, posy)
    if clicoupalavra == roleta[indice]:
        print('Você acertou!')
        pontos = pontos + 1
def dead():
    pygame.font.init()
    font = pygame.font.SysFont(None, 150)
    texto = font_perdeu.render("Você Perdeu!", True, (255,255, 255))
    tela.blit(texto, (100, 200))
    pygame.display.update()
    time.sleep(5)
contador = 0

def roleta1():
    pygame.font.init()
    font = pygame.font.get_default_font()
    font = pygame.font.SysFont(font, 60)
    text = font_ADIVINHE.render("ADIVINHE O NOME DA FRUTA: ", True, (255,255,255))
    textRect = text.get_rect()
    textRect.center = (472, 100)
    tela.blit(text, (150,150))
    pygame.display.update()

def sortearfruta(fazer):
    global indice
    if fazer == True:
        indice = randint(0, len(roleta) - 1)
    fruta = roleta[indice]
    tela.blit(fruta, (350, 100))
    pygame.display.update()

sortear = True

def carregarimagens(lista):
    x=30
    for i in lista:
        tela.blit(i, (x, 300))
        x=x+212
def carregarimagens2(lista):
    x=30
    for i in lista:
        tela.blit(i, (x, 375))
        x=x+212
    
running = True
while (running):
    # função fill define a cor de fundo da tela
    tela.fill(branco)
    tela.blit(fundo, (0, 0))
    carregarimagens(palavraselecao)
    carregarimagens2(palavraselecao2)
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    escolher = " Adivinhe o nome da fruta: "
    escolher_formatado = fonte.render(escolher, True, (255,255,255))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if clicoubotao(x, y, 901, 864, 537, 498):
                        clicou += 1
                    if clicoubotao(x, y, 415, 270, 467, 402):
                        clicouplay = 2
                        
                    if  clicoubotao(x, y, 679, 530, 460, 405):
                        
                        clicouexit = 2
            
        
    
    sortearfruta(sortear)
    sortear = False
    condicao = True
    condicao = False
    
    tela.blit(texto_formatado,(50,430))
    tela.blit(escolher_formatado,(265,50))
    pygame.display.update()
    relogio.tick(60)
