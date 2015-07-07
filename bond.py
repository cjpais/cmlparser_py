class Bond(object):
   bond_type = ""
   bond_equib_len = ""
   bond_force_const = ""
   bond_master = ""
   bond_slave = ""

   #constructor
   def __init__(self, bond_type, bond_master, bond_slave):
      self.bond_type = bond_type
      self.bond_master = bond_master
      self.bond_slave = bond_slave

def create_bonds(bond):
    bonds = []
    for i in range(0,len(bond)):
        currbond = str(bond[i].attrib).split()
        print currbond
        type = currbond[4].replace('}','').replace("'","")
        master = currbond[1].replace('a','').replace(',','').replace("'","")
        slave = currbond[2].replace('a','').replace(',','').replace("'","")
        bonds.append(Bond(type,master,slave))
    return bonds