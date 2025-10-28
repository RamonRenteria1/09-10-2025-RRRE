from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)

USUARIOS_REGISTRADOS = {
    'admin@correo.com': {
        'pasword': 'Admin123',
        'nombre': 'Administrador',
        'Fecha de Nacimiento': '1990-01-01'
    }
}

app.secret_key = 'cetis61Reymonxddd'


@app.route('/')
def inicio():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/Login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()

        if not email or not password:
            flash('Por favor ingresa email y contraseña', 'error')
            return redirect(url_for('login'))

        if email in USUARIOS_REGISTRADOS:
            usuario = USUARIOS_REGISTRADOS[email]
            if usuario['pasword'] == password:
                session['usuario_email'] = email
                session['usuario'] = usuario['nombre']
                session['logueado'] = True

                flash(f'Bienvenido {usuario["nombre"]}!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Contraseña incorrecta', 'error')
                return redirect(url_for('login'))
        else:
            flash('El usuario no existe', 'error')
            return redirect(url_for('login'))

        
    return render_template('login.html')


@app.route('/registro', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nombres = request.form.get('nombres')
        apellido = request.form.get('apellido')
        email = request.form.get('email')
        contraseña = request.form.get('password')
        confirmarcontraseña = request.form.get('confirm_password')
        dia = request.form.get('dia')

        if contraseña != confirmarcontraseña:
            flash("Las contraseñas no coinciden.", "error")
            return redirect(url_for('registrar'))

        print(f"Nuevo registro: {nombres} {apellido} - {email}")
        flash("Registro exitoso. Ahora puedes iniciar sesión.", "success")
        return redirect(url_for('login'))

    return render_template('Registrar.html')


@app.route('/acerca')
def acerca():
    return render_template('acerca.html')


@app.route('/animales')
def animales():
    return render_template('Animales.html')


@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html')


@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html')


@app.route('/logout')
def logout():
    session.clear()
    flash("Sesión cerrada correctamente.", "success")
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
