class OPLS_Atom(object):
    opls_id = ""
    opls_bondid = ""
    opls_type = ""
    pc = ""
    sigma = ""
    epsilon = ""

    def __init__(self,opls_id,opls_bondid,opls_type,pc,sigma,epsilon):
        self.opls_id = opls_id
        self.opls_bondid = opls_bondid
        self.opls_type = opls_type
        self.pc = pc
        self.sigma = sigma
        self.epsilon = epsilon

def create_atoms(atom,van,partial):
    opls_atoms = []
    for i in range(0,len(atom)):
        a = atom[i]
        v = van[i]
        p = partial[i]
        opls_atoms.append(OPLS_Atom(a[1],a[2],a[3],p[2],v[2],v[3]))
    return opls_atoms
