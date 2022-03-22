import ply.lex as lex
import ply.yacc as yacc
import sys
import Rpi.GPIO as gpio
import time
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
            traitementREVERSE(p[1]);
    elif (p[1][0]) == 'FORWARD':       
          traitementFORWARD(p[1]);
    elif (p[1][0]) == 'TURNRIGHT' :
            traitementTURNRIGHT(p[1]);
    elif p[1][0] == 'TURNLEFT' :
            traitementTURNLEFT(p[1]);
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




def init():

    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)


def traitementFORWARD(p) :
    print('here we go traitement DC motor FORWARD')
    command,power,time=p
    init()
    gpio.output (7, True)
    gpio.output (11, False)
    gpio.output (13, False)
    gpio.output (15, True)
    time.sleep(time) 
    gpio.cleanup()
    
def traitementREVERSE(p) :
    print('here we go traitement DC motor FORWARD')
    command,power,time=p
    init()
    gpio.output (7, False)
    gpio.output (11, True)
    gpio.output (13, True)
    gpio.output (15, False)
    time.sleep(time)
    gpio.cleanup()


def traitementTURNRIGHT(p) :
    print('here we go traitement TURNRIGHT')
    command,angle=p
    init()
    gpio.output (7, False)
    gpio.output (11, True)
    gpio.output (13, False)
    gpio.output (15, False)
    time.sleep(angle)
    gpio.cleanup()
     
def traitementTURNLEFT(p) :
    print('here we go traitement TURNLEFT')
    command,angle=p
    init() 
    gpio.output (7, True)
    gpio.output (11, True)
    gpio.output (13, True)
    gpio.output (15, False)
    time.sleep(angle)
    gpio.cleanup()
 
def traitementSTOP(p) :
    print('here we go traitement STOP motor')
    command=p
    init()
    gpio.output (7, False)
    gpio.output (11,False)
    gpio.output (13, False)
    gpio.output (15, False)
    gpio.cleanup()
 
parser = yacc.yacc()
while True :
    try :
        s=input('')
    except EOFError:
        break
    parser.parse(s)