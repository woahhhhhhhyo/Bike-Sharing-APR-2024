# Client Server Model Overview

This Readme contains all information behind our client-server machine learning model. Throughout this semester-long project we’ve trained data, created models, created visualizations and images, endpoints for the client to run, a website, and more, all to provide a coherent, deliverable, and transparent service to a client. Every file and directory in our project plays a crucial role in delivering a clear and transparent service. From processing data to notebooks for training models, each component helps ensure our service operates smoothly and can be easily understood, and below you will be able to read through and understand how each and every file aids us in delivering this final service. 

# Behind the Scenes of our Service (Specific Pieces)

## YAML File

The ```YAML``` file is a type of readable serialization file that contains endpoints in which our service references. This ```YAML``` file contains endpoints, recognizable by their starting ‘/’. Each of these endpoints corresponds to a service that one can access on our VM. For example, we have a prediction array and a prediction plot, both of which are endpoints defined in our ```YAML``` file. Each endpoint references our sources folder, then the proper ```.py``` file, and finally the proper function within the ```.py``` file, which results in the ```YAML``` file directing the traffic of our code. Simply, the ```YAML``` is used for data exchange, organization, and easy communication between the python code of our sources and our final VM.

## Server Python File

The ```server.py``` file is extremely important, and the core of the application, as it manages incoming requests and responses. In this file we have defined routes which establish links between endpoints and functions, like prediction generation or HTML template rendering, similar to a ```YAML```. The difference comes from the handling of requests and responses by the server, something the ```YAML``` has no jurisdiction over.

## Requirements Text File

This requirements file lists all the packages that PIP must install for our service to properly run. This text file is referenced in the make file, which runs when the docker is booted up. 

## Colab Notebook

This notebook contains all of our earliest work regarding the dataset, including importing, preprocessing, normalizing, and fitting the data to our linear regression model. After importing the dataset into the notebook, we studied the dataset’s features and started our preprocessing by making judgement calls on which features we wanted to fit out prediction towards. We decided to remove features that we thought would have little impact on our count, such as whether or not the day is a working day. Next, we normalize/scale the data so that all variable values are contained (scaled) within a given range, ensuring that no variable dominates the prediction. We then used an 80/20 split and trained our data as x and y values. This is followed by PCA, a method of dimensionality reduction, able to display variance and the strongest prediction. Finally, we fit our dataset into linear regression and display the corresponding plot. The code for the model can be seen in our src directory as well. 

## Src

This directory contains all of our python source code. The YAML file has endpoints pathed to each .py file and each definition or function within the .py file in order to execute the code and gain endpoint functionality. We currently have: ```figure.py```, ```file.py```, ```model_type.py```, ```plotting.py```, ```prediction.py```, ```readfile.py```, and ```reasons.py``` in the ```src``` folder. ```figure.py``` generates a plot displaying the spread of our original data. file.py allows users to upload their own data sets and receive predictions based on our linear regression model in other endpoints. ```model_type.py``` returns a string just displaying that we used linear regression. ```prediction.py``` returns an array of predicted number of bikes based on the dataset the user uploads. ```plotting.py``` displays a plot of the predicted bikes plus what day the prediction is for.  ```readfile.py``` is used to read the user uploaded file. Finally, ```reasons.py``` prints a sentence explaining why we chose linear regression as our model.

## Images

The images folder contains all the images which need to be rendered onto our website found in the templates folder. It’s important to note that moving any of these image files or changing their names will cause problems with how the images render on the website.

## Templates

The templates folder contains an html file called ```website.html``` which renders as a website when our service is run. This website contains the behind the scenes of our model production and offers some insight into what decisions we made about the model and why.

## Pickle File

The pickle file contains our linear regression model. All of our endpoints in the ```YAML``` file that need access to our linear regression model use the pickle file to get a prediction from user inputed data.

## Dockerfile

Docker is utilized in this project to containerize the application for deployment and management in our environment. The ```Dockerfile``` defines the environment setup, including installing dependencies and configuring the application. Docker does a lot of the heavy lifting in creating our machine for us, and with it, we have insurance of consistent behavior regardless of pesky variables like infrastructure, which overall simplifies the deployment process for us. From a wider point of view, this ```Dockerfile``` is what we call upon to run our application, accessing all of our templates, sources, and files, in which finally the user can access our endpoints. 

## Makefile

The ```Makefile``` calls upon the ```Dockerfile``` and makes the deployment of docker simple and easy. With simple commands that we've repeated over the semester like make docker-all and make docker-clean the makefile is able to build the Docker image and run the Docker container.

# Running the Service on your Machine

Running our service on your machine should be relatively easy. Once you've downloaded our ```app_v0``` folder all you should need to do is run the make command below:

```bash
make docker-all
```
Then, using a browser go to the following: http://vm-148-X.ise.luddy.indiana.edu:11000/e222/ui/

*Note: X is your assigned virtual machine number.*

At this point you can interact with the service through the endpoints provided.

However, to view the website which discusses the development behind our linear regression model you must specify a different URL: 
http://vm-148-X.ise.luddy.indiana.edu:11000/html/website.html

Finally, when you're done interacting with the service, it's important to stop the service using the following command:

```bash
make docker-clean
```

Happy service using!
