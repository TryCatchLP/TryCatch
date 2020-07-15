import ply.yacc as sintaxis
import lexico
tokens = lexico.tokens

errors = False

def p_sentencias(p):
    '''sentencias : asignacion
    | imprimir
    | leer
    | declaracion
    | iter SEMICOLON
    | if
    | while
    | for
    | condicion
    | metodos
    | sentencias sentencias'''

def p_imprimir(p):
    'imprimir : CONSOLE WRITELINE LPAREN valor RPAREN SEMICOLON'

def p_imprimir_error(p):
    'imprimir : CONSOLE WRITELINE error'
    printerror("Error en WriteLine, sintaxis incorrecta")
    printhelp("\tConsole.WriteLine(\"!Hola Mundo!\");")

def p_metodos_void(p):
    '''metodos : remove
        | add
        | contains
        | union'''

def p_metodo_error(p):
    '''metodos : ID error LPAREN valor RPAREN SEMICOLON
        |  ID metodos error valor RPAREN SEMICOLON
        | ID metodos LPAREN valor error SEMICOLON
    '''
    printerror("Error en el metodo")
    printhelp("\tlista.Remove(5);\n\tlista.Add(5);\n\tlista.Contains(5);")

def p_valor(p):
    '''valor : TRUE
        | FALSE
        | str
        | string
        | NEW coleccion LESS tipo GREATER LPAREN RPAREN
        | ID GETRANGE LPAREN INTEGER COMMA INTEGER RPAREN
        | tupla
        | expresion'''
    
def p_if(p):
    '''if : IF LPAREN condicion RPAREN LLLAVE sentencias RLLAVE
    | IF LPAREN condicion LPAREN LLLAVE sentencias RLLAVE else'''

def p_if_error(p):
    'if : IF error'
    printerror("Error en sentencia if")
    printhelp("\tif(a > b){\n\t\tConsole.WriteLine(\"a es mayor que b\");\n\t}")

def p_tupla(p):
   'tupla : LPAREN contenido  RPAREN'

def p_contenido(p):
    'contenido : valor'

def p_contenido_item(p):
    'contenido : ID DOTS valor'
    
def p_contenido_coma(p):
    'contenido : contenido COMMA contenido'

def p_for(p):
    'for : FOR LPAREN inicio SEMICOLON condicion SEMICOLON iter RPAREN LLLAVE sentencias RLLAVE '

def p_for_error(p):
    'for : FOR error'
    printerror("Error en sentencia for")
    printhelp("\tfor(int i=0; a > b; i++){\n\t\ta--;\n\t\tConsole.WriteLine(\"a es mayor que b\");\n\t}")

def p_ini_for(p):
    '''inicio : ID
        | factor
    '''

def p_iter(p):
    '''iter : incremento
        | decremento
    '''

def p_incremento(p):
    '''incremento : INCRE ID
        | ID INCRE
        | ID PLUS TOASSIGN term
    '''
def p_incremento_error(p):
    'incremento : incremento error'
    printerror("Error de incremento")
    printhelp("\tint a=1;\n\ta++; \n\ta+=1;\n\tint b=9;\n\t++b;")

def p_decremento(p):
    '''decremento : DECRE ID
        | ID DECRE
        | ID MINUS TOASSIGN term
    '''
def p_decremento_error(p):
    'decremento : decremento error'
    printerror("Error de decremento")
    printhelp("\tint a=5;\n\ta--;\n\ta-=1;\n\tint b=9;\n\t--b;")

def p_while(p):
    'while : WHILE LPAREN condicion RPAREN LLLAVE sentencias RLLAVE '
def p_while_error(p):
    'while : WHILE error'
    printerror("Error en sentencia while")
    printhelp("\twhile(a > b){\n\t\ta--;\n\t\tConsole.WriteLine(\"a es mayor que b\");\n\t}")

def p_else(p):
    'else : ELSE LLLAVE sentencias RLLAVE'

def p_declaracion_coleccion(p):
    'declaracion : coleccion LESS tipo GREATER asignacion'
def p_declaracion(p):
    'declaracion : tipo ID SEMICOLON'
def p_declaracion_ini(p):
    'declaracion : tipo asignacion'

def p_coleccion(p):
    ''' coleccion : LIST
        | HASHSET
    '''
def p_tipo(p):
    '''tipo : VAR
        | BOOL
        | FLOAT
        | INT
        | STRING
    '''

def p_asignacion(p):
    'asignacion : ID TOASSIGN valor SEMICOLON'

def p_asignacion_error(p):
    'asignacion : ID TOASSIGN error SEMICOLON'
    printerror("Error en la asignación")
    printhelp("\tint a = 2;")

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
        | nombre
        | item
        | indexar
    '''

def p_float(p):
    'factor : FLOAT ID TOASSIGN DECIMAL'
def p_entero(p):
    'factor : INT ID TOASSIGN INTEGER'
def p_var(p):
    '''factor : VAR ID TOASSIGN INTEGER
        | VAR ID TOASSIGN DECIMAL
    '''

def p_leer(p):
    'leer : CONSOLE READLINE LPAREN RPAREN SEMICOLON'

def p_leer_error(p):
    'leer : CONSOLE READLINE error'
    printerror("Error en ReadLine, sintaxis incorrecta")
    printhelp("\tConsole.Readline();")

def p_add(p):
    'add : ID ADD LPAREN valor RPAREN SEMICOLON'

def p_contains(p):
    '''contains : ID CONTAINS LPAREN valor RPAREN SEMICOLON
        | string CONTAINS LPAREN string RPAREN
    '''
    
def p_list_remove(p):
    'remove : ID REMOVE LPAREN valor RPAREN SEMICOLON'
def p_index_list(p):
    'indexar : ID LCORCHETE INTEGER TOASSIGN RCORCHETE'

def p_set_union(p):
    'union : ID UNION LPAREN ID RPAREN SEMICOLON'

def p_union_error(p):
    '''union : ID error LPAREN ID RPAREN SEMICOLON
        |  ID UNION error ID RPAREN SEMICOLON
        | ID UNION LPAREN ID error SEMICOLON
    '''
    printerror("Error en el metodo UnionWith")
    printhelp("\tconjunto1.UnionWith(conjunto2);")

def p_index_str(p):
    'indexar : string LCORCHETE INTEGER RCORCHETE'
   
def p_tupla_item(p):
    'item : ID ITEM'

def p_tupla_item_nombre(p):
    'nombre : ID DOT ID'
    
def p_string(p):
    '''string : SSTRING
        | DSTRING
    '''

def p_string_replace(p):
    'replace : string REPLACE LPAREN string COMMA string RPAREN'

def p_string_sub(p):
    'substring : string SUBSTRING LPAREN INTEGER COMMA INTEGER RPAREN'

def p_str(p):
    '''str : replace
        | contains
        | substring
    '''


# Error generado
def p_error(p):
    errors = True
    pos = find_column(p.lexer.lexdata, p) 
    line = p.lineno
    exp = p.lexer.lexdata.split("\n")
    exp = exp[line - 1]
    exp = exp.strip()
    print("\nError de sintaxis en línea: {}; posisión: {}".format((line), pos))
    print(exp)
    print("^")
# Construir parser

def find_column(input, token):
     line_start = input.rfind('\n', 0, token.lexpos) + 1
     return (token.lexpos - line_start) + 1

def printerror(error):
    print("\033[91m{}\033[0m".format(error))

def printhelp(help):
    print("Help: \033[92m\n{}\033[0m".format(help))

parser = sintaxis.yacc()


def sintactico(fuente):
    print(fuente)
    result = parser.parse(fuente)
    if not errors:
        print("Codigo ejecutado con éxito")


#cadena = "var a = 2.5f;\nfloat suma = a + 1;\nConsole.WriteLine(a);\nif(suma>3){\n\ta = 1;\n\tsuma=2-2;\n}"
#cadena = "var a = 2.5f;\nfloat suma = a + 1;\nConsole.WriteLine(a);\nfor(int i=0;suma>3; i++){\n\ta = 1;\n\tsuma=2-2;\n}"
#cadena = "suma ---;\nresta +++;"
#cadena = "var a = 2.5f;\nfloat suma = a -* 1;"
#cadena="HashSet<int> conjunto2 = new HashSet<int>();\nconjunto2.Add(1);\nconjunto2.Add(3);\nconjunto.UnionWith(conjunto2);"
#cadena="List<int>lista = new List<int>();\nlista.Add(1);\nlista.Add(3);\nlista.Add(7);\nlista.Remove(1);"
cadena="Console.ReadLine();"

sintactico(cadena)

# while True:
#     line = 0
#     s = ""
#     try:
#         s = input('<c#>')
#     except EOFError:
#         break
#     if not s: continue
#     result = parser.parse(s)
#     print(result)