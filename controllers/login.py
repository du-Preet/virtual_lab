class LoginController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.login_button.configure(command=self.login_event)    

    def login_event(self):
        if self.model.check_uname_pwd(self.view.username_entry.get(), self.view.password_entry.get()):
            self.view.switch_to_main_frame()
