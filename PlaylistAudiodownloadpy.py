from pytube import Playlist
import re
import os

YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
DOWNLOAD_DIR = 'c:/Users/jao/Downloads/pythonvid'

link = input('Coloca o link da playlist aqui: ')
yt = Playlist(link)

# this fixes the empty playlist.videos list
yt._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print('Na playlist tem %s' % len(yt.video_urls), 'musicas.')

print("Começando a baixar...")

for video in yt.videos:
    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    audioStream.download(output_path=DOWNLOAD_DIR)
    
print('Download finalizado!')