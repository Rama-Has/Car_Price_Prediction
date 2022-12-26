from fastapi import FastAPI  
import pickle
import pandas as pd
from http import HTTPStatus  
from src.data_handler  import CarFeatures, valid_columns_names   

#Importing Models
decision_tree_regressor_model = open('./models/decision tree regressor.pkl', 'rb')
decision_tree_regressor = pickle.load(decision_tree_regressor_model) 
poly2_lasso_model = open('./models/polynomial degree 2 lasso.pkl', 'rb')
poly2_lasso = pickle.load(poly2_lasso_model)   

app = FastAPI()

@app.get('/_health')
def _health_check():
    return{
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK, 
        "status": "work"
    }   

@app.post("/price_prediction_tree")
def _price_prediction(car_features: CarFeatures):
    """
    return the predicted price using decision tree regressor
    """
    #get a list of a dictionary 
    car_features_values = [vars(car_features)]
    #convert the list to a df so it can be passed to the model
    car_data = pd.DataFrame(car_features_values) 
    #rename columns as the original dataset 
    car_data.rename(columns=valid_columns_names, inplace=True)
    #predict the price using decision tree regressor
    predection = decision_tree_regressor.predict(car_data)
    #return the predicted value 
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "predicted_value": predection[0]    
        } 
    return response

@app.post("/price_prediction")
def _price_prediction(car_features: CarFeatures):
    """
    return the predicted price using lasso with polynomial regression with degree of 2
    """
    #get a list of a dictionary 
    car_features_values = [vars(car_features)]
    #convert the list to a df so it can be passed to the model
    car_data = pd.DataFrame(car_features_values) 
    #rename columns as the original dataset 
    car_data.rename(columns=valid_columns_names, inplace=True)
    #predict the price using lasso with polynomial regression with degree of 2
    predection = poly2_lasso.predict(car_data)
    #return the predicted value  
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "predicted_value": predection[0]    
        } 
    return response 