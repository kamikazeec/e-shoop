from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    #TOMAR EN CUENTA EL name='rol_enum' Y EL nullable=False
    rol = db.Column(db.Enum('admin', 'cliente', name='rol_enum'), nullable=False, default='cliente')
    activo = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.now())

    # -- METODOS DE CONTRASEÑA
    def set_password(self, password_plano):
        """ Hash a la contraseña en texto plano"""
        self.password = generate_password_hash(password_plano)

    def check_password(self, password):
        """ Verifica si la contraseña ingresada coincide con la almacenada en la base de datos"""
        return check_password_hash(password)
    
    def es_admin(self):
        """ Verifica si el usuario tiene rol de administrador"""
        return self.rol == 'admin'
    
    def __repr__(self):
        #OJO ESTA AUTOCOMPLETADO, NO SE SI ES CORRECTO
        return f'<Usuario {self.nombre} - {self.email} - Rol: {self.rol}>'