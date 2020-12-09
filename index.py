from winsound import Beep
import time
def freq(o, s):
    if s == '도':     return 524*2**o
    elif s == '도샾': return 554*2**o
    elif s == '레':   return 587*2**o
    elif s == '레샾': return 622*2**o
    elif s == '미':   return 659*2**o
    elif s == '파':   return 698*2**o
    elif s == '파샾': return 740*2**o
    elif s == '솔':   return 784*2**o
    elif s == '솔샾': return 831*2**o
    elif s == '라':   return 880*2**o
    elif s == '라샾': return 932*2**o
    elif s == '시':   return 988*2**o
import keyboard
while 1:
    if keyboard.is_pressed('1'):   Beep(freq(0,'도'),200)
    elif keyboard.is_pressed('2'): Beep(freq(0,'레'),200)        
    elif keyboard.is_pressed('3'): Beep(freq(0,'미'),200)   
    elif keyboard.is_pressed('4'): Beep(freq(0,'파'),200)   
    elif keyboard.is_pressed('5'): Beep(freq(0,'솔'),200)   
    elif keyboard.is_pressed('6'): Beep(freq(0,'라'),200)   
    elif keyboard.is_pressed('7'): Beep(freq(0,'시'),200)        
    elif keyboard.is_pressed('8'): Beep(freq(1,'도'),200) 
    elif keyboard.is_pressed('z'): Beep(freq(1,'레'),200)
    elif keyboard.is_pressed('x'): Beep(freq(1,'미'),200)   
    elif keyboard.is_pressed('c'): Beep(freq(1,'파'),200)   
    elif keyboard.is_pressed('v'): Beep(freq(1,'솔'),200)   
    elif keyboard.is_pressed('b'): Beep(freq(1,'라'),200)   
    elif keyboard.is_pressed('n'): Beep(freq(1,'시'),200)