# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 12:38:05 2022

@author: Samaniego Francisco
"""



from LDE import ListaDobleEnlazada

class ColaDoble:
    """Método para inicializar la estructura"""
    def __init__(self):
        self._items = ListaDobleEnlazada()
        self._tamanio = 0
    
    @property
    
    def tamanio(self):
        """Atributo de clase que define el tamaño de la cola doble 
           Retorna: el tamaño de la cola doble -> int"""
        return self._tamanio
        
    def cola_vacia(self):
        """ Metodo para saber si la cola doble esta vacia, returna True en dicho caso
            y False en caso de que no esté vacia
            Retorna: True o False"""
        return self._items.esta_vacia()

    def agregar_frente(self, item):
        """ Método para agregar elementos (item) en la parte del frente de la cola doble, una vez agregado se actualiza 
            el valor del tamanio """
        
        self._items.agregar(item)
        self._tamanio +=1
   
    def agregar_final(self, item):
        """ Método para agregar elementos (item) en el final de la cola doble, una vez agregado se actualiza el valor
           del tamanio """
        
        self._items.anexar(item)
        self._tamanio+=1 
    
    
    def remover_frente(self,posicion = 0):
        """ Método para remover elementos (item) del frente de la cola doble, una vez extraido se actualiza el valor
            del tamanio y se retorna el elemento removido -> Nodo """
        
        extraidofrente = self._items.extraer(posicion)
        self._tamanio -= 1 
        return extraidofrente

    def __iter__(self):
        """ Método para recorrer elemento a elemento de la cola """
        
        nodo = self._items.cabeza
        while nodo:
            yield nodo
            nodo = nodo.siguiente  
            
    def __str__ (self):
        """ Metodo para retornar los valores de los datos en los nodos de la cola doble"""
        return str([nodo.dato for nodo in self])
    
    def __len__(self):
        """ Método para poder utilizar la función len() 
            Retorna: el tamanio de la lista --> int"""
        return self._tamanio

    
