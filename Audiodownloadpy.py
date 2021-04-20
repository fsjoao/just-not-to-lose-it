from pytube import YouTube
from pytube.cli import on_progress
#Para botar o link do video
link = input('Coloca o link do vídeo aqui: ')
yt = YouTube(link, on_progress_callback=on_progress)

#Pega todos as extensões do vídeo, mp3, mp4, e filtra apenas o aúdio.
videos= yt.streams.filter(only_audio=True)

#Detalhes, duração etc
print('Título: ', yt.title)
#Pega o tamanho e divide por 60 para virar minutos
duracao = yt.length/60
#Formata os minutos em 2 numeros após a virgula
print('Tamanho do vídeo: {:.2f}'.format(duracao))

#Lista as extensões, e da a opção pra escolher de acordo com o digito qual quer, seja mp4, webm...
###for i in range(len(videos)):
    ###print(i,'. ',videos[i])
#vnum = int(input("Coloque o dígito do vídeo: "))

#Como só tenho interesse em MP4, e na melhor qualidade, é a opção 0, a primeira, então não quero listar e já deixo direto.
vnum = 0
#Local de download
videos[vnum].download("c:/Users/jao/Downloads/pythonvid")
print('Teje baixado meu querido.')