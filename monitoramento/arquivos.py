import os


def listar_arquivos():
    lista = os.listdir()
    arquivos = {}

    # tipo, tamanho, data de criação
    for i in lista:
        arquivos[i] = []
        if os.path.isfile(i):
            arquivos[i].append("Arquivo")
        else:
            arquivos[i].append("Diretório")

        arquivos[i].append(os.stat(i).st_size)
        arquivos[i].append(os.stat(i).st_atime)

    return arquivos
