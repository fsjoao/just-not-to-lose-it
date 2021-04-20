from pytube import YouTube
from pytube.cli import on_progress
import os 

#Coloca o link e o local se quiser
#Vou fazer com o local direto 

link = input('Coloque o link do vídeo aqui: ')
path = ('c:/Users/jao/Downloads/pythonvid')

#faz a progress bar
yt = YouTube(link, on_progress_callback=on_progress)

#Detalhes, duração etc
print('Título: ', yt.title)
#Pega o tamanho e divide por 60 para virar minutos
duracao = yt.length/60
#Formata os minutos em 2 numeros após a virgula
print('Tamanho do vídeo: {:.2f}'.format(duracao))

#Pega maior resolução
ys = yt.streams.get_highest_resolution()

#Começa o 

print('Baixando...')
ys.download(path)
print('======== Download completo! ==========') 