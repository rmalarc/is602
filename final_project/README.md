# Image Analysis:

**Author: Mauricio Alarcon <rmalarc@msn.com>**

## Objective

The overall purpose of the project is to be able to use traffic cammera data in order to estimate traffic volume and traffic speed.

## Data Aggregation / Datasources

We identified the following datasources that we will use in order to generate the models:

* NYC Real-Time Traffic Cameras: http://nyctmc.org/
* NYC Real-Time Traffic Speed Data: https://data.cityofnewyork.us/Transportation/Real-Time-Traffic-Speed-Data/xsat-x5sa
* Current Weather Data: http://openweathermap.org/current

**[Click here for details](project_data_capturing.ipynb)**

## Image Feature Extraction

The goal of this section of the project is to extract quantitative features from the traffic cameras.

We will attempt to obtain the following features from the captured images:

* Object count: We will obtain object count after applying various thresholding schemes.
* Standard deviation of the value of the pixels

**[Click here for details](project_image_processing_and_feature_extraction.ipynb)**

## Data Integration

The goal of this section of the project is harmonize and integrate traffic and weather data.

The resulting integrated dataset will include the following fields:

* Camera ID
* Speed
* Weather status
* Timestamp
* Time of day (Hour)
* Is Daytime

**[Click here for details](project_traffic_and_weather_data_integration.ipynb)**

## Data Analysis

The goal of this final section is to analyze the captured traffic data along the Van Wyck Expressway.

We seek to find out if it is possible to build a model that estimates traffic speed based on traffic camera images.

**[Click here for details](project_analysis.ipynb)**

## Conclusion

It is possible to build some sort of statistical model that correlates traditional quantitative data such as traffic speed to algorithmically extracted features from unstructured data, images in particular.

Exploring more sophisticated feature extraction algorithms is a well-worth pursuit which should yield in data that can be used in a linear regression and other quantitative models.
