# Predicting Home Prices Using Linear Regression

## Deliverables
* Find major drivers of home Prices
* Deliverable 1: Presentation slides (Audience == Zillow Team)

* Deliverable 2: Repo containing Jupyter Notebook displaying your work through the pipeline with detailed documentation.

* Deliverable 3: .py modules containing functions that ensure your work is reproducible.

* Deliverable 4: README.md

* Deliverable 5: Tax Rate Distribution for each County
***


## Install pyGAM (https://pygam.readthedocs.io/en/latest/) before running jupyter notebook. This library is needed to GAM models i used

***


## SQL Data Acquisition 
Must use your own env file to access data.

* Choose home transaction during May and June 2017 only.

* Single-unit residential properties only
***

## Hypothesis Testing
Lets do some hypothesis testing 

* $H_0$: there is no relationship between home values and number of bedrooms, bathrooms and square_feet.

* $H_a$: There is a relationship between home values and number of bedrooms, bathrooms and square_feet
***

## Technical Skills used

* Python
* SQL
* Various data science libraries (Pandas, Numpy, Matplotlib etc)
* Stats (Hypothesis testing, correlation tests)
* Linear Regression (Single Linear Regression, Multiple Linear Regression, Generalized Additive Models, Ridge Regression)


## Data Dictionary

payment_type_id:              7043 non-null int64  (payment type id)\

internet_service_type_id  :  7043 non-null int64 (type of internet service subscribed)\

contract_type_id    :        7043 non-null int64 (type of contract, month-to-month, one year, two year)\
customer_id       :          7043 non-null object (unique customer ID)\
gender            :          7043 non-null object (male or female)\
senior_citizen    :          7043 non-null int64  (senior citizen or not)\
partner           :          7043 non-null object (have partner or is single)\
dependents        :          7043 non-null object (has dependents or not)\
tenure            :          7043 non-null int64 (how long with company in months)\
phone_service     :          7043 non-null object (has phone service or not)\
multiple_lines     :         7043 non-null object (has multiple phone lines or  not)\
online_security    :         7043 non-null object (have online security service subscribed)\
online_backup     :          7043 non-null object (have online backup service subscribed)\
device_protection :          7043 non-null object (have device_protection service subscribed)\
tech_support        :        7043 non-null object (have tech_support service subscribed)\
streaming_tv       :         7043 non-null object (streams tv)\
streaming_movies   :         7043 non-null object (streams movies)\
paperless_billing   :        7043 non-null object (have paperless billing)\
monthly_charges    :         7043 non-null float64 (monthly charges)\
total_charges      :         7043 non-null object (total charges during the tenure)\
churn              :         7043 non-null object (whether churned or not)\
contract_type      :         7043 non-null object (contract type month-to-month, one year, two year)\
internet_service_type  :     7043 non-null object (Fiber optic, DSL or none as service)\
payment_type         :       7043 non-null object (type of payment method used by subscriber)\

# Files in this repo you need to run this (you will need your own env file)
* acquire_r.py
* wrangle.py
* evaluate.py
* preprocess.py
* models.py
* logistic_regression_util.py
* knn_lesson_util.py
* Telco_Churn_Final.ipynb (Main notebook)


# Executive Summary
* We created a logistic regression model to predict customers who are likely to churn.
* The model is able to correctly predict 80% of customers who actually churn.
* Customers most likely to churn:\
** Month to month contract\
** New customers (tenure less than 2 years)\
** Have fiber optic internet
* Focus resources on retaining ‘new’ customers since company does fine retaining the longer tenured customers



# Summary of findings
See the link below for summary slides

https://docs.google.com/presentation/d/1ODagzmh01di-fNy54dmKlKO4DzZ1UNsL3oVOOEth95E/edit?usp=sharing
