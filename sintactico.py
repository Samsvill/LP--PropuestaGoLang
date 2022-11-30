import ply.yacc as sintactico
import time 
from lexico import tokens



def p_instrucciones(p): #puede probar imprimir(var)
  '''instrucciones : impresion
                      | for
                      | for2
                      | for3
                      | mapa
                      | si
                      | array
                      '''

def p_impresion(p):
  'impresion : PRINT LPAREN valor RPAREN'


def p_valor(p):
  '''valor : INT
          | STRING
          '''

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
  '''array : VAR VARIABLE EQUALS LBRACKET INT RBRACKET TDATA LCBRACKET elementArray RCBRACKET
            | VARIABLE FASTDEC LBRACKET INT TDATA LCBRACKET elementArray RCBRACKET'''

def p_elementArray(p) :
  '''elementArray : valor
                   | valor COMMA elementArray '''

#----------------------- FIN - ARRAY -------------------------

#----------------------------SAM - MAPA -----------------------
def p_mapa(p):
  '''mapa : VARIABLE EQUALS MAP LBRACKET TDATA RBRACKET TDATA LCBRACKET adentro RCBRACKET
  '''

def p_dataTokensAvailable(p):
  '''TDATA : TSTRING 
  | TINT
  '''

def p_adentro(p):
  '''adentro : dato 
  | dato adentro
  '''

def p_tipo(p):
  '''tipo : INT 
  | STRING'''

def p_dato(p):
  ''' dato : tipo COLON tipo
  '''

def p_valor_variable(p):
  'valorV : VARIABLE'

#----------------------------FIN - SAM - MAPA -----------------------

#---------------------------- IF - SAM ------------------------------

def p_bloquecodigo(p):
  "bloque : instrucciones "
def p_logico(p):
  '''logicos : COMPARA_IGUAL
  | MAYORQUE
  | MENORQUE'''

def p_if(p):
  "si : IF  LCBRACKET bloque RCBRACKET"

#------------------------- FIN - IF - SAM ---------------------------

 # Error rule for syntax errors
def p_error(p):
  if p:
    print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")
 
#-----------------------BUILDER------------------------

parser = sintactico.yacc()
#------------------Agregar al txt----------------------
  


#proyecto lenguaje y libreria
#------------------WHILE-------------------------------
#while True:
#  try:
#    s = input('GoLang >> ')
#  except EOFError:
#    break
#  if not s: continue
#  file = open("log.txt","a")
#  file.write(time.strftime("\n [ %d/%m/%y -- %H:%M:%S ] ") + s )
#  print(time.strftime("\n [ %d/%m/%y -- %H:%M:%S ] ") + s)
#  file.close()
#  validaRegla(s)