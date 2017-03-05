class NodoCola(object):           #Esta clase es el nodo de la cola

    def __init__(self,num):
        self.__num=num             #numero que va a contener el nodo
        self.__siguiente=None      #puntero siguiente

    def obtenerNummero(self):
        return self.__num
