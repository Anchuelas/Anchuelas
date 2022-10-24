



# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 19:00:13 2022

@author: Samaniego Francisco
"""

from cola_doble import ColaDoble
import random 
class JuegoGuerra:
    
    def __init__(self, random_seed = 167):
        
        """Método inicializador del juego, se definen los valores y palos a utilizar, provenientes de la baraja
        de poker, los cuales son introducidos a una lista de python antes de crear el mazo, para ser manipulados
        de manera mas sencilla"""
        
        self.jugador1=ColaDoble()
        self.jugador2=ColaDoble()
        self.n_jugadores=2
        self.valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        # self.comparar = self.valores.index()
        self.palos = ['♠', '♥', '♦', '♣']
        random.seed(random_seed)
        self.barajar()
    
   
        
        
    @property
    def turnos_jugados(self):
        """Atributo del juego que cuenta la cantidad de turnos jugados, requerida por el test 
           Retorna: None"""
        pass
    
    
    @property
    def empate(self):
        """Atributo de clase que define si el juego termina en empate, requerida por el test
           Retorna: True or False"""
        return self._empate
    
    
    @property
    def ganador(self):
        """Atributo de clase que define el ganador del juego, requerida por el test
            Retorna: ganador del juego"""
        return self.jugador_ganador
   
    
   
    
    def crear_mazo(self):
        """Método para crear el mazo, se forma una lista con las combinaciones de los valores y palos correspondientes"""
        self.mazo=[]
        for x in self.valores:
            for y in self.palos:
                carta='{} {}'.format(x,y)
                self.mazo.append(carta)
    
    def iniciar_juego(self,n_semilla=0):
        
        """Método para empezar la partida, se definen la cantidad de turnos a jugar en total, en el caso de llegar se considerará
        empate"""
        
        self.cantidad_turnos=1000
        self._empate=False
        
        """Mezclamos las cartas de la lista mazo y se agregan a una cola doble: el mazo mezclado"""
    
        random.shuffle(self.mazo)
        self.mazo_mezclado=ColaDoble()
        for i in range (len(self.mazo)):
            self.mazo_mezclado.agregar_frente(self.mazo[i])
        
        """Se reparten las cartas a cada jugador, de modo tal que la primera carta del tope del mazo va para el jugador 1, la segunda para el 
           jugador 2 y asi intercaladamente hasta terminar con la cantidad total: 26 para cada uno, cada jugador es una estructura de datos del 
           tipo cola doble"""
       
        for i in range(26):
            
            
            self.jugador1.agregar_frente(self.mazo_mezclado.remover_frente())
            
            self.jugador2.agregar_frente(self.mazo_mezclado.remover_frente())
            
        """Se definen dos variables a utilizar durante el juego, la cantidad de cartas de cada jugador"""    
        
        self.num_cartasj1=len(self.jugador1)
        self.num_cartasj2=len(self.jugador2)
        
        print(self.jugador1)
        
        print(self.jugador2)
        
        """Número de turno jugado durante la simulación"""
        
        n_turno=0
    
        """Se definen las condiciones para que el juego acabe, mientras el número de turno jugado sea menor
           al número limite acordado por los jugadores, el juego seguirá, además el juego se mostrará por pantalla
           hasta que el ciclo se rompa"""
        
        while n_turno <self.cantidad_turnos:
            self.mostrar_juego(n_turno+1,self.jugador1.remover_frente(), self.jugador2.remover_frente(), estado='en juego') 
            n_turno +=1
            
            """Si el jugador 1 se queda sin cartas en su mazo, se rompe el ciclo y se declara al jugador 2 como ganador
               De la misma manera, si el jugador 2 se queda sin cartas en su mazo, se declara al jugador 1 como ganador
               Por último, si el n° de turnos jugados coincide con la cantidad acordada se declarará un empate"""
           
            if self.num_cartasj1 == 0:
                self.jugador_ganador= "Jugador 2"
                print('***JUGADOR 2 GANA LA PARTIDA***')
                break
            
            elif self.num_cartasj2 == 0:
                self.jugardor_ganador = "Jugador 1"
                print('***JUGADOR 1 GANA LA PARTIDA***')
                break
            
            elif n_turno == self.cantidad_turnos:
                self._empate = True
                print('***EMPATE***')
                break

            
            

    

    def mostrar_juego(self,turno,cartaj1, cartaj2, estado= 'en juego'):
        """Método para mostrar el juego por consola"""
        
        escala = ['2','3','4','5','6','7','8','9','1','J','Q','K','A']
       
        """Utilizamos el n° de indice para realizar la comparación en lugar del numero de la carta, así nos ahorramos los
           problemas con las letras"""
        
        if escala.index(cartaj1[0]) < escala.index(cartaj2[0]):
            print('------------------------------------------------------------')
            print(f'Turno: {turno}')
            print('   Jugador 1: ' )
            print('-X '*(self.num_cartasj1-1))
            print ("                 "f'{cartaj1 } {cartaj2 }')
            print('-X '*(self.num_cartasj2-1))
            
            print(  'Jugador 2 ')
            print('------------------------------------------------------------')
            self.num_cartasj1 =self.num_cartasj1-1
            self.num_cartasj2=self.num_cartasj2+1
            
            self.jugador2.agregar_final(cartaj1)
            self.jugador2.agregar_final(cartaj2)
           
            print(self.num_cartasj1)
            print(self.num_cartasj2)
        elif escala.index(cartaj1[0]) > escala.index(cartaj2[0]):
            print('------------------------------------------------------------')
            print(f'Turno: {turno}')
            print(  'Jugador 1 ' )
            print('-X '*(self.num_cartasj1-1))
            print ("              "f'{cartaj1 } {cartaj2 }')
            print('-X '*(self.num_cartasj2-1))
            
            print(  'Jugador 2 ')
            print('------------------------------------------------------------')
            self.num_cartasj2 -= 1
            self.num_cartasj1 += 1
            
            self.jugador1.agregar_final(cartaj2)
            self.jugador1.agregar_final(cartaj1)
            
            print(self.num_cartasj1)
            print(self.num_cartasj2)
            
        elif escala.index(cartaj1[0]) == escala.index(cartaj2[0]):
              print('----------------------------------------------------------')
              print("             ", "****Guerra!!!!****")
              print(f'Turno: {turno}')
              print(    'Jugador 1 ' )
              print('-X'*(self.num_cartasj1-5))
              cartaj1_1 = self.jugador1.remover_frente()
              cartaj2_1 = self.jugador2.remover_frente()
              cartaj1_2 = self.jugador1.remover_frente()
              cartaj2_2 = self.jugador2.remover_frente()
              cartaj1_3 = self.jugador1.remover_frente()
              cartaj2_3 = self.jugador1.remover_frente()
              cartaj1_4 = self.jugador1.remover_frente()
              cartaj2_4 = self.jugador2.remover_frente()
              print ("               ", f'{cartaj1 } {cartaj2 }', "-X"*6 , f'{cartaj1_4 } {cartaj2_4 }' )
              print('-X'*(self.num_cartasj2-5))
              print(    "Jugador 2")
              print('----------------------------------------------------------')
              if escala.index(cartaj1_4[0]) > escala.index(cartaj2_4[0]):
                  self.jugador1.agregar_final(cartaj1)
                  self.jugador1.agregar_final(cartaj2)
                  self.jugador1.agregar_final(cartaj1_1)
                  self.jugador1.agregar_final(cartaj2_1)
                  self.jugador1.agregar_final(cartaj1_2)
                  self.jugador1.agregar_final(cartaj2_2)
                  self.jugador1.agregar_final(cartaj1_3)
                  self.jugador1.agregar_final(cartaj2_3)
                  self.jugador1.agregar_final(cartaj1_4)                      
                  self.jugador1.agregar_final(cartaj2_4)
                  self.num_cartasj2 -= 5
                  self.num_cartasj1 += 5
                  print(self.num_cartasj1)
                  print(self.num_cartasj2)
                  
              if escala.index(cartaj1_4[0]) < escala.index(cartaj2_4[0]):
                 self.jugador2.agregar_final(cartaj1)
                 self.jugador2.agregar_final(cartaj2)
                 self.jugador2.agregar_final(cartaj1_1)
                 self.jugador2.agregar_final(cartaj2_1)
                 self.jugador2.agregar_final(cartaj1_2)
                 self.jugador2.agregar_final(cartaj2_2)
                 self.jugador2.agregar_final(cartaj1_3)
                 self.jugador2.agregar_final(cartaj2_3)
                 self.jugador2.agregar_final(cartaj1_4)                      
                 self.jugador2.agregar_final(cartaj2_4)
                 self.num_cartasj1 -= 5
                 self.num_cartasj2 += 5
                 print(self.num_cartasj1)
                 print(self.num_cartasj2)            
              elif escala.index(cartaj1_4[0]) == escala.index(cartaj2_4[0]):
                 print('--------------------------------------------------------')
                 print("             ", "****Guerra!!!!****")
                 print(f'Turno: {turno}')
                 print(  'Jugador 1 ' )
                 print('-X'*(self.num_cartasj1-9))
                 cartaj1_5 = self.jugador1.remover_frente()
                 cartaj2_5 = self.jugador2.remover_frente()
                 cartaj1_6 = self.jugador1.remover_frente()
                 cartaj2_6 = self.jugador2.remover_frente()
                 cartaj1_7=  self.jugador1.remover_frente()
                 cartaj2_7 = self.jugador1.remover_frente()
                 cartaj1_8 = self.jugador1.remover_frente()
                 cartaj2_8 = self.jugador2.remover_frente()
                 print ("               ", f'{cartaj1 } {cartaj2 }', "-X"*6 , f'{cartaj1_4 } {cartaj2_4 }' )
                 print ("               ", '-X'*6, f'{cartaj1_8 } {cartaj2_8 }' )
                 print('-X'*(self.num_cartasj2-9))
                 print(  "Jugador 2")
                 print('---------------------------------------------------------')
                 if escala.index(cartaj1_8[0]) > escala.index(cartaj2_8[0]):
                     self.jugador1.agregar_final(cartaj1)
                     self.jugador1.agregar_final(cartaj2)
                     self.jugador1.agregar_final(cartaj1_1)
                     self.jugador1.agregar_final(cartaj2_1)
                     self.jugador1.agregar_final(cartaj1_2)
                     self.jugador1.agregar_final(cartaj2_2)
                     self.jugador1.agregar_final(cartaj1_3)
                     self.jugador1.agregar_final(cartaj2_3)
                     self.jugador1.agregar_final(cartaj1_4)                      
                     self.jugador1.agregar_final(cartaj2_4)
                     self.jugador1.agregar_final(cartaj1_5)
                     self.jugador1.agregar_final(cartaj2_5)
                     self.jugador1.agregar_final(cartaj1_6)
                     self.jugador1.agregar_final(cartaj2_6)
                     self.jugador1.agregar_final(cartaj1_7)
                     self.jugador1.agregar_final(cartaj2_7)
                     self.jugador1.agregar_final(cartaj1_8)
                     self.jugador1.agregar_final(cartaj2_8)
                     self.num_cartasj1 += 9
                     self.num_cartasj2 -= 9
                     print(self.num_cartasj1)
                     print(self.num_cartasj2)
                 if escala.index(cartaj1_8[0]) <escala.index(cartaj2_8[0]):
                     self.jugador2.agregar_final(cartaj1)
                     self.jugador2.agregar_final(cartaj2)
                     self.jugador2.agregar_final(cartaj1_1)
                     self.jugador2.agregar_final(cartaj2_1)
                     self.jugador2.agregar_final(cartaj1_2)
                     self.jugador2.agregar_final(cartaj2_2)
                     self.jugador2.agregar_final(cartaj1_3)
                     self.jugador2.agregar_final(cartaj2_3)
                     self.jugador2.agregar_final(cartaj1_4)                      
                     self.jugador2.agregar_final(cartaj2_4)
                     self.jugador2.agregar_final(cartaj1_5)
                     self.jugador2.agregar_final(cartaj2_5)
                     self.jugador2.agregar_final(cartaj1_6)
                     self.jugador2.agregar_final(cartaj2_6) 
                     self.jugador2.agregar_final(cartaj1_7)
                     self.jugador2.agregar_final(cartaj2_7)
                     self.jugador2.agregar_final(cartaj1_8)
                     self.jugador2.agregar_final(cartaj2_8)
                     self.num_cartasj1 -= 9
                     self.num_cartasj2 += 9
                     print(self.num_cartasj1)
                     print(self.num_cartasj2)

    
    
    