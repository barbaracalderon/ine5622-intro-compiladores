from ply.yacc import yacc
from lexica import *
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
        self.sem_erros = False

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
# ast = parser.parse(data())

def parse(data):
    # ast = parser.parse(data)
    parser.parse(data)
    if (e.sem_erros):
        print('Não foram detectados erros sintáticos')
