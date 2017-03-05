#JORGE BILLY OCHOA TOBAR
#201314795

import os
from graphviz import Digraph
import NodoLista

nodo = NodoLista

class ListaSimple(object):                       #Lista Simplemente enlazada
	def __init__(self):							 #CONSTRUCTOR
		self.__primero = None
		self.__ultimo = None
		self.__tam = 0

	def ListaVacia(self):                        #VARIFICAR LISTA VACIA
		if self.__primero == None:
			return True

	def insertarNodoLista(self ,palabra):        #INSERTANDO NODOS A LA LISTA
		nuevo = nodo.NodoLista(palabra)
		if self.ListaVacia() == True:
			self.__primero = nuevo
			self.__ultimo = nuevo
		else:
			self.__ultimo.siguiente = nuevo
			self.__ultimo = nuevo
		self.__tam +=1

	def obtenerTamañoLista(self):				   #OBTENER TAMAÑO DE LA LISTA
		return self.__tam

	def buscarNodoLista(self,dato):                #BUSCANDO NODO DE LA LISTA
		temporal = self.__primero
		contador = 0
		contador2 = 0
		mensaje = 'No se encontro ningun dato'
		while temporal!=None and contador!=1:
			if dato == temporal.obtenerPalabra():
				contador = 0
				mensaje2 = "El Dato que busca se encuentra en el indice <" + str(contador2) + ">"
				return mensaje2
			elif contador2 == self.__tam-1:				
				return mensaje
			else:
				temporal = temporal.siguiente
				contador2+=1

	def eliminarNodoLista(self,indice):             #ELIMINANDO NODO DE LAS LISTAS
		if indice == 0:
			self.__primero = self.__primero.siguiente
			self.__tam -=1
		elif indice == self.__tam -1:
			valor = True
			temporal = self.__primero
			while(valor):
				if temporal.siguiente == self.__ultimo:
					temporal2 = self.__ultimo
					self.__ultimo = temporal
					temporal2 = None
					valor = False
					self.__tam -=1
				else:
					temporal = temporal.siguiente
		elif indice > self.__tam-1:
			print("El indice que usted dio no existe")
		else:
			temporal = self.__primero
			contador = 0
			while contador<indice-1:
				temporal = temporal.siguiente
				contador +=1
			temporal2 = temporal.siguiente
			temporal.siguiente = temporal2.siguiente
			temporal2 = None
			temporal = None
			self.__tam -=1

	def imprimirNodosLista(self):                     #IMPRIMIR NODOS
		if self.ListaVacia()==True:
			return("Esta lista esta vacia")
		else:
			valor = True
			temporal = self.__primero
			while(valor):
				print(temporal.obtenerPalabra())
				if temporal == self.__ultimo:
					valor = False
				else:
					temporal = temporal.siguiente

	def graficarLista(self):                         #GRAFICANDO LISTA SIMPLE
		temporal = self.__primero
		file_path = "Grafos"
		try:
			if not os.path.exists(file_path):
				os.makedirs(file_path)
			archivo = open("Grafos/listasimple.dot","w")
			archivo.write("digraph Lista_simple{\n")
			archivo.write("subgraph cluster_1{\n")
			archivo.write("\t node[shape=box,color=yellow];\n")
			while temporal!=None :
				archivo.write("\t"+temporal.obtenerPalabra())										
				if temporal !=self.__ultimo:
					temporal = temporal.siguiente
					archivo.write("->"+temporal.obtenerPalabra())
					archivo.write("\n")					
				else:
					archivo.write("; \n")
					temporal = None
			archivo.write("\t label = \" Lista Simple \" ;\n")
			archivo.write("\t color=yellow")
			archivo.write("\t}\n")
			archivo.write("}")
			archivo.close()
			cmd = '"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe" -Tjpg Grafos\\ListaSimple.dot -o Grafos\\ListaSimple.jpg'
			os.system(cmd)

		except ValueError:
			print("Error!")
