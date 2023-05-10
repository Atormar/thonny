from microbit import*
from Maqueen import*
class Maqueen:
    def backward(self):
        self.set_motor(0,-255)
        self.set_motor(1,-255)
        
ma=Maqueen()

ma.backward()
sleep(1000)
ma.motor_stop_all()