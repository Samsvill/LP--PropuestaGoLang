import ply.yacc as sintactico
import time 
from lexico import tokens
from tkinter import *

root = Tk()
caja_resultados= Text(root)
caja_resultados.config(bd=0, padx=6, pady=4,font=("JetBrains Mono",12) ,
             insertbackground='white',spacing1='4',highlightthickness=2,
             insertborderwidth=10, background='black', fg='white',highlightbackground='#AEACAC',highlightcolor='#FFFFFF')
caja_resultados.grid(row=1, column=4,padx=10,sticky="w", columnspan=2)

def p_bloqueinstrucciones(p):
  '''bloqueI : instrucciones
              | instrucciones bloqueI '''


def p_instrucciones(p): #REGLA PADRE !!!
  '''instrucciones : impresion
                      | for
                      | for2
                      | for3
                      | mapa
                      | si
                      | array
                      | funcion
                      | concatDatos
                      | ArraySemantica
                      | switchh
                      | asignaciones
                      | expresionCondicion
                      '''

#---------------------------IMPRESION DE DATOS----------------------------------------
def p_impresion(p):
  '''impresion : PRINT LPAREN dato RPAREN
  | PRINTLN LPAREN dato RPAREN'''

def p_dato(p):
  '''dato : INT 
  | STRING
  | FLOAT
  | VARIABLE'''



#-------------------------- YANA - FOR (ESTRUCTURA DE CONTROL) ------------------------

#for con ciclo comun
def p_for(p):
  'for : FOR VARIABLE FASTDEC  INT PUNTO_COMA VARIABLE sigcomparacion  INT PUNTO_COMA VARIABLE incremento LCBRACKET  bloqueI  RCBRACKET'

#for estilo while
def p_for2(p):
  'for2 : FOR comparacionF LCBRACKET  bloqueI  RCBRACKET'

#for infinito
def p_for3(p):
  'for3 : FOR LCBRACKET bloqueI  RCBRACKET'

def p_incremento(p):
  '''incremento : MASMAS
                | MENOSMENOS'''
def p_signoscomparacion(p):
  '''sigcomparacion : MENORQUE
                     | MAYORQUE
                     | DIFERENTE
                     | COMPARA_IGUAL
                     | MAYORIGUAL
                     | MENORIGUAL
                     '''

def p_comparacion(p):
  'comparacionF : dato sigcomparacion dato'

#----------------------------FIN FOR---------------------------

#--------------ARRAY - YANA (ESTRUCTURA DE DATOS) -------------

def p_array(p):
  '''array : VAR VARIABLE EQUALS LBRACKET INT RBRACKET TDATA LCBRACKET elementArray RCBRACKET
            | VARIABLE FASTDEC LBRACKET INT RBRACKET  TDATA LCBRACKET elementArray RCBRACKET'''

def p_elementArray(p) :
  '''elementArray : dato
                   | dato COMMA elementArray '''

#----------------------- FIN - ARRAY -------------------------

#-------------------- DECLARACION DE FUNCIONES - YANA ------------------
#FUNCION BASICA
def p_funciones(p):
  '''funcion : funSimple
              | funcPa
              | funcRetorno
              | funcCompleta '''
def p_funcionSimple(p):
  'funSimple : FUNC nombreFuncion LPAREN RPAREN LCBRACKET bloqueI RCBRACKET'

def p_funcionParametros(p):
  'funcPa : FUNC nombreFuncion LPAREN parametrosF RPAREN LCBRACKET bloqueI RCBRACKET'

def p_funcRetorno(p):
  'funcRetorno : FUNC nombreFuncion LPAREN  RPAREN LPAREN datoReturn  RPAREN LCBRACKET bloqueI  returnF RCBRACKET'

def p_funcionCompleta(p):
  'funcCompleta : FUNC nombreFuncion LPAREN parametrosF RPAREN LPAREN datoReturn  RPAREN LCBRACKET bloqueI  returnF RCBRACKET'

def p_nombreFuncion(p):
  'nombreFuncion : VARIABLE'

def p_parametrosfuncion(p):
  '''parametrosF : VARIABLE TDATA
                | VARIABLE TDATA COMMA parametrosF'''
def p_datoReturn(p):
  '''datoReturn : TDATA
                  | TDATA COMMA TDATA'''
def p_return(p):
  '''returnF : RETURN dato
              | RETURN elementArray '''

#----------------------------SAM - MAPA (ESTRUCTURA DE DATOS) -----------------------
def p_mapa(p):
  '''mapa : VARIABLE EQUALS MAP LBRACKET TDATA RBRACKET TDATA LCBRACKET adentro RCBRACKET
  '''
def p_dataTokensAvailable(p):
  '''TDATA : TSTRING 
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

#---------------------------- IF - SAM (ESTRUCTURA DE CONTROL) ------------------------------
def p_if(p):
  "si : IF comparacion LCBRACKET instrucciones RCBRACKET"
def p_bloquecomparacion(p):
  "comparacion : dato sigcomparacion dato"
#------------------------- FIN - IF - SAM ---------------------------

#--------------------- DECLARACION DE VARIABLES (SAM) ---------------
def p_asignaciones(p):
  '''asignaciones : varsimple
  | varobviado
  | decfast'''
def p_simplevar(p):
  '''varsimple : VAR VARIABLE TDATA EQUALS dato'''
def p_varobviado(p):
  '''varobviado : VAR VARIABLE EQUALS dato'''
def p_decfast(p):
  '''decfast : VARIABLE FASTDEC dato'''

#------------------------REGLAS SEMANTICAS--------------------------
#--------------------------- YANALEEN ------------------------------
#El operador + no puede usarse entre dos tipos de datos diferentes
def p_ConcatenacionDeDatos(p):
  '''concatDatos : STRING MAS STRING
                  | INT MAS INT '''

#Los arreglos en GO solo pueden contener elementos de un mismo tipo
def p_SemanticaARRAY(p):
  '''ArraySemantica :  VAR VARIABLE EQUALS LBRACKET INT RBRACKET TSTRING LCBRACKET elementStringS RCBRACKET
            | VARIABLE FASTDEC LBRACKET INT TINT LCBRACKET elementIntS RCBRACKET'''


def p_ElementstringA(p):
  '''elementStringS : STRING
                   | STRING COMMA elementStringS '''
def p_ElementIntA(p):
  '''elementIntS : INT
                   | INT COMMA elementIntS '''
#-------------------------------- SAM ---------------------------------------
#--------------------------------- EXPRESIONES DE CONDICIONES -----------------------------
def p_expresionCondiciones(p):
  '''expresionCondicion : VARIABLE FASTDEC comparacion'''

#-------------------------- SWITCH (ESTRUCTURA DE CONTROL) ------------------------

def p_switch(p):
  '''switchh : SWITCH VARIABLE LCBRACKET cases def RCBRACKET'''
def p_cases(p):
  '''cases : case1 
  | case1  cases'''
def p_case(p):
  '''case1 : CASE INT COLON instrucciones'''
def p_def(p):
  '''def : DEFAULT COLON instrucciones'''
#-------------------------- FIN SWITCH (ESTRUCTURA DE CONTROL) ----------------------

 # ERRORES DE SINTAXIS
def p_error(p):
  if p:
    print(f"Error de sintaxis - Token: {p.type}, L??nea: {p.lineno}, Col: {p.lexpos}")
    caja_resultados.insert('1.0', f"Error de sintaxis - Token: {p.type}, L??nea: {p.lineno}, Col: {p.lexpos}\n")
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

# while True:
#   try:
#     s = input('GoLang >> ')
#   except EOFError:
#     break
#   if not s: continue
#   file = open("log.txt","a")
#   file.write(time.strftime("\n [ %d/%m/%y -- %H:%M:%S ] ") + s )
#   print(time.strftime("\n [ %d/%m/%y -- %H:%M:%S ] ") + s)
#   file.close()
#   validaRegla(s)
