#JORGE BILLY OCHOA TOBAR
#201314795

import os
from graphviz import Digraph
import NodoCola

nodo = NodoCola

class Cola(object):                    #Clase Cola
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
				if temporal.siguiente == self.__ultimo:
					temporal2 = self.__ultimo
					self.__ultimo = temporal
					temporal2 = None
					valor = False
					print("El Elemento se a Eliminado")
				else:
					temporal = temporal.siguiente

	def imprimirNodoCola(self):                                        #IMPRIMIR PILA
		palabra = ""
		if self.ColaVacia()==True:
			return("Esta lista esta vacia")
		else:
			valor = True
			temporal = self.__primero
			while(valor):
				palabra = palabra+"--->"+ str(temporal.obtenerNumero())
				print(temporal.obtenerNumero())
				if temporal == self.__ultimo:
					valor = False
				else:
					temporal = temporal.siguiente
		return palabra

	def graficarCola(self):                                            #GRAFICANDO PILA
		temporal = self.__primero
		file_path = "Graficas"
		try:
			if not os.path.exists(file_path):
				os.makedirs(file_path)
			archivo = open("Graficas/Cola.dot","w")
			archivo.write("digraph Cola{\n")
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
			archivo.write("\tlabel = \" Cola \" ;\n")
			archivo.write("\tcolor=yellow")
			archivo.write("\t}\n")
			archivo.write("}")
			archivo.close()
			cmd = '"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe" -Tjpg Graficas\\Cola.dot -o Graficas\\Cola.jpg'
			os.system(cmd)

		except ValueError:
			print("Error!")
