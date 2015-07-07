class Ring(object):
    ring_type = 0
    improper = False
    fused = False
    atom1 = ""
    atom2 = ""
    atom3 = ""
    atom4 = ""
    atom5 = ""
    atom6 = ""

    def __init__(self,a1,a2,a3,a4,a5,a6=None):
        self.atom1 = a1
        self.atom2 = a2
        self.atom3 = a3
        self.atom4 = a4
        self.atom5 = a5
        self.atom6 = a6

        a1.ring = True
        a2.ring = True
        a3.ring = True
        a4.ring = True
        a5.ring = True

        self.ring_type = 5
        if a6 != None:
            self.ring_type = 6
            a6.ring = True

    def list(self):
        rList = []
        rList.append(self.atom1)
        rList.append(self.atom2)
        rList.append(self.atom3)
        rList.append(self.atom4)
        rList.append(self.atom5)
        if self.atom6 != None:
            rList.append(self.atom6)
        return rList

def create_rings(d):
    rings = []
    for i in range(0,len(d)):
        for j in range(0,len(d)):
            if d[i] == d[j]:
                continue
            if d[i].dihedral_master1.ring:
                continue
            dList = [d[j].dihedral_master1,d[j].dihedral_master2,d[j].dihedral_slave1,d[j].dihedral_slave2]
            outList = [d[i].dihedral_master1,d[i].dihedral_master2,d[i].dihedral_slave1,d[i].dihedral_slave2]
            if outList[0] not in dList and outList[1] not in dList:
                if outList[2] in dList and outList[3] in dList:
                    rings.append(Ring(outList[0],outList[1],outList[2],outList[3],dList[0],dList[1]))
            elif outList[0] in dList and outList[2] in dList and outList[3] in dList:
                if outList[1] not in dList:
                    rings.append(Ring(outList[0],outList[1],outList[2],outList[3],dList[3]))
            elif outList[1] in dList and outList[2] in dList and outList[3] in dList:
                if outList[0] not in dList:
                    rings.append(Ring(outList[0],outList[1],outList[2],outList[3],dList[2]))
    return rings