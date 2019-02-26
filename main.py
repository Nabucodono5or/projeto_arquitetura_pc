from monitoramento import cpu
from monitoramento import memory
from monitoramento import disks

tempo = int(input("Entrada de tempo: "))
print('Processador: ', cpu.nome_cpu())
print('Velocidade: {} GHz'.format(cpu.frequencia()))
print('Cores : ', cpu.cores())
print("Cores fìsicos: ", cpu.cores_fisicos())
print("Total  de memória: ", memory.total_gb(), "GB")
print("Total de disco em uso: ", disks.total_gb(), "GB")
print("Total de espaço livre: ", disks.livre_gb(), "GB")
print()
print("___________________")

def imprimir_consumo(t):
    for x in range(t):
        print("Consumo da CPU: ", round(cpu.consumo_cpu_porcentagem_formatado(), 1), "%")
        # print("Livre :", round(cpu.cpu_livre_porcentagem()), "%")
        print("Consumo da memória: ", memory.porcentagem(), "%")
        print("Consumo de disco: ", disks.porcentagem_de_uso(), "%")
        print("_________________")

if tempo >= 1:
    imprimir_consumo(tempo)