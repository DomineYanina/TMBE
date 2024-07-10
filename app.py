from flask import Flask, session
from flask_session import Session
from flask_cors import CORS
from app.database import iniciar_app
from app.views import *

app = Flask(__name__)
app.secret_key = 'proycodoacodo'  # Asegúrate de definir una clave secreta segura
app.config['SESSION_TYPE'] = 'filesystem'  # Puedes elegir otro tipo según tus necesidades

Session(app)
iniciar_app(app)
CORS(app)

# Rutas existentes
app.route("/", methods=["GET"])(index)
app.route("/crear_usuario", methods=["POST"])(crear_usuario)
app.route("/traer_usuarios", methods=["GET"])(traer_usuarios)
app.route("/traer_usuario/<int:id>", methods=["GET"])(traer_usuario)
app.route("/actualizar_usuario/<int:id>", methods=["PUT"])(actualizar_usuario)
app.route("/eliminar_usuario/<int:id>", methods=["DELETE"])(eliminar_usuario)
app.route("/crear_reserva", methods=["POST"])(crear_reserva)
app.route("/traer_reservas", methods=["GET"])(traer_reservas)
app.route("/traer_reserva/<int:idReserva>", methods=["GET"])(traer_reserva)
app.route("/actualizar_reserva/<int:id>", methods=["PUT"])(actualizar_reserva)
app.route("/eliminar_reserva/<int:id>", methods=["DELETE"])(eliminar_reserva)

# Nuevas rutas para login/logout
app.route("/login/<string:emailUsuario>/<string:clave>", methods=["POST"])(login)
app.route("/logout", methods=["POST"])(logout)

if __name__ == "__main__":
    app.run(debug=True)
