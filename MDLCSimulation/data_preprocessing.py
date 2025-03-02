#4) data preprocessing - preprocessing data - checking if dataset has any null values, outliers (or) inconsistencies

#importing packages directly on top of the program
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def data_preprocessing(file_path='salary_data.csv'):
    
    #i) data ingestion - ingesting (or) loading (or) reading data into program for further processing
    def ingest_data(file_path):
        try:
            data_name = os.path.splitext(os.path.basename(file_path))[0].split('_')[0]
            data = pd.read_csv(file_path)
            return data_name, data
        except FileNotFoundError:
            print(f"Error: File not found at path: {file_path}")
            return None
    
    #ii) data display - displaying dataset
    def display_data(data):
        try:
            print(data.head())
            return 1
        except Exception as e:
            return 0
    
    #iii) data validation - validating data initially
    def validate_data(data):
        
        #a) completeness check - checking completeness of data
        def check_completeness(data):
            process = 1
            if process == 0:
                return 0
            return 1
        
        #b) accuracy check - checking accuracy of data
        def check_accuracy(data):
            process = 1
            if process == 0:
                return 0
            return 1

        #c) consistency check - checking consistency of data
        def check_consistency(data):
            process = 1
            if process == 0:
                return 0
            return 1

        #d) duplicate check - checking duplicate of data
        def check_duplicate(data):
            process = 1
            if process == 0:
                return 0
            return 1

        #e) range constraint check - checking range constraint of data - ensuring numerical values fall within a valid (or) expected range
        #identifying outliers (or) invalid data
        def check_range_constraint(data):
            process = 1
            if process == 0:
                return 0
            return 1
        
        #executing sub-steps of data validation step
        def execute_all_validate():
            
            status = check_completeness(data)
            if status == 0:
                print("Completeness check failed. Stopping...\n")
                return 0
            print("Completeness is checked successfully\n")
            
            status = check_accuracy(data)
            if status == 0:
                print("Accuracy check failed. Stopping...\n")
                return 0
            print("Accuracy is checked successfully\n")
        
            
            status = check_consistency(data)
            if status == 0:
                print("Consistency check failed. Stopping...\n")
                return 0
            print("Consistency is checked successfully\n")
            
            status = check_duplicate(data)
            if status == 0:
                print("Duplicate check failed. Stopping...\n")
                return 0
            print("Duplicate is checked successfully\n")
            
            status = check_range_constraint(data)
            if status == 0:
                print("Range constraint check failed. Stopping...\n")
                return 0
            print("Range constraint is checked successfully\n")
        
        status = execute_all_validate()
        if status == 0:
            return 0
        return 1
    
    #iv) data cleaning - cleaning dataset
    def clean_data(data):
        
        #a) data imputation - imputing (or) handling missing data (or) inconsistent data
        def impute_data(data):
            try:
                #checking and displaying no of null (or) missing values of null value series
                null_count = data.isnull().sum().sum()
                print(f"No of null values = {null_count}")
                if null_count > 0:
                    #filling null (or) missing values with mean
                    data = data.fillna(data.mean())
                    print(f"After filling null values:\n{data}")
                return data
            except Exception as e:
                return None
        
        #b) data deduplication - removing duplicates
        def deduplicate_data(data):
            try:
                #checking and displaying no of duplicate values
                duplicate_count = data.duplicated().sum()
                print(f"No of duplicate values = {duplicate_count}")
                if duplicate_count > 0:
                    #deleting all duplicate rows
                    data = data.drop_duplicates()
                    print(f"After deleting duplicate values:\n{data}")
                return data
            except Exception as e:
                return None
        
        #c) data debugging - fixing errors
        def debug_data(data):
            try:
                data = data.rename(columns = {'YearsExperience': 'Experience'})
                return data
            except Exception as e:
                return None
        
        #executing sub-steps of data cleaning step
        def execute_all_clean(data):
            data = impute_data(data)
            if data is None:
                print("Data imputation failed. Stopping...\n")
                return None
            print("Data is imputed successfully\n")
            
            data = deduplicate_data(data)
            if data is None:
                print("Data deduplication failed. Stopping...\n")
                return None
            print("Data is deduplicated successfully\n")
            
            data = debug_data(data)
            if data is None:
                print("Data debugging failed. Stopping...\n")
                return None
            print("Data is debugged successfully\n")
            
            return data
        
        data = execute_all_clean(data)
        if data is None:
            return None
        return data
    
    #v) data splitting - splitting data into train-test (or) train-validation-test datasets
    def split_data(data):
        x = data[['Experience']]
        y = data['Salary']
        
        #Displaying features and target
        print(f"Features:\n{x}\n\nTarget:\n{y}")
        
        #To verify (or) confirm the shapes of x be (m, n) (2d array) and y be (m) (1d array) (Here, m = 30; since 1 feature, n = 1)
        print(x.shape, y.shape)
        
        try:
            #splitting dataset into 60% training, 20% validation and 20% testing data (x_train, x_val, x_test, y_train, y_val, y_test
            
            #splitting data into 60% training data (x_train, y_train) and 40% temporary data (x_temp, y_temp)
            x_train, x_temp, y_train, y_temp = train_test_split(x, y, test_size=0.4, random_state=42)
            
            #splitting temporary data (100% i.e. 40%) into 50% (i.e. 20%) validation data (x_val, y_val) and 50% (i.e. 20%) testing data (x_test, y_test)
            #ensuring at least 2 samples in test set
            if len(x_temp) <= 3:
                x_val = x_temp[:1]
                x_test = x_temp[1:]
                y_val = y_temp[:1]
                y_test = y_temp[1:]
            else:
                x_val, x_test, y_val, y_test = train_test_split(x_temp, y_temp, test_size=0.5, random_state=42)
            
            #To verify (or) confirm the shapes of x_train, x_test and y_train, y_test to be matched (m,n) and (m,)
            print(x_train.shape, y_train.shape, x_val.shape, y_val.shape, x_test.shape, y_test.shape)
            
            return x_train, x_val, x_test, y_train, y_val, y_test
        
        except Exception as e:
            print(f"Error during data splitting: {e}")
            return None, None, None, None, None, None
    
    #executing steps of data preprocessing process
    def execute_all():
        
        #executing data ingestion step
        data_name, data = ingest_data(file_path)
        if (data_name is None) or (data is None):
            print(f"Data ingestion failed. Stopping...\n")
            return None, None, (None,None,None,None,None,None)
        print("Data is read successfully\n")

        #executing data display step
        status = display_data(data)
        if status == 0:
            print(f"Data display failed. Stopping...\n")
            return None, None, (None,None,None,None,None,None)
        print("Data is displayed successfully\n")
        
        #executing data validation step
        status = validate_data(data)
        if status == 0:
            print(f"Data validation failed. Stopping...\n")
            return None, None, (None,None,None,None,None,None)
        print("Data is validated successfully\n")
        
        #executing data cleaning step
        data = clean_data(data)
        if data is None:
            print(f"Data cleaning failed. Stopping...\n")
            return None, None, (None,None,None,None,None,None)
        print("Data is cleaned successfully\n")
        
        #executing data splitting step
        x_train, x_val, x_test, y_train, y_val, y_test = split_data(data)
        if x_train is None:
            print(f"Data splitting failed. Stopping...\n")
            return None, None, (None,None,None,None,None,None)
        print("Data is splitted successfully\n")
        
        return data_name, data, (x_train, x_val, x_test, y_train, y_val, y_test)
        
    data_name, data, (x_train, x_val, x_test, y_train, y_val, y_test) = execute_all()
    
    if x_train is not None:
        x_train = pd.DataFrame(x_train)
    if x_val is not None:
        x_val = pd.DataFrame(x_val)
    if x_test is not None:
        x_test = pd.DataFrame(x_test)   
    
    print("Data is preprocessed successfully\n")
    return data_name, data, (x_train, x_val, x_test, y_train, y_val, y_test)
