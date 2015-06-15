"""
Created on Thurs May 21 22:23:22 2015

@author: Christopher Pais
"""

import sys
import xml.etree.ElementTree as ET
import helper as help
import time

#get filename from commandline
file = sys.argv[1]

#begin parsing, gets single atom.
tree = ET.parse(file)
root = tree.getroot()
atomList = root.findall('./atomArray/atom')
bondList = root.findall('./bondArray/bond')