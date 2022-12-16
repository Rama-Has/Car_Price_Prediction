import numpy as np
import pandas as pd
import re
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import PolynomialFeatures  


def previous_owners(text):
    """
    function to get number of previous owner as type of float instead of the available text for 
    each car
    input:
        text (str): value of the cell to be converted to a number based on the 
    output:
        value (float):  [0-10] if the text exists in one of the given patterns
    
    """ 
    try:
        value = int(text)
        return value 
    except ValueError:
        if text is np.nan:
            return text 
        elif re.search(r'أول|اول|۱|1|واحد', text):
            return 1 
        elif re.search(r'ثاني|تاني|۲|2', text):
            return 2 
        elif re.search(r'ثالث|تالت|ثلاث|تلاث|3|۳', text):
            return int(3)
        elif re.search(r'رابع|اربع|4|٤', text):
            return 4 
        elif re.search(r'خامس|خمس|٥|5', text):
            return 5 
        elif re.search(r'سادس|ستة|٦|6', text):
            return 6 
        elif re.search(r'سابع|سبع|۷|7', text):
            return 7 
        elif re.search(r'ثامن|تامن|ثمن|تمن|۸|8', text):
            return 8 
        elif re.search(r'تاسع|تسع|۹|9', text):
            return 9 
        elif re.search(r'عشر|عاشر|۱۰|10', text):
            return 10 
        elif re.search(r'ستيراد|مستورد|جديد|صفر|غير|شرك|Zero|0|۰|مش|لا', text):  
            return 0  
        else:
            return np.nan




def convert_text_to_number(text):
    """
    function that handle inconsistant data in 'عداد السيارة' column and convert text to float 
    type 
    input:      
        text (str): value of cell 
    output: 
        value (float): nan if the text is meaningless and a valid number 
    """
    try:
        value = float(text)
        return value
    except ValueError:
        #check if the text contains الف، الاف so return integers with the text multiplied by 1000
        if re.search(r'ألف|الف|الاف', text):
            numbers = re.findall(r'\d+', text)
            if len(numbers) == 0:
                return 1000
            else:
                value = re.findall(r'\d+', text)[0]
                value = float(value) * 1000
                return value
        #check if the text contains km... then retrun the value as it is since the unit of this feature is km
        elif re.search(r'كيلو|كم|km|KM|Km|kM', text):
            numbers = re.findall(r'\d+', text)
            if len(numbers) == 0: 
                return 0
            else:
                value = float(numbers[0])
            return value
        else: 
            return np.nan  





def passengers_number(value):
    """  
    function that convert the text in form '1 + 1' to a numaric value which will be valid
    to pass in the model
    input:      
        text (str): value of cell which represent the passegers number in a particular car
    output: 
        value (int): 
    """
    try:
        #try handling values of 1 and "اكثر من 10"
        if(value == '1 '): 
            return 1
        elif(value == 'اكثر من 10 '): 
            return 11 
        else: 
            #handle the equations
            numbers_list = value.split('+') 
            return int(numbers_list[0]) + int(numbers_list[1])
    except:
        try:
            value = int(value)
            return value
        except:
            return np.nan



def get_model_scores(models, transformed_X, y):
    """
    a function to go over allmodels and get a list of scores for each 
    model using cross_val_score method 
    returns: 
        models a dictionary contains the scores list for each model with the other information 
    """ 
    # go over all models
    for model_id in models: 
        # check if polynomial to get polynomial data
        if models[model_id].get("degree"): 
            print("degree")
            #get degree of the given model
            degree = models[model_id]["degree"] 
            poly = PolynomialFeatures(degree)
            #get polynomial data  
            transformed_X = poly.fit_transform(transformed_X) 
        
        scores = cross_val_score(models[model_id]['model'], transformed_X, y)
        #models[model_id]['model'].fit(X_train, y_train)
        models[model_id]['scores_list'] = scores 
        models[model_id]['score_mean'] = np.mean(scores)
        
    # return the new dictionary
    return models



def outlier_detector(df, column_name, extreme):
    """
    a function to detecct the outliers exists in a given data
    inputs: 
        df(DataFrame): the dataframe contains the whole data
        column_name(str): the column we want to find outliers from its values
        extreme(bool): to decide to return extreme outliers or not, true for extremes false for not
    returns:
        a bool series True if outlier and False if not
    """
    if extreme:
        IQR_coef = 3
    else: 
        IQR_coef = 1.5

    quartile_1st = df[column_name].quantile(0.25)
    quartile_3rd = df[column_name].quantile(0.75)
    IQR = quartile_3rd - quartile_1st
    lower_limit = quartile_1st - IQR * IQR_coef
    upper_limit = quartile_3rd + IQR * IQR_coef
    #check if the value lies outside the lower and upper limit then set it to True otherwise set it to False
    bool_series = (df[column_name] < lower_limit) | (df[column_name] > upper_limit) 
    return bool_series

def outlier_detector_zscore(df, column_name):
    """
    a function to detect outliers using z-score method
    inputs:
        df(DataFrame): the dataframe contains the whole data
        column_name(str): the column we want to find outliers from its values
    returns:
        a bool series True if outlier and False if not
    """
    upper_limit = df[column_name].mean() + 3 * df[column_name].std()
    lower_limit = df[column_name].mean() - 3 * df[column_name].std() 
    bool_series = (df[column_name] > upper_limit) | (df[column_name] < lower_limit)
    return   bool_series

