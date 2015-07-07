class OPLS_Bond(object):
    opls_master = ""
    opls_slave = ""
    fc = ""
    el = ""

    def __init__(self,opls_master,opls_slave,fc,el):
        self.opls_master = opls_master
        self.opls_slave = opls_slave
        self.fc = fc
        self.el = el

def create_bonds(bond):
    opls_bonds = []
    for i in range(0,len(bond)):
        bList = bond[i]
        opls_bonds.append(OPLS_Bond(bList[1],bList[2],bList[3],bList[4]))
    return opls_bonds
