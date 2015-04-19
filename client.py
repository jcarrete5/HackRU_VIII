'''

@author: Jason Carrete
'''
import threading, game, socket
from flask import Flask, request, redirect
from threading import Thread
from game import gameFunc
from Queue import Queue

commandsQueue = Queue()
def netcode(commandsQueue):
    host = "45.33.88.126"
    port = 9999
    client = socket.socket()
    client.connect((host, port))
    while True:
        string = client.recv(4096)
        for char in string:
            commandsQueue.put(char)
netThread = Thread(target = netcode, args=(commandsQueue,))
thread = Thread(target = gameFunc, args=(commandsQueue,))
netThread.start()
thread.start()
