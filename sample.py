import ply.lex as lex
from ply.lex import TOKEN

# List of token names.   This is always required
tokens = (
   'DECIMAL',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   "SEMICOLON",
   "COMMA",
   "LBRACE",
   "RBRACE",
   'ASSIGNMENT',
   'ASSIGNMENT_ADD',
   'ASSIGNMENT_SUB',
   'ASSIGNMENT_MUL',
   'ASSIGNMENT_DIV',
   'GREATER',
   'LESS',
   'EQUAL',
   'UNARY_MINUS',
)


def t_COMMENT(t):
    r'\(\*\s+.*?\*\)'
    t.type = 'COMMENT'
    t.value = t.value[2:-2]
    return t

def t_LPAREN(t):
    r'\('
    return t
t_RPAREN  = r'\)'

# def t_COMMENT(t): 
#     r'(.*)' 
#     t.type = 'COMMENT' 
#     t.value = t.value[1:-1] 
#     return t


# Regular expression rules for simple tokens
# t_LPAREN  = r'\('
t_SEMICOLON = r';'
t_COMMA = r','
t_LBRACE = r'{'
t_RBRACE = r'}'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_ignore  = ' \t'
t_ASSIGNMENT = r'='




def t_DOUBLE(t):
    r"(-?\d*\.\d+)"
    t.value = float(t.value)
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r"(-?[1-9]\d*(_[1-9]\d*)*|0(_[1-9]\d*)*)(L|l)?"
    t.value = int(t.value.replace('_', '').rstrip('lL'))  
    return t

def t_CHAR(t):
    r'"(\\.|[^"\n])"'
    t.value = t.value[1:-1]
    return t

def t_IDENTIFIER(t):
    r"[a-zA-Z][a-zA-Z0-9_]*"
    if t.value in ['if', 'then', 'else', 'end', 'print', 'double', 'int', 'long', 'char', 'bool', 'fun', 'bool', 'true', 'false', 'orelse' ,'andalso']:
        t.type = 'KEYWORD'
    return t


def t_ASSIGNMENT_ADD(t):
    r'[+]='
    t.type = 'ASSIGNMENT_ADD'
    return t

def t_ASSIGNMENT_SUB(t):
    r'[-]='
    t.type = 'ASSIGNMENT_SUB'
    return t

def t_ASSIGNMENT_MUL(t):
    r'[\*]='
    t.type = 'ASSIGNMENT_MUL'
    return t

def t_ASSIGNMENT_DIV(t):
    r'/=+'
    t.type = 'ASSIGNMENT_DIV'
    return t



# Regular expression for comparison operators
def t_GREATER(t):
    r'>'
    t.type = 'GREATER'
    return t

def t_LESS(t):
    r'<'
    t.type = 'LESS'
    return t



# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore_COMMENT = r'\#.*'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



# Build the lexer
lexer = lex.lex()

inputFile = open('input.txt', 'r')

data = inputFile.read()

inputFile.close()
# Test it out
# data = '''
#     (* comments *)  
# fun sq (int x)=x*x; 
# if i > j then 1 else 2 ; 

# bool x = false;

# int x=-2;

# int x=2l; 

# long x12=2L; 

# {
# double i,j; 

# i+=j;
# }
# char c = "a";
 
# i-j=3;


# fun isWeekend x = (x = Sa orelse x = Su);

# '''

# Give the lexer some input
lexer.input(data)

outputFile = open('output.txt', 'w')

output = ""

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    output += str(tok) + "\n"

outputFile.write(output)