# Challenge 3:  Introduction to Custom Machine Learning

## Background

Challenge 2 set the team up for success by providing quality data. Challenge 3 will begin a journey into custom Machine Learning.

AdventureWorks wants their Data Science team, including your team members, to begin learning how and when to perform custom Machine Learning with powerful, more programmatic APIs. Becoming proficient in Machine Learning takes some time, however, beginning with a high-level API, that is stable and has good documentation, is a great start. Some of the reasons to move on to custom Machine Learning include:

* To explore different algorithms to optimize what works best for the data
* To create a workflow with more control over your process
* To deploy a model to a specific architecture or configuration
* Certain limits in bandwidth or data size for a current service have been exceeded

Some of these points will be addressed in this challenge.

## Prerequisites

* Team has a setup for sharing code and working in Jupyter
* Preprocessed Gear image data from Challenge 2
* An installation of the Python package called `scikit-learn` - check if it is installed and update it to the lastest or simply install (see [Hints](#hints)).
* The test dataset 
    * Cloud setup `! curl -O https://aka.ms/gear-testset`
    * Local setup [Download](https://aka.ms/gear-testset)

## Challenge

One of the most popular and well-established Python ML packages, Scikit-Learn, is often the go-to package for starting out and is not uncommon in production systems.  It has a simple, intuitive API (often modeled by other packages) and is a great place to start for learning, implementing and programming traditional ML and basic neural networks in Python.

Use the team setup and team expertise to do the following tasks.

Use a non-parametric classification method (see [References](#references)) to create a model to predict the class of a new gear image, training on the preprocessed 128x128x3 gear data from Challenge 2.  The algorithm should be chosen from "off-the-shelf" non-parametric algorithms for classification found in the `scikit-learn` library.

Find more information in the [References](#references) and [Hints](#hints).

Perform the following as a team:

* Choose an algorithm from `scikit-learn` documentation
* Train the model with the preprocessed image array data from Challenge 2
* Predict the class of the following piece of gear with the model: <a href="https://shop.epictv.com/sites/default/files/ae42ad29e70ba8ce6b67d3bdb6ab5c6e.jpeg" target="_blank">here</a>
* Using your methods from Challenge 2, preprocess the test set.
* Evaluate the model with a confusion matrix to see how individual classes performed (use test set)
* Output the overall accuracy (use test set)

## Success Criteria

* The team will run one code cell in a Jupyter notebook for the coach predicting the class successfully of a piece of gear in the provided url above.
* The team will run one code cell in a Jupyter notebook for the coach showing the accuracy score on the provided test data set.  This score should be above 80%.

## References

**Read me first**

* `scikit-learn` algorithm cheatsheet <a href="http://scikit-learn.org/stable/index.html" target="_blank">Ref</a>
* `jupyter` <a href="https://jupyter.readthedocs.io/en/latest/running.html" target="_blank">Ref</a>

**ML and Scikit-Learn on Azure Notebooks**

* https://notebooks.azure.com/rheartpython/libraries/PythonDS101/html/10.MachineLearningI.ipynb
* https://notebooks.azure.com/rheartpython/libraries/PythonDS101/html/11.MachineLearningII.ipynb
https://notebooks.azure.com/rheartpython/libraries/PythonDS101/html/12.MachineLearningIII.ipynb

## Hints

  * Install packages with `pip install package_name` if it is not installed and `pip install --upgrade package_name` if it needs to be updated to the latest version.
  * It can help to create an "image reader" function if not already built.