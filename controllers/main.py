class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.comport_optionemenu.configure(command=self.change_com_port)

        self.config_setup_001()
    
    def config_setup_001(self):
        self.view.setup_001.start_button.configure(command=self.start_button_setup_1)
    
    def start_button_setup_1(self):
        self.model.active_setup_data[0][0] = True
        self.model.active_setup_data[0]['ip_data']['cyclic'] = '****RLDVM01VB01CID1COMP001ALive_data_req####'
        self.model.active_setup_data[0]['callback'] = self.cb_setup_001

        self.model.start_scheduler()
    
    def change_com_port(self, new_port: str):
        self.model.init_comm(new_port)
    
    def cb_setup_001(self):
        op_data = self.model.active_setup_data[0]['op_data']

        comp001a = int(op_data['cyclic'].decode("utf-8").strip('#')[-4:])

        self.view.setup_001.pb_mic_db.set(comp001a/1000)
