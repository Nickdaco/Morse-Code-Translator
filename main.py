import pygame as pg

# Uses pygame mixer to play sound

def playMorse(letter): # play the morse code
    file = 'PATH TO MORSE FOLDER/Morse-{}.ogg.mp3'.format(letter)
    volume = 1

    # initializes mixer
    pg.mixer.init()
    pg.mixer.music.set_volume(volume)

    pg.mixer.music.load(file)
    pg.mixer.music.play()

    clock = pg.time.Clock()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

morseDict =\
    {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
     'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
     'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.','O': '---', 'P': '.--.',
     'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
     'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..','1': '.----', '2': '..---',
     '3': '...--', '4': '....-', '5': '.....', '6': '-....','7': '--...', '8': '---..',
     '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-','?': '..--..', '/': '-..-.',
     '-': '-....-', '(': '-.--.', ')': '-.--.-', " ": " "}


# Class contains all different types of translations
class MorseTranslate:

    def morseTranslateBoth(self, input):

        string = ""
        for letter in input:
            if letter == " ":
                string += morseDict[letter.upper()]
            else:
                try:
                    string += morseDict[letter.upper()] + ' '
                    playMorse(letter)
                except KeyError:
                    pass

        print(string)
        return string

    def morseTranslateAudio(self, input):

        for letter in input:
            if letter == " ":
                pass
            else:
                try:
                    playMorse(letter)
                except KeyError:
                    pass

    def morseTranslateText(self, input):

        string = ""
        for letter in input:
            if letter == " ":
                string += morseDict[letter.upper()]
            else:
                try:
                    string += morseDict[letter.upper()] + ' '
                except KeyError:
                    pass
        print(string)
        return string


