import customtkinter

class Setup001(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        # create widgets
        self.create_widgets()
    
    def create_widgets(self):

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=9)
        self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=9)

        #--------------------------------------------------------------------#

        self.lbl_headline = customtkinter.CTkLabel(self, text="MIC and BUZZER", bg_color='grey', font=customtkinter.CTkFont(size=20, weight="bold"))
        self.lbl_headline.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        #--------------------------------------------------------------------#

        # self.selector_frame = customtkinter.CTkFrame(self, corner_radius=0)
        # self.selector_frame.grid_rowconfigure(0, weight=1)
        # self.selector_frame.grid_rowconfigure(1, weight=1)
        # self.selector_frame.grid_columnconfigure(0, weight=1)
        # self.selector_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        #--------------------------------------------------------------------#

        self.content_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.content_frame.grid_rowconfigure(0, weight=5)
        self.content_frame.grid_rowconfigure(1, weight=5)
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        #--------------------------------------------------------------------#

        # self.cb_comp_001 = customtkinter.CTkCheckBox(self.selector_frame, text='MIC')
        # self.cb_comp_001.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # self.cb_comp_002 = customtkinter.CTkCheckBox(self.selector_frame, text='BUZZER')
        # self.cb_comp_002.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        #--------------------------------------------------------------------#

        self.mic_frame = customtkinter.CTkFrame(self.content_frame, corner_radius=0)
        self.mic_frame.grid_rowconfigure(0, weight=1)
        self.mic_frame.grid_rowconfigure(1, weight=1)
        self.mic_frame.grid_columnconfigure(0, weight=1)
        self.mic_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        #--------------------------------------------------------------------#

        self.buz_frame = customtkinter.CTkFrame(self.content_frame, corner_radius=0)
        self.buz_frame.grid_rowconfigure(0, weight=1)
        self.buz_frame.grid_rowconfigure(1, weight=1)
        self.buz_frame.grid_rowconfigure(2, weight=1)
        self.buz_frame.grid_columnconfigure(0, weight=1)
        self.buz_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        #--------------------------------------------------------------------#

        self.lbl_mic = customtkinter.CTkLabel(self.mic_frame, text='MIC (dB)', bg_color='grey', font=customtkinter.CTkFont(size=20, weight="bold"))
        self.lbl_mic.grid(row=0, column=0, ipadx=5, ipady=5, padx=20, pady=10, sticky="ew")

        self.pb_mic_db = customtkinter.CTkProgressBar(self.mic_frame)
        self.pb_mic_db.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # self.pb_mic_db.set(0.02)

        #--------------------------------------------------------------------#

        self.lbl_buz = customtkinter.CTkLabel(self.buz_frame, text='BUZZER (PWM)', bg_color='grey', font=customtkinter.CTkFont(size=20, weight="bold"))
        self.lbl_buz.grid(row=0, column=0, ipadx=5, ipady=5, padx=20, pady=10, sticky="ew")

        self.slider_buzzer = customtkinter.CTkSlider(self.buz_frame, from_=1, to=100, number_of_steps=2)
        self.slider_buzzer.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.start_button = customtkinter.CTkButton(self.buz_frame, text="Start Fetching Data")
        self.start_button.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.slider_buzzer.set(1)
