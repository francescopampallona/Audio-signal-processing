import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import sounddevice as sd
'''
DATI SUL CAMPIONAMENTO 
'''
DURATA = 4.0 #Durata del suono in secondi
SF = 1500.0 #FREQUENZA DI CAMPIONAMENTO

'''
DATI DEL SEGNALE
'''
f = 500 #Frequenza del segnale
w = 2*math.pi*f #Pulsazione del segnale
t = np.arange(0, DURATA, 1/SF)
function = np.sin(w*t)
   

'''
Grafico del segnale in funzione del tempo
'''
print("GRAFICO")
fig, ax = plt.subplots()
ax.plot(t, function)
plt.title('SEGNALE SONORO IN FUNZIONE DEL TEMPO')
plt.ylabel('SUONO')
plt.xlabel('TEMPO IN SECONDI')
#plt.savefig("signal.png")
ax.grid()
plt.show()
'''
SALVATAGGIO DEL SEGNALE IN WAV E RIPRODUZIONE DEL SUONO TRAMITE LA LIBRERIA sounddevice
'''
print("NUMERO DI CAMPIONI: ",DURATA*SF)
write('test.wav', int(SF), function)
sd.play(function, SF)


