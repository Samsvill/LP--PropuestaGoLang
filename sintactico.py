import ply.yacc as sintactico
from lexico import tokens

def p_instrucciones(p): #puede probar imprimir(var)
  '''instrucciones : asignacion
                    | impresion '''  
def p_asignacion(p): #puede reconocer a=20
  'asignacion : VARIABLE IGUAL valor'

def p_impresion(p):
  'impresion : PRINT LPAREN valor RPAREN'

def p_valor(p):
  '''valor : INT
          | STRING
          '''

def p_valor_variable(p):
  'valor : VARIABLE'
 # Error rule for syntax errors
def p_error(p):
  if p:
    print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")
 
 # Build the parser
parser = sintactico.yacc()

def validaRegla(s):
  result = parser.parse(s)
  print(result)