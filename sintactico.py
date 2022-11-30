import ply.yacc as sintactico
import time 
from lexico import tokens



def p_instrucciones(p): #REGLA PADRE !!!
  '''instrucciones : impresion
                      | for
                      | for2
                      | for3
                      | mapa
                      | si
                      | array
                      '''

#---------------------------IMPRESION DE DATOS----------------------------------------
def p_impresion(p):
  'impresion : PRINT LPAREN dato RPAREN'

def p_dato(p):
  '''dato : INT 
  | STRING
  | FLOAT
  | VARIABLE'''

#-------------------------- YANA - FOR (ESTRUCTURA DE CONTROL) ------------------------

#for con ciclo comun
def p_for(p):
  'for : FOR VARIABLE FASTDEC  INT PUNTO_COMA VARIABLE sigcomparacion  INT PUNTO_COMA VARIABLE MASMAS LCBRACKET '

#for estilo while
def p_for2(p):
  'for2 : FOR VARIABLE sigcomparacion INT LCBRACKET'

#for infinito
def p_for3(p):
  'for3 : FOR LCBRACKET instrucciones RCBRACKET'


def p_signoscomparacion(p):
  '''sigcomparacion : MENORQUE
                     | MAYORQUE
                     | DIFERENTE
                     | COMPARA_IGUAL'''



#----------------------------FIN FOR---------------------------

#--------------ARRAY - YANA (ESTRUCTURA DE DATOS) -------------

def p_array(p):
  '''array : VAR VARIABLE EQUALS LBRACKET INT RBRACKET TDATO LCBRACKET elementArray RCBRACKET
            | VARIABLE FASTDEC LBRACKET INT TDATO LCBRACKET elementArray RCBRACKET'''

def p_elementArray(p) :
  '''elementArray : dato
                   | dato COMMA elementArray '''

#----------------------- FIN - ARRAY -------------------------

#----------------------------SAM - MAPA (ESTRUCTURA DE DATOS) -----------------------
def p_mapa(p):
  '''mapa : VARIABLE EQUALS MAP LBRACKET TDATO RBRACKET TDATO LCBRACKET adentro RCBRACKET
  '''
def p_dataTokensAvailable(p):
  '''TDATO : TSTRING 
  | TINT
  | TFLOAT
  '''
def p_adentro(p):
  '''adentro : definicion 
  | definicion COMMA adentro
  '''
def p_definicion(p):
  ''' definicion : dato COLON dato
  '''
#----------------------------FIN - SAM - MAPA -----------------------

#---------------------------- IF - SAM ------------------------------
def p_if(p):
  "si : IF comparacion LCBRACKET instrucciones RCBRACKET"
def p_bloquecomparacion(p):
  "comparacion : dato sigcomparacion dato"
#------------------------- FIN - IF - SAM ---------------------------

 # ERRORES DE SINTAXIS
def p_error(p):
  if p:
    print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")
 
#-----------------------BUILDER------------------------
parser = sintactico.yacc()

def validaRegla(s):
  result = parser.parse(s)
  print(result)
#------------------Agregar al txt----------------------

#proyecto lenguaje y libreria
#------------------WHILE-------------------------------
while True:
  try:
    s = input('GoLang >> ')
  except EOFError:
    break
  if not s: continue
  file = open("log.txt","a") 
  file.write(time.strftime("\n [ %d/%m/%y -- %H:%M:%S ] ") + s )
  print(time.strftime("\n [ %d/%m/%y -- %H:%M:%S ] ") + s)
  file.close()
  validaRegla(s)
