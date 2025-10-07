from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  
def hola():
    
    return render_template('Plantilla_base.html')

@app.route('/Inicio')
def index():
    return render_template('index.html')

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
