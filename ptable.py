class Periodic(object):
    atom_id = ""
    atomic_mass = ""

    def __init__(self,atom_id,atomic_mass):
        self.atom_id = atom_id
        self.atomic_mass = atomic_mass

def create_tableobj(plist):
    elements = []
    for i in range(0,len(plist)):
        id = plist[i][0].replace(" ","")
        mass = plist[i][1].replace("\r\n","")
        elements.append(Periodic(id,mass))
    return elements