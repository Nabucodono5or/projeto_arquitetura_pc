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
font_info = pygame.font.Font(None, 24)

tela = pygame.display.set_mode((largura_tela,altura_tela))
tela.fill(preto)
pygame.display.set_caption("Monitoramento de estado do PC")

def menu_display(t):
    t.fill(preto)
    mostra_texto(t, "Digite 1 para informações da CPU.", 10)
    mostra_texto(t, "Digite 2 para informações de MEMÓRIA.", 30)
    mostra_texto(t, "Digite 3 para informações de DISCO.", 50)
    mostra_texto(t, "Digite 4 para informações da REDE.", 70)

    tela.blit(t, (0, 10))


def mostra_texto(t, texto, pos_y):
    texto_final = font_info.render(texto, True, branco)
    t.blit(texto_final, (10, pos_y))

def info_cpu_display(t):
    t.fill(preto)

    mostra_texto(t, "Processador: "+ str(cpu.nome_cpu()), 10)
    mostra_texto(t, "Arquitetura: " + str(cpu.arquitetura()), 30)
    mostra_texto(t, "Palavra: " + str(cpu.palavra()) + "bits", 50)
    mostra_texto(t, "Velocidade: {} GHz".format(cpu.frequencia()), 70)
    mostra_texto(t, "Cores (Físicos): {} ({})".format(cpu.cores(), cpu.cores_fisicos()), 90)

    tela.blit(t, (0, altura_tela/3))

# def info_display(t):
#     # larg = largura_tela - 2 * 20
#     # pygame.draw.rect(t, preto, (20, 20, larg, 70))
#     t.fill(preto)
#     texto_processador = str(cpu.nome_cpu())
#     texto_cores = "Cores: " + str(cpu.cores())
#     texto_rede = "Endereço IP: " + str(rede.get_ip_address())
#
#     texto_final = font.render(texto_processador, True, branco)
#     t.blit(texto_final, (20, 10))
#
#     texto_final = font.render(texto_cores, True, branco)
#     t.blit(texto_final, (20, 40))
#
#     texto_final = font.render(texto_rede, True, branco)
#     t.blit(texto_final, (20, 70))
#
#     tela.blit(t, (0, 10))
#
# def disks_display(t):
#     d = disks.porcentagem_de_uso()
#     larg = largura_tela - 2*20
#     t.fill(preto)
#     pygame.draw.rect(t, azul, (20, 50, larg, 70))
#     larg = larg * d/100
#     pygame.draw.rect(t, vermelho, (20, 50, larg, 70))
#     total = disks.total_gb()
#     texto_titulo = "Consumo de Disco ( Total: " + str(total) + " GB):"
#     texto_final = font.render(texto_titulo, 1, branco)
#     t.blit(texto_final, (20, 10))
#     tela.blit(t, (0, 3*altura_tela/4))
#
#
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
    tela.blit(t, (0, 2*altura_tela/3))


# def memoria_display(t):
#     mem = memory.porcentagem()
#     larg = largura_tela - 2*20
#     t.fill(preto)
#     pygame.draw.rect(t, azul, (20, 50, larg, 70))
#     larg = larg * mem/100
#     pygame.draw.rect(t, vermelho, (20, 50, larg, 70))
#     total = memory.total_gb()
#     texto_titulo = "Consumo de memoria ( Total: " + str(total) + " GB):"
#     texto_final = font.render(texto_titulo, 1, branco)
#     t.blit(texto_final, (20, 10))
#     tela.blit(t, (0, 2*altura_tela/4))

def iniciar_app():
    pygame.display.init()

    s0 = Surface((largura_tela, altura_tela/3))
    s1 = Surface((largura_tela, altura_tela/3))
    s2 = Surface((largura_tela, altura_tela/3))
    # s3 = Surface((largura_tela, altura_tela/4))

    clock = pygame.time.Clock()
    contador = 60

    terminou = False

    while not terminou:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True

        if contador == 60:
            # info_display(s0)
            # memoria_display(s1)
            # cpu_display(s2)
            # disks_display(s3)
            menu_display(s0)
            info_cpu_display(s1)
            cpu_display(s2)
            contador = 0

        pygame.display.update()
        clock.tick(60)
        contador = contador + 1

    pygame.display.quit()


if __name__ == '__main__':
    iniciar_app()