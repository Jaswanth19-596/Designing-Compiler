# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------
import sample2
from ply import yacc
from sample import tokens


tokens = (
#    'DECIMAL',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
#    'LPAREN',
#    'RPAREN',
#    "SEMICOLON",
#    "COMMA",
#    "LBRACE",
#    "RBRACE",
#    'ASSIGNMENT',
#    'ASSIGNMENT_ADD',
#    'ASSIGNMENT_SUB',
#    'ASSIGNMENT_MUL',
#    'ASSIGNMENT_DIV',
#    'GREATER',
#    'LESS',
   'EQUAL',
   'name', 
   'NUMBER'
#    'UNARY_MINUS',
)

def p_assign(p):
    '''assign : name EQUAL expr'''
    print("hehe")

def p_expr(p):
    '''expr : term PLUS term
            | term MINUS term
            | term
    '''

def p_term(p):
    '''term : factor TIMES factor
            | factor DIVIDE factor
            | factor
    '''

def p_factor(p):
    '''factor : NUMBER'''

def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}, unexpected token '{p.value}'")

yacc.yacc()

data = "a = 6 * 5"

yacc.parse(data)



# Parsing rules

# precedence = (
#     ('left', '+', '-'),
#     ('left', '*', '/'),
#     ('right', 'UMINUS'),
# )

# Define the tokens (not included here for brevity)

# Define the precedence (not included here for brevity)

# Symbol table to store identifiers and their types

# Parsing rules

# <program> ::= <StmtList>
# def p_program(p):
#     '''
#     program : stmt_list
#     '''
#     p[0] = p[1]


# Error rule for syntax errors


# # Build the parser
# parser = yacc.yacc()

# # Test the parser with some input
# data = '''
# int a, b;
# a = 10;
# b = a + 5;
# '''
# parser.parse(data)
 
# def p_statement_assign(p):
#     'statement : NAME "=" expression'
#     names[p[1]] = p[3]


# def p_statement_expr(p):
#     'statement : expression'
#     print(p[1])


# def p_expression_binop(p):
#     '''expression : expression '-' expression
#                   | expression '*' expression
#                   | expression '/' expression'''
#     if p[2] == '+':
#         p[0] = p[1] + p[3]
#     elif p[2] == '-':
#         p[0] = p[1] - p[3]
#     elif p[2] == '*':
#         p[0] = p[1] * p[3]
#     elif p[2] == '/':
#         p[0] = p[1] / p[3]


# def p_expression_uminus(p):
#     "expression : '-' expression %prec UMINUS"
#     p[0] = -p[2]


# def p_expression_group(p):
#     "expression : '(' expression ')'"
#     p[0] = p[2]


# def p_expression_number(p):
#     "expression : NUMBER"
#     p[0] = p[1]


# def p_expression_name(p):
#     "expression : NAME"
#     try:
#         p[0] = names[p[1]]
#     except LookupError:
#         print("Undefined name '%s'" % p[1])
#         p[0] = 0


# def p_error(p):
#     if p:
#         print("Syntax error at '%s'" % p.value)
#     else:
#         print("Syntax error at EOF")

# import ply.yacc as yacc
# parser = yacc.yacc()

# while True:
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s:
#         continue
    
# yacc.parse('''int i, j;
# int x = 4, y = 6;
# i = 3.0;
# char a = "b";
# bool a; 
# a = true;''')