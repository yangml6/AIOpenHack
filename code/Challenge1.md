# Challenge 1 -  Gearing up for Machine Learning

## Background

AdventureWorks, a major outdoor and climbing gear retailer, wants to understand customer behavior by learning more about the gear that consumers wear.  As a joint project with their Data Science team, they have provided data in the form of product catalog images for your team to get started. The team is tasked with trying several Machine Learning approaches to categorize gear present in the catalog data, a first step towards their goal. 

AdventureWorks would, eventually, like to use this knowledge to classify gear in images from Mt. Rainier, a popular climbing destination for mountaineers from around the world, and other destinations as well.  This will give a more realistic picture of current needs of existing and future customers worldwide.

Machine Learning solutions are complex and custom models require time, expertise, data preparation, ongoing maintenance and deployment. As a first approach, pre-built solutions offer a way to create a ready-to-use solution quickly before moving on to the work it takes to build custom models.

## Prerequisites

* Team has a setup for sharing code and working in Jupyter
* Team has access to the Gear catalog dataset (link and instructions provided in Challenge 0, Data Downloads)
* Team has at least 1 Custom Vision Account. Create <a href="https://customvision.ai" target="_blank">Here</a>

## Challenge

Use the team setup and expertise to do the following tasks.

Custom Vision Service is a tool for building custom image classifiers. Your challenge is to create a classification model using a portion of the gear catalog images for **hardshell jackets** and **insulated jackets** and test new images using Python and Jupyter Notebooks.

## Success Criteria

* Each team member can call the team's Custom Vision prediction endpoint from a Jupyter Notebook to predict the class of a jacket image not used in training and show a successful response

## References

Read me first

* Definitions of some common Machine Learning terms <a href="https://docs.microsoft.com/en-us/azure/machine-learning/studio/what-is-machine-learning#key-machine-learning-terms-and-concepts" target="_blank">Ref</a>
* Classification description <a href="https://docs.microsoft.com/en-us/azure/machine-learning/studio/data-science-for-beginners-the-5-questions-data-science-answers#question-1-is-this-a-or-b-uses-classification-algorithms" target="_blank">Ref</a>
* Jupyter notebook usage <a href="http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Notebook%20Basics.html" target="_blank">Doc</a>

Custom Vision Service

* Custom Vision Python SDK <a href="https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/python-tutorial" target="_blank">Ref</a>
* Custom Vision service <a href="https://customvision.ai" target="_blank">Ref</a>
* Custom Vision <a href="https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/home" target="_blank">Docs</a>