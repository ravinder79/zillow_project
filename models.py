
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn.model_selection import train_test_split
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, explained_variance_score
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.preprocessing import QuantileTransformer, quantile_transform
from sklearn.metrics import median_absolute_error, r2_score
from math import sqrt
from sklearn.preprocessing import PolynomialFeatures
from pygam import LinearGAM, s, f, te
from sklearn.linear_model import RidgeCV
from sklearn.compose import TransformedTargetRegressor



def ols_model_log(X,y):
    predictions = pd.DataFrame({
    'actual': y_train.log2value
    })
    #predictions.head(2)
    from statsmodels.formula.api import ols
    
def GAM_linear(X, y):
    X= X.to_numpy()
    y = y.to_numpy()
    from pygam import LinearGAM, s, f, te
    gam = LinearGAM(s(0) +s(1) +f(2))
    gam.gridsearch(X,y)
    y_pred = gam.predict(X)
    y_pred = pd.DataFrame(y_pred)
    y_pred['actual'] =y
    y_pred['residual'] = y_pred.actual-y_pred[0]
    return gam, gam.summary(), y_pred
