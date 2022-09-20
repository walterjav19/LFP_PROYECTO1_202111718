import math
from expression import *
from operador import Operador
from generador import Generador

class Aritmeticas(Expression):
    
    def __init__(self, left, right, tipo, fila, column):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, column)


    def ejecutar(self, getER):
        genAux = Generador()
        generador = genAux.getInstance()
        
        izq = self.left.ejecutar(getER)
        if self.right is not None:
            der = self.right.ejecutar(getER)
            if self.tipo == Operador.SUMA:
                return generador.addExpresion(izq, der, '+') if getER else izq+der 
                return izq+der
            elif self.tipo == Operador.RESTA:
                 return generador.addExpresion(izq, der, '-') if getER else izq-der
                 return izq - der
            elif self.tipo == Operador.MULTIPLICACION:
                 return generador.addExpresion(izq, der, '*') if getER else izq*der
                 return izq * der
            elif self.tipo == Operador.DIVISION:
                if der != 0:
                     return generador.addExpresion(izq, der, '/') if getER else izq/der
                     return izq / der
                else:
                    print("Error: Division por cero")
                    return None
            elif self.tipo == Operador.POTENCIA:
                 return generador.addExpresion(izq, der, '^') if getER else izq**der 
                 return izq ** der
            elif self.tipo == Operador.MODULO:
                 return generador.addExpresion(izq, der, '%') if getER else izq%der 
                 return izq % der
            elif self.tipo == Operador.RAIZ:
                return generador.addExpresion_raiz(izq, der, '^') if getER else izq ** (1/der) 
                return izq ** 1/der                
            else:
                return 0
        else:
            if self.tipo == Operador.INVERSO:
                return generador.addExpresion(1, izq, '/') if getER else 1/izq 
                return izq**-1
            elif self.tipo == Operador.SENO:
                return generador.addExpresion_trigonom(izq, 'SENO') if getER else math.sin(izq)
                return math.sin(izq)                
            elif self.tipo == Operador.COSENO:
                return generador.addExpresion_trigonom(izq, 'COSENO') if getER else math.cos(izq) 
                return math.sin(izq)                    
            elif self.tipo == Operador.TANGENTE:
                return generador.addExpresion_trigonom(izq, 'TANGENTE') if getER else math.tan(izq) 
                return math.sin(izq)                
 
    
