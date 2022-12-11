from fastapi import FastAPI, Request
import pickle
import pandas as pd
from http import HTTPStatus  
from src.data  import CarFeatures

decision_tree_regressor_model = open('./models/Decision Tree Regressor.pkl', 'rb')
decision_tree_regressor = pickle.load(decision_tree_regressor_model)  

app = FastAPI()


valid_columns_names = {
    'model': 'الموديل',
    'model_year': 'موديل سنة',
    'color': 'لون السيارة',
    'motor_power': 'قوة الماتور',
    "passengers_number":'عدد الركاب',
    "trip": 'عداد السيارة',
    "previous_owners":'أصحاب سابقون',
    "original_type":'أصل السيارة',
    "license": 'رخصة السيارة',
    "fuel_type":'نوع الوقود',
    "gear_type":'نوع الجير',
    "glass_type":'الزجاج',
    "airbag": 'وسادة حماية هوائية',
    "leather_seats":'فرش جلد',
    "mag_rims":'جنطات مغنيسيوم',
    "sunroof": 'فتحة سقف',
    "cd_player":'مسجل CD',
    "closer": 'إغلاق مركزي',
    "air_condition": 'مُكيّف',
    "alarm": "جهاز إنذار"
} 

@app.get('/_healthh')
def _health_check():
    return{
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK, 
        "status": "work"
    }   

@app.post("/price_prediction")
def _price_prediction(input_params: CarFeatures):
    # try:
    #input_data = list(vars(input_params).values())[0:-1] #converting the json input to dictionary then conver its values to a list 
    data = [vars(input_params)]
    input_data = pd.DataFrame(data) 
    input_data.rename(columns=valid_columns_names, inplace=True)
    predection = decision_tree_regressor.predict(input_data) 
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "predicted_value": predection[0]    
        } 
    return response
