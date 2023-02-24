from serial import Serial
Arduino = None
def Connect(Port):
    global Arduino
    Arduino = Serial(Port)
def R(mode):
    M = "rl"
    if mode:
        M = "rh"
    Arduino.write(M.encode())
def G(mode):
    M = "gl"
    if mode:
        M = "gh"
    Arduino.write(M.encode())
def B(mode):
    M = "bl"
    if mode:
        M = "bh"
    Arduino.write(M.encode())