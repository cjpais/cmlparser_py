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

An example of use would be:

python cml.py inputs/smdppeh.cml outputs/data.first d

This would effectively run the program, using the smdppeh molecule as its input.
The flag outputs/data.first is the data file to output and for lammps to read.
The final 'd' at the end is to get some debugging output.
