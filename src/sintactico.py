import ply.yacc as sintaxis
import lexico
tokens = lexico.tokens

def p_sentencias(p):
    '''sentencias : asignacion
    | imprimir
    | expresion
    | while
    | for
    | if'''
def p_imprimir(p):
    'imprimir : CONSOLE WRITELINE factor SEMICOLON'
def p_if(p):
    '''if : IF condicion LLLAVE sentencias RLLAVE
    | IF condicion LLLAVE sentencias RLLAVE else'''
def p_for(p):
    'for : FOR condicion LLLAVE sentencias RLLAVE '
def p_while(p):
    'while : WHILE condicion LLLAVE sentencias RLLAVE '
def p_else(p):
    'else : ELSE LLLAVE sentencias RLLAVE'
def p_asignacion(p):
    'asignacion : ID TOASSIGN expresion'
def p_expresion_suma(p):
    'expresion : expresion PLUS factor'
def p_expresion_resta(p):
    'expresion : expresion MINUS term'
def p_expresion_producto(p):
    'expresion : expresion BY term'
def p_expresion_division(p):
    'expresion : expresion DIV term'
def p_expression_term(p):
    'expresion : term'
def p_compare(p):
    '''compare : LESS
        | GREATER
        | DEQUALS
        | NOTEQUALS
        | GREATEREQUALS
        | LESSEQUAL
        | AND
        | NOT
        | OR'''
def p_condicion(p):
    'condicion : factor compare factor'
def p_term_factor(p):
    'term : factor'
def p_factor_num(p):
    'factor : INTEGER'
def p_factor_var2(p):
    'factor : ID'
def p_float(p):
    'factor : FLOAT ID TOASSIGN DECIMAL SEMICOLON'
def p_entero(p):
    'factor : INT ID TOASSIGN INTEGER SEMICOLON'
def p_booleano(p):
    '''factor : BOOL ID TOASSIGN TRUE SEMICOLON
        | BOOL ID TOASSIGN FALSE SEMICOLON'''
def p_tupla(p):
    'factor : VAR ID TOASSIGN LPAREN contenido  RPAREN SEMICOLON'
def p_contenido(p):
    ' contenido : factor COMMA factor'
def p_factor_expr(p):
    'factor : LPAREN expresion RPAREN'

# Error generado
def p_error(p):
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