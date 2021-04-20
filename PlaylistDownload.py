import pytube  
url = input('BOTA')
playlist = pytube.Playlist (url)
trash = 'c:/Users/jao/Downloads/pythonvid'
print('Na playlist tem %s' % len(playlist.video_urls), 'videos.')

print("Começando a baixar...")

for url in playlist:
    video = pytube.YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path=trash)

print('Download finalizado!')