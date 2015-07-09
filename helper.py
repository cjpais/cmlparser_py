def get_atoms(atomList, i):
   """ Returns a single atom with its attributes split into a object list

   Keyword Arguments:
   atomList -- The list of atoms you want to parse
   i -- The index of the atom to return
   """

   singleAtom = str(atomList[i].attrib)
   singleAtomSplit = singleAtom.split()
   return singleAtomSplit

def object_list(atoms):
   """ Returns a list ready to be input into an Atom object constructor

   Keyword Arguments:
   atoms -- A sinlge atom that you want to proccess into a list for input into
            the Atom constructor
   """

   x_val = atoms[1].replace(",","").replace("'","")
   y_val = atoms[3].replace(",","").replace("'","")
   elem = atoms[5].replace(",","").replace("'","")
   atom_id = atoms[7].replace(",","").replace("'","")
   z_val = atoms[9].replace("}","").replace("'","")
   aList = [atom_id,elem,x_val,y_val,z_val]
   return aList

def bond_list(bonds):
   """ Returns a list of a seperated bond attribute from the cml

   Keyword Arguments:
   bonds -- The bond you want to split for input into the Bond object
   """

   bond_type = bonds[4].replace("}","").replace("'","")
   bond_master = bonds[1].replace(",","").replace("'","")
   bond_slave = bonds[2].replace(",","").replace("'","")
   bList = [bond_type,bond_master,bond_slave]
   return bList

def get_bonds(bondList, i):
   """ Reads in a single bond and splits it for proccessing

   Keyword Arguments:
   bondList -- The list of bonds you want to parse and split
   i -- the index of the bond you want to split
   """

   singleBond = str(bondList[i].attrib)
   singleBondSplit = singleBond.split()

def get_num_bonds(atom, bondList):
   """
   Gets the number of bonds for a specified atom and gets the list of other
   atoms it is bonded to

   Keyword Arguments:
   atom -- The atom you want to get the number of bonds for
   bondList -- the list of bonds to check against
   """
   
   numBonds = 0
   bondedTo = []
   for i in range(0,len(bondList)):
      if atom.atom_id == bondList[i].bond_master or atom.atom_id == bondList[i].bond_slave:
         if atom.atom_id == bondList[i].bond_master:
            numBonds += 1
            bondedTo.append(bondList[i].bond_slave)
         if atom.atom_id == bondList[i].bond_slave:
            numBonds += 1
            bondedTo.append(bondList[i].bond_master)
   atom.Num_Bonds = numBonds #set atoms number of bonds
   atom.Bonds = bondedTo     #set the atoms it is bonded to

def get_min_max(list):
   min = list[0]
   max = list[1]
   for i in range(0,len(list)):
      if list[i] < min:
         min = list[i]
      elif list[i] > max:
         max = list[i]
   return min,max