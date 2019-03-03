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

tela = pygame.display.set_mode((largura_tela, altura_tela))
tela.fill(preto)
pygame.display.set_caption("Monitoramento de estado do PC")

'''
    ** Funções de exibições do texto na tela 
'''


def mostra_texto(t, texto, pos_y):
    texto_final = font_info.render(texto, True, branco)
    t.blit(texto_final, (10, pos_y))


def menu_display(t):
    t.fill(preto)

    mostra_texto(t, "Digite 1 para informações da CPU.", 10)
    mostra_texto(t, "Digite 2 para informações de MEMÓRIA.", 30)
    mostra_texto(t, "Digite 3 para informações de DISCO.", 50)
    mostra_texto(t, "Digite 4 para informações da REDE.", 70)
    mostra_texto(t, "Digite 5 para informação RESUMIDA.", 90)

    tela.blit(t, (0, 10))


def info_cpu_display(t):
    t.fill(preto)

    mostra_texto(t, "Processador: {}".format(cpu.nome_cpu()), 10)
    mostra_texto(t, "Arquitetura: {}".format(cpu.arquitetura()), 30)
    mostra_texto(t, "Palavra: {} bits".format(cpu.palavra()), 50)
    mostra_texto(t, "Velocidade: {} GHz".format(cpu.frequencia()), 70)
    mostra_texto(t, "Cores (Físicos): {} ({})".format(cpu.cores(), cpu.cores_fisicos()), 90)

    tela.blit(t, (0, altura_tela / 3))


def info_memoria_display(t):
    t.fill(preto)

    mostra_texto(t, "Total  de memória: {} GB".format(memory.total_gb()), 10)
    mostra_texto(t, "Total de memória swap: {} GB".format(memory.memoria_swap()), 30)
    mostra_texto(t, "Memória swap usada: {} GB".format(memory.memoria_swap_usada()), 50)
    mostra_texto(t, "Consumo atual da memória: {}%".format(memory.porcentagem()), 70)

    tela.blit(t, (0, altura_tela / 3))


def info_disco_display(t):
    t.fill(preto)

    mostra_texto(t, "Total do disco: {} GB".format(disks.total_gb()), 10)
    mostra_texto(t, "Total de disco em uso: {} GB".format(disks.usado_gb()), 30)
    mostra_texto(t, "Total de espaço livre em disco: {} GB".format(disks.livre_gb()), 50)
    mostra_texto(t, "Consumo atual do disco: {}%".format(disks.porcentagem_de_uso()), 70)

    tela.blit(t, (0, altura_tela / 3))


def info_rede_display(t):
    t.fill(preto)

    mostra_texto(t, "Endereço IP: {}".format(rede.get_ip_address()), 10)

    tela.blit(t, (0, altura_tela / 3))


def info_resumo_display(t):
    t.fill(preto)

    mostra_texto(t, "Processador: " + str(cpu.nome_cpu()), 10)
    mostra_texto(t, "Velocidade: {} GHz".format(cpu.frequencia()), 30)
    mostra_texto(t, "Arquitetura do processador: " + str(cpu.arquitetura()), 50)
    mostra_texto(t, "Total  de memória: {} GB".format(memory.total_gb()), 70)
    mostra_texto(t, "Total de memória swap: {} GB".format(memory.memoria_swap()), 90)
    mostra_texto(t, "Total do disco: {} GB".format(disks.total_gb()), 110)
    mostra_texto(t, "Endereço IP: {}".format(rede.get_ip_address()), 130)

    tela.blit(t, (0, altura_tela / 3))


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

'''
    **funções de display gráfico na tela
'''


def disks_display(t):
    d = disks.porcentagem_de_uso()
    larg = largura_tela - 2 * 20
    t.fill(preto)
    pygame.draw.rect(t, azul, (20, 50, larg, 70))
    larg = larg * d / 100
    pygame.draw.rect(t, vermelho, (20, 50, larg, 70))
    total = disks.total_gb()
    texto_titulo = "Consumo de Disco ( Total: " + str(total) + " GB):"
    texto_final = font.render(texto_titulo, 1, branco)
    t.blit(texto_final, (20, 10))
    tela.blit(t, (0, 3 * altura_tela / 4))


def cpu_display(t):
    procss = cpu.consumo_cpu_porcentagem_formatado()
    larg = largura_tela - 2 * 20
    t.fill(preto)
    pygame.draw.rect(t, azul, (20, 50, larg, 70))
    larg = larg * procss / 100
    pygame.draw.rect(t, vermelho, (20, 50, larg, 70))
    total = cpu.frequencia()
    texto_titulo = "Consumo de cpu ( Frequencia: " + str(total) + " GHz):"
    texto_final = font.render(texto_titulo, 1, branco)
    t.blit(texto_final, (20, 10))
    tela.blit(t, (0, 2 * altura_tela / 3))


def memoria_display(t):
    mem = memory.porcentagem()
    larg = largura_tela - 2 * 20
    t.fill(preto)
    pygame.draw.rect(t, azul, (20, 50, larg, 70))
    larg = larg * mem / 100
    pygame.draw.rect(t, vermelho, (20, 50, larg, 70))
    total = memory.total_gb()
    texto_titulo = "Consumo de memoria ( Total: " + str(total) + " GB):"
    texto_final = font.render(texto_titulo, 1, branco)
    t.blit(texto_final, (20, 10))
    tela.blit(t, (0, 2 * altura_tela / 3))


'''
    ** Função de inicio da tela
'''


def iniciar_app():
    pygame.display.init()

    s0 = Surface((largura_tela, altura_tela / 3))
    s1 = Surface((largura_tela, altura_tela / 3))
    s2 = Surface((largura_tela, altura_tela / 3))
    # s3 = Surface((largura_tela, altura_tela/4))

    clock = pygame.time.Clock()
    contador = 60

    terminou = False

    opcao = 1
    while not terminou:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    opcao = 1
                elif event.key == pygame.K_2:
                    opcao = 2
                elif event.key == pygame.K_3:
                    opcao = 3
                elif event.key == pygame.K_4:
                    opcao = 4
                elif event.key == pygame.K_5:
                    opcao = 5

        if contador == 60:
            tela.fill(preto)
            menu_display(s0)

            if opcao == 1:
                info_cpu_display(s1)
                cpu_display(s2)
            elif opcao == 2:
                info_memoria_display(s1)
                memoria_display(s2)
            elif opcao == 3:
                info_disco_display(s1)
                disks_display(s2)
            elif opcao == 4:
                info_rede_display(s1)
            elif opcao == 5:
                info_resumo_display(s1)
            contador = 0

        pygame.display.update()
        clock.tick(60)
        contador = contador + 1

    pygame.display.quit()


if __name__ == '__main__':
    iniciar_app()
