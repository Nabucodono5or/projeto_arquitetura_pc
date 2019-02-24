import psutil
import platform
import os

# modulo de operaçoes para cheque da cpu

def frequencia():
    return round((psutil.cpu_freq().max/1000), 1)

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
    return model