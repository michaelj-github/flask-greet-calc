from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_route():
    """ return the sum of a and b """
    a = request.args["a"]
    b = request.args["b"]
    c = add(int(a), int(b))
    # return f"<h1>add: {a} + {b} = {c}</h1>"
    return str(c)

@app.route('/sub')
def sub_route():
    """ return b - a """
    a = request.args["a"]
    b = request.args["b"]
    c = sub(int(a), int(b))
    # return f"<h1>subtract: {a} - {b} = {c}</h1>"
    return str(c)

@app.route('/mult')
def mult_route():
    """ return the product of a and b """
    a = request.args["a"]
    b = request.args["b"]
    c = mult(int(a), int(b))
    # return f"<h1>multiply: {a} * {b} = {c}</h1>"
    return str(c)

@app.route('/div')
def div_route():
    """ return a divided by b"""
    a = request.args["a"]
    b = request.args["b"]
    c = int(div(int(a), int(b)))
    # return f"<h1>divide: {a} / {b} = {c}</h1>"
    return str(c)

@app.route('/math/<operation>')
def math_route(operation):
    """ return the result of the operation applied to a and b """
    a = request.args["a"]
    b = request.args["b"]

    operations = {
        "add": add(int(a), int(b)),
        "sub": sub(int(a), int(b)),
        "mult": mult(int(a), int(b)),
        "div": div(int(a), int(b))
    }
    return str(int(operations[operation]))