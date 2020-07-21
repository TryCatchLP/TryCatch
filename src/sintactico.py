import ply.yacc as sintaxis
import lexico
tokens = lexico.tokens

errors = False
output = []


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

""" def p_sentencias_error(p):
    'sentencias : sentencias error'
    line   = p.lineno(1)
    index  = p.lexpos(1)
    printerror("Error: no se encuentra el ;") """

def p_imprimir(p):
    'imprimir : CONSOLE WRITELINE LPAREN valor RPAREN SEMICOLON'

def p_imprimir_error(p):
    'imprimir : CONSOLE WRITELINE error SEMICOLON'
    printerror("Error en WriteLine, sintaxis incorrecta")
    printhelp("\tConsole.WriteLine(\"!Hola Mundo!\");")

def p_metodos_void(p):
    '''metodos : remove SEMICOLON
        | add SEMICOLON
        | contains SEMICOLON
        | union SEMICOLON'''

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
        | ID GETRANGE LPAREN expresion COMMA expresion RPAREN
        | tupla
        | expresion'''
    
def p_if(p):
    '''if : IF LPAREN condicion RPAREN LLLAVE sentencias RLLAVE
    | IF LPAREN condicion RPAREN LLLAVE sentencias RLLAVE else'''

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
    printhelp("\tint a = 2;\n\tfloat a = 2.5f;\n\tbool a = true;")

""" def p_asignacion_coma_error(p):
    'asignacion : ID TOASSIGN valor error'
    printerror("Error se encuentra el ;") """

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
        | ID
        | TRUE
        | FALSE
    '''
def p_condicion_oper(p):
    '''condicion : NOT condicion
        | condicion AND condicion
        | condicion OR condicion
        | LPAREN condicion RPAREN
        | condicion DEQUALS TRUE
        | condicion NOTEQUALS TRUE
        | condicion DEQUALS FALSE
        | condicion NOTEQUALS FALSE
        | condicion DEQUALS condicion
        | condicion NOTEQUALS condicion
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
def p_fact_init(p):
    '''factor : ID TOASSIGN INTEGER
        | ID TOASSIGN DECIMAL
    '''

def p_leer(p):
    '''leer : tipo ID TOASSIGN CONSOLE READLINE LPAREN RPAREN SEMICOLON
    | ID TOASSIGN CONSOLE READLINE LPAREN RPAREN SEMICOLON'''

def p_leer_error(p):
    'leer : CONSOLE READLINE error'
    printerror("Error en ReadLine, sintaxis incorrecta")
    printhelp("\tConsole.Readline();")

def p_add(p):
    'add : ID ADD LPAREN valor RPAREN'

def p_contains(p):
    '''contains : ID CONTAINS LPAREN valor RPAREN
        | string CONTAINS LPAREN string RPAREN
    '''
    
def p_list_remove(p):
    'remove : ID REMOVE LPAREN valor RPAREN'
    
def p_index_list(p):
    '''indexar : ID LCORCHETE INTEGER RCORCHETE
    | ID LCORCHETE expresion RCORCHETE
    '''

def p_set_union(p):
    'union : ID UNION LPAREN ID RPAREN'

def p_union_error(p):
    '''union : ID UNION error ID RPAREN SEMICOLON
        | ID UNION LPAREN ID error SEMICOLON
    '''
    printerror("Error en el metodo UnionWith")
    printhelp("\tconjunto1.UnionWith(conjunto2);")

def p_index_str(p):
    '''indexar : string LCORCHETE INTEGER RCORCHETE
    | string LCORCHETE expresion RCORCHETE
    '''
   
def p_tupla_item(p):
    'item : ID ITEM'

def p_tupla_item_nombre(p):
    'nombre : ID DOT ID'
    
def p_string(p):
    '''string : SSTRING
        | DSTRING
    '''

def p_string_replace(p):
    '''replace : string REPLACE LPAREN string COMMA string RPAREN
    | ID REPLACE LPAREN string COMMA string RPAREN'''

def p_string_sub(p):
    '''substring : string SUBSTRING LPAREN expresion COMMA expresion RPAREN
    | ID SUBSTRING LPAREN expresion COMMA expresion RPAREN'''

def p_str(p):
    '''str : replace
        | contains
        | substring
    '''

# Error generado
def p_error(p):
    global errors
    errors = True
    global output
    if p != None:
        pos = find_column(p.lexer.lexdata, p) 
        line = p.lineno
        exp = p.lexer.lexdata.split("\n")
        if line > 0:
            if not isSemiError(exp, line, p.value):
                exp = exp[line - 1]
            else:
                exp = exp[line - 2]
                line -= 1
                printerror("Debe colocar ; al final de una instrucción")
        else:
            exp = exp[line]
            line += 1
        exp = exp.strip()
        print("\nError de sintaxis en línea: {}; posisión: {}".format((line), pos))
        print(exp)
        print((pos*" ") + "^")
        output.append("\nError de sintaxis en línea: {}; posisión: {}".format((line), pos))
        output.append(exp)
        output.append((pos*" ") + "^")
    else:
        print("Error en la útima línea")
        output.append("Error en la útima línea")
# Construir parser

def isSemiError(data: list, line: int, value: str):
    if line > 1:
        text = data[line-1]
        dat = text.index(value)
        if dat == 0 and data[line-2][-1] != ';':
            return True
    return False

def find_column(input, token):
     line_start = input.rfind('\n', 0, token.lexpos) + 1
     return (token.lexpos - line_start) + 1

def printerror(error):
    global output
    print("\033[91m{}\033[0m".format(error))
    output.append(error)

def printhelp(help):
    global output
    print("Help: \033[92m\n{}\033[0m".format(help))
    output.append("Help:\n{}".format(help))


parser = sintaxis.yacc()


def sintactico(fuente):
    print(fuente)
    lexico.analizador.lineno = 1
    lexico.analizador.lexpos = 0
    global output, errors
    output = []
    errors = False
    result = parser.parse(fuente)
    if not errors:
        print("Codigo ejecutado con éxito")
        output.append("Codigo ejecutado con éxito")
    return output


#cadena = "var a = 2.5f;\nfloat suma = a + 1;\nConsole.WriteLine(a);\nif(suma>3){\n\ta = 1;\n\tsuma=2-2;\n}"
#cadena = "var a = 2.5f;\nfloat suma = a + 1;\nConsole.WriteLine(a);\nfor(i=0; suma>3; i++){\n\ta = 1;\n\tsuma=2-2;\n}"
#cadena = "suma ---;\nresta +++;"
#cadena = "var a = 2.5f;\nfloat suma = a -* 1;"
#cadena="HashSet<int> conjunto2 = new HashSet<int>();\nconjunto2.Add(1);\nconjunto2.Add(3);\nconjunto.UnionWith(conjunto2);"
#cadena="List<int>lista = new List<int>();\nlista.Add(1);\nlista.Add(3);\nlista.Add(7);\nbool c = lista.Contains(3);\nlista.Remove(1);"
#cadena="Console.ReadLine();"

# ============================ Kenny Camba ===============================

# Operación compleja con asignación
cadena1 = "int b = 1; \nvar a = 2 + 5.2f * (3*b)/b-5;\nConsole.WriteLine(a);" 
sintactico(cadena1)

print()

# Declaracion de una lista, uso de un ciclo while, que tiene una condición compuesta, adentro de este se hace un incremento, agragamiento a la lista y un if para presentat el primer elemento de la lista
cadena2 = "var lista = new List<int>();\nint a = 2;\nwhile(a > 5 && a != 10 || a+1>3){\n\ta++;\n\tlista.Add(a);\n\tif(a==8){\n\t\tConsole.WriteLine(lista[0]);\n\t}\n}"
sintactico(cadena2)

print()
# Asignación de variables y inicialización de tupla con los valores de esta.
cadena3 = "int edad = 21;\nstring nombre = \"Kenny\";\nvar tupla = (nombre: nombre, edad: edad);\nConsole.WriteLine(tupla.edad + 1);"
sintactico(cadena3)

#========================Yuleixi Garcia=============================

print()
#asignacion de variable, uso de if mediante una comparacion de la variable, impesion de un string y pedida de ingreso por consola
cadena1= "int edad = 21;\nif(edad>=18){\n\tConsole.WriteLine(\"Ingrese su nombre: \");\n\tstring nombre = Console.ReadLine();\n}"
sintactico(cadena1)

print()
#declaracion de dos HashSet, agregacion de datos a los ocnjuntos y realizar la operacion union entre ambbos conjuntos
cadena2="HashSet<int> set= new HashSet<int>();\nset.Add(456);\nset.Add(345);\nset.Add(42);\nHashSet<int> cojunto= new HashSet<int>();\nset.Add(456);\nset.UnionWith(conjunto);"
sintactico(cadena2)

print()
#uso de incrementadores y decrementadores
cadena3= "int numero = 6;\nnumero--;\nnumero ++;\n++numero;\n--numero;\nnumero+=2;\nnumero-=1;"
sintactico(cadena3)

# ============================ Steven Araujo ===============================

print()
# declaracion de tupla e impresion de un item
cadena1 = "var tupla = ('Steven', 'Araujo');\nConsole.WriteLine(tupla.Item1);"
sintactico(cadena1)

print()
# declaracion de un string y validacion de contenido de un subconjunto en el string 
cadena2 = 'string nombre_completo = "Steven Araujo";\nbool apellido = nombre_completo.Contains("Araujo");\nConsole.WriteLine(apellido);'
sintactico(cadena2)

print()
# uso de while con decrementador
cadena3 = 'int contador = 5;\nwhile(contador >= 5){\n\tcontador--;\n}'
sintactico(cadena3)

print()
# uso de Substring
cadena4 = 'string nombre_completo = "Steven Araujo";\nstring apellido = nombre_completo.Substring(7, 6);\nConsole.WriteLine(apellido);'
sintactico(cadena4)

print()
# uso de Replace
cadena5 = 'string nombre_completo = "Steven Araujo";\nstring resultado = nombre_completo.Replace("Araujo", "Moran");\nConsole.WriteLine(resultado);'
sintactico(cadena5)

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