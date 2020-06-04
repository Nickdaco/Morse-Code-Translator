from tkinter import *
from main import MorseTranslate

root = Tk()

root.title('Morse Translator')

# Enter Label
enterLabel = Label(root, text='Enter:',)
enterLabel.grid(row=0, column=0)

# Allow user to type
enter = Entry(root, width=35)
enter.grid(row=0, column=1, columnspan=3, padx=10, pady=20)

outputLabel = Label(root)

# Copy Button
def copyClick():
    morseText = MorseTranslate().morseTranslateText(enter.get())
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(morseText)
    print("Copied!")

copyButton = Button(root, text='Copy to Clipboard', command=copyClick)


# Button Press Logic
def textClick():
    # Clear old stuff written in outputLabel
    global outputLabel
    outputLabel.destroy()
    # Get new stuff and display
    morseText = MorseTranslate().morseTranslateText(enter.get())
    outputLabel = Label(root, text=morseText)
    outputLabel.grid(row=2, column=1, columnspan=5, padx=30, pady=20)
    # Add copy button
    copyButton.grid(row=2, column=0, padx=10)


def bothClick():

    # Clear old stuff written in outputLabel
    global outputLabel
    outputLabel.destroy()
    # Get new stuff and display
    morseText = MorseTranslate().morseTranslateText(enter.get())
    outputLabel = Label(root, text=morseText)
    outputLabel.grid(row=2, column=1, columnspan=5, padx=30, pady=20)
    # Play sound
    MorseTranslate().morseTranslateBoth(enter.get())
    # Add copy button
    copyButton.grid(row=2, column=0)


def audioClick():
    # Play sound
    MorseTranslate().morseTranslateAudio(enter.get())


# Buttons
textButton = Button(root, text='Text', command=textClick)
bothButton = Button(root, text='Both', command=bothClick)
audioButton = Button(root, text='Audio', command=audioClick)
copyButton = Button(root, text='Copy to Clipboard', command=copyClick)

# Add Buttons to grid
textButton.grid(row=1, column=1)
bothButton.grid(row=1, column=2)
audioButton.grid(row=1, column=3)


root.mainloop()
