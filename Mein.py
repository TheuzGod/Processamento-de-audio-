#CARREGANDO E REPRODUZINDO
import urllib.request
from pydub import AudioSegment
from pydub.playback import play
#Baixar um arquivo de áudio
urllib.request.urlretrive("https://tinyurl.com/wx9amev", "matallic-dums.wav")
#Carregar no PyDub
loop = AudioSegment.from_wav("metallic-drum.wav")
#Jogue o resultado
play(loop)

#PROCESSAMENTO BÁSICO DE ÁUDIO

#Repita 2 vezes
loop2 = loop * 2:
#Obter comprimento em milissegundos
length = Len(loop2)
#Definir o tempo de desvanecimento
fade_time = int(length * 0.5")
#Fade dentro e fora
fade = loop2.falle_in(fade_time).fade_out(fade_time)
