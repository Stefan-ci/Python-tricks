import sounddevice as sound
from scipy.io.wavfile import write
import wavio as wv

frequence = 44100
duration = 10 # Seconds

recording = sound.rec(int(duration * frequence), samplerate=frequence, channels=2)
sound.wait()
write('recorded.wav', frequence, recording)
