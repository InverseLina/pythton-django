# encoding=utf-8
from socket import *

__author__ = 'Hinsteny'

dst = '192.168.30.'
scanPort = [135,]
ips = [22, 24, 73, 100, 127, 252,]


def test_port(target_IP, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(0.01)
    re = s.connect_ex((target_IP, port))
    s.close()
    return re == 0

if __name__ == '__main__':
    for ip in ips:
        print('Scan %d.'% ip)
        bid_port = 0
        for port in range(1, 9000):
            result = test_port(dst + str(ip), port)
            if result:
                bid_port = port
                break
        print("IP: %d %s" % (ip, bid_port != 0))
    print('Finished scanning.')


