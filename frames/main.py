import customtkinter

from .setup_001 import Setup001
from .setup_002 import Setup002
from .setup_003 import Setup003

class MainFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        # create widgets
        self.create_widgets()
    
    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=9)
        self.grid_rowconfigure(0, weight=1)

        #--------------------------------------------------------------------#

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar_frame.grid_rowconfigure(8, weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        #--------------------------------------------------------------------#
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Virtual Lab", bg_color='grey', font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=10, pady=(10,500), sticky="nsew")
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=4, column=0, padx=10, pady=(300,10))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=5, column=0, padx=10, pady=10)

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Select COM Port:", anchor="w")
        self.scaling_label.grid(row=6, column=0, padx=10, pady=10)

        self.comport_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["---", "COM0", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9"])
        self.comport_optionemenu.grid(row=7, column=0, padx=10, pady=10)

        #--------------------------------------------------------------------#

        self.content_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.content_frame.grid_rowconfigure(0, weight=9)
        self.content_frame.grid_rowconfigure(1, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        #--------------------------------------------------------------------#

        # create tabview
        self.tabview = customtkinter.CTkTabview(self.content_frame)
        self.tabview.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.tabview.add("Setup_1")
        self.tabview.add("Setup_2")
        self.tabview.add("Setup_3")
        
        self.tabview.tab("Setup_1").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Setup_1").grid_columnconfigure(0, weight=1)

        self.tabview.tab("Setup_2").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Setup_2").grid_columnconfigure(0, weight=1)

        self.tabview.tab("Setup_3").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Setup_3").grid_columnconfigure(0, weight=1)

        self.setup_001 = Setup001(self.tabview.tab("Setup_1"))
        self.setup_001.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.setup_002 = Setup002(self.tabview.tab("Setup_2"))
        self.setup_002.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.setup_003 = Setup003(self.tabview.tab("Setup_3"))
        self.setup_003.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.logout_button = customtkinter.CTkButton(self.content_frame, text="Logout", command=self.switch_to_login_frame)
        self.logout_button.grid(row=1, column=0, ipadx=20, ipady=20, padx=5, pady=5)

        #--------------------------------------------------------------------#

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.comport_optionemenu.set("---")

        #--------------------------------------------------------------------#

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
    def switch_to_login_frame(self):
        self.parent.switch_to_login_frame()
