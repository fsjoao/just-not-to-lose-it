import pdfplumber  # LIB USADA PRA TRANSFORMAR O TXT
from gtts import gTTS  # LIB PRA CONVERTER EM AUDIO

raw_str = ""  

#u_path = input("Enter the path and filename") #ESSE SE FOR PRA COLOCAR O LOCAL
########### TIRA UM E BOTA O OUTRO ###########
u_path =  "snowden2.pdf" # AQUI O NOME DO ARQUIVO COM .PDF

# OPENING AND READING
with pdfplumber.open(u_path) as pdf:
    total_pages = pdf.pages  # GETTING ALL PAGES OF PDF

    # ITERATING OVER ALL PAGES
    for itr in range(len(total_pages)):
        first_page = pdf.pages[itr] #ALTERAR AQUI SE QUISER COMEÇAR POR UMA PAGINA ESPECIFICA

        try:
            raw_str = raw_str + "" + first_page.extract_text()
        except Exception as e:
            print(e)

# PRINTA O TEXTO QUE VAI SER CONVERTIDO EM AUDIO
#print(f"Text we fetch from {u_path} ->" + raw_str) #TIRA ## SE QUISER

# INIT GTTS
gtts_obj = gTTS(text=raw_str, lang="pt-br")
# BOTANDO O NOME AQUI DO ARQUIVO
filename = input("Input filename for your audio ")

# SALVANDO O ARQUIVO
while True:
    try:
        gtts_obj.save(filename + ".mp3")
        break
    except Exception as e:
        print(e)
print("Acabou corno, abre no VLC pra regular a velocidade.")
