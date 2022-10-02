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
