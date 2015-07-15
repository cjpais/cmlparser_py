# cmlparser_py
Parses avogadro created .cml files

Uses a command line argument specifying the location of the file to parse.
It doesn't check the filename for the extention cml, so be sure it is a cml
file otherwise there may be issues.

There are a few command line flags to be aware of (show in parens):

python cml.py (cml-filename) (output-filename) (d)
* cml-filename - The name and location of the cml file you would like to parse
* output-filename - The file name and location for a lammps output
* d - Used for debugging output, lines in cml.py will help print out debugging info
