#JORGE BILLY OCHOA TOBAR
#201314795

import ListaSimple
import Pila
import Cola
from flask import Flask, request

listita = ListaSimple.ListaSimple()
colita = Cola.Cola()
pilita = Pila.Pila()
app = Flask("EDD_Python")


#Metodos para el control de la lista simple en web service
@app.route('/insertarNodoLista',methods=['POST'])
def insertarNodoLista():
	palabra = str(request.form['palabra'])
	listita.insertarNodoLista(str(palabra))
	listita.imprimirNodosLista()
	listita.graficarLista()
	return "Se inserto el valor en la lista simple " + str(palabra)

@app.route('/eliminarNodoLista',methods=['POST'])
def eliminarNodoLista():
	numero = str(request.form['numero'])
	listita.eliminarNodoLista(int(numero))	
	listita.imprimirNodosLista()
	listita.graficarLista()
	return "Se elimino el indice <" + str(numero) +">"

@app.route('/buscarNodoLista',methods=['POST'])
def buscarNodoLista():
	palabra = str(request.form['palabra'])
	auxiliar = listita.buscarNodoLista(str(palabra))
	return str(auxiliar)

#Metodos para el control de la cola
@app.route('/Encolar',methods=['POST'])
def Encolar():
	numero = str(request.form['numero'])
	colita.Encolar(int(numero))
	colita.graficarCola()
	palabra = str(colita.imprimirNodoCola())
	return palabra

@app.route('/Desencolar',methods=['POST'])
def Desencolar():
	numero = str(request.form['numero'])
	colita.Desencolar()
	colita.graficarCola()
	palabra = str(colita.imprimirNodoCola())
	return palabra

#Metodos para el control de la pila
@app.route('/ApilarNodo',methods=['POST'])
def ApilarNodo():
	numero = str(request.form['numero'])
	pilita.ApilarNodo(int(numero))
	pilita.graficarPila()
	palabra = str(pilita.imprimirNodoPila())
	return palabra

@app.route('/RetirarNodo',methods=['POST'])
def RetirarNodo():
	numero = str(request.form['numero'])
	pilita.RetirarNodo()
	pilita.graficarPila()
	palabra = str(pilita.imprimirNodoPila())
	return palabra

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')