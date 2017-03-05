#JORGE BILLY OCHOA TOBAR
#201314795

import os
from graphviz import Digraph
import NodoPila

nodo = NodoPila

class Pila(object):                    #Clase Cola
	def __init__(self):                #constructor
		self.__primero = None
		self.__ultimo = None
		self.__tam = 0

	def PilaVacia(self):                                                #PARA SABER SI ESTA VACIA
		if self.__primero == None:
			return True

	def obtenerTamañoPila(self):
		return self.__tam

	def ApilarNodo(self,num):                                           #PARA AGREGAR UN NUEVO NODO
		nuevo = nodo.NodoPila(num)
		if self.PilaVacia()==True:
			self.__primero = self.__ultimo = nuevo
		else:
			nuevo.siguiente = self.__primero
			self.__primero = nuevo
	    
	def RetirarNodo(self):                                              #RETIRANDO UN NODO DE LA PILA
		if self.PilaVacia()==True:
			print("Esta pila esta vacia")
		elif self.__primero == self.__ultimo:
			self.__primero = None
			self.__ultimo = None
			print("El Elemento a sido Eliminado")
		else:
			temporal = self.__primero
			self.__primero = self.__primero.siguiente
			temporal = None
			print("El Elemento a sido Eliminado")
		
	def imprimirNodoPila(self):                                        #IMPRIMIR PILA
		palabra = ""
		if self.PilaVacia()==True:
			return("Esta lista esta vacia")
		else:
			valor = True
			temporal = self.__primero
			while(valor):
				palabra = palabra+"->"+ str(temporal.obtenerNumero())
				print(temporal.obtenerNumero())
				if temporal == self.__ultimo:
					valor = False
				else:
					temporal = temporal.siguiente
		return palabra

	def graficarPila(self):                                            #GRAFICANDO PILA
		temporal = self.__primero
		file_path = "Graficas"
		try:
			if not os.path.exists(file_path):
				os.makedirs(file_path)
			archivo = open("Graficas/Pila.dot","w")
			archivo.write("digraph Pila{\n")
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
			cmd = '"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe" -Tjpg Graficas\\Pila.dot -o Graficas\\Pila.jpg'
			os.system(cmd)

		except ValueError:
			print("Error!")
