import socketio as SIO
SERVER_PORT = 5000
sio = SIO.Client()
@sio.event
def connect():
    print("We are connected!")
    sio.emit('ping-server', 'Hi!')
@sio.on('ping-client')
def fetch_log(payload):
    print('Server says: ', payload)
if __name__ == "__main__":
    # connect to sockeio server
    SERVER_URL = 'http://localhost:{}'.format(SERVER_PORT)
    print('Client connecting to:', SERVER_URL)
    sio.connect(SERVER_URL)
