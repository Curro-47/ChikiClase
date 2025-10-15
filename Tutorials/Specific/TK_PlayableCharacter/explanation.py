## This is a tutorial on how to make a playable character, with movement and collisions

"This is a little more complicated than the simple RPG"
"And thats because we use a few new libraries and topics"
"The list of things we will be using is the following"
######## LIBRARIES ##
# Tkinter     (Main system and app)
# time        (Clean loops)
# keyboard    (Detecting key presses)
# threading   (Using keyboard without crashing the app)
######## NEW TOPICS ##
# Arrays
# Tkinter canvas

"!!IMPORTANT!!"
"Keyboard is an EXTERNAL library (All others are built in so dont worry about them)"
"You NEED to install it"
"to do it open Command Prompt on your computer"
"and paste the following text there"
#########################################
"pip install keyboard" # (Without the "")
#########################################
"This might not work if you are using Spyder Anaconda"
"I really recommend installing visual studio"

## Now, to begin create an empty tkinter file as such
#---------------------#
import tkinter as tk
root = tk.Tk()

root.mainloop()
#---------------------#


## We will configure the window size, and create our canvas object
#---------------------#
import tkinter as tk
root = tk.Tk()
root.geometry("1000x600") # Screen size

## Canvas
area = tk.Canvas(root, width=500, height=500, bg='gray')
area.place(x=500, y=300, anchor="center") # Positioned in the middle of the screen

root.mainloop()
#---------------------#
## This canvas object looks like an empty gray rectangle
# but has the hability to draw objects and move them quickly
# Lets zoom on the canvas creation and add our player


#################################### OBJECT MOVEMENT ################################################################

"#################################################################"
## Canvas
area = tk.Canvas(root, width=500, height=500, bg='gray')
area.place(x=500, y=300, anchor="center") # Positioned in the middle of the screen
## Here we will create our player
player = area.create_rectangle(0, 0, 20, 20, fill='blue') # Creates a blue rectangle of 20x20 pixels
"#################################################################"

## And we are able to move the player with
area.move(player, 1, 2) # Moves player object one pixel to the left and 2 down


##################################### CONTROLS ###########################################################

## To create our controls we need to have a loop that checks our key inputs every couple frames
# this will be an infinite loop, which you know python (and chikis) does not like
# this is why we use threads
# It allows our movement code to execute asynchronously, or in other words at the same time as other code
# To create it we use the threading librarly

#--------------------------------------------------#
import threading

def a():  ## Function which will be threaded
    while True:
        print("a")

threading.Thread(target=a, daemon=True).start() ## Thread begins, executing infinite loop on function a

## Yet it still reaches this code, because it is running at the same time
root.mainloop()
#--------------------------------------------------#

## Lets focus on this line
threading.Thread(target=a, daemon=True).start()

# here, "target" is the function to run, and start() is what actually tells our thread to begin
# Threads automatically close when the function finishes
# But because our function has an infinite loop, it never finishes, and the thread never ends
# daemon=True, tells our thread that the program should not wait for this thread to finish to be able to close
# if daemon were False, the app could not be closed until the thread finished (which would be never)

## So, to adapt this to our system
# We will have our thread and have our control systems inside
# You can detect key presses like:
#-------------------------#
import keyboard

if keyboard.is_pressed("left"): print("hi") # If left arrow is pressed, print hi
#-------------------------#
## Altough this only checks it once, so we need to put it inside a loop, and inside a thread
## We will also check for all 4 directions
## The loop is running a lot of times per frame, which might cause some lag
## So we also add a
time.sleep(0.02)
## This just tells the code to wait for 0.02 seconds every frame
#------------------------------------------------------#
import keyboard
import threading
import time

def Controls():
    while True:
        if keyboard.is_pressed("left"): print("Moving left")
        if keyboard.is_pressed("right"): print("Moving right")
        if keyboard.is_pressed("up"): print("Moving up")
        if keyboard.is_pressed("down"): print("Moving down")

        time.sleep(0.02)

threading.Thread(target=Controls, daemon=True).start()
#------------------------------------------------------#

## Now we just need to add our objects and make the keybinds move the player
# The new keybinds would look like
if keyboard.is_pressed("left"): area.move(player, 1, 0)

## And the full code would be something like
#--------------------------------------------------------#
import keyboard
import threading
import time
import tkinter as tk

root = tk.Tk()
root.geometry("1000x600")

area = tk.Canvas(root, width=500, height=500, bg='gray')
area.place(x=500, y=300, anchor="center")
player = area.create_rectangle(0, 0, 20, 20, fill='blue')
area.move(player, 250, 250)

def Update():
    while True:
        if keyboard.is_pressed("left"): area.move(player, -3, 0)
        if keyboard.is_pressed("right"): area.move(player, 3, 0)
        if keyboard.is_pressed("up"): area.move(player, 0, -3)
        if keyboard.is_pressed("down"): area.move(player, 0, 3)

        time.sleep(0.01)

threading.Thread(target=Update, daemon=True).start()

root.mainloop()
#---------------------------------------------------------#

"You can test this on this same folder on the name of example_movement.py"





################# COLLISIONS ###################################################################################

# To be done in the future (me dio flojera)

