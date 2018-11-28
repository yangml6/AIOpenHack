# Challenge 6 - Deploy to the Cloud

## Background

It's not just enough to be able to build a world class machine learning model, you need to know how to expose it so that it can be consumed by team members, developers, and 3rd parties to provide useful functionality to applications and services for AdventureWorks customers.

In this challenge you will operationalize your model as a scoring REST API in the cloud (deploy it as a webservice), so that the developers at AdventureWorks and elsewhere can then write consumer applications and use this scoring endpoint for prediction.

In this helpful diagram, the deployment phase is shown prominently as part of the Data Science lifecycle.

<img src="https://docs.microsoft.com/en-us/azure/machine-learning/team-data-science-process/media/overview/tdsp-lifecycle2.png" width="50%" height="50%" alt="Data Science Lifecycle">

## Prerequisites

* Docker engine (Docker for Windows or Docker for Mac) installed and running locally or on a VM
* Azure CLI and Azure ML CLI (`azure-cli` and `azure-cli-ml` packages)
* Tooling such as the `curl` command line tool or [Postman](https://www.getpostman.com/) to send a request to your model endpoint
* Saved model from Challenge 3, 4 or 5

## Challenge

Use the team setup and team expertise to do the following tasks.

* Deploy the team's saved model from Challenge 3, 4 or 5 as a real-time web service on Azure. 

Use one of the following tools to deploy the model as and API to which data may be sent (e.g. arrays or json) and a json response recieved - see [References](#references) for useful links.

* Azure Machine Learning CLI standalone
* Azure Machine Learning Workbench
* Non-CLI methods, e.g. Flask with Docker (see a suggestion, below)


It'd be best for AdventureWorks to have a fairly simple API, so a json-serialized image would work well.

## Success Criteria

* Demonstrate with `curl` or Postman that sending an image, via a URL or serialized, to your cloud deployed web service returns the model output - the class of gear or a helmet bounding box.

## References

**Read Me First**
* Overview of Azure ML model management <a href="https://docs.microsoft.com/en-us/azure/machine-learning/preview/model-management-overview" target="_blank">Doc</a>
* Deployment walkthrough <a href="https://azure.github.io/LearnAI-Bootcamp/lab04.2-deploying_a_scoring_service_to_aks/0_README" target="_blank">Ref</a>

**More on Deployment**
* Microsoft Blog on deploying from Azure ML Workbench and the Azure ML CLI <a href="https://blogs.technet.microsoft.com/machinelearning/2017/09/25/deploying-machine-learning-models-using-azure-machine-learning/" target="_blank">Ref</a>
* Setting up with the Azure ML CLI for deployment 
<a href="https://docs.microsoft.com/en-us/azure/machine-learning/preview/deployment-setup-configuration" target="_blank">Doc</a>
* Non-CLI deployment methods (AML alternative) <a href="https://github.com/Azure/ACS-Deployment-Tutorial" target="_blank">Ref</a>

**Schema References**
* Example of schema generation <a href="https://docs.microsoft.com/en-us/azure/machine-learning/preview/model-management-service-deploy#2-create-a-schemajson-file" target="_blank">Doc</a>
* Example showing a CNTK model and serializing an image as a `PANDAS` data type for input data to service <a href="https://github.com/Azure/MachineLearningSamples-ImageClassificationUsingCntk/blob/master/scripts/deploymain.py" target="_blank">Ref</a>
* Example showing a `scikit-learn` model and a `STANDARD` data type (json) for input data to service <a href="https://github.com/Azure/Machine-Learning-Operationalization/blob/master/samples/python/code/newsgroup/score.py" target="_blank">Ref</a>

**Docker**

* Docker Docs <a href="https://docs.docker.com/get-started/" target="_blank">Ref</a>

## Hints

* There are different input data type options for sending up to the service and you can specify this when you generate the schema for the service call.