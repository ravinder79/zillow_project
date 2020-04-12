# Predicting Home Prices Using Linear Regression

## Deliverables
* Find major drivers of home Prices
* Deliverable 1: Presentation slides (Audience == Zillow Team)

* Deliverable 2: Repo containing Jupyter Notebook displaying your work through the pipeline with detailed documentation.

* Deliverable 3: .py modules containing functions that ensure your work is reproducible.

* Deliverable 4: README.md

* Deliverable 5: Tax Rate Distribution for each County
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

# Summary of findings
See the link below for summary slides

https://docs.google.com/presentation/d/1glw4Udz6z8rrbGHgXGB5m5Gg88Ss7asb7lqrd8KiGaM/edit?usp=sharing