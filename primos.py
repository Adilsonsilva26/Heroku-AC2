import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def numeros_primos():

    limite=100
    qtdprimo = 2
    numero = 3

    primos = "1,2,"

    while qtdprimo < limite:
        ehprimo = 1
        for i in  range (2, numero):
            if numero % i == 0:
                ehprimo = 0
                break
        if (ehprimo):
            primos = primos + str(numero) + ","
            qtdprimo += 1
            if(qtdprimo % 10 ==0):
                primos = primos + "->" + str(qtdprimo) + "<br>"
        numero+=1
    return primos

    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)

