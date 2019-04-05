#!/usr/bin/env python3

### server.py ###
import socket
import json
import time
import os
from filetransfer import Filetransfer


class Server:
    def __init__(self, port, host=''):
        self._host = host
        self._port = port
        workdir = None
        
        while not workdir:
            workdir = input("Enter working directory: ")
            if not os.path.exists(workdir):
                print ("Invalid path")
                workdir = None
            
        os.chdir(workdir)

    def create(self, connections=5):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind the socket to port and hostname
        self.s.bind((self._host, self._port))

        # start listening to maximum connections
        self.s.listen(connections)
        print("waiting for connection...")

    def receive(self):
        # accept connections from outside
        (clientsocket, address) = self.s.accept()
        print("Got a connection from {0}".format(address))

        try:
            receive = Filetransfer()

            receive.receive_init(clientsocket)
            receive.receive_filename()
            receive.receive_filesize()
            receive.receive_chunk()
            receive.close_socket()
        except Exception as error:
            print(error)
        finally:
            del receive


    def process_meta(self):
        if not os.path.isfile("/home/jop/work/server/meta.json"):
            print ("rip")
            return

        with open("/home/jop/work/server/meta.json") as data:
            meta = json.load(data)

            for filenames in meta:
                print (meta[filenames])



def main():
    s = Server(port=5037)
    s.create()

    # main loop of server
    while True:
#        s.process_meta()
        s.receive()
#        time.sleep(5)

    s.close()

if __name__ == "__main__":
    main()

