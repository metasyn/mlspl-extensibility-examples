# mlspl-extensibility-examples

This repository holds examples of custom algorithms that can be used with the [Splunk Machine Learning Toolkit](https://splunkbase.splunk.com/app/2890/).

Many of the examples can also be found in the [ML-SPL API Documentation](https://docs.splunk.com/Documentation/MLApp/latest/API/Introduction).

This app does require that you alreay have the MLTK & Python for Scientific Computing add-on already installed.

# Examples

The examples can be found in `bin/examples`.

## Hello World

This is more or less the most minimal example possible, as you'd expect.

## Correlation Matrix

This is a simple example showing abitrary data frame manipulation. In this case, we call panda's `corr` method on the data frame.

## Savgol Filter

This is another example of an arbitrary data transformation - in this case, using a Savitzky-Golay filter on fields.

## Agglomerative Clustering

This shows how one might use some of the utility methods in the MLTK.

## SVR 

This shows how to inherit the main methods from the mixin classes.

## AdaBoostClassifier

This also shows using the mixin classes, in this case, with a more complex model.

## Bernoulli Restricted Boltzman Machine

This once again shows using the mixin classes, to add a neural network to the MLTK.
