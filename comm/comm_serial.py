import serial

class CommSerial:
    def __init__(self) -> None:
        self.comm_ser = None
    
    def init_comm_port(self, port):
        self.comm_ser = serial.Serial(port=port, baudrate=115200, timeout=1)
    
    def close_comm_port(self):
        if self.comm_ser != None:
            self.comm_ser.close()
    
    def write_and_read(self, data):
        response = b''
        for _ in range(5):
            response = self._write_and_read(data)
            if response == b'':
                print('---')
            else:
                break
        
        print('\n\nVB -> VM : ', response)
        return response

    def _write_and_read(self, data):
        resp = b''
        self.comm_ser.reset_input_buffer()
        self.comm_ser.reset_output_buffer()
        self.comm_ser.write(data.encode())
        # self.comm_ser.reset_input_buffer()
        # self.comm_ser.reset_output_buffer()
        self.comm_ser.flush()
        print('\n\nVM -> VB : ', data)
        resp = self.comm_ser.readline()
        return resp.rstrip()
