# Description

Wall-E detects trash on a live video feed and automatically classifies it among
5 main categories (paper, plastic, metal, paper, organic),

# Stack overview

Languages: Python & JavaScript
Roboflow for image annotations
Tensorflow API for modeling
Tensorflow JS for deployment to production

# Project steps

## 1. Data collection

Datasets used :
- TACO: https://github.com/pedropro/TACO
- Drinking Waste Dataset: https://www.kaggle.com/datasets/arkadiyhacks/drinking-waste-classification

A complete list of potential datasets considered: https://github.com/AgaMiko/waste-datasets-review

## 2. Data cleaning & preprocessing

The 2 datasets used did not have the same split of categories. We combined them to form 5 unique categories commonly used for recycling purposes:
1. Paper
2. Plastic
3. Glass
4. Metal
5. Organic

Step 1: change annotations of TACO dataset to reduce from 60 categories to 5 categories

Step 2: match the 4 categories of the Drinking_Waste_Classification dataset to match our 5 categories

Step 3: combine all annotations into one file (PASCAL, JSON, ???)

## 3. Model selection & training

## 4. Test predictions on photos

## 5. Lifecycle setup of model

## 6. Deployment to JavaScript app
