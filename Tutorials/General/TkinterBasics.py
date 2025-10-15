
################ Initiation #################################################################################

# To create a simple, empty window

## Normal
#-------------------------------------------------------#
import tkinter as tk    # Imports tkinter

root = tk.Tk()          # Creates the main window (but doesnt display it yet)

# Your code goes here

root.mainloop()         # Displays the main window and starts the app
#-------------------------------------------------------#

## Simplified variation
#-------------------------------------------------------#
"         Note                          "
"You can also use                       "
"from tkinter import *                  "
"To avoid having to use tk all the time "
"For example:                           "

from tkinter import *

root = Tk()

root.mainloop()
# This code and the previous one works exactly the same
#-------------------------------------------------------#







################ Widgets #########################################################################

# To start creating texts, images, buttons and everything else we create widgets
# Here are some example widgets

#-------------------------------------------------------#
import tkinter as tk
root = tk.Tk()

text = tk.Label(root, text="Hello world")  # Creates the text widget
text.place(x=0, y=0)                       # Places the widget in the window

root.mainloop()
#-------------------------------------------------------#

# Widgets can take many parameters, like text color, background color, etc

"You can find the whole widget list here --> https://coderslegacy.com/python/list-of-tkinter-widgets/"

# More examples of many widgets
#------------------------------------------------------#
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
#------------------------------------------------------#
"This example is the same as Examples\SimpleTkinter.py"
"In case you want to test it"

"Here is the full tkinter color list --> https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html"








################ CONFIGURATION ##############################################################################3

# To configure window properties you can use
root.title("Waffles")           # Change window title
root.iconbitmap("my_icon.ico")  # Change window icon, Replace the str with the path to your .ico file
root.iconphoto(True, tk.PhotoImage(file="my_icon.png")) # Change to a png ICON
root.geometry("400x300")        # Change screen size
root.resizable(True, False)     # Enable or disable screen rezising on x and y
root.minsize(400, 300)          # Minimum window size
root.maxsize(1200, 800)         # Maximum window size
root.attributes("-fullscreen", True) # Fullscreen
root.overrideredirect(True)     # Removes window decorations such as titlebar

# You can also change any widget property, for example when using
label = tk.Label(root, text="Hello", bg='black')
# You can change any of those parameters later, even ones you didnt set using
label.configure(text= "Goodbye")
label.configure(bg= 'white')
label.configure(fg= 'yellow')
