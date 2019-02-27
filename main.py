from monitoramento import cpu
from monitoramento import memory
from monitoramento import disks
from monitoramento import rede

tempo = int(input("Entrada de tempo: "))
print('Processador: ', cpu.nome_cpu())
print('Velocidade: {} GHz'.format(cpu.frequencia()))
print('Cores : ', cpu.cores())
print("Cores fìsicos: ", cpu.cores_fisicos())
print("Total  de memória: ", memory.total_gb(), "GB")
print("Total do disco: ", disks.total_gb(), "GB")
print("Total de disco em uso: ", disks.usado_gb(), "GB")
print("Total de espaço livre em disco: ", disks.livre_gb(), "GB")
print("Informações de rede: ", rede.ip_adress())
print()
print("___________________")


def imprimir_consumo(t):
    for x in range(t):
        print("Consumo atual da CPU: ", round(cpu.consumo_cpu_porcentagem_formatado(), 1), "%")
        # print("Livre :", round(cpu.cpu_livre_porcentagem()), "%")
        print("Consumo atual da memória: ", memory.porcentagem(), "%")
        print("Consumo atual do disco: ", disks.porcentagem_de_uso(), "%")
        print("_________________")


if tempo >= 1:
    imprimir_consumo(tempo)
