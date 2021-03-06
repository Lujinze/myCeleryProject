import os
import sys
# sys.path.append(r'C:\Users\juhao\PycharmProjects')
# from  myCeleryProject.app import app

import time
from myCeleryProject.celery import app
import socket


def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


@app.task
def add(x, y):
    s = x + y
    time.sleep(5)  # 模拟耗时操作
    print("主机IP {}: x + y = {}".format(get_host_ip(), s))
    return s


@app.task
def taskA():
    print("taskA begin...")
    print("主机IP: %s "%get_host_ip())
    time.sleep(3)
    print("taskA done.")


@app.task
def taskB():
    print("taskB begin...")
    print("主机IP: %s " % get_host_ip())
    time.sleep(4)
    print("taskB done.")