import psutil

disco = psutil.disk_usage('.')
fator_gb = 1024 * 1024 * 1024
fator_mb = 1024 * 1024

'''
    valores em MB
'''


def total_mb():
    return round(disco.total / fator_mb)


def usado_mb():
    return round(disco.used / fator_mb)


def livre_mb():
    return round(disco.free / fator_mb)


'''
    valores em GB
'''


def total_gb():
    return round(disco.total / fator_gb)


def usado_gb():
    return round(disco.used / fator_gb)


def livre_gb():
    return round(disco.free / fator_gb)


'''
    valor em porcentagem
'''


def porcentagem_de_uso():
    return disco.percent
