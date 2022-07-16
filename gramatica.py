
from ply.lex import lex
from ply.yacc import yacc

reserved = {
    'def'       :   'DEF',
    'int'       :   'INT',
    'float'     :   'FLOAT',
    'string'    :   'STRING',
    'break'     :   'BREAK',
    'print'     :   'PRINT',
    'read'      :   'READ',
    'return'    :   'RETURN',
    'if'        :   'IF',
    'else'      :   'ELSE',
    'for'       :   'FOR',
    'new'       :   'NEW',
    'null'      :   'NULL',
    'call'      :   'CALL'
}

tokens = ('LPAREN', 'RPAREN', 'LCHAVES', 'RCHAVES', 'VIRGULA', 'PONTO_VIRGULA', 'LCOLCHETES', 'RCOLCHETES', 'ATRIBUICAO', 'MENOR',
          'MENORIGUAL', 'IGUAL','DIFERENTE', 'MAIOR', 'MAIORIGUAL', 'SOMA', 'SUBTRACAO', 'MULTIPLICACAO', 'DIVISAO', 'RESTO', 'IDENT',
          'INT_CONSTANT', 'FLOAT_CONSTANT', 'STRING_CONSTANT', 'DEF', 'INT', 'FLOAT', 'STRING', 'BREAK', 'PRINT', 'READ', 'RETURN',
          'IF', 'ELSE', 'FOR', 'NEW', 'NULL', 'CALL')
        #   + list(reserved.values())

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
    # if t.value in reserved:# Verifica se está nas palavras reservadas.
    #     t.type = reserved[t.value]
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
    #r'\"([^\\\n]|(\\.))*?\"'    # "letra*"
    r'\"\w\"'
    return t

# Definição de uma regra para encontrar o número da linha.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
# Vide t_ignore

# Error handling rule
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

# Build the lexer object
lexer = lex()
    
# data = 'def funcao ( int A , int B , float C , string Z ) { break ; }'

# lexer.input(data)

# for tok in lexer:
#     print(tok)

# --- Parser

def p_program(p):
    '''
    program : statement
                | funclist
                | epsilon
    '''
    
def p_funclist(p):
    '''
    funclist : funcdef funclist2
    '''
    
def p_funclist2(p):
    '''
    funclist2 : funclist
                | epsilon
    '''    
    
def p_funcdef(p):
    '''
    funcdef : DEF IDENT LPAREN paramlist RPAREN LCHAVES statelist RCHAVES
    '''
        
def p_paramlist(p):
    '''
    paramlist : INT IDENT paramlist2
                | FLOAT IDENT paramlist2
                | STRING IDENT paramlist2
                | epsilon
    '''
    
def p_paramlist2(p):
    '''
    paramlist2 : VIRGULA paramlist
                    | epsilon
    '''

def p_statement(p):
    '''
    statement : vardecl PONTO_VIRGULA
                | atribstat PONTO_VIRGULA
                | printstat PONTO_VIRGULA
                | readstat PONTO_VIRGULA
                | returnstat PONTO_VIRGULA
                | ifstat
                | forstat
                | LCHAVES statelist RCHAVES
                | BREAK PONTO_VIRGULA
                | PONTO_VIRGULA
    '''

def p_vardecl(p):
    '''
    vardecl :   INT IDENT a
                | FLOAT IDENT a
                | STRING IDENT a
    '''
    
def p_a(p):
    '''
    a   :   LCOLCHETES INT_CONSTANT RCOLCHETES a
            | epsilon
    '''
    
def p_atribstat(p):
    '''
    atribstat   :   lvalue ATRIBUICAO atribstat2
    '''


def p_atribstat2(p):
    '''
    atribstat2 :    expression
                    | allocexpression
                    | funccall
    '''

def p_funccall(p):

    '''
    funccall :  CALL IDENT LPAREN paramlistcall RPAREN
    '''
    
def p_paramlistcall(p):
    '''
    paramlistcall   :   IDENT paramlistcall2
                        | epsilon
    '''
    
def p_paramlistcall2(p):
    '''
    paramlistcall2  :   VIRGULA paramlistcall
                        | epsilon
    '''

def p_printstat(p):
    '''
    printstat   :   PRINT expression
    '''

def p_readstat(p):
    '''
    readstat    :   READ lvalue
    '''

def p_returnstat(p):
    '''
    returnstat  :   RETURN
    '''

def p_ifstat(p):
    '''
    ifstat  :   IF LPAREN expression RPAREN statement ifstat2
    '''

def p_ifstat2(p):
    '''
    ifstat2 :   ELSE statement PONTO_VIRGULA
                | PONTO_VIRGULA
    '''

def p_forstat(p):
    '''
    forstat :   FOR LPAREN atribstat PONTO_VIRGULA expression PONTO_VIRGULA atribstat RPAREN statement
    '''
    
def p_statelist(p):
    '''
    statelist :    statement statelist2
    '''
    
def p_statelist2(p):
    '''
    statelist2  :   statelist
                    | epsilon
    '''

def p_allocexpression(p):
    '''
    allocexpression :   NEW allocexpression2
    '''

def p_allocexpression2(p):
    '''
    allocexpression2    :   INT e
                            | FLOAT e
                            | STRING e
    '''

def p_e(p):
    '''
    e   :   LCOLCHETES numexpression RCOLCHETES e2
    '''
    
def p_e2(p):
    '''
    e2  :   e
            | epsilon
    '''

def p_expression(p):
    '''
    expression  :   numexpression expression2
    '''

def p_expression2(p):
    '''
    expression2 : MENOR numexpression
                    | MAIOR numexpression
                    | MENORIGUAL numexpression
                    | MAIORIGUAL numexpression
                    | IGUAL numexpression
                    | DIFERENTE numexpression
                    | epsilon
    '''


def p_numexpression(p):
    '''
    numexpression   :   term d
    '''

def p_d(p):
    '''
    d   :   SOMA term d
            | SUBTRACAO term d
            | epsilon
    '''
    
def p_term(p):
    '''
    term    :   unaryexpr b
    '''

def p_b(p):
    '''
    b   :   MULTIPLICACAO unaryexpr b
            | DIVISAO unaryexpr b
            | RESTO unaryexpr b
            | epsilon
    '''

def p_unaryexpr(p):
    '''
    unaryexpr   :   SOMA factor
                    | SUBTRACAO factor
                    | factor
    '''

def p_factor(p):
    '''
    factor  :   INT_CONSTANT
                | FLOAT_CONSTANT
                | STRING_CONSTANT
                | NULL
                | lvalue
                | LPAREN numexpression RPAREN
    '''

def p_lvalue(p):
    '''
    lvalue  :   IDENT c
    '''

def p_c(p):
    '''
    c   :   LCOLCHETES numexpression RCOLCHETES c
            | epsilon
    '''

def p_epsilon(p):
    'epsilon :'

class Erros:
    def __init__(self, sem_erros):
        self.sem_erros = sem_erros
    
    def set_erros(self):
        self.sem_erros = not self.sem_erros

e = Erros(True)

def p_error(p):
    e.set_erros()
    print('INE5622')
    print('Leitura de p: ', p)
    print(f'Erro de sintaxe em: {p.value!r}')
    print()

# Build the parser

parser = yacc()

# Parse an expression
#ast = parser.parse('def nomefuncao ( int A , int B ) { break ; }')
#ast = parser.parse('call def funcao ( int A , int B ) { }')
ast = parser.parse('def funcao ( int A , int B , float C , string Z ) { break ; }')

if (e.sem_erros):
    print('Não foram detectados erros sintáticos')

