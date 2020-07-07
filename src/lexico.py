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
    'Console': 'CONSOLE'
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
    'SEMICOLON',
    'ID',
    'DECIMAL',
    'SSTRING',
    'DSTRING',
    'INTEGER',
    'TRUE',
    'FALSE',
    'CONTAINS',
    'REPLACE',
    'SUBSTRING',
    'ADD',
    'REMOVE',
    'ITEM',
    'COMMA',
    'WRITELINE',
    'READLINE'

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
t_SEMICOLON= r';'
t_DECIMAL = r'\d*\.\d+f'
t_SSTRING = r'\'.*\''
t_DSTRING = r'".*"'
t_INTEGER = r'\d+'
t_TRUE = r'true'
t_FALSE = r'false'
t_CONTAINS = r'\.Contains'
t_REPLACE = r'\.Replace'
t_SUBSTRING = r'\.Substring'
t_ADD = r'\.Add'
t_REMOVE = r'\.Remove'
t_ITEM = r'\.Item[1-9][0-9]*'
t_COMMA = r'\,'
t_WRITELINE = r'\.WriteLine'
t_READLINE = r'\.ReadLine'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_error(t):
    print("No se ha reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lex.lex()

def analizar(cadena):
    analizador = lex.lex()
    analizador.input(cadena)

    while True:
        tok = analizador.token()
        if not tok:
            break
        print(tok)

#========================Steven Araujo=============================
cadena1 = 'var tupla = ("Steven", "Araujo");\nConsole.WriteLine(tupla.Item1);'
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

