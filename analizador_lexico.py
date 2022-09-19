from texto import Texto
from numero import Numero # Importamos la clase Numero para la creacion del objeto Numero
from aritmeticas import Aritmeticas # Lo mismo para la clase de creacion de Operaciones
from operador import Operador # Los operadores Mas, Menos... 
from errores import Errores
from estilo import Estilo
from funcion import Funcion


# Aqui se declaran los nombres de los tokens
tokens = (
    'RESTILO',
    'ROPERACIONES',
    'RTIPO',
    'RTEXTO',
    'RTIPO2',
    'RTEXTO2',
    'RFUNCION',
    'RTITULO',
    'RDESCRIPCION',
    'RCONTENIDO',
    'ROPERACION',
    'RCOLOR',
    'RTAMANIO',
    'RNUMERO',
    'RSUMA',
    'RRESTA',
    'RMULTIPLICACION',
    'RDIVISION',
    'RRAIZ',
    'RPOTENCIA',
    'RSENO',
    'RCOSENO',
    'RTANGENTE',
    'RMOD',
    'RINVERSO',
    'RESCRIBIR',
    'LLAA',
    'LLAC',
    'IGUAL',
    'DIV',
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'CORA',
    'CORC',
    'RAZUL',
    'RVERDE',
    'RROJO',
    'RNEGRO',
    'RBLANCO',
    'RGRIS',
    'RCELESTE',
    'RCAFE',
)

# Aqui se dan los valores de cada token
# En este caso decimos el valor que va a contener cada token osea, el lexema

t_RESTILO = r'Estilo'
t_RTIPO2  = r'TIPO'
t_RTEXTO2  = r'TEXTO'
t_RTIPO       = r'Tipo'
t_RTEXTO        = r'Texto'
t_RFUNCION      = r'Funcion'
t_RTITULO       = r'Titulo'
t_RDESCRIPCION  = r'Descripcion'
t_RCONTENIDO    = r'Contenido'
t_ROPERACION     = r'Operacion'
t_ROPERACIONES = r'Operaciones'
t_RCOLOR        = r'Color'
t_RTAMANIO      = r'Tamanio'
t_RSUMA       = r'SUMA'
t_RRESTA       = r'RESTA'
t_RMULTIPLICACION = r'MULTIPLICACION'
t_RDIVISION = r'DIVISION'
t_RRAIZ=r'RAIZ'
t_RMOD=r'MOD'
t_RSENO=r'SENO'
t_RPOTENCIA=r'POTENCIA'
t_RCOSENO=r'COSENO'
t_RTANGENTE=r'TANGENTE'
t_RINVERSO = r'INVERSO'
t_RESCRIBIR = r'ESCRIBIR'
t_RNUMERO     = r'Numero'
t_LLAA        = r'<'
t_LLAC        = r'>'
t_IGUAL       = r'='
t_DIV         = r'/'
t_CORA        = r'\['
t_CORC        = r'\]'
t_RAZUL       = r'AZUL'
t_RVERDE      = r'VERDE'
t_RROJO       = r'ROJO'
t_RNEGRO      = r'NEGRO'
t_RBLANCO = r'BLANCO'
t_RGRIS = r'GRIS'
t_RCELESTE = r'CELESTE'
t_RCAFE = r'CAFE'





# GRAMATICAS PARA NÚMEROS
# Pueden repasar la parte de gramáticas en la clase 4

# Gramática para números con punto decimal
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

# Gramática para números enteros
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Esta esa para poder aceptar cadenas de texto, lo vamos a usar más adelante
def t_CADENA(t):
    r'(\".*?\")'
    t.value = t.value[1:-1] #Se remueven las comillas de la entrada
    t.value = t.value.replace('\\t','\t')
    t.value = t.value.replace('\\n','\n')
    t.value = t.value.replace('\\"','\"')
    t.value = t.value.replace("\\'","\'")
    t.value = t.value.replace('\\\\','\\')
    return t

# Esta función cuando lee un salto de línea lo agrega al analizador para 
# Saber en qué linea se encuentra
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Caracteres ignorados en este caso los espacios y las tabulaciones
t_ignore = " \t"

# Este es un error léxico, pueden irlos almacenando en un array para obtenerlos después
def t_error(t):
    # print("Error Lexico, no se reconoce: '%s'" % t.value[0])
    error = Errores(t.value[0],'Error Lexico', find_column(input,t), t.lineno)
    errores_.append(error)
    t.lexer.skip(1)


# Contruccion del analizador lexico
import re
import ply.lex as lex
lexer = lex.lex()

# ------ DE AQUI EN ADELANTE EMPIEZA EL ANALIZADOR SINTACTICO ------
# Pueden guiarse con esto que les dejé, ya solo es de 
# agregar las demás operaciones que hagan falta y agregarlas en el archivo aritmeticas.py

# ANALIZADOR SINTACTICO
# Definicion de la gramatica


def p_init(t):
    'init : instrucciones'
    t[0] = t[1]
    return t[0]

def p_instrucciones_lista(t):
    '''instrucciones    : instrucciones instruccion
                        |   instruccion'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]

def p_instruccion(t):
    '''instruccion  : INSTIPO
                    | INSTEXTO
                    | INSTFUNCION
                    | INSTESTILO
                    
                    
'''
    t[0] = t[1]

def p_instruccionTipo(t):
    'INSTIPO    :   LLAA RTIPO LLAC instrucciones_2 LLAA DIV RTIPO LLAC'
    t[0] = t[4]

def p_instruccionTexto(t):
    'INSTEXTO   :   LLAA RTEXTO LLAC CADENA LLAA DIV RTEXTO LLAC'
    t[0] = Texto(t[4], t.lineno(1), find_column(input,t.slice[1]))

def p_instruccionFuncion(t):
    'INSTFUNCION    :   LLAA RFUNCION IGUAL RESCRIBIR LLAC instrucciones_2 LLAA DIV RFUNCION LLAC'
    t[0] = Funcion(t[6][0], t[6][1], t[6][2], t.lineno(1), find_column(input,t.slice[1]))

def p_instruccionEstilo(t):
    'INSTESTILO     :   LLAA RESTILO LLAC instrucciones_2 LLAA DIV RESTILO LLAC'
    t[0] = t[4]

def p_instrucciones_2_lista(t):
    'instrucciones_2 : instrucciones_2 instruccion_2'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_2_instruccion(t):
    'instrucciones_2 :  instruccion_2'
    t[0] = [t[1]]

def p_instruccion_2(t):
    'instruccion_2  :  LLAA ROPERACION IGUAL tipo LLAC instrucciones_2 LLAA DIV ROPERACION LLAC'
    if len(t[6]) == 2:
        t[0] = Aritmeticas(t[6][0], t[6][1], t[4], t.lineno(1), find_column(input,t.slice[1]))
    else:
        t[0] = Aritmeticas(t[6][0], None, t[4], t.lineno(1), find_column(input,t.slice[1]))

def p_instruccion_2_decimal(t):
    'instruccion_2 : LLAA RNUMERO LLAC DECIMAL LLAA DIV RNUMERO LLAC '
    t[0] = Numero(float(t[4]), t.lineno(1), find_column(input,t.slice[1]))

def p_instruccion_2_entero(t):
    'instruccion_2 : LLAA RNUMERO LLAC ENTERO LLAA DIV RNUMERO LLAC '
    t[0] = Numero(int(t[4]), t.lineno(1), find_column(input,t.slice[1]))

def p_instruccion_2_texto(t):
    'instruccion_2 : CADENA'
    t[0] = Numero(t[4], t.lineno(1), find_column(input,t.slice[1]))

def p_instruccion_2_titulo(t):
    'instruccion_2 : LLAA RTITULO LLAC ROPERACIONES LLAA DIV RTITULO LLAC'
    t[0] = t[4]

def p_instruccion_2_descripcion(t):
    'instruccion_2 : LLAA RDESCRIPCION LLAC CORA RTEXTO2 CORC LLAA DIV RDESCRIPCION LLAC'
    t[0] = t[5]

def p_instruccion_2_contenido(t):
    'instruccion_2 : LLAA RCONTENIDO LLAC CORA RTIPO2 CORC LLAA DIV RCONTENIDO LLAC'
    t[0] = t[5]

def p_instruccion_2_titulo_2(t):
    'instruccion_2 : LLAA RTITULO RCOLOR IGUAL COLOR RTAMANIO IGUAL ENTERO DIV LLAC'
    t[0] = Estilo(t[2], t[5], t[8], t.lineno(1), find_column(input,t.slice[1]))

def p_instruccion_2_descripcion_2(t):
    'instruccion_2 : LLAA RDESCRIPCION RCOLOR IGUAL COLOR RTAMANIO IGUAL ENTERO DIV LLAC'
    t[0] = Estilo(t[2], t[5], t[8], t.lineno(1), find_column(input,t.slice[1]))

def p_instruccion_2_contenido_2(t):
    'instruccion_2 : LLAA RCONTENIDO RCOLOR IGUAL COLOR RTAMANIO IGUAL ENTERO DIV LLAC'
    t[0] = Estilo(t[2], t[5], t[8], t.lineno(1), find_column(input,t.slice[1]))

def p_color(t):
    '''COLOR    : RAZUL 
                | RVERDE 
                | RROJO 
                | RNEGRO 
                | RBLANCO 
                | RGRIS 
                | RCELESTE 
                | RCAFE'''
    t[0] = t[1]

def p_tipo(t):
    '''tipo :   RSUMA
            |   RRESTA
            |   RMULTIPLICACION
            |   RDIVISION
            |   RINVERSO
            |   RMOD
            |   RRAIZ
            |   RSENO
            |   RCOSENO
            |   RTANGENTE
            |   RPOTENCIA
    '''
    if t[1] == 'SUMA':
        t[0] = Operador.SUMA
    elif t[1] == 'RESTA':
        t[0] = Operador.RESTA
    elif t[1] == 'MULTIPLICACION':
        t[0] = Operador.MULTIPLICACION
    elif t[1] == 'DIVISION':
        t[0] = Operador.DIVISION
    elif t[1] == 'INVERSO':
        t[0] = Operador.INVERSO
    elif t[1] == 'MOD':
        t[0] = Operador.MODULO
    elif t[1] == 'RAIZ':
        t[0] = Operador.RAIZ        
    elif t[1] == 'SENO':
        t[0] = Operador.SENO
    elif t[1] == 'COSENO':
        t[0] = Operador.COSENO
    elif t[1] == 'TANGENTE':
        t[0] = Operador.TANGENTE
    elif t[1] == 'POTENCIA':
        t[0] = Operador.POTENCIA   
# Aqui reconoce un error de sintaxis, pueden crear un array e irlos agregando
# para obtenerlos después
def p_error(t):
    print("Error de sintaxis en '%s'" % t.value)

# Esta función busca la columna en la que se encuentra el token o lexema
def find_column(inp, tk):
    try:
        line_start = inp.rfind('\n',0,tk.lexpos) + 1
        return (tk.lexpos - line_start) + 1
    except:
        return 0

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    lexer.lineno = 1
    return parser.parse(input)

global input
global errores_
errores_ = []

def actualizar_input(entrada):
    global input
    input=entrada

