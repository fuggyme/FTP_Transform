#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : hgh


from core import socket_client
import os
import sys
from colorama import init

init(autoreset=True)
#sys.path.append('C:\\Users\\Wang Jinfang\\Desktop\\FTPdemo\\FTP-python-master\\core\\socket_client.py')

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

if __name__ == "__main__":
    host, port = "10.1.0.74", 9901
    myClient = socket_client.MySocketClient(host, port)
    myClient.start()
