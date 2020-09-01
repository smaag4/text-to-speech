# Dieser Code erstellt aus einer Textdatei ein MP3 File

import os
from gtts import gTTS

#Options

language = "en"
slow_speed = False
output = "<OUTPUT FILE.mp3>"

def reading_from_file():
    file_to_read = '<INPUT FILE.txt>'
    f = open(file_to_read, 'r')
    file_text = f.read()
    f.close()

    audio_created = gTTS(text=file_text, lang=language, slow=slow_speed)
    audio_created.save(output)

    #os.system(f'start {output}')

if __name__ == '__main__':
    reading_from_file()
