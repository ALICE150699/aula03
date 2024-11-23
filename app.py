from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/plano1')
def plano1():
    return render_template('plano1.html')

@app.route('/plano2')
def plano2():
    return render_template('plano2.html')

@app.route('/plano3')
def plano3():
    return render_template('plano3.html')