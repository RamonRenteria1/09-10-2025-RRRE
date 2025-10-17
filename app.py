from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def inicio():
    return redirect(url_for('index')) 

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nombres = request.form.get('nombres')
        apellido = request.form.get('apellido')
        email = request.form.get('email')

        
        print(f"Nuevo registro: {nombres} {apellido} - {email}")

        # Después del registro manda al inicio
        return redirect(url_for('index'))

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

if __name__ == '__main__':
    app.run(debug=True)
