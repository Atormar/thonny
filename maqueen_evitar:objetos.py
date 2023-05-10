from microbit import*
from maqueen import*

ma=Maqueen()
while True:
    c=ma.Read_distance()
    if c<10:
        ma.turn_left()
        ma.forward()
        sleep(500)
        ma.turn_right()
        ma.forward()
        sleep(500)
        ma.turn_right()
        ma.forward()
        sleep(500)
        ma.turn_left()
    else:
        ma.forward()
        