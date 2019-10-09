import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import sounddevice as sd
    
'''
DATI SULLA DURATA DEL SEGNALE E SUL SUO CAMPIONAMENTO 
'''
DURATA = 4.0 #Durata del suono in secondi
SF = 10000.0 #FREQUENZA DI CAMPIONAMENTO

'''
DATI DEL SEGNALE (w=pulsazione)
'''
w1 = 2*math.pi*500
w2 = 2*math.pi*4
t = np.arange(0, DURATA, 1/SF)
function = np.sin(w1*t)*np.sin(w2*t)
   

'''
Grafico del segnale in funzione del tempo
'''
fig, ax = plt.subplots()
ax.plot(t, function)
plt.title('SEGNALE SONORO IN FUNZIONE DEL TEMPO')
plt.ylabel('SUONO')
plt.xlabel('TEMPO IN SECONDI')
plt.savefig("signal.png")
ax.grid()
plt.show()
'''
SALVATAGGIO DEL SEGNALE IN WAV
'''
print("NUMERO DI CAMPIONI: ",DURATA*SF)
write('test.wav', int(SF), function)
sd.play(function, SF)


