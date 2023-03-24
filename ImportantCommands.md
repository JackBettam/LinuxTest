## Basic Linux terminal

There are some basic terminal commands that may be useful. 
* A single dot can be used to go down a level from where the terminal exists. This allows a file to run from a nested directory. For example: ```./some_directory```. 
* A double dot can be used to go up a level from where the terminal exists. This allows a file to run from a different directory.For example: ```../some_directory```
* To go to the users directory a tilde can be used. From here, other directories can be accessed: ```~/some_directory```.

## Basic docking

This is a more in-depth version of the basic docking tutorial provided by AutoDock Vina.[^1]

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
* using the ```reduce``` command - this is a custom command from the Richardson lab[^2] - and is now included in ADFR. 

Hence, the reduce command should be run to add explicit hyrdogens:

```
reduce Input_protein.pdb > Output_protein_H.pdb
```

The next step is to create a PDBQT file. This is a file that contains[^3]:
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
> 
>PDB files should __not__ be used for small molecules - these filetypes do not contain bond connections. 

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

The final step is to create an autogrid map files (which are affinity maps) that will be used for molecular docking. This is performed by:

```
autogrid4 -p output_protein.gpf -l output_protein.glg 
```
This produces 4 types of files (but may be more files...):
* `output_protein_receptor.maps.fld` : grid data file
* `output_protein_receptor.*.map` : affinity maps for each atom type (there will be a different map for each atom type, and thus there may be multiple of these maps)
* `output_protein_receptor.d.map` : desolvation map
* `output_protein_receptor.e.map` : electrostatic map

### Running Autodock Vina

There are two methods of running - either using the AutoDock4 forcefield (requires affinity maps, above) or Vina forcefield (which does not require any affinity maps). For this tutorial, Autodock will be used.

In both of these, there is an exhaustiveness variablee, which has a default value of `8` - increasing the value to `32` leads to more consistent docking results.

Autodock uses various variables:
* `--ligand` is the ligand that is being docked (.pdbqt file)
* `--maps` is the name of the grid data file (.maps.fld without the extensions - just the file name)
* `--scoring` is the scoring method - this `ad4` uses AutoDock4 forcefield. `vinardo` will use the Vinardo scoring function. 
* `--exhaustiveness` is the amount of computational effort put in - discussed above
* `--out` is the output file. 

This leads to the following command:
```
vina --ligand output_ligand.pdbqt --maps output_protein_receptor --scoring ad4 --exhaustiveness 32 --out docking_out.pdbqt
```

### Reading the Output of the 

The output from this is placed in the respective output file. The table in the command line lists the poses that have been generated, and their affinity (in kcal/mol). A reminder: the lower the binding energy the better fit a ligand is. 

In the output file is all of the poses that were calculated. This is a pdbqt file. As the Linux WSL has no GUI, this should be copied across to Windows. This then can be opened on [AutoDockTools](https://ccsb.scripps.edu/mgltools/downloads/) running on Windows. This is the same for any pdbqt files - they need to be copied from the WSL to the Windows partition. 

> Whilst it is possible to open files in the WSL, it appears to be slow and can cause crashes of software.

Basic analysis can be shown below [^4]

1. After opening AutoDockTools, select Analyze --> Dockings --> Open AutoDock vina result and select the output pdbqt results file - `docking_out.pdbqt`
2. The different poses can be opened using arrow keys. The number presented is the binding energy. 
3. The protein can be added in using the Analyze --> Macromolecule --> New and select `output_protein.pdbqt`.
4. There are a few rendering tools that can be used:
* Selecting the 's' button of the ligand or protein will highlight the selected ligand or protein.
* Selecting the 'l' button of the ligand or protein will show the respective skeletal structure drawing.
* Selecting the 'b' button of the ligand or protein will show the respective ball and stick structure.
* Selecting the 'c' button will show the respective atomic sphere structure. 
* Selecting the 'r' button of the protein will show the ribbon form of the protein. 
* selecting the  'm' button will show the molecular surface for the selection
5. Interactions can be shown for a relevant docking by selecting Analyze -> Dockings -> Show Interactions.

## References
[^1]: Basic docking - Autodock Vina 1.2.0 documentation, [https://autodock-vina.readthedocs.io/en/latest/docking_basic.html](https://autodock-vina.readthedocs.io/en/latest/docking_basic.html), (Accessed March 2023)
[^2]: Richardson Laboratory: Reduce, [http://kinemage.biochem.duke.edu/software/reduce/](http://kinemage.biochem.duke.edu/software/reduce/), (Accessed March 2023)
[^3]: Morris, G. M., et. al., _AutoDock 4.2 User Guide_, Scripps Research, San Diego (USA), 2014 
[^4] Autodock Vina Result Analysis, [https://www.youtube.com/watch?v=EkXY1uaMscg&ab_channel=QuickLearn360](https://www.youtube.com/watch?v=EkXY1uaMscg&ab_channel=QuickLearn360), (Accessed March 2023)