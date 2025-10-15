#### This is a tutorial on the videogame 2nd partial exam


# First we will initialize our tkinter file as usual
# If you dont know how to do this read TkinterBasics.py in the Tkinter folder

#----------------------------------#
import tkinter as tk
root = tk.Tk()

root.mainloop()
#----------------------------------#

# Now, in this simple version, each screen will have a Text, an Image, and 2 buttons
# So, lets create those

#----------------------------------#
import tkinter as tk
root = tk.Tk()
root.geometry("1000x600")

## Gets the image from the Resources folder
img_forest = tk.PhotoImage(file="Tkinter\\Resources\\forest.png").subsample(3,3)

## Creates the top text
text = tk.Label(root, text="Description")
text.place(x=500, y=20, anchor="center")

## Creates the image
image = tk.Label(root, image=img_forest)
image.place(x=500, y=300, anchor="center")

## Creates the buttons
button1 = tk.Button(root, text="button1")
button1.place(x=250, y=550, anchor="center")

button2 = tk.Button(root, text="button2")
button2.place(x=750, y=550, anchor="center")

root.mainloop()
#----------------------------------#
# This will make a screen with our forest image, a text on top that says "description", and 2 buttons below
"You can see the result in the folder Example Images, it is titled rpg0"

# Now lets make the starter screen
# Every screen will be a function, so we can easily go from one to another
# If you dont know what functions are, check PyyhonBasics.py

#----------------------------------#
def scene_forest(): ## Here we configure our scene
    text.configure(text= "You are in a forest, what direction do you walk to")
    image.configure(image= img_forest)

    ## Changes the buttons text
    button1.configure(text="Left")
    button2.configure(text="Right")

scene_forest()
root.mainloop()
#----------------------------------#

# Dont forget to execute the scene_forest function so that that is the initial scene

## So now we can easily add scenes, we just need to change to what scene the buttons take you
## This is a finalized example scene

#----------------------------------#
img_forest = tk.PhotoImage(file="Tkinter\\Resources\\forest.png").subsample(3,3)
img_treasure = tk.PhotoImage(file="Tkinter\\Resources\\treasure.png").subsample(3,3)
img_death = tk.PhotoImage(file="Tkinter\\Resources\\death.png").subsample(3,3)
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




# Now we just need to create the remaining scenes
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
def scene_exit():
    root.destroy()



### So now we have 3 scenes, forest, win and loose
## Now all its missing its to combine everything
"You can see the final result on Examples/SimpleRPG.py"
