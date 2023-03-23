## Basic Linux terminal

There are some basic terminal commands that may be useful. 
* A single dot can be used to go down a level from where the terminal exists. This allows a file to run from a nested directory. For example: ```./some_directory```. 
* A double dot can be used to go up a level from where the terminal exists. This allows a file to run from a different directory.For example: ```../some_directory```
* To go to the users directory a tilde can be used. From here, other directories can be accessed: ```~/some_directory```.

## Basic docking

The following commands require ADFR, and need to be routed to the bin directory of ADFR. If ADFR10 is in the same directory you're running the bash terminal in, then you can use something like the following to activate the functions:
```
./ADFR10/bin/*your_command*
```
Where ```*your_command*``` is the command you wish to run. 

For the commands below, for simplicity, the command should replace ```*your_command*``` above with the chosen command, and the input files (and output files) should also have the file location (relative directory etc.) specified

### Preparing receptor

First Excplicit hydrogens need to be added.

There are two ways to add hydrogens to a protein/receptor:
* using the ```prepare_receptor``` command - this uses OpenBabel to add hydrogens. This is automatic, but no longer the recommended way of adding hydrogens. 
* using the ```reduce``` command - this is a custom command from the Richardson lab[^1] - and is now included in ADFR. 

Hence, the reduce command should be run to add explicit hyrdogens:

```
reduce Input_protein.pdb > Output_protein_H.pdb
```

The next step is to create a PDBQT file. This is a file that contains[^2]:
* Polar hydrogen atoms
* Partial charges
* Atom charges
* Information on the articulation of flexible molecules. 

This can be done using the `prepare_receptor` command. By adding the variable `-h` it is possible to see all possible variable that can be added. In this case, there will be two variables added - the receptor PDB (with explict hydrogens embedded from earlier) and the output name. These are added with the flags `-r` and `-o` respectively. 

Hence, the code will take receptor `Output_protein_H.pdb` and produce a file called `Output_protein.pdbqt`:

```
prepare_receptor -r Output_protein_H.pdb -o Output_protein.pdbqt
```

### Prpeare the Ligand
The next step is to prepare the ligand. This also creates a PDBQT file. This uses Meeko. This inputs standard 3D formats (mol, mol2, sdf etc.). This uses the script `mk_prepare_ligand.py`. The ligand files may not contain hydorgens, and so these will be automatically added. 

> #### Warning
> PDB files should __not__ be used for small molecules - these filetypes do not contain bond connections. 

Full flag types can be found by passing `--help` when calling the script. In this case, we're calling the `-i` and `-o` variables to represent the input and output of the ligands. 

```
mk_prepare_ligand.py -i input_ligand.sdf -o output_ligand.pdbqt
```

### Generating Affinity Maps
This step is optional, but for completeness of the guide, this will be included. This uses the MGLtools programs. 

First a gpf file is generated for AutoGrid4. This requires that MGLtools is installed (if an error such as `pythonsh: command not found` then it is likely MGLtools is not installed correctly). 

The script can be [downloaded](https://github.com/ccsb-scripps/AutoDock-Vina/tree/develop/example/autodock_scripts) - as the one that is included in MGLtools has been adapted by the authors of Vina. This can be installed in any location and called as below. 

In the terminal, this can be run as:

```
pythonsh <script_directory>/prepare_gpf.py -l output_ligand.pdbqt -r output_protein.pdbqt -y
```

The flags `-l`, `-r` and `-y` specify the ligand, receptor and centre the grid automatically around the ligand. 

This creates a single file called `output_protein.gpf`

The final step is to create an autogrid map files that will be used for molecular docking. This is performed by:

```
autogrid4 -p output_protein.gpf -l 1iep.glg 
```
This produces 4 types of files (but may be more files...):
* `1iep_receptor.maps.fld` : grid data file
* `1iep_receptor.*.map` : affinity maps for each atom type (there will be a different map for each atom type, and thus there may be multiple of these maps)
* `1iep_receptor.d.map` : desolvation map
* `1iep_receptor.e.map` : electrostatic map



## References
[^1]: Richardson Laboratory: Reduce, [http://kinemage.biochem.duke.edu/software/reduce/](http://kinemage.biochem.duke.edu/software/reduce/), (March 2023)
[^2]: Morris, G. M., et. al., _AutoDock 4.2 User Guide_, Scripps Research, San Diego (USA), 2014 