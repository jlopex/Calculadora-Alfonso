from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello!'


@app.route('/calcular')
def calcular():
    a = request.args.get('valor1', '0')
    b = request.args.get('valor2', '0')
    operador = request.args.get('operador', '+')
    if operador == '/':
        result = round(eval(a + operador + str(float(b))), 3)
    else:
        result = eval(a + operador + b)
    return str(result)


if __name__ == '__main__':
    app.run()
