import sys

def dft(dihedrals):
    dftfile = open('outputs/dft.nw','w')
    sys.stdout = dftfile

    print 'title "SMDPPEH with displacement: 04.00 Angstroms"\n'
    print 'memory stack 750 mb heap 1500mb global 1500 mb\n'
    print 'geometry mol1  units angstroms noautoz noautosim'
    counter = 1
    for i in range(len(dihedrals)):
        if dihedrals[i].dft:
            print 'geometry mol%s units angstroms noautoz noautosim' % counter
            print "%s %s %s %s" % (dihedrals[i].dihedral_master1.atom_type,dihedrals[i].dihedral_master1.x_pos,dihedrals[i].dihedral_master1.y_pos,dihedrals[i].dihedral_master1.z_pos)
            print "%s %s %s %s" % (dihedrals[i].dihedral_master2.atom_type,dihedrals[i].dihedral_master2.x_pos,dihedrals[i].dihedral_master2.y_pos,dihedrals[i].dihedral_master2.z_pos)
            print "%s %s %s %s" % (dihedrals[i].dihedral_slave1.atom_type,dihedrals[i].dihedral_slave1.x_pos,dihedrals[i].dihedral_slave1.y_pos,dihedrals[i].dihedral_slave1.z_pos)
            print "%s %s %s %s" % (dihedrals[i].dihedral_slave2.atom_type,dihedrals[i].dihedral_slave2.x_pos,dihedrals[i].dihedral_slave2.y_pos,dihedrals[i].dihedral_slave2.z_pos)
            print "end\n"
            counter += 1

    print "basis"
    print " * library 6-31++G*"
    print "end\n"

    counter = 1
    for i in range(len(dihedrals)):
        if dihedrals[i].dft:
            print "set geometry mol%s" % counter
            print "dft"
            print " xc b31yp"
            print " odft"
            print " vectors input atomic outpus mol%s.mos" % counter
            print "end\n"
            print "task dft ignore\n"
            counter += 1
    dftfile.close()
