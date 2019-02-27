import pygame
from pygame import Surface

largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption("Monitoramento de estado do PC")
pygame.display.init()

azul = (0, 0, 255)

s1 = Surface((largura_tela, altura_tela/3))
s2 = Surface((largura_tela, altura_tela/3))
s3 = Surface((largura_tela, altura_tela/3))

clock = pygame.time.Clock()

terminou = False

while not terminou:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True


    pygame.display.update()
    clock.tick(60)

pygame.display.quit()