class Angle(object):
    #Angle_master specifies the master angle. Etc for slaves
    Angle_type = 0
    Angle_equib_len = ""
    Angle_force_const = ""
    Angle_master = ""
    Angle_slave1 = ""
    Angle_slave2 = ""

    #constructor
    def __init__(self, Angle_type, Angle_master, Angle_slave1, Angle_slave2):
        self.Angle_type = Angle_type
        self.Angle_master = Angle_master
        self.Angle_slave1 = Angle_slave1
        self.Angle_slave2 = Angle_slave2