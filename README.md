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

bathrooms : 14873 non-null float64\
bedrooms :  14873 non-null float64\
square_feet  :         14873 non-null float64\
fips      :            14873 non-null int64\
lot_size   :           14873 non-null int64\
pool     :             14873 non-null int64\
zip_code     :         14873 non-null int64\
year_built    :        14873 non-null int64\
latitude      :        14873 non-null float64\
longitude      :       14873 non-null float64\
assessed_value  :      14873 non-null float64\
tax_value       :      14873 non-null float64\
transaction_date   :   14873 non-null object\
tax_rate       :       14873 non-null float64\
County         :       14873 non-null object\
log2sf          :      14873 non-null float64 (log2 of square feet)\
log2lot_size    :      14873 non-null float64 (log2 of lot size)\
log2value       :      14873 non-null float64 (log2 of home assessed value)\
age             :      14873 non-null int64 (age of home)\
zip_median      :      14873 non-null float64 (median home price of a zip code calculated from Training Data)\
log2_zip_median  :     14873 non-null float64 (log2 of zip_median)\
haversine_distance   : 14873 non-null float64 (distance between two points on earth)\

# Files in this repo you need to run this (you will need your own env file)
* wrangle.py
* evaluate.py
* explore.py
* models.py
* Zillow_project_notebook.ipynb (Main notebook)
* zillow_explore.ipynb (notebook used for exploration only)


# Executive Summary
* Location! Location! Location! Implication: “Location matters”
* Location, home size (sq feet) and neighbourhood (e.g. median zip code home prices) are major driver of home value
    * Inland house values are lower than coastal house values. There are clusters of higher and lower values homes
    * Adding Geo-Spatial parameters (e.g. haversine distance) in models should help improve accuracy

* Other classification methods (KNN/Decision tree) should help improve the accuracy of models.


# Summary of findings
See the link below for summary slides

https://docs.google.com/presentation/d/1glw4Udz6z8rrbGHgXGB5m5Gg88Ss7asb7lqrd8KiGaM/edit?usp=sharing