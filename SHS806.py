import pyvisa

class SiglentSHS806():
    def __init__(self):
        rm = pyvisa.ResourceManager()
        scope = rm.open_resource('USB0::0xF4EC::0xEE3A::SHS08DAX4R0062::INSTR')
        print(scope.query("*IDN?"))

if __name__ == '__main__':
    scope = SiglentSHS806()
