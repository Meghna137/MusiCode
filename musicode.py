import streamlit as st
import pygame
import numpy as np
import os

pygame.mixer.init()
def load_sound_dash(option):
    if option == 'Piano': 
        return pygame.mixer.Sound("piano1.wav")
    elif option == 'Drums': 
        return pygame.mixer.Sound("drums1.wav")
    elif option == 'Guitar': 
        return pygame.mixer.Sound("guitar1.wav")

def load_sound_dot(option):
    if option == 'Piano': 
        return pygame.mixer.Sound("piano2.wav")
    elif option == 'Drums': 
        return pygame.mixer.Sound("drums2.wav")
    elif option == 'Guitar': 
        return pygame.mixer.Sound("guitar2.wav")

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

def text_to_morse(text):
    return ' '.join(morse_code_dict.get(char.upper(), '') for char in text)

def play_morse_code(morse_code, dot_sound, dash_sound):
    for symbol in morse_code:
        if symbol == '.':
            dot_sound.play()
            pygame.time.delay(300)  # dot
        elif symbol == '-':
            dash_sound.play()
            pygame.time.delay(900)  # dash
        else:
            pygame.time.delay(300)  # between characters

#ui
st.title("MusiCode")
user_input = st.text_input("Enter text to convert to Morse Code:")
option = st.radio("Select your instrument:", ('Piano', 'Drums', 'Guitar'))

if user_input:
    morse_code = text_to_morse(user_input)
    st.write(f"Morse Code: {morse_code}")
    
    if st.button("Play Music"):
        dot_sound = load_sound_dot(option)
        dash_sound = load_sound_dash(option)
        play_morse_code(morse_code, dot_sound, dash_sound)
    