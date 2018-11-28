# Challenge 0: Setting Up Your Workspace For A Successful OpenHack

## Background

Before the team can begin working on Machine Learning and Data Science tasks, everyone needs to have a development environment that will work well with common Python libraries.

## Challenge

Set up an environment that is conducive for Machine Learning tasks. It should include:

* Python 3.5
* Jupyter or JupyterHub access
* pip (Python package manager)
* See additional (optional) tools [here](#optional)

This environment can take advantage of cloud Data Science specific [Azure](#linux-dsvm) tooling or a [Local](#local-computer) Data Science setup on your machine.

### Ubuntu DSVM

This setup has been found to help the team work together in a consistent environment. 

We've commonly found the following setup to work very well:

* Ubuntu Data Science Virtual Machine (DSVM)
    * OS:  Ubuntu
    * Size:  CSP _DS12 v2_ (4 /	28.00 GiB	RAM / 56 GiB Temporary Storage)	~$0.299/hour - optimized for memory and a medium workload
    * Region:  West Central US
    * This will also include:
      * Python 3.5
      * Jupyterhub
    * Setting up one DSVM for the whole group and logging in with Jupyterhub is best to foster collaboration and consistency
    * See [References](#references) for more guidance and help

* See data download instructions [here](#data-downloads)
* Determine whether any [optional](#optional) installs should be added to team members' environments

### Local computer

* Install Anaconda Python **3.5.2** (this is equivalent to Anaconda 4.1.1) if you don't have it for your system:
  * Installation information [here](https://conda.io/docs/user-guide/install/index.html)
  * If creating conda environments, there are alternatives to installing a specific conda version [Ref](https://docs.anaconda.com/anaconda/faq#id3)
* Use the Python package manager to at least install Juypyter
  * `pip install jupyter`
* Install other Data Science packages as the need arises

* See data download instructions [here](#data-downloads)
* Determine whether any [optional](#optional) installs should be added to team members' environments

## Success Criteria

* Run 2 code cells, one with each of the following command blocks to ensure successful setup.
   ```bash
  ! pip freeze
  ! pip --version
  ````
  ```python
  import sys
  sys.version
  ```

## References

### Ubuntu DSVM

* Create a Linux Data Science Virtual Machine (DSVM) and use JupyterHub to code with your team - [Video](https://www.youtube.com/watch?v=4b1G9pQC3KM) or [Doc](https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/linux-dsvm-walkthrough#jupyterhub)

### Data Downloads

* For the cloud setup, with the DSVM, a convenient way to download the data is through OS commands within a Jupyter notebook, e.g.:

    ! curl -O https://challenge.blob.core.windows.net/challengefiles/gear_images.zip

* For the local setup, download the gear dataset [by clicking here](https://challenge.blob.core.windows.net/challengefiles/gear_images.zip).

### Optional

* Git [Download](https://git-scm.com/downloads)
* Azure ML CLI [Install](https://docs.microsoft.com/en-us/azure/machine-learning/preview/deployment-setup-configuration)

Using installed tools
* Getting started with conda [Doc](https://conda.io/docs/user-guide/getting-started.html)
* Creating and activating a conda environment [Ref](https://conda.io/docs/user-guide/tasks/manage-environments.html)
* Look here if your Jupyter Notebook isn't able to use your conda environment [Ref](http://ipython.readthedocs.io/en/stable/install/kernel_install.html#kernels-for-different-environments)