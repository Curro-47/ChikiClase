import tkinter as tk
root = tk.Tk()

#### LABEL (text) WIDGET
text = tk.Label(root, text="Hello world", bg='black', fg='white')
text.place(x=0, y=0)

#### LABEL (image) WIDGET
img = tk.PhotoImage("path/to/your/image.png") # Change this to the actual path to your image file
image = tk.Label(root, image=img)
image.place(x=100, y=100)

def button_function(): # Gets executed on button press
    root.destroy()

#### BUTTON WIDGET
button = tk.Button(root, text="Exit", command=button_function)
button.place(x=100, y=0)

root.mainloop()