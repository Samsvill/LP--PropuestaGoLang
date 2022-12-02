
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CASE COLON COMMA COMPARA_IGUAL DEFAULT DIFERENTE DIV DQMARK ELSE EQUALS FALLTHROUGH FASTDEC FLOAT FOR FUNC IF INT LBRACKET LCBRACKET LPAREN MAP MAS MASMAS MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MENOSMENOS MUL PRINT PRINTLN PUNTO_COMA RANGE RBRACKET RCBRACKET RETURN RPAREN STRING SWITCH TFLOAT TINT TSTRING VAR VARIABLEinstrucciones : impresion\n                      | for\n                      | for2\n                      | for3\n                      | mapa\n                      | si\n                      | array\n                      | funcion\n                      | concatDatos\n                      | ArraySemantica\n                      | switchh\n                      | asignaciones\n                      | expresionCondicion\n                      impresion : PRINT LPAREN dato RPAREN\n  | PRINTLN LPAREN dato RPARENdato : INT \n  | STRING\n  | FLOAT\n  | VARIABLEfor : FOR VARIABLE FASTDEC  INT PUNTO_COMA VARIABLE sigcomparacion  INT PUNTO_COMA VARIABLE MASMAS LCBRACKET for2 : FOR VARIABLE sigcomparacion INT LCBRACKETfor3 : FOR LCBRACKET instrucciones RCBRACKETsigcomparacion : MENORQUE\n                     | MAYORQUE\n                     | DIFERENTE\n                     | COMPARA_IGUAL\n                     | MAYORIGUAL\n                     | MENORIGUAL\n                     array : VAR VARIABLE EQUALS LBRACKET INT RBRACKET TDATA LCBRACKET elementArray RCBRACKET\n            | VARIABLE FASTDEC LBRACKET INT TDATA LCBRACKET elementArray RCBRACKETelementArray : dato\n                   | dato COMMA elementArray funcion : FUNC nombreFuncion LPAREN RPAREN LCBRACKET instrucciones RCBRACKET\n              | FUNC nombreFuncion LPAREN parametrosF RPAREN LCBRACKET instrucciones RCBRACKETnombreFuncion : VARIABLEparametrosF : VARIABLE TDATA\n                | VARIABLE TDATA COMMA parametrosFmapa : VARIABLE EQUALS MAP LBRACKET TDATA RBRACKET TDATA LCBRACKET adentro RCBRACKET\n  TDATA : TSTRING \n  | TINT\n  | TFLOAT\n  adentro : definicion \n  | definicion COMMA adentro\n   definicion : dato COLON dato\n  si : IF comparacion LCBRACKET instrucciones RCBRACKETcomparacion : dato sigcomparacion datoasignaciones : varsimple\n  | varobviado\n  | decfastvarsimple : VAR VARIABLE TDATA EQUALS datovarobviado : VAR VARIABLE EQUALS datodecfast : VARIABLE FASTDEC datoconcatDatos : STRING MAS STRING\n                  | INT MAS INT ArraySemantica :  VAR VARIABLE EQUALS LBRACKET INT RBRACKET TSTRING LCBRACKET elementStringS RCBRACKET\n            | VARIABLE FASTDEC LBRACKET INT TINT LCBRACKET elementIntS RCBRACKETelementStringS : STRING\n                   | STRING COMMA elementStringS elementIntS : INT\n                   | INT COMMA elementIntS expresionCondicion : VARIABLE FASTDEC comparacionswitchh : SWITCH VARIABLE LCBRACKET cases def RCBRACKETcases : case1 \n  | case1  casescase1 : CASE INT COLON instruccionesdef : DEFAULT COMMA instrucciones'
    
_lr_action_items = {'PRINT':([0,31,62,98,111,114,115,],[15,15,15,15,15,15,15,]),'PRINTLN':([0,31,62,98,111,114,115,],[16,16,16,16,16,16,16,]),'FOR':([0,31,62,98,111,114,115,],[17,17,17,17,17,17,17,]),'VARIABLE':([0,17,20,21,22,24,28,29,31,33,50,51,52,53,54,55,62,63,64,69,83,90,98,107,111,112,114,115,130,132,135,138,149,150,],[18,30,40,41,43,45,40,40,18,40,-23,-24,-25,-26,-27,-28,18,40,40,86,40,105,18,40,18,86,18,18,40,40,40,147,40,40,]),'IF':([0,31,62,98,111,114,115,],[20,20,20,20,20,20,20,]),'VAR':([0,31,62,98,111,114,115,],[21,21,21,21,21,21,21,]),'FUNC':([0,31,62,98,111,114,115,],[22,22,22,22,22,22,22,]),'STRING':([0,20,28,29,31,33,44,50,51,52,53,54,55,62,63,64,83,98,107,111,114,115,130,132,135,136,149,150,153,],[23,38,38,38,23,38,70,-23,-24,-25,-26,-27,-28,23,38,38,38,23,38,23,23,23,38,38,38,146,38,38,146,]),'INT':([0,20,28,29,31,33,34,48,49,50,51,52,53,54,55,58,62,63,64,81,83,89,98,107,108,111,114,115,116,130,132,133,135,149,150,],[19,37,37,37,19,37,61,74,75,-23,-24,-25,-26,-27,-28,78,19,37,37,96,37,104,19,37,120,19,19,19,129,37,37,120,37,37,37,]),'SWITCH':([0,31,62,98,111,114,115,],[24,24,24,24,24,24,24,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,25,26,27,37,38,39,40,59,60,61,70,72,73,76,80,82,91,95,97,113,124,131,134,137,148,151,152,158,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-47,-48,-49,-16,-17,-18,-19,-61,-52,-54,-53,-14,-15,-22,-46,-51,-21,-45,-50,-62,-33,-30,-56,-34,-38,-29,-55,-20,]),'RCBRACKET':([2,3,4,5,6,7,8,9,10,11,12,13,14,25,26,27,37,38,39,40,56,59,60,61,70,72,73,76,79,80,82,91,95,97,101,110,113,118,119,120,121,124,125,127,131,134,137,139,140,142,143,144,145,146,148,151,152,155,156,157,158,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-47,-48,-49,-16,-17,-18,-19,76,-61,-52,-54,-53,-14,-15,-22,95,-46,-51,-21,-45,-50,113,124,-62,131,-31,-59,134,-33,137,-66,-30,-56,-34,148,-42,-32,-60,151,152,-57,-38,-29,-55,-43,-44,-58,-20,]),'CASE':([2,3,4,5,6,7,8,9,10,11,12,13,14,25,26,27,37,38,39,40,59,60,61,70,71,72,73,76,80,82,88,91,95,97,113,124,128,131,134,137,148,151,152,158,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-47,-48,-49,-16,-17,-18,-19,-61,-52,-54,-53,89,-14,-15,-22,-46,-51,89,-21,-45,-50,-62,-33,-65,-30,-56,-34,-38,-29,-55,-20,]),'DEFAULT':([2,3,4,5,6,7,8,9,10,11,12,13,14,25,26,27,37,38,39,40,59,60,61,70,72,73,76,80,82,87,88,91,95,97,103,113,124,128,131,134,137,148,151,152,158,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-47,-48,-49,-16,-17,-18,-19,-61,-52,-54,-53,-14,-15,-22,-46,-51,102,-63,-21,-45,-50,-64,-62,-33,-65,-30,-56,-34,-38,-29,-55,-20,]),'LPAREN':([15,16,42,43,],[28,29,69,-35,]),'LCBRACKET':([17,35,37,38,39,40,45,66,67,68,75,80,84,93,94,99,117,122,123,154,],[31,62,-16,-17,-18,-19,71,-39,-40,-41,91,-46,98,107,108,111,130,135,136,158,]),'EQUALS':([18,41,65,66,67,68,],[32,64,83,-39,-40,-41,]),'FASTDEC':([18,30,],[33,48,]),'MAS':([19,23,],[34,44,]),'FLOAT':([20,28,29,33,50,51,52,53,54,55,63,64,83,107,130,132,135,149,150,],[39,39,39,39,-23,-24,-25,-26,-27,-28,39,39,39,39,39,39,39,39,39,]),'MENORQUE':([30,36,37,38,39,40,60,105,],[50,50,-16,-17,-18,-19,50,50,]),'MAYORQUE':([30,36,37,38,39,40,60,105,],[51,51,-16,-17,-18,-19,51,51,]),'DIFERENTE':([30,36,37,38,39,40,60,105,],[52,52,-16,-17,-18,-19,52,52,]),'COMPARA_IGUAL':([30,36,37,38,39,40,60,105,],[53,53,-16,-17,-18,-19,53,53,]),'MAYORIGUAL':([30,36,37,38,39,40,60,105,],[54,54,-16,-17,-18,-19,54,54,]),'MENORIGUAL':([30,36,37,38,39,40,60,105,],[55,55,-16,-17,-18,-19,55,55,]),'MAP':([32,],[57,]),'LBRACKET':([33,57,64,],[58,77,81,]),'RPAREN':([37,38,39,40,46,47,66,67,68,69,85,100,126,],[-16,-17,-18,-19,72,73,-39,-40,-41,84,99,-36,-37,]),'COMMA':([37,38,39,40,66,67,68,100,102,119,120,140,146,156,],[-16,-17,-18,-19,-39,-40,-41,112,114,132,133,149,153,-44,]),'COLON':([37,38,39,40,104,141,],[-16,-17,-18,-19,115,150,]),'TSTRING':([41,77,78,86,106,109,],[66,66,66,66,66,123,]),'TINT':([41,77,78,86,106,109,],[67,67,94,67,67,67,]),'TFLOAT':([41,77,78,86,106,109,],[68,68,68,68,68,68,]),'RBRACKET':([66,67,68,92,96,],[-39,-40,-41,106,109,]),'PUNTO_COMA':([74,129,],[90,138,]),'MASMAS':([147,],[154,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,31,62,98,111,114,115,],[1,56,79,110,125,127,128,]),'impresion':([0,31,62,98,111,114,115,],[2,2,2,2,2,2,2,]),'for':([0,31,62,98,111,114,115,],[3,3,3,3,3,3,3,]),'for2':([0,31,62,98,111,114,115,],[4,4,4,4,4,4,4,]),'for3':([0,31,62,98,111,114,115,],[5,5,5,5,5,5,5,]),'mapa':([0,31,62,98,111,114,115,],[6,6,6,6,6,6,6,]),'si':([0,31,62,98,111,114,115,],[7,7,7,7,7,7,7,]),'array':([0,31,62,98,111,114,115,],[8,8,8,8,8,8,8,]),'funcion':([0,31,62,98,111,114,115,],[9,9,9,9,9,9,9,]),'concatDatos':([0,31,62,98,111,114,115,],[10,10,10,10,10,10,10,]),'ArraySemantica':([0,31,62,98,111,114,115,],[11,11,11,11,11,11,11,]),'switchh':([0,31,62,98,111,114,115,],[12,12,12,12,12,12,12,]),'asignaciones':([0,31,62,98,111,114,115,],[13,13,13,13,13,13,13,]),'expresionCondicion':([0,31,62,98,111,114,115,],[14,14,14,14,14,14,14,]),'varsimple':([0,31,62,98,111,114,115,],[25,25,25,25,25,25,25,]),'varobviado':([0,31,62,98,111,114,115,],[26,26,26,26,26,26,26,]),'decfast':([0,31,62,98,111,114,115,],[27,27,27,27,27,27,27,]),'comparacion':([20,33,],[35,59,]),'dato':([20,28,29,33,63,64,83,107,130,132,135,149,150,],[36,46,47,60,80,82,97,119,141,119,119,141,156,]),'nombreFuncion':([22,],[42,]),'sigcomparacion':([30,36,60,105,],[49,63,63,116,]),'TDATA':([41,77,78,86,106,109,],[65,92,93,100,117,122,]),'parametrosF':([69,112,],[85,126,]),'cases':([71,88,],[87,103,]),'case1':([71,88,],[88,88,]),'def':([87,],[101,]),'elementArray':([107,132,135,],[118,142,144,]),'elementIntS':([108,133,],[121,143,]),'adentro':([130,149,],[139,155,]),'definicion':([130,149,],[140,140,]),'elementStringS':([136,153,],[145,157,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> impresion','instrucciones',1,'p_instrucciones','sintactico.py',8),
  ('instrucciones -> for','instrucciones',1,'p_instrucciones','sintactico.py',9),
  ('instrucciones -> for2','instrucciones',1,'p_instrucciones','sintactico.py',10),
  ('instrucciones -> for3','instrucciones',1,'p_instrucciones','sintactico.py',11),
  ('instrucciones -> mapa','instrucciones',1,'p_instrucciones','sintactico.py',12),
  ('instrucciones -> si','instrucciones',1,'p_instrucciones','sintactico.py',13),
  ('instrucciones -> array','instrucciones',1,'p_instrucciones','sintactico.py',14),
  ('instrucciones -> funcion','instrucciones',1,'p_instrucciones','sintactico.py',15),
  ('instrucciones -> concatDatos','instrucciones',1,'p_instrucciones','sintactico.py',16),
  ('instrucciones -> ArraySemantica','instrucciones',1,'p_instrucciones','sintactico.py',17),
  ('instrucciones -> switchh','instrucciones',1,'p_instrucciones','sintactico.py',18),
  ('instrucciones -> asignaciones','instrucciones',1,'p_instrucciones','sintactico.py',19),
  ('instrucciones -> expresionCondicion','instrucciones',1,'p_instrucciones','sintactico.py',20),
  ('impresion -> PRINT LPAREN dato RPAREN','impresion',4,'p_impresion','sintactico.py',25),
  ('impresion -> PRINTLN LPAREN dato RPAREN','impresion',4,'p_impresion','sintactico.py',26),
  ('dato -> INT','dato',1,'p_dato','sintactico.py',29),
  ('dato -> STRING','dato',1,'p_dato','sintactico.py',30),
  ('dato -> FLOAT','dato',1,'p_dato','sintactico.py',31),
  ('dato -> VARIABLE','dato',1,'p_dato','sintactico.py',32),
  ('for -> FOR VARIABLE FASTDEC INT PUNTO_COMA VARIABLE sigcomparacion INT PUNTO_COMA VARIABLE MASMAS LCBRACKET','for',12,'p_for','sintactico.py',40),
  ('for2 -> FOR VARIABLE sigcomparacion INT LCBRACKET','for2',5,'p_for2','sintactico.py',44),
  ('for3 -> FOR LCBRACKET instrucciones RCBRACKET','for3',4,'p_for3','sintactico.py',48),
  ('sigcomparacion -> MENORQUE','sigcomparacion',1,'p_signoscomparacion','sintactico.py',52),
  ('sigcomparacion -> MAYORQUE','sigcomparacion',1,'p_signoscomparacion','sintactico.py',53),
  ('sigcomparacion -> DIFERENTE','sigcomparacion',1,'p_signoscomparacion','sintactico.py',54),
  ('sigcomparacion -> COMPARA_IGUAL','sigcomparacion',1,'p_signoscomparacion','sintactico.py',55),
  ('sigcomparacion -> MAYORIGUAL','sigcomparacion',1,'p_signoscomparacion','sintactico.py',56),
  ('sigcomparacion -> MENORIGUAL','sigcomparacion',1,'p_signoscomparacion','sintactico.py',57),
  ('array -> VAR VARIABLE EQUALS LBRACKET INT RBRACKET TDATA LCBRACKET elementArray RCBRACKET','array',10,'p_array','sintactico.py',67),
  ('array -> VARIABLE FASTDEC LBRACKET INT TDATA LCBRACKET elementArray RCBRACKET','array',8,'p_array','sintactico.py',68),
  ('elementArray -> dato','elementArray',1,'p_elementArray','sintactico.py',71),
  ('elementArray -> dato COMMA elementArray','elementArray',3,'p_elementArray','sintactico.py',72),
  ('funcion -> FUNC nombreFuncion LPAREN RPAREN LCBRACKET instrucciones RCBRACKET','funcion',7,'p_funciones','sintactico.py',79),
  ('funcion -> FUNC nombreFuncion LPAREN parametrosF RPAREN LCBRACKET instrucciones RCBRACKET','funcion',8,'p_funciones','sintactico.py',80),
  ('nombreFuncion -> VARIABLE','nombreFuncion',1,'p_nombreFuncion','sintactico.py',82),
  ('parametrosF -> VARIABLE TDATA','parametrosF',2,'p_parametrosfuncion','sintactico.py',85),
  ('parametrosF -> VARIABLE TDATA COMMA parametrosF','parametrosF',4,'p_parametrosfuncion','sintactico.py',86),
  ('mapa -> VARIABLE EQUALS MAP LBRACKET TDATA RBRACKET TDATA LCBRACKET adentro RCBRACKET','mapa',10,'p_mapa','sintactico.py',93),
  ('TDATA -> TSTRING','TDATA',1,'p_dataTokensAvailable','sintactico.py',96),
  ('TDATA -> TINT','TDATA',1,'p_dataTokensAvailable','sintactico.py',97),
  ('TDATA -> TFLOAT','TDATA',1,'p_dataTokensAvailable','sintactico.py',98),
  ('adentro -> definicion','adentro',1,'p_adentro','sintactico.py',101),
  ('adentro -> definicion COMMA adentro','adentro',3,'p_adentro','sintactico.py',102),
  ('definicion -> dato COLON dato','definicion',3,'p_definicion','sintactico.py',105),
  ('si -> IF comparacion LCBRACKET instrucciones RCBRACKET','si',5,'p_if','sintactico.py',111),
  ('comparacion -> dato sigcomparacion dato','comparacion',3,'p_bloquecomparacion','sintactico.py',113),
  ('asignaciones -> varsimple','asignaciones',1,'p_asignaciones','sintactico.py',118),
  ('asignaciones -> varobviado','asignaciones',1,'p_asignaciones','sintactico.py',119),
  ('asignaciones -> decfast','asignaciones',1,'p_asignaciones','sintactico.py',120),
  ('varsimple -> VAR VARIABLE TDATA EQUALS dato','varsimple',5,'p_simplevar','sintactico.py',122),
  ('varobviado -> VAR VARIABLE EQUALS dato','varobviado',4,'p_varobviado','sintactico.py',124),
  ('decfast -> VARIABLE FASTDEC dato','decfast',3,'p_decfast','sintactico.py',126),
  ('concatDatos -> STRING MAS STRING','concatDatos',3,'p_ConcatenacionDeDatos','sintactico.py',132),
  ('concatDatos -> INT MAS INT','concatDatos',3,'p_ConcatenacionDeDatos','sintactico.py',133),
  ('ArraySemantica -> VAR VARIABLE EQUALS LBRACKET INT RBRACKET TSTRING LCBRACKET elementStringS RCBRACKET','ArraySemantica',10,'p_SemanticaARRAY','sintactico.py',137),
  ('ArraySemantica -> VARIABLE FASTDEC LBRACKET INT TINT LCBRACKET elementIntS RCBRACKET','ArraySemantica',8,'p_SemanticaARRAY','sintactico.py',138),
  ('elementStringS -> STRING','elementStringS',1,'p_ElementstringA','sintactico.py',142),
  ('elementStringS -> STRING COMMA elementStringS','elementStringS',3,'p_ElementstringA','sintactico.py',143),
  ('elementIntS -> INT','elementIntS',1,'p_ElementIntA','sintactico.py',145),
  ('elementIntS -> INT COMMA elementIntS','elementIntS',3,'p_ElementIntA','sintactico.py',146),
  ('expresionCondicion -> VARIABLE FASTDEC comparacion','expresionCondicion',3,'p_expresionCondiciones','sintactico.py',150),
  ('switchh -> SWITCH VARIABLE LCBRACKET cases def RCBRACKET','switchh',6,'p_switch','sintactico.py',155),
  ('cases -> case1','cases',1,'p_cases','sintactico.py',157),
  ('cases -> case1 cases','cases',2,'p_cases','sintactico.py',158),
  ('case1 -> CASE INT COLON instrucciones','case1',4,'p_case','sintactico.py',160),
  ('def -> DEFAULT COMMA instrucciones','def',3,'p_def','sintactico.py',162),
]
