import tkinter as tk

root = tk.Tk()
root.title("Drum Machine")

canvas_width = 400
canvas_height = 400
cell_size = 40
	
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

for i in range(0, canvas_width, cell_size):
    canvas.create_line(i, 0, i, canvas_height, fill="gray")

for i in range(0, canvas_height, cell_size):
    canvas.create_line(0, i, canvas_width, i, fill="gray")

root.mainloop()