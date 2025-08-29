import tkinter as tk
import pygame
import os

print("Current working directory:", os.getcwd())

pygame.mixer.init()


sounds = {
    "Kick": pygame.mixer.Sound("ZachWaltersProject/kick-drum.wav"),
    "Snare": pygame.mixer.Sound("ZachWaltersProject/snare.wav"),
    "Hi-Hat": pygame.mixer.Sound("ZachWaltersProject/hihat.wav"),
    "Tom": pygame.mixer.Sound("ZachWaltersProject/tom.wav"),
}

root = tk.Tk()
root.title("Drum Machine")

canvas_width = 320
canvas_height = 320
cell_size = 160
	
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

for i in range(0, canvas_width, cell_size):
    canvas.create_line(i, 0, i, canvas_height, fill="gray")

for i in range(0, canvas_height, cell_size):
    canvas.create_line(0, i, canvas_width, i, fill="gray")
    
def play_kick():
    sounds["Kick"].play()
    
def play_snare():
    sounds["Snare"].play()

def play_hihat():
    sounds["Hi-Hat"].play()

def play_tom():
    sounds["Tom"].play()
    
button_kick = tk.Button(root, text="Kick", command=play_kick)
button_snare = tk.Button(root, text="Snare", command=play_snare)
button_hihat = tk.Button(root, text="Hi-Hat", command=play_hihat)
button_tom = tk.Button(root, text="Tom", command=play_tom)

canvas.create_window(80,80, window=button_kick)
canvas.create_window(240, 80, window=button_snare)
canvas.create_window(80, 240, window=button_hihat)
canvas.create_window(240, 240, window=button_tom)

def key_pressed(event):
    key_to_sound = {
        '1': play_kick,
        '2': play_snare,
        '3': play_hihat,
        '4': play_tom
    }
    sound_name = key_to_sound.get(event.char)
    if sound_name:
        sound_name()
        
root.bind("<KeyPress>", key_pressed)


root.mainloop()