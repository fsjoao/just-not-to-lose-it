import pyttsx3
import PyPDF2 as pdf
from gtts import gTTS
import pdfplumber

livro = open('pfedital.pdf', 'rb')
leitorpdf = pdf.PdfFileReader(livro)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 160)

for voice in voices:
    engine.setProperty('voice', voice.id)

paginas = leitorpdf.numPages

for numeropag in range(1, paginas):
    page = leitorpdf.getPage(numeropag)
    textoparaaudio = page.extractText()
    engine.say(textoparaaudio)

engine.save_to_file(livro, 'test.mp3')
engine.runAndWait()
#engine.save_to_file(leitorpdf, 'test.mp3')

