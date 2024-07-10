from app.database import get_db_connection

class Usuario:
    def __init__(self, id=None, usuario=None, clave=None, nombre=None, apellido=None, email=None, telefono=None):
        self.id = id
        self.usuario = usuario
        self.clave = clave
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def guardar(self):
        db = get_db_connection()
        cur = db.cursor()
        if self.id:
            cur.execute("UPDATE usuario SET clave=%s, nombre=%s, apellido=%s, email=%s, telefono=%s WHERE id=%s",
                        (self.clave, self.nombre, self.apellido, self.email, self.telefono, self.id))
        else:
            cur.execute(
                "INSERT INTO usuario (usuario, clave, nombre, apellido, email, telefono) VALUES (%s, %s, %s, %s, %s, %s)", (self.usuario, self.clave, self.nombre, self.apellido, self.email, self.telefono))

        db.commit()
        cur.close()

    @staticmethod
    def traer_todos():
        db = get_db_connection()
        cur = db.cursor()
        cur.execute("SELECT * FROM usuario")
        registros = cur.fetchall()
        usuarios = []
        for registro in registros:
            usuarios.append(Usuario(
                registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6]))

        cur.close()
        return usuarios

    @staticmethod
    def traer_uno(id):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuario WHERE id=%s", (id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Usuario(id=row[0], usuario=row[1], clave=row[2], nombre=row[3], apellido=row[4], email=row[5], telefono=row[6])

        return None

    def eliminar(self):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM usuario WHERE id=%s", (self.id,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id': self.id,
            'usuario': self.usuario,
            'clave': self.clave,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono
        }


class Reserva:
    def __init__(self, idReserva=None, cantidadPersonas=None, fecha=None, ubicacion=None, ocasionEspecial=None, ocasionEspecialCual=None, idUsuario=None):
        self.idReserva = idReserva
        self.cantidadPersonas = cantidadPersonas
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.ocasionEspecial = ocasionEspecial
        self.ocasionEspecialCual = ocasionEspecialCual
        self.idUsuario = idUsuario

    def guardar(self):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO reserva (cantidadPersonas, fecha, ubicacion, ocasionEspecial, ocasionEspecialCual, idUsuario) VALUES (%s, %s, %s, %s, %s, %s)",
            (self.cantidad_personas, self.fecha, self.ubicacion, self.ocasion_especial, self.ocasion_especial_cual, self.id_usuario)
        )
        db.commit()
        cursor.close()
    
    @staticmethod
    def traer_todos():
        db = get_db_connection()
        cur = db.cursor()
        cur.execute("SELECT * FROM reserva")
        registros = cur.fetchall()
        reservas = []
        for registro in registros:
            reservas.append(Reserva(
                registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6]))

        cur.close()
        return reservas

    @staticmethod
    def traer_uno(idReserva):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM reserva WHERE idReserva=%s", (idReserva,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Reserva(idReserva=row[0], cantidadPersonas=row[1], fecha=row[2], ubicacion=row[3], ocasionEspecial=row[4], ocasionEspecialCual=row[5], idUsuario=row[6])
        return None
    
    def eliminar(self):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM reserva WHERE idReserva=%s", (self.idReserva,))
        db.commit()
        cursor.close()

    
    def serialize(self):
        return {
            'idReserva': self.idReserva,
            'cantidadPersonas': self.cantidadPersonas,
            'fecha': self.fecha.isoformat(),  # Formatear la fecha si es necesario
            'ubicacion': self.ubicacion,
            'ocasionEspecial': self.ocasionEspecial,
            'ocasionEspecialCual': self.ocasionEspecialCual,
            'idUsuario': self.idUsuario
            # Añadir más campos si es necesario
        }