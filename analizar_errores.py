
import math
from errores import Errores


class Lexico:
    angular_abierta = 0
    igual = False

    def __init__(self,lista_cadena):
        self.objeto_errores=[]
        self.tokens_reservadas = {
            'Tipo'      : 't_TIPO',
            'Operacion' : 't_OPERACION',
            'Numero'    : 't_NUMERO',
            '<'         : 't_AA',
            '>'         : 't_AC',
            '='         : 't_IGUAL',
            '/'         : 't_DIV',
        }

        self.tokens_operaciones = {
            'SUMA'    : 't_SUMA',
            'RESTA'   : 't_RESTA',
            'MULTITPLICACION'    : 't_MULT',
            'DIVISION'    : 't_DIV',
        }
        self.errores = ['?',"$","~","!","¡","%","#","(",")",":",",","-","|","{","}","[","]","_","^","¨"]
        self.lista_cadena=lista_cadena
        self.linea = 1
        self.columna = 0

    def Analizar(self):
        tkn = '' # Token
        getToken = ''
        for i in range(len(self.lista_cadena)):
            cadena=self.lista_cadena[i]
            self.igual=False
            for j in range(len(cadena)):
                tkn+=self.Ignorar(cadena[j])
                if cadena[j] !=">" or cadena[j]!="=":
                    getToken=self.getToken(tkn)
            if getToken=="t_TIPO" and self.angular_abierta==2:
                self.angular_abierta=0
                n=i
        self.lista_cadena.pop(n)
        self.angular_abierta=0
        self.operacion(self.lista_cadena)        
            
                


    def operacion(self,lista):
        tkn=''
        getToken=''
        for i in range(len(lista)):
            cadena=lista[i]
            for j in range(len(cadena)):
                tkn+=self.Ignorar(cadena[j])
                print(tkn)
                if cadena[j] != "=":
                    getToken=self.getToken(tkn)
                if getToken=="t_OPERACION" and self.igual==True:
                    self.igual=False
                    tkn=""
                    print(getToken)
                    print(self.angular_abierta)
                if getToken=="t_SUMA" and self.angular_abierta==2:
                    self.angular_abierta=0
                    print(getToken)
                    



    

        
    def Ignorar(self, lexema):
        if lexema not in self.errores:
            if lexema == ' ':
                self.columna += 1
                return ''
            elif lexema == '\n':
                self.columna = 0
                self.linea += 1
                return ''
            else:
                if lexema == '<' or lexema == '>':
                    self.columna += 1
                    self.angular_abierta += 1 # Si esta en 1, es una angular abierta, si esta en 2, es una angular cerrada
                    return ''
                elif lexema == '=':
                    self.igual=True
                    self.columna += 1
                    return ''
                self.columna += 1
                return lexema
        else:
            self.columna += 1
            error = Errores(lexema, self.linea, self.columna)
            self.objeto_errores.append(error)
            return ''


    def get_objeto_errores(self):
        return self.objeto_errores    

    def getToken(self,cadena):
        tkn=cadena
        if tkn in self.tokens_reservadas:
            return self.tokens_reservadas[tkn]
        elif tkn in self.tokens_operaciones:
            return self.tokens_operaciones[tkn]    
        return ''    





