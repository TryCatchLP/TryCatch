import ply.lex as lex

reserved = {
    'var': 'VAR',
    'string': 'STRING',
    'for': 'FOR',
    'while': 'WHILE',
}

tokens = [
    'PLUS',
    'MINUS',
    'LESS',
    'GREATER',
    'DEQUALS',
    'AND',
    'LPAREN',
    'RPAREN',
    'DOT',
    'ID',
    'DECIMAL',
    'SSTRING',
    'DSTRING'
] + list(reserved.values())

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_LESS = r'<'
t_GREATER = r'>'
t_DEQUALS = r'=='
t_AND = r'&&'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_DECIMAL = r'\d*\.\d+f'
t_SSTRING = r'\'.*\''
t_DSTRING = r'".*"'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t
lex.lex()

"""
cadena = 'var casa == a + "hola" - (15.5f + .01f) && . >< for while'
analizador = lex.lex()
analizador.input(cadena)

while True:
    tok = analizador.token()
    if not tok:
        break
    print(tok)

"""