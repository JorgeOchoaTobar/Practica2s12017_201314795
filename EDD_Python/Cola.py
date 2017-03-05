#JORGE BILLY OCHOA TOBAR
#201314795

import os
from graphviz import Digraph
import NodoCola

nodo = NodoCola

#Clase Lista simple enlazada
class cola(object):
	def __init__(self):                #constructor
		self.__primero = None
		self.__ultimo = None
		self.__tam = 0

	def ColaVacia(self):               #Para saber que la lista esta vacia
		if self.__primero == None:
			return True

	def obtenerTamañoCola(self):       #Para obtener el tamaño de nuestra cola
		return self.__tam

	def Encolar(self,num):             #Encolamos un nuevo nodo
		nuevo = nodo.NodoCola(num)
		if self.ColaVacia()==True:
			self.__primero = self.__ultimo = nuevo
		else:
			nuevo.siguiente = self.__primero
			self.__primero = nuevo

	def Desencolar(self):              #desencolamos un nodo
		if self.ColaVacia()==True:
			print("Esta Cola es Vacia")
		elif self.__primero == self.__ultimo:
			self.__primero = None
			self.__ultimo = None
			print("El Elemento se a Eliminado")
		else:
			valor = True
			temporal = self.__primero
			while(valor):
				if temp.siguiente == self.__ultimo:
					temporal2 = self.__ultimo
					self.__ultimo = temporal
					temporal2 = None
					valalor = False
					print("l Elemento se a Eliminado")
				else:
					temporal = temporal.siguiente

	def imprimirNodoCola(self):        #imprimimos el nodo de la cola
		palabra = ""
		if self.ColaVacia()==True:
			return("lista vacia")
		else:
			valor = True
			temporal = self.__primero
			while(valor):
				palabra = palabra +"->"+ str(temporal.obtenerNumero())
				print(temporal.obtenerNumero())
				if temporal == self.__ultimo:
					ValueError = False
				else:
					temporal = temporal.siguiente
		return palabra

	def graficarCola(self):                     #graficando cola
		temporal = self.__primero
		file_path = "Grafos"
		try:
			if not os.path.exists(file_path):
				os.makedirs(file_path)
			archivo = open("Grafos/pila.dot","w")
			archivo.write("digraph pila{\n")
			archivo.write("subgraph cluster_1{\n")
			archivo.write("\t node[shape=box,color=yellow];\n")
			while temporal!=None :
				archivo.write("\t"+ str(temporal.obtenerNumero()))										
				if temporal !=self.__ultimo:
					temporal = temporal.siguiente
					archivo.write("->"+ str(temporal.obtenerNumero()))
					archivo.write("\n")					
				else:
					archivo.write("; \n")
					temporal = None
			archivo.write("\tlabel = \" Pila \" ;\n")
			archivo.write("\tcolor=yellow")
			archivo.write("\t}\n")
			archivo.write("}")
			archivo.close()
			cmd = '"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe" -Tjpg Grafos\\Cola.dot -o Grafos\\Cola.jpg'
			os.system(cmd)

		except ValueError:
			print("Error!")