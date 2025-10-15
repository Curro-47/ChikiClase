import tkinter as tk
root = tk.Tk()
root.geometry("1000x600")

## Getting the images from the Resources folder
img_forest = tk.PhotoImage(file="Tkinter\\Resources\\forest.png").subsample(3,3) # Here subsample makes the images smaller, they were too large to fit the 1000x600 screen
img_treasure = tk.PhotoImage(file="Tkinter\\Resources\\treasure.png").subsample(1,1)
img_death = tk.PhotoImage(file="Tkinter\\Resources\\death.png").subsample(2,2)

## Create all objects
text = tk.Label(root, text="Description") # Top text
text.place(x=500, y=20, anchor="center")

image = tk.Label(root, image=img_forest) # Image
image.place(x=500, y=300, anchor="center")

button1 = tk.Button(root, text="button1") # Button left
button1.place(x=250, y=550, anchor="center")

button2 = tk.Button(root, text="button2") # Button right
button2.place(x=750, y=550, anchor="center")

##### SCENES
#----------------------------------#
def scene_forest():
    text.configure(text= "You are in a forest, what direction do you walk to") ## Description
    image.configure(image= img_forest) ## Scene Image

    ## Changes the buttons text
    button1.configure(text="Left")
    button2.configure(text="Right")

    ## Change to what scenes the buttons take you
    button1.configure(command=scene_win)
    button2.configure(command=scene_loose)
#----------------------------------#
def scene_win():
    text.configure(text= "You found the treasutre, yaaaay") ## Description
    image.configure(image= img_treasure) ## Scene Image

    ## Changes the buttons text
    button1.configure(text="Restart")
    button2.configure(text="Exit")

    ## Change to what scenes the buttons take you
    button1.configure(command=scene_forest)
    button2.configure(command=scene_exit)
#----------------------------------#
def scene_loose():
    text.configure(text= "You died") ## Description
    image.configure(image= img_death) ## Scene Image

    ## Changes the buttons text
    button1.configure(text="Restart")
    button2.configure(text="Exit")

    ## Change to what scenes the buttons take you
    button1.configure(command=scene_forest)
    button2.configure(command=scene_exit)
#---------------------------------#
def scene_exit(): # This function closes the app
    root.destroy()

scene_forest()
root.mainloop()