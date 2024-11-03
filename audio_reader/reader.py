from scipy.io.wavfile import read
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

'''
READ AUDIO FROM WAV FILE 
'''
print("Inserire il titolo del file wav. Es. title.wav")
title=input()
data=read(title)
'''
SAMPLE FREQUENCY
'''
sf=data[0]
print("SAMPLE FREQUENCY: ", sf)
'''
SIGNAL DATA
'''
sound=np.array(data[1])
SAMPLES=len(sound)
DURATA = SAMPLES/sf
print(SAMPLES, " " , sound.dtype, " DURATA: ", DURATA, " s")
'''
GRAFICO DEL SEGNALE AUDIO
'''
t = np.arange(0, DURATA, 1/sf)
fig, ax = plt.subplots()
ax.plot(t, sound)
plt.title('SEGNALE SONORO IN FUNZIONE DEL TEMPO')
plt.ylabel('SUONO')
plt.xlabel('TEMPO IN SECONDI')
plt.savefig("signal.png")
ax.grid()
plt.show()
'''
PLAY AUDIO
'''
sd.play(sound, sf)


