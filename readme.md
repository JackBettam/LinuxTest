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

To resolve this error, the most recent version of Python will need to be uninstalled and reinstalled. For the tested versions, Python 3.9.7 appears to be working. This also ensures compatability with other packages.

First, an environment called vina is created, activated and configured with conda-forge (to access packages).

```
conda create -n vina
conda activate vina
conda install python=3.9.7
conda config --env --add channels conda-forge
```

A sanity check can be done now - check the version of Python installed (sometimes conda can install the most recent version of Python...). If this is the case, uninstall Python and reinstall it at this point - uninstalling after this point will remove other packages!!

```
conda python -V
# if Python is incorrect version
conda uninstall python
conda install python=3.9.7
```

The package and prerequisite packages can now be installed:
```
conda install -c conda-forge numpy swig boost-cpp sphinx sphinx_rtd_theme
pip install vina
```

## Install OpenBabel (rdkit, scipy & numpy)
OpenBabel requires rdkit, scipy and numpy to function. The following is set up for a conda install. __Ensure that the vina environment is active!!__

```
conda install -c conda-forge numpy openbabel scipy rdkit
pip install meeko
```

## Install ADFR
ADFR can be installed using[ ADFR's tutorial](https://ccsb.scripps.edu/adcp/windows10/). This seems to work quite well and relaibly. This is done for the system, and not for the environment. 

Basic documentation of ADFR can be found [here](https://ccsb.scripps.edu/adfr/tutorial-redocking/). 

## Install MGLtools
MGLTools may also be required. Documentation seems to be lacking for this installation in virtualised environments as it's designed for running on full GUI versions. But the below seems to work fairly well.

First the download files are installed in the home directory of the user, followed by unzipping in a directory called mgltools.

```
cd ~
curl -k https://ccsb.scripps.edu/download/532/ --output mgltools.tar.gz
mkdir -p mgltools
tar -xvzf mgltools.tar.gz -C mgltools --strip-components=1
```

Now the tools should be installed:

```
cd mgltools
bash install.sh
source ./initMGLtools.sh
```

This now will have made a directory on the users directory called `mgltools` which all scripts are placed in. 

## Install AutoGrid
AutoGrid can be installed via the sudo command:
```
sudo apt install autogrid
```