import ply.lex as lex

reserved = {
  'if':'IF', #YANALEEN PLUAS{
  'for':'FOR',
  'else' : 'ELSE',
  'Print':'PRINT',
  'Println' : 'PRINTLN',

  'switch':'SWITCH',
  'return':'RETURN',
  'func':'FUNC',#YANALEENPLUAS}
  'select':'SELECT',#SAM{
  'import' : 'IMPORT',
  'case' : 'CASE',
  'break' : 'BREAK',
  'default' : 'DEFAULT',
  'struct' : 'STRUCT',
  'map' : 'MAP', #Sam
  'string' : 'TSTRING',
  'int' : 'TINT'
}

tokens = [
  'INT',
  'FLOTANTE',
  'COMPLEJO',
  'MENOS',
  'MAS',
  'PRODUCTO',
  'DIVISION',
  'LPAREN',
  'RPAREN',
  'VARIABLE',
  'STRING',
  'EQUALS',
  'MENORQUE',
  'MAYORQUE',
  'DIFERENTE',
  'COMPARA_IGUAL',
  'PUNTO_COMA',
  'LCBRACKET',
  'RCBRACKET',
  'INCREMENT',
  'LBRACKET',
  'RBRACKET',
  'DQMARK',
  'COLON',
  'COMMA'
] + list(reserved.values())

# TOKENS SIMPLES
t_MAS     = r'\+'
t_MENOS   = r'-'
t_PRODUCTO   = r'\*'
t_DIVISION = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUALS = r'='
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_DIFERENTE = r'!='
t_COMPARA_IGUAL = r'=='
t_PUNTO_COMA = r';'
t_LCBRACKET = r'\{'
t_RCBRACKET = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
#t_DQMARK = r'"'
t_COLON = r':'
t_COMMA = r','
t_STRING = r'"[a-zA-Z\w\s]*"'

# DEFINICION DE TOKENS
def t_FLOTANTE(t):
  r'\d+\.\d+'
  return t
  
def t_INT(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_VARIABLE(t):
  r'[a-zA-Z_][a-zA-Z0-9]*'
  t.type = reserved.get(t.value,'VARIABLE')
  return t


def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_INCREMENT(t):
  r'\+{2}'
  return t

 
# IGNORAR
t_ignore  = ' \t'

def t_COMMENTS(t):
  r'\#.*'
  pass
  
# ERRORES
def t_error(t):
  print("Caracter no permitido'%s'" % t.value[0])
  t.lexer.skip(1)
 
 # LEXER
lexer = lex.lex()

def getTokens(lexer):
  for tok in lexer:
    print(tok)

# PROBAR -------SAM----------------
Sam_instruc = """
nameAgeMap = map[string]int{
"James" : 50,
"Ali" :   39,
}
"""
lexer.input(Sam_instruc)
getTokens(lexer)
# FIN PROBAR -------SAM----------------

# SEGUIR LEYENDO
linea=" "
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")

