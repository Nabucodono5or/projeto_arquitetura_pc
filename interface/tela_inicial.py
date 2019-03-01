import pygame
from pygame import Surface
from monitoramento import memory
from monitoramento import cpu
from monitoramento import disks
from monitoramento import rede

azul = (246, 244, 243)
vermelho = (236, 11, 67)
preto = (84, 151, 167)
branco = (248, 241, 255)

largura_tela = 800
altura_tela = 600

pygame.font.init()
font = pygame.font.Font(None, 35)

tela = pygame.display.set_mode((largura_tela,altura_tela))
tela.fill(preto)
pygame.display.set_caption("Monitoramento de estado do PC")

def info_display(t):
    # larg = largura_tela - 2 * 20
    # pygame.draw.rect(t, preto, (20, 20, larg, 70))
    t.fill(preto)
    texto_processador = str(cpu.nome_cpu())
    texto_cores = "Cores: " + str(cpu.cores())
    texto_rede = "Endereço IP: " + str(rede.get_ip_address())

    texto_final = font.render(texto_processador, True, branco)
    t.blit(texto_final, (20, 10))

    texto_final = font.render(texto_cores, True, branco)
    t.blit(texto_final, (20, 40))

    texto_final = font.render(texto_rede, True, branco)
    t.blit(texto_final, (20, 70))

    tela.blit(t, (0, 10))

def disks_display(t):
    d = disks.porcentagem_de_uso()
    larg = largura_tela - 2*20
    t.fill(preto)
    pygame.draw.rect(t, azul, (20, 50, larg, 70))
    larg = larg * d/100
    pygame.draw.rect(t, vermelho, (20, 50, larg, 70))
    total = disks.total_gb()
    texto_titulo = "Consumo de Disco ( Total: " + str(total) + " GB):"
    texto_final = font.render(texto_titulo, 1, branco)
    t.blit(texto_final, (20, 10))
    tela.blit(t, (0, 3*altura_tela/4))


def cpu_display(t):
    procss = cpu.consumo_cpu_porcentagem_formatado()
    larg = largura_tela - 2*20
    t.fill(preto)
    pygame.draw.rect(t, azul, (20, 50, larg, 70))
    larg = larg * procss/100
    pygame.draw.rect(t, vermelho, (20, 50, larg, 70))
    total = cpu.frequencia()
    texto_titulo = "Consumo de cpu ( Frequencia: " + str(total) + " GHz):"
    texto_final = font.render(texto_titulo, 1, branco)
    t.blit(texto_final, (20, 10))
    tela.blit(t, (0, altura_tela/4))


def memoria_display(t):
    mem = memory.porcentagem()
    larg = largura_tela - 2*20
    t.fill(preto)
    pygame.draw.rect(t, azul, (20, 50, larg, 70))
    larg = larg * mem/100
    pygame.draw.rect(t, vermelho, (20, 50, larg, 70))
    total = memory.total_gb()
    texto_titulo = "Consumo de memoria ( Total: " + str(total) + " GB):"
    texto_final = font.render(texto_titulo, 1, branco)
    t.blit(texto_final, (20, 10))
    tela.blit(t, (0, 2*altura_tela/4))

def iniciar_app():
    pygame.display.init()

    s0 = Surface((largura_tela, altura_tela/4))
    s1 = Surface((largura_tela, altura_tela/4))
    s2 = Surface((largura_tela, altura_tela/4))
    s3 = Surface((largura_tela, altura_tela/4))

    clock = pygame.time.Clock()
    contador = 60

    terminou = False

    while not terminou:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True

        if contador == 60:
            info_display(s0)
            memoria_display(s1)
            cpu_display(s2)
            disks_display(s3)
            contador = 0

        pygame.display.update()
        clock.tick(60)
        contador = contador + 1

    pygame.display.quit()

iniciar_app()