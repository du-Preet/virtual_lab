import customtkinter

class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        # create widgets
        self.create_widgets()
    
    def create_widgets(self):
        self.login_label = customtkinter.CTkLabel(self, text="VirtualLab\nLogin Page",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))

        self.username_entry = customtkinter.CTkEntry(
            self, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))

        self.password_entry = customtkinter.CTkEntry(
            self, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        
        self.login_button = customtkinter.CTkButton(
            self, text="Login", width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
    
    def switch_to_main_frame(self):
        self.parent.switch_to_main_frame()
