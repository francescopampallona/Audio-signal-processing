import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import sounddevice as sd
'''
SEGNALE
'''
def signal(w, t):
    signal = np.sin(w*t)*np.sin((w/500)*t)
    return signal
    
'''
DATI SULLA DURATA DEL SEGNALE E SUL SUO CAMPIONAMENTO 
'''
DURATA = 4.0 #Durata del suono in secondi
SF = 10000.0 #FREQUENZA DI CAMPIONAMENTO

'''
DATI DEL SEGNALE
'''
f = 500 #Frequenza del segnale
w = 2*math.pi*f #Pulsazione del segnale
t = np.arange(0, DURATA, 1/SF)
function = signal(w, t)
   

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


