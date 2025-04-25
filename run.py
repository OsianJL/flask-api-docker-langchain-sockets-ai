from app import create_app
from app.extensions.extensions import socketio

app = create_app()

print("🚀 Flask-SocketIO is starting...")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
