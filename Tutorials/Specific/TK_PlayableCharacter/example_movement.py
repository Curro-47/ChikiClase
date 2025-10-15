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