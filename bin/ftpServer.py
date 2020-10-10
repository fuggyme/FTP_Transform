#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : hgh

import sys
import os
import socket
from core import socket_server

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


if __name__ == "__main__":
    print("服务器地址", get_host_ip())
    HOST, PORT = get_host_ip(), 9901
    server = socket_server.socketserver.ThreadingTCPServer((HOST, PORT), socket_server.MyTCPServer)
    server.serve_forever()
