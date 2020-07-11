import ply.yacc as sintaxis
import lexico
tokens = lexico.tokens

# def p_sentencias(p):
#     '''sentencias : asignacion
#     | imprimir
#     | while
#     | for
#     | if 
#     | tupla
#     | declaracion'''

def p_sentencias(p):
    '''sentencias : asignacion
    | imprimir
    | declaracion
    | condicion'''

def p_imprimir(p):
    'imprimir : CONSOLE WRITELINE LPAREN valor RPAREN SEMICOLON'

def p_valor(p):
    '''valor : TRUE
        | FALSE
        | SSTRING
        | DSTRING
        | expresion'''
    
def p_if(p):
    '''if : IF LPAREN condicion RPAREN LLLAVE sentencias RLLAVE
    | IF LPAREN condicion LPAREN LLLAVE sentencias RLLAVE else'''
# def p_for(p):
#     'for : FOR condicion LLLAVE sentencias RLLAVE '
# def p_while(p):
#     'while : WHILE condicion LLLAVE sentencias RLLAVE '
def p_else(p):
    'else : ELSE LLLAVE sentencias RLLAVE'

def p_declaracion(p):
    'declaracion : tipo ID SEMICOLON'

def p_declaracion_ini(p):
    'declaracion : tipo asignacion'

def p_tipo(p):
    '''tipo : VAR
        | BOOL
        | FLOAT
        | INT
        | STRING
    '''

def p_asignacion(p):
    'asignacion : ID TOASSIGN valor SEMICOLON'
def p_expresion_suma(p):
    'expresion : expresion PLUS expresion'
def p_expresion_resta(p):
    'expresion : expresion MINUS expresion'
def p_expresion_producto(p):
    'expresion : expresion BY expresion'
def p_expresion_division(p):
    'expresion : expresion DIV expresion'
def p_expression_term(p):
    'expresion : term'

def p_expression_paren(p):
    'expresion : LPAREN expresion RPAREN'
def p_compare(p):
    '''compare : LESS
        | GREATER
        | DEQUALS
        | NOTEQUALS
        | GREATEREQUALS
        | LESSEQUAL'''
def p_condicion(p):
    '''condicion : expresion compare expresion
        | TRUE
        | FALSE
    '''

def p_condicion_oper(p):
    '''condicion : NOT condicion
        | condicion AND condicion
        | condicion OR condicion
        | LPAREN condicion RPAREN
    '''

def p_term_factor(p):
    '''term : INTEGER
        | DECIMAL
        | ID
    '''
# def p_factor_num(p):
#     'factor : INTEGER'
# def p_factor_var2(p):
#     'factor : ID'
# def p_float(p):
#     'factor : FLOAT ID TOASSIGN DECIMAL SEMICOLON'
# def p_entero(p):
#     'factor : INT ID TOASSIGN INTEGER SEMICOLON'
# def p_booleano(p):
#     '''factor : BOOL ID TOASSIGN TRUE SEMICOLON
#         | BOOL ID TOASSIGN FALSE SEMICOLON'''

# def p_tupla(p):
#     'tupla : VAR ID TOASSIGN LPAREN contenido  RPAREN SEMICOLON'
# def p_contenido(p):
#     ' contenido : factor COMMA factor'

"""
def p_factor_expr(p):
    'factor : LPAREN expresion RPAREN'

def p_factor_expr_str(p):
    '''factor : LPAREN SSTRING RPAREN
              | LPAREN DSTRING RPAREN
    '''
"""

# Error generado
def p_error(p):
    print(p)
    print("Error de sintaxis:")
# Construir parser

parser = sintaxis.yacc()

while True:
    try:
        s = input('<c#>')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)