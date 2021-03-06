import socket, SimpleHTTPServer, SocketServer
import os, random, time
import clipboard

def is_port_in_use(port):
    # http://stackoverflow.com/questions/19196105/python-how-to-check-if-a-network-port-is-open-on-linux
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1',port))
    sock.close()
    return result == 0
    
def gen_port():
    while True:
        port = random.randint(1111, 2222)
        if not is_port_in_use(port):
            return port

def main():
    path = os.path.normpath(clipboard.paste())
    if not os.path.exists(path):
        print path, 'does not exit'
        time.sleep(2)
        return
    print 'content in clipboard (will use as dir path)', path
    os.chdir(path)
    print 'script at', os.getcwd()

    port = gen_port()
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("0.0.0.0", port), Handler)

    print "! serve at ------->", str(port)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
