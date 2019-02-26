#!/usr/bin/env python3

### client.py ###
import os
import time
import getpass
import configparser
from watcher import Watcher

WATCH_TIME = 5

class Client(Watcher):

    def __init__(self, conf_path):
        # get the absolute path to the current directory
        self.abs_file_path = os.path.abspath(os.path.dirname(__file__))
        self.config_path = os.path.join(self.abs_file_path, conf_path)

    def read_config(self):
        config = configparser.RawConfigParser()
        config.read(self.config_path)
        self._host = config.get('example-config', 'host')
        self._port = int(config.get('example-config', 'port'))

    def get_home_dir():
        return os.path.join("/home", getpass.getuser())

    def watch(self, metapath=None, watchdir=None, recursive=True):
        Watcher.__init__(self, metapath, watchdir, recursive)


def main():
    # Make new client and read config
    c = Client("../config")
    c.read_config()
    metapath = os.path.join(c.abs_file_path, "../meta.json")
    print(metapath)
    # Set the directory to watch
    c.watch(metapath)

    # main loop
    while True:
        c.scan()
        time.sleep(WATCH_TIME)


if __name__ == "__main__":
    main()
