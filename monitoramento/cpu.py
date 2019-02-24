import psutil
import platform
import os


# modulo de operaçoes para cheque da cpu

def frequencia():
    return psutil.cpu_freq().max / 1000


def nome_cpu():
    if sistema_operacional() == 'Linux':
        return busca_info_arq()
    return platform.processor()


def sistema_operacional():
    return os.uname().sysname


def busca_info_arq():
    with open('/proc/cpuinfo') as f:
        for line in f:
            if line.strip():
                if line.rstrip('\n').startswith('model name'):
                    model_name = line.rstrip('\n').split(':')[1]
                    model = model_name
                    model = model.strip()
                    break
    return model + " " + platform.processor()


def cores():
    return psutil.cpu_count()


def cores_fisicos():
    return psutil.cpu_count(logical=False)


def consumo_cpu_percentagem():
    return psutil.cpu_times_percent(interval=1)


def consumo_cpu_porcentagem_formatado():
    consumo = consumo_cpu_percentagem()
    return consumo.user + consumo.system


def cpu_livre_porcentagem():
    return consumo_cpu_percentagem().idle
