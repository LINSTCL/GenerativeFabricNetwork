


class Neure():
    def __init__(self, in_port, out_port, 
                 disseminate_fun, value):
        self.in_port = in_port
        self.out_port = out_port
        self.disseminate_fun = disseminate_fun
        self.value = value

    def run(self):
        self.value = self.disseminate_fun(self.in_port.value)
        return self.out_port

