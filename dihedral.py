class Dihedral(object):
    dihedral_eqib_len = ""
    dihedral_force_const = ""
    dihedral_master1 = ""
    dihedral_master2 = ""
    dihedral_slave1 = ""
    dihedral_slave2 = ""

    def __init__(self, dihedral_master1, dihedral_master2, dihedral_slave1, dihedral_slave2):
        self.dihedral_master1 = dihedral_master1
        self.dihedral_master2 = dihedral_master2
        self.dihedral_slave1 = dihedral_slave1
        self.dihedral_slave2 = dihedral_slave2

def get_unique(dihedrals):
    dihedrals_new = []
    for i in range(0,len(dihedrals)):
        for j in range(0,len(dihedrals)):
            if dihedrals[i] == dihedrals[j]:
                continue
            if dihedrals[i].dihedral_master1 == dihedrals[j].dihedral_master2 and dihedrals[i].dihedral_master2 == dihedrals[j].dihedral_master1:
                if dihedrals[i].dihedral_slave1 == dihedrals[j].dihedral_slave2 and dihedrals[i].dihedral_slave2 == dihedrals[j].dihedral_slave1:
                    dihedrals_new.append(dihedrals[j])
    dihedrals_new = remove_duplicates(dihedrals_new)
    for i in range(0,len(dihedrals_new)):
        dihedrals.remove(dihedrals_new[i])
    return dihedrals

def remove_duplicates(l):
    """ Given any list remove the duplicates from it

        Keyword Arguments:
        l - Any list that you want to remove duplicates from
    """
    return list(set(l))

def create_dihedrals(dihedral):
    dihedrals = []
    for i in range(0,len(dihedral)):
        outlist = [dihedral[i].Angle_master,dihedral[i].Angle_slave1,dihedral[i].Angle_slave2]
        for j in range(0,len(dihedral)):
            if dihedral[i] == dihedral[j]:
                continue
            inF = [dihedral[j].Angle_master,dihedral[j].Angle_slave1]
            inS = [dihedral[j].Angle_slave1,dihedral[j].Angle_slave2]
            inFL = [dihedral[j].Angle_master,dihedral[j].Angle_slave2]
            if outlist[0] in inF and outlist[1] in inF:
                dihedrals.append(Dihedral(outlist[0],outlist[1],outlist[2],inS[1]))
            elif outlist[0] in inS and outlist[1] in inS:
                dihedrals.append(Dihedral(outlist[0],outlist[1],outlist[2],inF[0]))
            elif outlist[0] in inFL and outlist[1] in inFL:
                dihedrals.append(Dihedral(outlist[0],outlist[1],outlist[2],inS[0]))
    dihedrals = get_unique(dihedrals)
    return dihedrals
