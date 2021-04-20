import pytube

#Coloca o link e o local se quiser
#Vou fazer com o local direto 
link = input('Coloque o link do vídeo aqui!')
#path = input('bota o cao do lugar que tu quer macho')
yt = pytube.YouTube(link)

#Detalhes, duração etc
print('Título: ', yt.title)
print('Tamanho do vídeo: ', yt.length, 'segundos')

#Pega maior resolução
video = yt.streams.first()

video.download()

#Começa o download
#print('Baixando...')
#ys.download(path)
#print('Download completo!') 