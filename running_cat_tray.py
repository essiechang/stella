import tkinter as tk
from pystray import Icon, MenuItem, Menu
import threading
import time

class RunningCatAnimation:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Running Cat')
        self.label = tk.Label(self.root, font=('Courier', 12), fg='black')
        self.label.pack()
        self.running = True
        self.frames = ["/\_/\ ", "/ o o \ ", "\_=__=/ "]  # Animated frames
        self.current_frame = 0  

    def update_frame(self):
        if self.running:
            self.label.config(text=self.frames[self.current_frame])
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.root.after(500, self.update_frame)  # Update every 500 ms

    def run(self):
        self.update_frame()
        self.root.geometry('100x100')
        self.root.mainloop()

    def stop(self):
        self.running = False

def create_tray_icon():
    icon = Icon('running_cat')
    icon.menu = Menu(MenuItem('Quit', stop_animation))
    icon.run(setup_tray_icon)

def setup_tray_icon(icon):
    icon.visible = True

def stop_animation(icon):
    cat_animation.stop()
    icon.stop()

if __name__ == '__main__':
    cat_animation = RunningCatAnimation()
    threading.Thread(target=cat_animation.run).start()  
    create_tray_icon()  
