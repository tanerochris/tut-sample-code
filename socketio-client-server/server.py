from gevent import monkey
monkey.patch_all()
from flask import Flask
from flask_socketio import SocketIO

application = app = Flask(__name__)
app.config['SECRET_KEY'] = 'socket_io_server'
socketio = SocketIO(app, async_mode='gevent', cors_allowed_origins="*")

@socketio.on('ping-server')
def test_server(payload):
    print('Client says:', payload)
    socketio.emit('ping-client', 'Hey buddy!')

if __name__ == "__main__":
  socketio.run(app)