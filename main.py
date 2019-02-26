from monitoramento import cpu
from monitoramento import memory

tempo = int(input("Entrada de tempo: "))
print('Processador: ', cpu.nome_cpu())
print('Velocidade: {} GHz'.format(cpu.frequencia()))
print('Cores : ', cpu.cores())
print("Cores fìsicos: ", cpu.cores_fisicos())
print()
print("___________________")

def imprimir_consumo(t):
    for x in range(t):
        print("Consumo da CPU: ", round(cpu.consumo_cpu_porcentagem_formatado(), 1), "%")
        # print("Livre :", round(cpu.cpu_livre_porcentagem()), "%")
        print("Consumo da memória: ", memory.porcentagem(), "%")
        print("_________________")

if tempo >= 1:
    imprimir_consumo(tempo)