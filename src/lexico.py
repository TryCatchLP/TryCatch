import ply.lex as lex

reserved = {
    'var': 'VAR',
    'string': 'STRING',
    'int':'INT',
    'float': 'FLOAT',
    'bool':'BOOL',
    'for': 'FOR',
    'while': 'WHILE',
    'if' : 'IF',
    'else': 'ELSE',
    'new': 'NEW',
    'Console': 'CONSOLE',
    'true' : 'TRUE',
    'false' :'FALSE',
    'List' : 'LIST',
    'HashSet' : 'HASHSET'
}

tokens = [
    'PLUS',
    'MINUS',
    'LESS',
    'DIV',
    'BY',
    'INCRE',
    'DECRE',
    'GREATER',
    'DEQUALS',
    'NOTEQUALS',
    'LESSEQUAL',
    'GREATEREQUALS',
    'AND',
    'OR',
    'NOT',
    'TOASSIGN',
    'LPAREN',
    'RPAREN',
    'LCORCHETE',
    'RCORCHETE',
    'LLLAVE',
    'RLLAVE',
    'DOT',
    'DOTS',
    'SEMICOLON',
    'ID',
    'DECIMAL',
    'SSTRING',
    'DSTRING',
    'INTEGER',
    'CONTAINS',
    'REPLACE',
    'SUBSTRING',
    'ADD',
    'REMOVE',
    'ITEM',
    'COMMA',
    'WRITELINE',
    'READLINE',
    'UNION',
    'GETRANGE'

] + list(reserved.values())

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIV = r'/'
t_INCRE = r'\+\+'
t_DECRE = r'--'
t_BY= r'\*'
t_LESS = r'<'
t_GREATER = r'>'
t_DEQUALS = r'=='
t_NOTEQUALS = r'!='
t_LESSEQUAL = r'<='
t_GREATEREQUALS = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_TOASSIGN=r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCORCHETE = r'\['
t_RCORCHETE = r'\]'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_DOT = r'\.'
t_DOTS = r'\:'
t_SEMICOLON= r';'
t_DECIMAL = r'\d*\.\d+f'
t_SSTRING = r'\'[^\'.]*\''
t_DSTRING = r'"[^".]*"'
t_INTEGER = r'\d+'
t_CONTAINS = r'\.Contains'
t_REPLACE = r'\.Replace'
t_SUBSTRING = r'\.Substring'
t_ADD = r'\.Add'
t_REMOVE = r'\.Remove'
t_ITEM = r'\.Item[1-9][0-9]*'
t_COMMA = r'\,'
t_WRITELINE = r'\.WriteLine'
t_READLINE = r'\.ReadLine'
t_UNION=r'\.UnionWith'
t_GETRANGE=r'\.GetRange'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_error(t):
    print("No se ha reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += 1

lex.lex()

def analizar(cadena):
    analizador = lex.lex()
    analizador.input(cadena)

    while True:
        tok = analizador.token()
        if not tok:
            break
        print(tok)

""" #========================Steven Araujo=============================
cadena1 = "var tupla = ('Steven', 'Araujo');\nConsole.WriteLine(tupla.Item1);"
cadena2 = 'string nombre_completo = "Steven Araujo";\nstring apellido = nombre_completo.Substring(7, 6);\nConsole.WriteLine(apellido);'
cadena3 = 'int contador = 5;\nwhile(contador >= 5){\n\tcontador--;\n}'
print(cadena1)
analizar(cadena1)
print(20*"-")
print(cadena2)
analizar(cadena2)
print(20*"-")
print(cadena3)
analizar(cadena3)
print(20*"-")

#========================Kenny Camba=============================
print()
cadena1 = "float salario = 350.5f;\nvar porcentaje = 25;\nfloat total = salario*porcentaje/100;"
cadena2 = 'Console.WriteLine("Tabla del 2:");\nfor(var i=0; i<20; i++){\n\tConsole.WriteLine(2 * i);\n}'
cadena3 = 'Console.WriteLine("Ingrese usuario: ");\nstring usuario = Console.ReadLine();\nif(usuario != "Admin"){\n\tConsole.WriteLine("No autorizado!!");\n}'
print(cadena1)
analizar(cadena1)
print(20*"-")
print(cadena2)
analizar(cadena2)
print(20*"-")
print(cadena3)
analizar(cadena3)
print(20*"-")

#========================Yuleixi Garcia=============================
cadena1= "List<int> lista = new List<int>();\n lista.Add(456);\nlista.Contains(1);\nlista.Remove(2);"
cadena2="HashSet<int> set= new HashSet<int>();\nset.Add(456); set.Add(4);"
cadena3= "bool verdadero=true;\nbool falso=false;\nint num = 3;\nif(verdadero == falso || num <=3){\n     num++; \n} else {\n    verdadero = false; \n}"
print(cadena1)
analizar(cadena1)
print(20*"-")
print(cadena2)
analizar(cadena2)
print(20*"-")
print(cadena3)
analizar(cadena3)
print(20*"-")
 """