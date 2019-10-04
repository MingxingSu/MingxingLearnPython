'''
Terminologies: 
 
LABEL: variable we are predicting: spam or not spam?
    typically represented by  variable 'y'

Features: are input variables describing our data
    typically represented by the variables {X1,X2, ..., Xn}
    
Example: is a particular instance of data, x

Labeled example:  has {features, lable}:(x, y)
    used to train the model
    
Unlabeled example: has {features, ?} :(x,y)
    used for making predictions on new data

Model: maps examples to predicted lables:  y'
    defined by internal parameters, which are learned.
    
Training: create or learning the model. show model examples and enable the model to gradually learn
    the relationship between features and label
    
Inference: apply trained model to unlabeled examples to make useful predictions.

Regression:
    model predict continuous values. for example, what's the value of a house in a city?

Classification:
    model predict yes or no.
    is an image of a dog , a cat, or a hamster?

Loss function:
    measure how good the model is.
    Squared loss(also called as L2 Loss) = sum[( y-prediction(x))^2] -- distance between label and prediction
    Mean square error(MSE): square loss divide by the numbers of examples.

Linear regression:  
    y' = b + w1*x1
    y' is the predicted label
    b is the bias
    w1 is the weight of features
    x1 is a features

Reducing loss:
    Gradient Descent:
        Loss function is square level, take a proper step to find the mini value of loss function.
        Negative gradient steps, this strategy is called 'Gradient Descent'
    Hyperparameters: configuration settings used to tune how the model is trained.
    Derivative of loss function with respect to the weights and biases tells us how the loss changes for a given example.

Weight Initialization:
    for convex problems, weights can start anywhere, just has oen minimum, like bowl shape
    for foreshadowing: not true of neural nets.
    non-convex: like an egg crate ,more than 1 minimum, strong dependency on initial values

Batch Gradient Descent: compute over entire data set
SGD: Stochastic Gradient Descent: one example at a time
Mini-Batch Gradient Descent: batches of 10 ~ 1000.
    loss&gradients are averaged over the batch.


 

'''