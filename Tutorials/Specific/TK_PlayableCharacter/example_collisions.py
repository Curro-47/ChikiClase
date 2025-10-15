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

player_speed = 3

def Update():
    while True:
        pos = area.coords(player)
        movement = [0, 0]

        if keyboard.is_pressed("left"): movement[0] = -player_speed
        if keyboard.is_pressed("right"): movement[0] = player_speed
        if keyboard.is_pressed("up"): movement[1] = -player_speed
        if keyboard.is_pressed("down"): movement[1] = player_speed

        new_pos = [pos[0] + movement[0], pos[1] + movement[1]]
        check_collision = new_pos[0] > 0 and new_pos[1] > 0 and new_pos[0] <= 480 and new_pos[1] <= 480
        
        if check_collision: area.move(player, movement[0], movement[1])

        time.sleep(0.01)

threading.Thread(target=Update, daemon=True).start()

root.mainloop()