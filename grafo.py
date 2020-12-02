from pprint import pprint, pformat
import json
from algoritmos import distanciaeuclidiana

class Grafo:

    def __init__(self):
        self.__grafo = {}
 
    def __Add__(self,ox,oy,dx,dy):
   
        origen = (ox,oy)
        destino = (dx,dy)

        o_d = str(dx)+',' + str(dy)+',' 
        d_o = str(ox)+',' + str(oy)+',' 

        if origen in self.__grafo:
            self.__grafo[origen].append(o_d + str(distanciaeuclidiana(ox,oy,dx,dy)))
        else:
            self.__grafo[origen] = [o_d + str(distanciaeuclidiana(ox,oy,dx,dy))]

        if destino in self.__grafo:
            self.__grafo[destino].append(d_o + str(distanciaeuclidiana(ox,oy,dx,dy)))
        else:
            self.__grafo[destino] = [d_o + str(distanciaeuclidiana(ox,oy,dx,dy))]

    def Mostrargrafo(self):
        str = pformat(self.__grafo, width=40, indent=1)
        print(str)

    @property
    def  Grafo(self):
        return self.__grafo

    
    
        

