from gtts import gTTS
import pygame
import os
import uuid

def speak(text):
    print(f"Jarvis: {text}")
    tts = gTTS(text=text, lang='en', tld='co.uk')
    filename = f"temp_{uuid.uuid4()}.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.quit()
    os.remove(filename)
