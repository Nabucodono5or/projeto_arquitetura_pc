
'''
    ** versão de uso do terminal como display e entrada de controle da visualição  
'''

from monitoramento import cpu
from monitoramento import memory
from monitoramento import disks
from monitoramento import rede


# tempo = int(input("Entrada de tempo: "))
print('Processador: ', cpu.nome_cpu())
print('Arquitetura: ', cpu.arquitetura())
print('Palavra: ', cpu.palavra(), 'bits')
print('Velocidade: {} GHz'.format(cpu.frequencia()))
print('Cores (físicos): ', cpu.cores(), '(', cpu.cores_fisicos(), ')')
print("___________________")


print("Total  de memória: ", memory.total_gb(), "GB")
print("Total de memória swap: ", memory.memoria_swap(), "GB")
print("Memória swap usada: ", memory.memoria_swap_usada(), "GB")
print("___________________")

print("Total do disco: ", disks.total_gb(), "GB")
print("Total de disco em uso: ", disks.usado_gb(), "GB")
print("Total de espaço livre em disco: ", disks.livre_gb(), "GB")
print("___________________")

print("Endereço IP: ", rede.ip_adress())
# print()
print("___________________")


# def imprimir_consumo(t):
#     for x in range(t):
#         print("Consumo atual da CPU: ", round(cpu.consumo_cpu_porcentagem_formatado(), 1), "%")
#         # print("Livre :", round(cpu.cpu_livre_porcentagem()), "%")
#         print("Consumo atual da memória: ", memory.porcentagem(), "%")
#         print("Consumo atual do disco: ", disks.porcentagem_de_uso(), "%")
#         print("_________________")


# if tempo >= 1:
#     imprimir_consumo(tempo)





#
# if __name__ == '__main__':
#     iniciar_app()
