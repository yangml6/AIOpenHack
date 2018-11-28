# Challenge 5:  Detecting Safety

## Background

AdventureWorks has partnered with a local guide service to help them collect images of mountaineers and climbers wearing helmets in an effort to encourage the use of helmets for safety. AdventureWorks wants a solution that can locate every helmet present in an image.

Object detection adds a layer of complexity and usefulness on top of classification. It predicts whether something is present, and where in the image it is located. This is important if the model needs to identify multiple instances of a class in a given image.

### Prerequisites

* The new helmet dataset 
    * Cloud setup `! curl -O https://aka.ms/helmet-testset`
    * Local setup <a href="https://aka.ms/helmet-testset" target="_blank">Download</a>
* Team decides upon a deep learning framework to use in this Challenge, after reading about several different frameworks (See [References](#references))
* Team performs any installs or updates to the latest versions of frameworks in their chosen setup

### Challenge

Using the deep learning library of your choice, create an object detection solution utilizing a modern model like Faster R-CNN. This model should be able to detect and create a bounding box around each helmet present in an image.

### Success Criteria

* Demonstrate logging or TensorBoard output showing a maximum Mean Average Precision (mAP) over 90%

## References

Read this first

* What is object detection <a href="https://tryolabs.com/blog/2017/08/30/object-detection-an-overview-in-the-age-of-deep-learning/" target="_blank">Ref</a>
* What is mAP <a href="http://fastml.com/what-you-wanted-to-know-about-mean-average-precision/" target="_blank">Ref</a>

Tooling

* Visual Object Tagging Tool `VoTT`. Works for TensorFlow and CNTK <a href="https://github.com/Microsoft/VoTT" target="_blank">Ref</a>
* When on Linux, the Tensorflow Object Detection API <a href="https://github.com/tensorflow/models/tree/master/research/object_detection" target="_blank">Ref</a>
* CNTK Documentation <a href="https://www.microsoft.com/en-us/cognitive-toolkit/" target="_blank">Ref</a>
* ONNX provides the ability to move an existing model to another model format <a href="https://onnx.ai/" target="_blank">Ref</a>

### Hints

* When the team is planning for image processing, explore what functionality your deep learning framework offers