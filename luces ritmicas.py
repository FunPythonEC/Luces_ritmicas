import neopixel as np
import machine, time
adc = machine.ADC(0)
np = np.NeoPixel(machine.Pin(12), 19)
while True:
    dat=adc.read()
    
    
    if dat <= 65:
        num=3        
    if dat > 65 and dat < 67:
        num=10
    if dat > 67 :
        num=19                        
   
        
    for i in range(int(num)):
        np[i]=(int(dat/10), dat, int(dat/5))

           
    for i in range(int(num),19):
        np[i]=(0,0,0)
    np.write()
    print(dat)
    print(num)
    print(np[2])
   
    
