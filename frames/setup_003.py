import customtkinter

class Setup003(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        # create widgets
        self.create_widgets()
    
    def create_widgets(self):
        self.label_tab_3 = customtkinter.CTkLabel(self, text="CTkLabel on Setup_3")
        self.label_tab_3.grid(row=0, column=0, padx=20, pady=20)
