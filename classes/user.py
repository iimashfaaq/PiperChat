class User():
    def __init__(self, sock, ip, port, name=None):
        self._sock = sock
        self._ip = ip
        self._port = port
        if name is None:
            self.name = ip
        else:
            self.name = name

    def sock(self):
        return self._sock

    def ip(self):
        return self._ip

    def port(self):
        return self._port