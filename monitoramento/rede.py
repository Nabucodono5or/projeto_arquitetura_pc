import psutil
import socket

rede_cabeada = psutil.net_if_addrs()
socket_connections = psutil.net_connections(kind='inet')


# específica para eth0
def ip_adress():
    return rede_cabeada['enp2s0'][0][1]


# qualquer tipo de interface de rede
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
