import sys
sys.dont_write_bytecode = True

import customtkinter

from view import View
from model import Model

customtkinter.set_appearance_mode("System")    # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("VIRTUAL LAB")
        # self.state('zoomed')

        # create a model
        model = Model()

        # create a view and place it on the root window
        view = View(self, model)

        view.grid(row=0, column=0)

if __name__ == '__main__':
    app = App()
    app.mainloop()
