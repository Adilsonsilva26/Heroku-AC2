import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def numeros_primos():

    
    ordem_p = 2
    num = 3

    org = "2-"

    while ordem_p < 101:
        primo = 1
        for i in  range (2, num):
            if num % i == 0:
                primo = 0
                break
        if (primo):
            org = org + str(num) + "-"
            ordem_p += 1
        num+=1
    return org

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  

