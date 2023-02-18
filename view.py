import customtkinter
from PIL import Image
import os

from frames.login import LoginFrame
from frames.main import MainFrame

from controllers.login import LoginController
from controllers.main import MainController

class View(customtkinter.CTkFrame):

    SCH_TIME = 500

    def __init__(self, parent, model):
        super().__init__(parent)

        self.model = model

        # create widgets
        self.create_widgets()

    def create_widgets(self):
        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/assets/circuit.jpg"),
                                               size=(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        self.login_frame = LoginFrame(self)
        self.main_frame = MainFrame(self)

        self.login_controller = LoginController(self.model, self.login_frame)
        self.main_controller = MainController(self.model, self.main_frame)

        self.login_frame.grid(row=0, column=0, sticky="ns")
    
    def switch_to_login_frame(self):
        self.main_frame.grid_forget()                        # remove main frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame

        self.model.stop_scheduler()
    
    def switch_to_main_frame(self):
        self.login_frame.grid_forget()                        # remove login frame
        self.main_frame.grid(row=0, column=0, sticky="nsew")  # show main frame

        # self.model.start_scheduler()

        self.main_frame.after(View.SCH_TIME, self.call_scheduler)
    
    def call_scheduler(self):
        self.model.scheduler()
        self.main_frame.after(View.SCH_TIME, self.call_scheduler)
