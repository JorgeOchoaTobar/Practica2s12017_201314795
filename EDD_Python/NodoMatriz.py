class NodoMatriz(object):           #Esta clase es el nodo de la lista simple

    def __init__(self,palabra):
        self.__palabra=palabra     #palabra que va a contener el nodo
        self.__izq=None
        self.__Der=None
        self.__Arriba=None
        self.__Abajo=None      #puntero siguiente

    def obtenerPalabra(self):
        return self.__palabra
