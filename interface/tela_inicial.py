import pygame
from pygame import Surface
from monitoramento import memory
from monitoramento import cpu
from monitoramento import disks
from monitoramento import rede

azul = (0, 0, 255)
vermelho = (255, 0, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)

largura_tela = 800
altura_tela = 600

pygame.font.init()
font = pygame.font.Font(None, 35)

tela = pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption("Monitoramento de estado do PC")

def info_display(t):
    texto_processador = str(cpu.nome_cpu())
    texto_cores = "Cores: " + cpu.cores()
    texto_rede = "IP Adress: " + rede.get_ip_address()
    texto_resultado = texto_processador + "/n" + texto_cores + "/n" + texto_rede
    texto_resultado = font.render(texto_resultado, 1, branco)
    t.blit(texto_resultado, (20, 10))

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
    tela.blit(t, (0, 2*altura_tela/3))


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
    tela.blit(t, (0, altura_tela/3))


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
    tela.blit(t, (0, 0))

pygame.display.init()


s1 = Surface((largura_tela, altura_tela/3))
s2 = Surface((largura_tela, altura_tela/3))
s3 = Surface((largura_tela, altura_tela/3))

clock = pygame.time.Clock()
contador = 60

terminou = False

while not terminou:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    if contador == 60:

        memoria_display(s1)
        cpu_display(s2)
        disks_display(s3)
        contador = 0

    pygame.display.update()
    clock.tick(60)
    contador = contador + 1

pygame.display.quit()