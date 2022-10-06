# 💡 Description

Wall-E detects trash on a live video feed and automatically classifies it among
7 main categories (paper, plastic, metal, glass, organic, e-waste and non-recyclable),

# 🤖 Stack overview

Languages: Python & JavaScript

Roboflow and `fiftyone` library for image annotations and format conversion

Tensorflow API for modeling

Tensorflow JS for deployment to production

# 🪜 Project steps

## 1. 💽 Data collection

Datasets used :
- TACO: https://github.com/pedropro/TACO
- Drinking Waste Dataset: https://www.kaggle.com/datasets/arkadiyhacks/drinking-waste-classification
- Fruit Detection: https://www.kaggle.com/datasets/andrewmvd/fruit-detection
- Fruit Images for Object Detection: https://www.kaggle.com/datasets/mbkinaci/fruit-images-for-object-detection
- Mobile Images Dataset: https://www.kaggle.com/datasets/amirhamzahaq/mobile-images-dataset
- Garbage Classification: https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification (added custom annotations for cardboard & paper categories)
- Open Images Dataset V.6: https://storage.googleapis.com/openimages/web/index.html (used for E-Waste)

A complete list of potential datasets considered: https://github.com/AgaMiko/waste-datasets-review

## 2. 🧹 Data cleaning, merging & preprocessing

The 2 datasets used did not have the same split of categories. We combined them to form 7 unique categories commonly used for recycling purposes:
1. Paper
2. Plastic
3. Glass
4. Metal
5. Organic
6. E-Waste
7. Non-recyclable

Step 1: change annotations of TACO dataset to reduce from 60 categories to 7 categories

Step 2: match the 4 categories of the Drinking_Waste_Classification dataset to match our 7 categories

Step 3: combine all annotations into one COCO format annotation

Total number of images: 9478
Total number of annotations: 13854

## 3. ✨ Model selection & training

## 4. 📸 Test predictions on photos

## 5. 🚲 Lifecycle setup of model

## 6. 🌟 Deployment to JavaScript app

There are a few key steps:

1. Convert the trained model to Tensorflow JS (script in the modelling notebook)
2. Host the model on Google Cloud Storage
3. Ensure CORS is setup so we can access the model from the Javascript app
4. Use React.JS to build the front-end application (we used an existing boilerplate for that)
5. Load the graph model from URL
6. Update the Javascript code as to match the labelmap of the model
7. Make detection with the webcam! ✨
