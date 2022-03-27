import serial                                                              #Serial imported for Serial communication
import time
import ply.lex as lex
import ply.yacc as yacc
import sys
StringTypes = (str, bytes)

#Lexicale Analysis
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
#----------------------------------------------
#Syntaxix Analysis
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
    commandSERVO : TURNLEFT INT
        | TURNRIGHT INT
    '''
    p[0] = (p[1],p[2])
def p_error(p):
    print("Syntax ERROR !")
    
def p_empty(p):
    '''
    empty :
    '''
    p[0]=None



def traitementFORWARD(p) :
    print('here we go traitement DC motor FORWARD')
    command,power,temps=p
    ArduinoUnoSerial.write(bytes('0', 'utf-8'))
    
    while True :
     print (ArduinoUnoSerial.readline())                         #read the serial data and print it as line 
     print ("You have new message from Arduino")
    
    time.sleep(temps) #send 1 to the arduino's Data code        
    
    
def traitementREVERSE(p) :
    
    print('here we go traitement DC motor REVERSE')
    command,power,temps=p
    #ArduinoUnoSerial.write(b'REVERSE')
    ArduinoUnoSerial.write(bytes('1' , 'utf-8'))
    
    #send 1 to the arduino's Data code        
    time.sleep(temps)   


def traitementTURNRIGHT(p) :
    print('here we go traitement TURNRIGHT')
    command,temps=p
   # ArduinoUnoSerial.write(b'TURNRIGHT')
    ArduinoUnoSerial.write(bytes('2', 'utf-8'))
    #send 1 to the arduino's Data code        
    time.sleep(temps) 
     
def traitementTURNLEFT(p) :
    print('here we go traitement TURNLEFT')
    command,temps=p
    #ArduinoUnoSerial.write(b'TURNLEFT')
    ArduinoUnoSerial.write(bytes('3', 'utf-8')) #send 1 to the arduino's Data code        
    time.sleep(temps) 
 
def traitementSTOP(p) :
    print('here we go traitement STOP motor')
    command=p
    #ArduinoUnoSerial.write(b'STOP')
    ArduinoUnoSerial.write(bytes('4', 'utf-8'))#send 1 to the arduino's Data code        
    time.sleep(2) 
 
parser = yacc.yacc()
#--------------------------------------------


#Required to use delay functions   
ArduinoUnoSerial = serial.Serial('com4',9600)#Create Serial port object called ArduinoUnoSerialData time.sleep(2)                                                             #wait for 2 secounds for the communication to get established
ArduinoUnoSerial.reset_input_buffer()
print (ArduinoUnoSerial.readline())                         #read the serial data and print it as line 
print ("You have new message from Arduino")

while True :  #get input from user
    try :
        var=input('')
    except EOFError:
        break
    parser.parse(var)

