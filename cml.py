import sys
import xml.etree.ElementTree as ET
import atom
import bond

if len(sys.argv) == 1:
    print "You need to specifiy a file to read!"
    quit()

cmlfile = sys.argv[1]

tree = ET.parse(cmlfile)
root = tree.getroot()

atomTree = root.findall('./atomArray/atom')
bondTree = root.findall('./bondArray/bond')

atoms = atom.create_atoms(atomTree)
bonds = bond.create_bonds(bondTree)