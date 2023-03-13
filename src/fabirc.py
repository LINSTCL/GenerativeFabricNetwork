

class Neure():
    def __init__(self, in_port_num, out_port_num, 
                 disseminate_fun, internal:bool, prev_neure=None):
        self.in_port_num = in_port_num
        self.out_port_num = out_port_num
        self.disseminate_fun = disseminate_fun


