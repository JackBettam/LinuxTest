## Setting up WSL2
Follow [instructions](https://learn.microsoft.com/en-us/windows/wsl/install) on how to set up WSL2.0 with an Ubuntu distro. 

## Install Conda
1. 	Open Ubuntu app
2. 	update and upgrade:
    ```
    sudo apt update
    sudo apt upgrade
    ```
3. 	Download Anaconda:
    * Visit: https://www.anaconda.com/products/distribution
    * Find the most recent Anaconda package for Linux and copy URL
    * Run the following in Ubuntu:
        ````
        wget URL-FOR-CONDA-PACKAGE
        ````
4.	Run installer script
    ```
    ls
    bash Anaconda*-*-Linx-x86_64.sh
    ```
5. Accept license and install 

6. Reload shell
    ```
    source ~/.bashrc
    ```

## Installing Autodock Vina
Ideally the [tutorial from Vina will](https://autodock-vina.readthedocs.io/en/latest/installation.html) work, but a fatal error is currently problematic:
    ```
    error in vina setup command: 'python_requires' must be a string containing valid version specifiers; Invalid specifier: '>=3.5.*'
    ```

To resolve this error, the most recent version of Python will need to be uninstalled and reinstalled. Full work-around details are below.

### Workaround for version error
If the [above error](#installing-autodock-vina) occurs, then the following workaround can be performed. This largely follows the Installation guide, but has a couple of extra lines which resolved the issue.

#### Setup environment
This creates a conda environment called vina. 
```
conda create -n vina python=3
conda activate vina
conda config --env --channels conda-forge
```

#### Install pre-requisite packages
This installs all pre-requsite packages.
```
conda install -c conda-forge numpy swig boost-cpp sphinx sphinx_rtd_theme
```

#### Remove Python and install Python 3.9
This removes the current version of Python and installs an earlier version:
```
conda uninstall python
conda install ptyhon=3.9
```

#### Install Vina
Finally, Vina can be installed:
```
pip install vina
```

## Install ADFR
ADFR can be installed using[ ADFR's tutorial](https://ccsb.scripps.edu/adcp/windows10/).