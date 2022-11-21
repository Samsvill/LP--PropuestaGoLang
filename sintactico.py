import ply.yacc as sintactico
from lexico import tokens

def p_instrucciones(p):
  '''instrucciones : asignacion
                    | impresion 
                    | mapa'''  
def p_asignacion(p): #puede reconocer a=20
  'asignacion : VARIABLE IGUAL tipo'

def p_impresion(p):
  'impresion : PRINT LPAREN tipo RPAREN'

def p_tipoDato(p):
  '''tipo : STRING 
  | INT'''


#----------------------------SAM - MAPA -----------------------
def p_mapa(p):
  '''mapa : STRING EQUALS MAP LBRACKET TDATA RBRACKET TDATA LCBRACKET adentro RCBRACKET
  '''

def p_dataTokensAvailable(p):
  '''TDATA : TSTRING 
  | TINT
  '''

def p_adentro(p):
  '''adentro : dato 
  | dato adentro
  '''

def p_dato(p):
  ''' dato : tipo COLON tipo
  '''

def p_valor_variable(p):
  'valor : VARIABLE'

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


#------------------WHILE-------------------------------
while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  validaRegla(s)