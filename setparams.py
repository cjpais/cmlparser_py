import sys

def set_help():
    units = raw_input("Enter Lammps units: ")
    atom_style = raw_input("Enter Lammps atom_style: ")
    boundary = raw_input("Enter Lammps boundary: ")
    bond_style = raw_input("Enter Lammps atom_style: ")
    dielectic = raw_input("Enter Lammps dielectic: ")
    pair_style = raw_input("Enter Lammps pair_style: ")
    angle_style = raw_input("Enter Lammps angle_style: ")
    dihedral_style = raw_input("Enter Lammps dihedral_style: ")
    special_bonds = raw_input("Enter Lammps special_bonds: ")
    improper_style = raw_input("Enter Lammps improper_style: ")
    kspace_style = raw_input("Enter Lammps kspace_style: ")
    thermo_style = raw_input("Enter Lammps thermo_style")
    neighbor = raw_input("Enter Lammps neighbor: ")
    neigh_modify = raw_input("Enter Lammps neigh_modify: ")
    fix1 = raw_input("Enter fix 1: ")
    fix2 = raw_input("Enter fix 2: ")
    velocity = raw_input("Enter velocity: ")
    timestep = raw_input("Enter timestep: ")
    thermo = raw_input("Enter thermo: ")
    run = raw_input("Enter run time: ")
    replicate = raw_input("Enter how many times to replicate: ")
    fix3 = raw_input("Enter fix1 after replication: ")
    fix4 = raw_input("Enter fix2 after replication: ")
    velocity2 = raw_input("Enter velocity post replication: ")
    run2 = raw_input("Enter run time after replication: ")

    #ADD IN HELP FOR HELP
    print units
    print atom_style
    print boundary
    print bond_style
    print dielectic
    print pair_style
    print angle_style
    print dihedral_style
    print special_bonds
    print improper_style
    print kspace_style
    print thermo_style
    print neighbor
    print neigh_modify
    print fix1
    print fix2
    print velocity
    print timestep
    print thermo
    print run
    print replicate
    print fix3
    print fix4
    print velocity2
    print run2

    correct = raw_input("Are The Values above correct? (y/n)")
    if correct == "n":
        set()
    else:
        return units,atom_style,boundary,bond_style,dielectic,atom_style
