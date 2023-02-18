import csv
import os

from comm.comm_serial import CommSerial

class Model:
    def __init__(self):

        self.active_setup_data = [
            {0:False, 'ip_data':{'cyclic': None, 'acyclic': None}, 'op_data':{'cyclic': None, 'acyclic': None}, 'callback': None},
            {1:False, 'ip_data':{'cyclic': None, 'acyclic': None}, 'op_data':{'cyclic': None, 'acyclic': None}, 'callback': None},
            {2:False, 'ip_data':{'cyclic': None, 'acyclic': None}, 'op_data':{'cyclic': None, 'acyclic': None}, 'callback': None},
        ]

        self.comm_ser = CommSerial()

        self.run_scheduler = False

        # self.init_comm('COM8')

    def init_comm(self, port):
        self.comm_ser.init_comm_port(port)
        # self.start_scheduler()

    def check_uname_pwd(self, uname, pwd):
        login = False

        current_path = os.path.dirname(os.path.realpath(__file__))

        with open(current_path + '/db/upassword.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if uname in row:
                    if pwd == row[1]:
                        login = True
                        break
    
        return login
    
    def start_scheduler(self):
        self.run_scheduler = True
    
    def stop_scheduler(self):
        self.run_scheduler = False
    
    def scheduler(self):
        if self.run_scheduler:
            # print('Scheduler running...')
            for setup in range(len(self.active_setup_data)):
                if self.active_setup_data[setup][setup]:
                    self.process_setup_data(setup)
                else:
                    pass
        
            # print('\n\n\n', self.active_setup_data)
    
    def process_setup_data(self, setup):
        ip_data_cyclic = self.active_setup_data[setup]['ip_data']['cyclic']
        ip_data_acyclic = self.active_setup_data[setup]['ip_data']['acyclic']

        callback = self.active_setup_data[setup]['callback']

        op_data = {'cyclic': None, 'acyclic': None}

        if ip_data_cyclic != None:
            op_data['cyclic'] = self.comm_ser.write_and_read(ip_data_cyclic)
        
        if ip_data_acyclic != None:
            op_data['acyclic'] = self.comm_ser.write_and_read(ip_data_acyclic)
        
        self.active_setup_data[setup]['op_data'] = op_data

        if callback != None:
            callback()
