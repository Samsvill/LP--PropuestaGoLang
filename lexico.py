import ply.lex as lex

reserved = {
  'si':'SI',
  'para':'PARA',
  'mientras':'MIENTRAS',
  'clase':'CLASE',
  'imprimir':'IMPRIMIR',
  'ingresar':'INGRESAR',
  'y':'Y',
  'o':'O',
  'no':'NO'
}

tokens = [
  'ENTERO',
  'FLOTANTE',
  'COMPLEJO',
  'MENOS',
  'MAS',
  'PRODUCTO',
  'DIVISION',
  'LPAREN',
  'RPAREN',
  'VARIABLE',
  'IGUAL',
  'MENORQUE',
  'MAYORQUE',
  'DIFERENTE',
  'COMPARA_IGUAL',
  'PUNTO_COMA',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_MAS     = r'\+'
t_MENOS   = r'-'
t_PRODUCTO   = r'\*'
t_DIVISION = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_IGUAL = r'='
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_DIFERENTE = r'!='
t_COMPARA_IGUAL = r'=='
t_PUNTO_COMA = r';'

# A regular expression rule with some action code
def t_FLOTANTE(t):
  r'\d+\.\d+'
  return t
  
def t_ENTERO(t):
  r'\d+' 
  return t

def t_COMPLEJO(t): #un tipo de dato nuevo
  r'\d+j+' 
  return t

def t_VARIABLE(t):
  r'[a-zA-Z_][a-zA-Z0-9]*'
  t.type = reserved.get(t.value,'VARIABLE')
  return t
  
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_COMMENTS(t):
  r'\#.*'
  pass
  
# Error handling rule
def t_error(t):
  print("Caracter no permitido'%s'" % t.value[0])
  t.lexer.skip(1)
 
 # Build the lexer
lexer = lex.lex()

def getTokens(lexer):
  for tok in lexer:
    print(tok)

'''
instructions = 'clase Padre 44>334+var;'
linea=" "
lexer.input(instructions)
getTokens(lexer)
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")

'''