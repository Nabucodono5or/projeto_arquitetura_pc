import psutil

# modulo de operaçoes para cheque da cpu

def frequencia():
    return psutil.cpu_freq()
