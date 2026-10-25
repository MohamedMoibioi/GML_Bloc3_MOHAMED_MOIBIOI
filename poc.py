import time 
import requests 
data_buffer = [] 
def main_loop(): 
global data_buffer 
while True: 
val = {'x': 12, 'y': -3.0} 
data_buffer.append(val)        
# <--- CAUSE 1 : Fuite Mémoire (Saturation RAM) 
if val['y'] < -2.5: 
requests.post('http://api.gml.com/alert...', json=val) # <--- CAUSE 2 : 
Appel Réseau Bloquant 
time.sleep(0.1) 