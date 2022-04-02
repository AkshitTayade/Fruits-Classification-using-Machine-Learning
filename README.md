
## Fruits Image classification using Machine Learning

In this story, we will classify the images of fruits - apples & oranges. 
The dataset contains 200 images of fruits and vegetables captured using a individual's phone camera.

## 1. Dataset Preparation

<p align='justify'>
Our team of three members acquired 40 image samples for each of the fruits — apples and oranges. That's a total of 120 for each class. Then, after manually inspecting each photograph, we deleted images that were not suitable or had disturbances in the image, such as noise or blur. Totaling 100 samples for each class, they were housed in two separate folders labelled the same as the fruit names. When the image folders were finished, it was time to create the csv file. To begin, we created our own Python library file with built-in functions such as image mean, standard deviation, kurtosis, skewness, and entropy calculation using the OpenCV and Numpy libraries. This file came in helpful because it allowed me to just call whichever function was required on an image and receive the desired outcome. Second, we simulated reading all of the folders and photos within it, applying all of the functions, and inserting the output rowise into our csv file. The entire process of creating 200 data samples took about 2 minutes.
</p>

## 2. EDA

<p align='center'>
<img alt="IMG" src="https://github.com/AkshitTayade/Fruits-Classification-using-ML/blob/master/readme_images/Screenshot%202022-04-02%20at%2010.22.49%20PM.png"/>

<img alt="IMG" src="https://github.com/AkshitTayade/Fruits-Classification-using-ML/blob/master/readme_images/Screenshot%202022-04-02%20at%2010.22.56%20PM.png"/>
</p>

<p align='justify'>
According to the plots, we found out that it was linearly not separable and had more like a regression pattern. We even tried to find whether any two input variable should linearly seperable pattern, but none had such pattern, and we concluded to use classification algorithms.
</p>

## 3. Data Scaling
<p align='justify'>
Data Normalization was very much needed. Lets consider two input variable, i.e., Mean and Kurtosis:

Range of Mean: (155, 221), Range of Kurtosis: (-1.4, 10)

As you can see there is a huge gap between these two variable’s data points. Just by slightly increasing any of the point, adversely affects the other. Therefore we performed **StandardScaler** normalization technique.
</p>

## 4. Model Training

After 5-fold cross validation, **we got 99.286% mean score by using SVM**. Accuracy score on training, testing data:
- Training accuracy = 1.0
- Testing accuracy = 1.0
- MAE training = 0.0
- MAE testing = 0.0

## Authors

- [@Aayush Maru](https://github.com/aayushmaru18)
- [@Vidhi Sejpal](https://github.com/Vidhi-Sejpal)
- [@Akshit Tayade](https://github.com/AkshitTayade)


