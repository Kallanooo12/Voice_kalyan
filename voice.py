
"""
pkg install play-audio
pip install gtts
"""
import os
try:
    import gtts
except:
    
    os.system("pip install gtts")
    import gtts
from gtts import gTTS

def create_(text,file):
    my_a = gTTS(text)
    my_a.save(file)


def play_audio(audio_file):
    os.system("play-audio "+audio_file)
    

def dual(text,file):
    create_(text,file)
    play_audio(file)

dual("hello sir ,I am  is kalyan haker and you is this fuk and garly hak and phone of you hack you is a so sad yas yas but sory you is a abal this my kalyan haker your mother's is so cut and so hot you mother's is give me and xxxxxxxxxxxxxx of night of morning of saxy day and you fuk and my name is kalyan haker so dangers haker your mother's is so carful secority and your phone my cantery of bangladsh my home borshil and my village charduni my calass of 9 of paower ful haker my     oky byyy by by by by by by by by and save your mother's","l.mp3")