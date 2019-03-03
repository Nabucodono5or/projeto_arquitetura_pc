
'''
    ** versão de uso do terminal como display e entrada de controle da visualição  
'''

from monitoramento import cpu
from monitoramento import memory
from monitoramento import disks
from monitoramento import rede


def imprimir_info_cpu():
    print()
    print("___________________")
    print("CPU")
    print('Processador: ', cpu.nome_cpu())
    print('Arquitetura: ', cpu.arquitetura())
    print('Palavra: ', cpu.palavra(), 'bits')
    print('Velocidade: {} GHz'.format(cpu.frequencia()))
    print('Cores (físicos): ', cpu.cores(), '(', cpu.cores_fisicos(), ')')
    print("Consumo atual da CPU: ", round(cpu.consumo_cpu_porcentagem_formatado(), 1), "%")
    print()
    print("___________________")
    print()


def imprimir_info_memoria():
    print()
    print("___________________")
    print("MEMÓRIA")
    print("Total  de memória: ", memory.total_gb(), "GB")
    print("Total de memória swap: ", memory.memoria_swap(), "GB")
    print("Memória swap usada: ", memory.memoria_swap_usada(), "GB")
    print("Consumo atual da memória: ", memory.porcentagem(), "%")
    print("___________________")
    print()


def imprimir_info_disco():
    print()
    print("___________________")
    print("DISCO")
    print("Total do disco: ", disks.total_gb(), "GB")
    print("Total de disco em uso: ", disks.usado_gb(), "GB")
    print("Total de espaço livre em disco: ", disks.livre_gb(), "GB")
    print("Consumo atual do disco: ", disks.porcentagem_de_uso(), "%")
    print("___________________")
    print()

def imprimir_info_rede():
    print()
    print("___________________")
    print("REDE")
    print("Endereço IP: ", rede.ip_adress())
    print("___________________")
    print()

def iniciar_app():
    quit = False

    while not quit:
        print("MONITORAMENTO DE COMPUTADOR")
        print(" --- escreva cpu para informações sobre cpu;")
        print(" --- escreva disco para informações sobre disco;")
        print(" --- escreva mem/memoria para informações sobre memória;")
        print(" --- escreva ip para informações sobre Rede;")
        print(" --- escreva resumo/t para informações resumidas;")
        print(" --- Escreva q/quit para sair;")
        print()
        resultado = input("Entre com a informação que você queira: ")

        if resultado == "cpu" :
            imprimir_info_cpu()
        elif resultado == "mem" or resultado == "memoria" :
            imprimir_info_memoria()
        elif resultado == "disco" :
            imprimir_info_disco()
        elif resultado == "ip" :
            imprimir_info_rede()
        elif resultado == "q" or "quit" :
            quit = True


if __name__ == '__main__':
    iniciar_app()
