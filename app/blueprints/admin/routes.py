from flask import render_template
from . import auth_bp

@admin_bp.route('/admin')
def login():
    return render_template('admin/index.html')

@admin_bp.route('admin/productos')
def productos():
    return render_template('admin/productos.html')

@admin_bp.route('admin/Clientes')
def clientes():
    return render_template('admin/clientes.html')

@admin_bp.route('admin/pedidos')
def pedidos():
    return render_template('admin/pedidos.html')