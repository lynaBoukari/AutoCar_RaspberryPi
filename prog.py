import ply.lex as lex
import ply.yacc as yacc
import sys
StringTypes = (str, bytes)



tokens = ('REVERSE','FORWARD','TURNLEFT','TURNRIGHT','STOP','INT', 'FLOAT')

def t_FORWARD(t):
    r'FORWARD'
    return t

def t_REVERSE(t):
    r'REVERSE'
    return t
def t_TURNLEFT(t):
    r'TURNLEFT'
    return t
def t_TURNRIGHT(t):
    r'TURNRIGHT'
    return t
def t_STOP(t):
    r'STOP'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value=float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value=int(t.value)
    return t

t_ignore  = ' \t'

def t_error(t):
    print ("illegal expression")
    t.lexer.skip(1)
    
lexer= lex.lex()

def p_prog(p) :
    '''
    prog : commandDC
    | commandSERVO
    | STOP
    | empty
    '''
    if p[1][0] == 'REVERSE':       
            traitementDC(p[1]);
    elif (p[1][0]) == 'FORWARD':       
            traitementDC(p[1]);
    elif (p[1][0]) == 'TURNRIGHT' :
            traitementSERVO(p[1]);
    elif p[1][0] == 'TURNLEFT' :
            traitementSERVO(p[1]);
    elif p[1] == 'STOP' :
            traitementSTOP(p[1]);
            
    else : print("No command in input")
    
def p_commandDC(p) :
    '''
    commandDC : FORWARD FLOAT INT
        | REVERSE FLOAT INT
    '''
    p[0] = (p[1],p[2],p[3])

def p_commandSERVO(p) :
    '''
    commandSERVO : TURNLEFT FLOAT
        | TURNRIGHT FLOAT
    '''
    p[0] = (p[1],p[2])
def p_error(p):
    print("Syntax ERROR !")
    
def p_empty(p):
    '''
    empty :
    '''
    p[0]=None

def traitementDC(p) :
    print('here we go traitement DC motor')
    command,power,time=p

def traitementSERVO(p) :
    print('here we go traitement SERVO motor')
    command,angle=p
 
def traitementSTOP(p) :
    print('here we go traitement STOP motor')
    command=p
    
parser = yacc.yacc()
while True :
    try :
        s=input('')
    except EOFError:
        break
    parser.parse(s)