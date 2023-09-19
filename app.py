from flask import Flask, render_template, request
from modulos import operaciones as op

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calcular():
    resultado = ""
    if request.method == "POST":
        try:
            opciones = ["+", "-", "*", "/"]
            operation = request.form["operation"]
            
            if operation not in opciones:
                raise Exception('No ingresaste una opción correcta, por favor vuelve a elegir.')
            
            num_1 = float(request.form["num_1"])
            num_2 = float(request.form["num_2"])
            
            if operation == '+':
                res = op.add(num_1, num_2)
            elif operation == '-':
                res = op.sub(num_1, num_2)
            elif operation == '*':
                res = op.mul(num_1, num_2)
            elif operation == '/':
                if num_2 == 0:
                    raise ZeroDivisionError('No se puede dividir por cero.')
                res = op.div(num_1, num_2)
        except ValueError:
            resultado = 'No has ingresado un número válido, por favor intenta de nuevo.'
        except ZeroDivisionError as e:
            resultado = str(e) + ", por favor intenta de nuevo."

        else:
            resultado = f"{num_1} {operation} {num_2} = {res}"
    
    return render_template("calculadora.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
