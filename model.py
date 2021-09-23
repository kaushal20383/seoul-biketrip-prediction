import joblib
import matplotlib as plt
import pandas as pd
import numpy as np
import os
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
 
curr_path = os.path.dirname(os.path.realpath(__file__))

feat_cols =['Distance', 'Haversine', 'Phour', 'Pmin',
             'Dhour', 'Dmin', 'Temp', 'Humid', 'Solar', 'Dust']

#model = joblib.load(curr_path+'../final_model.joblib') 

#print(model)

def predict_duration(attributes: np.ndarray):
    """ Returns Bike Trip Duration Value"""
    #pred = model.predict(attributes)
    print("Duration predicted")
    #return int(pred[0])
    return (10)



