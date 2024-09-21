import tkinter as tk
import customtkinter as ctk
from PIL import Image
from time import sleep

# Theming
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# App class
class PopUpWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window config
        self.title("Back Savior")
        self.geometry("680x290")
        
        # GIF setup
        self.file = "shrimp.gif"
        self.info = Image.open(self.file)
        self.frames = self.info.n_frames
        self.photoimage_objects = []
        for i in range(self.frames):
            obj = tk.PhotoImage(file=self.file, format=f"gif -index {i}")
            self.photoimage_objects.append(obj)

        # GIF frame
        self.gif_frame = ctk.CTkFrame(master=self, width=270, height=270)
        self.gif_frame.place(x=400, y=10)
        self.gif_label = ctk.CTkLabel(master=self.gif_frame, image = "", text="", width=270, height=270)
        self.animation()
        self.gif_label.place(x=0, y=0)

        # Text frame
        txt_frame = ctk.CTkFrame(master=self, width=380, height=220)
        txt_frame.place(x=10, y=10)
        txt_label = ctk.CTkLabel(
            master=txt_frame, width=380, height=220, justify="center",
            text="\n30min are over!\n\nStand up!\n\nStraighten your back!\n\nWalk a bit!\n\nAnd sit down in PROPER position!\n\nYou shrimp!"
        )
        txt_label.place(x=0, y=0)

        # Done button
        done_button = ctk.CTkButton(master=self, text="Done", width=380, height=40, command=self.destroy)
        done_button.place(x=10, y=240)

    # GIF animation function
    def animation(self, current_frame=0):
        global loop
        image = self.photoimage_objects[current_frame]
        self.gif_label.configure(image = image)
        current_frame = current_frame + 1
        if current_frame == self.frames:
            current_frame = 0
        loop = self.after(50, lambda: self.animation(current_frame))
    
    
# Main app loop
if __name__ == "__main__":
    while 1:
        app = PopUpWindow()
        app.mainloop()
        sleep(30*60)
    