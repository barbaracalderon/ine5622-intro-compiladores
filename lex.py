from ply.lex import lex
import re

reserved = {
    'def'       :   'DEF',
    'int'       :   'INT',
    'float'     :   'FLOAT',
    'string'    :   'STRING',
    'break'     :   'BREAK',
    'print'     :   'PRINT',
    'call'      :   'CALL',
    'read'      :   'READ',
    'return'    :   'RETURN',
    'if'        :   'IF',
    'else'      :   'ELSE',
    'for'       :   'FOR',
    'new'       :   'NEW',
    'null'      :   'NULL',
}

tokens = [
        'IDENT',
        'FLOAT_CONSTANT',
        'INT_CONSTANT',
        'STRING_CONSTANT',
        'LPAREN',
        'RPAREN',
        'LCHAVES',
        'RCHAVES',
        'VIRGULA',
        'PONTO_VIRGULA',
        'LCOLCHETES',
        'RCOLCHETES',
        'ATRIBUICAO',
        'MENOR',
        'MENORIGUAL',
        'IGUAL',
        'DIFERENTE',
        'MAIOR',
        'MAIORIGUAL',
        'SOMA',
        'SUBTRACAO',
        'MULTIPLICACAO',
        'DIVISAO',
        'RESTO',
        ] + list(reserved.values())


t_ignore            = ' \t'
t_DEF               = r'def'
t_INT               = r'int'
t_FLOAT             = r'float'
t_STRING            = r'string'
t_BREAK             = r'break'
t_PRINT             = r'print'
t_READ              = r'read'
t_RETURN            = r'return'
t_IF                = r'if'
t_ELSE              = r'else'
t_FOR               = r'for'
t_NEW               = r'new'
t_NULL              = r'null'
t_CALL              = r'call'
t_LPAREN            = r'\('
t_RPAREN            = r'\)'
t_LCHAVES           = r'\{'
t_RCHAVES           = r'\}'
t_VIRGULA           = r','
t_PONTO_VIRGULA     = r';'
t_LCOLCHETES        = r'\['
t_RCOLCHETES        = r'\]'
t_ATRIBUICAO        = r'='
t_MENOR             = r'<'
t_MAIOR             = r'>'
t_MENORIGUAL        = r'<='
t_IGUAL             = r'=='
t_DIFERENTE         = r'!='
t_MAIORIGUAL        = r'>='
t_SOMA              = r'\+'
t_SUBTRACAO         = r'-'
t_MULTIPLICACAO     = r'\*'
t_DIVISAO           = r'/'
t_RESTO             = r'%'


def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENT')
    return t

def t_FLOAT_CONSTANT(t):
    r'\d+[.]\d*|\d*[.]\d+'    # digito+.digito* | digito*.digito+
    t.value = float(t.value)
    return t

def t_INT_CONSTANT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING_CONSTANT(t):
    r'\"\w\"'
    return t

# Definição de uma regra para encontrar o número da linha.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)



# Build the lexer object
lexer = lex()

def analyse_lex(data):
    lexer.input(data)
    tabela_simbolo = []
    tabela_check = []
    cont = 1
    print('\nANÁLISE LÉXICA:\n')
    for tok in lexer:
        print(f'tok: {tok}')
        if tok.type == 'IDENT':
            tup = (tok.value, cont)
            if tup[0] not in tabela_check:
                cont += 1
                tabela_check.append(tup[0])
                tabela_simbolo.append(tup)
    print('\n')
    print('TABELA DE SÍMBOLOS:')
    for tup in tabela_simbolo:
        print(tup)
    return tabela_simbolo
