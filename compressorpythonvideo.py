import glob
import zipfile
import os

def compress(filename, volumeSize, filetype='*'):
    ''' Compacta arquivos do diretório em volumes filename{n}.zip
        com o tamanho máximo de volumeSize bytes.

        Uso: compress('volume.zip', 50000000, filetype='jpg')

        filename - Nome dos volumes .zip que serão gerados.
                   Ex: filename='myzip.zip'
                   myzip.zip, myzip1.zip, myzip2.zip, myzip(n)...

        filetype - Se informado compacta apenas os arquivos com a
                   extensão informada. Por padrão compacta todos
                   arquivos do diretório.
                   Ex: filetype='png'

        volumeSize - Tamanho máximo em bytes dos volumes .zip.
                     Ex(50MB): volumSize = 50000000

    '''
    userFileName = filename

    if filetype != '*':
        filesToCompress = [file for file in glob.glob('*.' + filetype)]
    else:
        filesToCompress = [file for file in glob.glob('*.png')]

    volumNumber = 1
    for file in filesToCompress:
        if os.path.isfile(filename):
            tmp = open(filename, 'rb').read()

        with zipfile.ZipFile(filename, 'a') as myzip:
            myzip.write(file)

        zipVolumeSize = os.stat(filename).st_size
        # se com a inclusão do arquivo exceder o tamamho maximo do volume
        if zipVolumeSize > volumeSize:
            # recupera o arquivo antes da inclusão
            with open(filename, 'wb') as myzip:
                myzip.write(tmp)

            # cria um novo volume zip e insere o arquivo
            name, extension = userFileName.split('.')
            filename = name + str(volumNumber) + '.' + extension
            with zipfile.ZipFile(filename, 'a') as myzip:
                myzip.write(file)
            volumNumber += 1
    print('{} arquivos compactados em {} volumes.'.format(len(filesToCompress),
                                                              volumNumber))