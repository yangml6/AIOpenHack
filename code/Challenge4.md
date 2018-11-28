# Challenge 4:  Deep Learning

## Background

The Data Science team at AdventureWorks and your team have now learned a great deal about classical Machine Learning and have put it to practical use. If the accuracy was acceptable, AdventureWorks would likely stick with a simple, easy-to-use frameworks like `scikit-learn`.

However, the gear retailer wants to try deep learning algorithms on the data to see if the accuracy of gear classification improves. AdventureWorks also anticipates an influx of catalog and outdoor pictures soon and deep learning shines when the data size gets bigger. Also, the Data Science team is eager to learn more about deep learning and Convolutional Neural Networks (CNNs) for image analysis because CNNs naturally lend themselves to performing well on complex data such as images.

What differentiates Deep Learning from the more general Artificial Neural Networks is the hidden layers in its architecture which help to better "recognize" features in data using very complex functions. Neural Networks are just a very specialized form of Machine Learning. Deep learning solutions can require less preprocessing and feature engineering.

### Prerequisites

* Team decides upon a deep learning framework to use in this Challenge, after reading about several different frameworks (see [References](#references))
* Team performs any installs or updates to the latest versions of frameworks in their chosen setup

### Challenge

Use the team setup and expertise to do the following tasks.

Create a Convolutional Neural Network (a deep learning architecture) to classify the gear data. The architecture or design should contain a mix of layers such as convolutional and pooling (see [References](#References)).

There is architecure information in a CNTK <a href="https://cntk.ai/pythondocs/CNTK_103D_MNIST_ConvolutionalNeuralNetwork.html#CNN-Model-Creation" target="_blank">Tutorial</a> that is helpful in understanding these concepts.

Train a model on the training dataset using the architecture the team has decided to try.  The team may have to iterate on the architecture.  Make sure the best trained model is saved to disk.

### Success Criteria

* Team will run a code cell in a Jupyter notebook for the coach that shows the model accuracy is 85% or greater (using the test data set from Challenge 3)
* Team will run a code cell in a Jupyter notebook for the coach that shows the model accuracy for each gear class (using the test data set from Challenge 3)

### References

Read this first

* What is a convolutional neural net <a href="https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/" target="_blank">Ref</a> or <a href="https://www.youtube.com/watch?v=FmpDIaiMIeA" target="_blank">Video</a>
* High level overview of Machine Learning <a href="https://youtu.be/k-K3g4FKS_c" target="_blank">Video</a>

Deep Learning Frameworks

* TensorFlow  
    * <a href="https://www.tensorflow.org/" target="_blank">Docs</a> And <a href="https://www.tensorflow.org/tutorials/" target="_blank">Tutorials</a>
* CNTK 
    * <a href="https://www.microsoft.com/en-us/cognitive-toolkit/" target="_blank">Docs</a> And <a href="https://cntk.ai/pythondocs/tutorials.html" target="_blank">Tutorials</a>
* Keras (an abstraction layer that works with TensorFlow or CNTK)
    * <a href="https://keras.io/" target="_blank">Docs</a> And <a href="https://github.com/fchollet/keras-resources" target="_blank">Tutorials</a>