from pynq import DefaultIP
import numpy as np
import time
class Timer:
    def __enter__(self):
        self.start = time.process_time()
        return self

    def __exit__(self, *args):
        self.end = time.process_time()
        self.interval = self.end - self.start
        
class AxiLiteDriverMuons(DefaultIP):
    ''' Driver inheriting from DefaultIP with predict function for a Neural Network ip with AxiLite interface. '''
    
    def __init__(self, description):
        super().__init__(description=description)
        self.addr_list_inp = [0x10,0x14,0x18,0x1c,0x20,0x24,0x28,0x2c,0x30,0x34,0x38,0x3c,0x40,0x44]
        self.addr_list_out = 0x4c

    bindto = ['xilinx.com:hls:myproject:1.0']
    
    
    def predict(self, inp_vec):

        inputfactor = 2**10
        outputfactor = 2**15
        with Timer() as t:
            j = 0
            for addr in self.addr_list_inp:
                try:
                    self.write(addr,round(inp_vec[j+1]*inputfactor)*2**16 + round(inp_vec[j]*inputfactor))
                except:
                    self.write(addr,round(inp_vec[j]*inputfactor))
                j+=2
            
        res = self.read(0x4c)/outputfactor
        
        print("Time spent (write + inference + read", t.interval)
        return res
