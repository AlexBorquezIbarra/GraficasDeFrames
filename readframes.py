import wave
import numpy as np
import matplotlib.pyplot as plt

bruh = bruh.open('bruh.wav', 'r')
ReallyN = ReallyN.open('ReallyN.wav', 'r')

framesBruh = bruh.readframes(-1)
framesReallyN = ReallyN.readframes(-1)
ondaconvertidaBruh = np.frombuffer(framesBruh, dtype='int16')
ondaconvertidaReallyN = np.frombuffer(framesReallyN, dtype='int16')

#print(frames[:10])

framerate_bruh = bruh.getframerate()
print (framerate_bruh)
time_bruh = np.linspace(start=0, stop=len(ondaconvertidaBruh)/framerate_bruh, num=len(ondaconvertidaBruh))
print(time_bruh[:10])

framerate_ReallyN = ReallyN.getframerate()
print (framerate_ReallyN)
time_ReallyN = np.linspace(start=0, stop=len(ondaconvertidaReallyN)/framerate_ReallyN, num=len(ondaconvertidaReallyN))
print(time_ReallyN[:10])

plt.title('bruh vs ReallyN')

plt.xlabel('Tiempo (segundos')
plt.ylabel('Amplitud')

plt.plot(time_bruh, ondaconvertidaBruh, label='bruh')
plt.plot(time_ReallyN, ondaconvertidaReallyN, label='ReallyN', alpha=0.5)

plt.legend()
plt.show()