## Basic Linux terminal
There are some basic terminal commands that may be useful. 
* When specifying a target directory for a file use a fullstop if the directory is nested in the directory that the bash script is running, then the target directory can be specified by ```./target_directory```. 

## Basic docking
The following commands require ADFR, and need to be routed to the bin directory of ADFR. If ADFR10 is in the same directory you're running the bash terminal in, then you can use something like the following to activate the functions:
```
./ADFR10/bin/*your_command*
```
Where ```*your_command*``` is the command you wish to run. 

For the commands below, for simplicity, the command should replace ```*your_command*``` above with the chosen command, and the input files (and output files) should also have the file location (relative directory etc.) specified

### Ensure that protein has explicit hydrogens
There are two ways to add hydrogens to a protein/receptor:
* using the ```prepare_receptor``` command - this uses OpenBabel to add hydrogens. This is automatic, but no longer the recommended way of adding hydrogens. 
* using the ```reduce``` command - this is a custom command from the Richardson lab - and is now included in ADFR. 

Hence, the reduce command should be run:
```
reduce Input_protein.pdb > Output_protein_H.pdb
```

This 