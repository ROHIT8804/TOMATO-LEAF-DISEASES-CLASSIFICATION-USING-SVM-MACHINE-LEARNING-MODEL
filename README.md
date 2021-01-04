# TOMATO-LEAF-DISEASES-CLASSIFICATION-USING-SVM-MACHINE-LEARNING-MODEL

In this Project images of tomato leaves (9 diseases and a healthy class) achieved from PlantVillage dataset is bring as input to feature extraction methods such as shape based features, colour based features and texture based features that will extract necessary features and save it to CSV file. The CSV file is use to find the accuracy from model Support Vector Machine (SVM) .Overall the way of training Support Vector Machine (SVM) model on large and publicly available images datasets provide a clear path to identify or classify various Tomato diseases easily and quickly.

#  Methodology:
A.	Data Acquisition

The data or images of tomato leaf disease have been collected from Plant Village repository. Images of tomato leaf (size 150MB) were downloaded using IDM downloader. The collected dataset has almost 18200 images that belongs to 10 various classes. 

B.	Data Pre-Processing

Step 1:  images of datasets were resized into 512*512 resolution so that the training process of model should be increased and beneficial for the computation. 

Step 2: Smoothing of images by using Guassian Filter. A Gaussian filter is a linear filter. It’s usually used to reduce noise or to blur the image. 

Step 3: Adaptive image thresholding using Otsu’s thresholding method. Image thresholding is a simple, effective way of partitioning an image into a background and foreground.

C.	Feature Extraction

In this method various features of plant leafs were used like: shape features, colour features, texture features.

D.	Classification 

Classification algorithm used SVM , LinearRegression, DecisionTree, RandomForest

E.  Result:

                                                                     	                         
Accuracy

1	
LinearRegression	
                                                            75.6%

2	
DecisionTree	
                                                            60.1%

3	
RandomForest	
                                                            82.4%

4	
SVM	
                                                            98.2%

F.  Conclusion and Future Work

This project explain different features of leaf image and also explain methods of extracting features. As part of future work different datasets and learning rates could also be used to improve or increase the accuracy of the model. One can also use new models to train dataset and classify diseases more accurately. So by using above model (SVM) decision can be made that support and help farmers to verify Tomato diseases as quickly as possible so that diseases can be cured. Methodology proposed having 97-98% accuracy that detect diseases accurately

G.  Paper Published:

Link: http://www.modern-journals.com/index.php/ijma/article/view/204

