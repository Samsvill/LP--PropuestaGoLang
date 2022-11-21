import ply.yacc as sintactico
from lexico import tokens

def p_instrucciones(p): #puede probar imprimir(var)
  '''instrucciones : impresion
                      | for'''

def p_impresion(p):
  'impresion : PRINT LPAREN valor RPAREN'


def p_valor(p):
  '''valor : INT
          | STRING
          '''

#--------------------------YANA-------------------------------
def p_signoscomparacion(p):
  '''sigcomparacion : MENORQUE
                     | MAYORQUE
                     | DIFERENTE
                     | COMPARA_IGUAL'''
def p_for(p):
  '''for : FOR VARIABLE COLON EQUALS INT PUNTO_COMA VARIABLE sigcomparacion  INT PUNTO_COMA MAS MAS LCBRACKET '''


#----------------------------SAM - MAPA -----------------------
#def p_mapa(p):
#  '''mapa : STRING EQUALS MAP LBRACKET TDATA RBRACKET TDATA LCBRACKET adentro RCBRACKET
#  '''
#
#def p_dataTokensAvailable(p):
#  '''TDATA : TSTRING 
#  | TINT
#  '''
#
#def p_adentro(p):
#  '''adentro : dato 
#  | dato adentro
#  '''
#
#def p_dato(p):
#  ''' dato : tipo COLON tipo
#  '''
#
#def p_valor_variable(p):
#  'valor : VARIABLE'

#----------------------------FIN - SAM - MAPA -----------------------

 # Error rule for syntax errors
def p_error(p):
  if p:
    print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")
 
#-----------------------BUILDER-------------------------
parser = sintactico.yacc()

def validaRegla(s):
  result = parser.parse(s)
  print(result)
#Agregar al txt
  file = open('log.txt', 'a')
  file.write('\n' + s)
  file.close()


#------------------WHILE-------------------------------
while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  validaRegla(s)