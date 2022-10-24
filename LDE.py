# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 10:04:51 2022

@author: fmasa
"""

from __future__ import annotations

class Nodo:
    def __init__(self, p_dato):
        self._dato=p_dato
        self._siguiente=None
        self._anterior=None
        
    @property
    def dato(self):
        """ Metodo para devolver el valor del dato"""
        return self._dato
    @dato.setter
    def dato(self, p_dato):
        """ Metodo para configurar el valor del dato"""
        self._dato=p_dato
    
    @property
    def siguiente(self):
        """ Metodo para devolver el valor del siguiente"""
        return self._siguiente
    @siguiente.setter
    def siguiente(self, p_siguiente):
        """ Metodo para configurar el valor del siguiente"""
        self._siguiente=p_siguiente
    
    @property
    def anterior(self):
        """ Metodo para devolver el valor del anterior"""
        return self._anterior
    @anterior.setter
    def anterior(self, p_anterior):
        """ Metodo para configurar el valor del anterior"""
        self._anterior=p_anterior
    def _str_(self):
        return str(self.dato)
    
    def __repr__(self)-> str:
        return str(self.dato) 
    

    
    
    def __lt__(self, n1 : Nodo()):
        if self.dato < n1.dato:
            return True
        else: 
            return False
    
    def __eq__(self, n1: Nodo()):
        if self.dato == n1.dato:
            return True
        else:
            return False
   
    def __gt__(self, n1: Nodo()):
        if  self.dato > n1.dato:
            return True
        else:
            return False
    
    def __getitem__(self, index):
        return self.dato[index]


class ListaDobleEnlazada:
    
    def __init__(self):
        """ Metodo inicializador de la clase ListaDobleEnlazada,
        Inicializo cabeza y cola en None y luego su tamanio en cero"""
        self._cabeza = None
        self._cola = None
        self._tamanio = 0
    
    @property
    def cabeza(self):
        """ Metodo para retornar el valor del dato en la cabeza"""
        return self._cabeza
    @cabeza.setter
    def cabeza(self, p_cabeza):
        """ Metodo para configurar el valor del dato en la cabeza"""
        self._cabeza = p_cabeza
     
    @property
    def cola(self):
        """ Metodo para retornar el valor del dato en la cola"""
        return self._cola
    @cola.setter
    def cola(self, p_cola):
        """ Metodo para configurar el valor del dato en la cola"""
        self._cola = p_cola
        
    @property
    def tamanio(self):
        """ Metodo para retornar el tamaño de la lista"""
        return self._tamanio

    def esta_vacia(self):
        """ Metodo para saber si la lista esta vacia, returna True en dicho caso
            y False en caso de que no esté vacia
            Retorna: True o False"""
        return self._tamanio == 0      

    def __iter__(self):
        """ Metodo para iterar sobre la lista
        Retorna: None"""
        nodo = self.cabeza
        while nodo:
            yield nodo
            nodo = nodo.siguiente  
    
    def __str__ (self):
        """ Metodo para retornar los valores de los datos en los nodos de la lista"""
        return str([nodo.dato for nodo in self])

    def agregar(self, item):
        """ Metodo para agregar un valor (item) al inicio de la lista,
        al finalizar actualiza el tamaño de la misma.
        Retorna: None"""
        temp = Nodo(item)
        
        if self.esta_vacia():
            self.cabeza = temp
            self.cola = temp
            
        else:
            temp.siguiente = self.cabeza
            self.cabeza.anterior = temp
            self.cabeza = temp
            
        self._tamanio +=1
     
    def anexar(self, p_item):    
        """ Metodo para anexar un valor (p_item) al final de la lista,
        al finalizar actualiza el tamaño de la misma.
        Si la lista esta vacia, emerge un mensaje de error.
        Retorna: None"""
        temp = Nodo(p_item)
        
        if self.esta_vacia():
            self.cabeza = temp
            self.cola = temp
            
        else:
            temp.anterior = self.cola
            self.cola.siguiente = temp
            self.cola = temp
        
        self._tamanio += 1
    
    def insertar(self, posicion, item):    
        """ Metodo para insertar un valor (p_item) en una posicion (p_posicion) de la lista,
        al finalizar actualiza el tamaño de la misma.
        Si la posicion esta por fuera de la lista emerge un mensaje de error
        Retorna: None"""
        
        if posicion>self._tamanio or posicion<0:
           raise ValueError("Posición fuera de rango")
           
        if posicion == 0:
           self.agregar(item)   
        elif posicion == self._tamanio:
           self.anexar(item)
        else:
           nuevo = Nodo(item)
           temp = self.cabeza
           
           for i in range (posicion-1):
               temp = temp.siguiente
               
           aux = temp.siguiente
           
           nuevo.anterior = temp
           nuevo.siguiente = aux
           
           temp.siguiente = nuevo
           aux.anterior = nuevo
           
           self._tamanio = self._tamanio+1


    def extraer (self, posicion=-1):
        """ Metodo para extraer un valor en una posicion (p_posicion) de la lista y devuelve el item en posicion,
        si el parametro no esta indicado, se elimina y devuelve el ultimo elemnto de la lista
        al finalizar actualiza el tamaño de la misma.
        Si la posicion esta por fuera de la lista emerge un mensaje de error."""
        
        if self.esta_vacia():
            raise ValueError("La lista está vacía")
        
        if posicion>=self._tamanio or posicion<-1:
            raise ValueError("Posición fuera de rango")
        
        elif posicion == 0:
            temp = self.cabeza
            aux = self.cabeza
            
            self.cabeza = temp.siguiente
            self._tamanio = self._tamanio-1
            return aux
        
        elif posicion == self._tamanio-1 or posicion == -1:
            temp = self.cola
            aux = self.cola
            
            self.cola = temp.anterior
            self._tamanio = self._tamanio-1
            
            return aux
        
        else:
            temp = self.cabeza
            for i in range (posicion):
                temp = temp.siguiente
                
            aux = temp.siguiente
            aux2 = temp.anterior
            
            aux2.siguiente = aux
            aux.anterior = aux2
            
            self._tamanio = self._tamanio-1
            
            return temp

    def copiar(self):
        """ Metodo para copiar los elementos de la lista al final de una nueva lista,
        devuelve la copia de dicha lista"""
        copia = ListaDobleEnlazada()
        
        for nodo in self:
            copia.anexar(nodo.dato)

        
        return copia
        
    def invertir(self):
        """ Metodo para invertir el orden de los elementos de la lista."""
        if self.esta_vacia():
            raise ValueError("La lista está vacía")
        primer_nodo = self.cabeza
        segundo_nodo = primer_nodo.siguiente
            
            #el primer nodo es el ultimo
        primer_nodo.siguiente = None
        primer_nodo.anterior = segundo_nodo #doy vuelta la flechita
            
            #recorro la lista para ir cambiando las flechitas:
        while segundo_nodo != None:
            segundo_nodo.anterior = segundo_nodo.siguiente
            segundo_nodo.siguiente = primer_nodo
                #muevo:
            primer_nodo = segundo_nodo
            segundo_nodo = segundo_nodo.anterior
        self.cabeza = primer_nodo
        

    
    def concatenar(self, l1 : ListaDobleEnlazada):
        """ Metodo para cocatenar dos listas doblemente enlazadas,
        Recibe una lista como argumento y retorna la lista actual habiendo cocatenado la que paso como parametro al final.
        al finalizar actualiza el tamaño de la misma.
        Si la posicion esta por fuera de la lista emerge un mensaje de error"""
        if l1.tamanio == 0:
            raise IndexError("La lista a concatenar esta vacia")
            return self
        else:
            cabeza=l1.cabeza
            self.cola.siguiente = cabeza 
            l1.cabeza.anterior = self.cola
            self.cola = l1.cola
            self._tamanio += l1.tamanio
            return self
    
    def _add_(self, l1: ListaDobleEnlazada()):
        """Sobrecarga del operador suma para cocatenar dos listas doblemente enlazadas """
        return self.cocatenar(l1)        
    
    def ordenar (self):
        """ Metodo para ordenar de menor a mayor los elementos de la lista """
        fin = None
        while self.cabeza != fin:
            actual = self.cabeza 
            temp = self.cabeza 
            
            while temp.siguiente != fin: 
                cambia = temp.siguiente 
                if temp.dato > cambia.dato:
                    temp.siguiente = cambia.siguiente 
                    cambia.siguiente = temp 
                    if temp != self.cabeza:
                        actual.siguiente = cambia 
                    else:
                        self.cabeza = cambia
                    aux = temp
                    temp = cambia 
                    cambia = aux 
                actual = temp 
                temp = temp.siguiente 
            fin=temp