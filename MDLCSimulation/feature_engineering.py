#6) feature engineering - engineering (or) creating, transforming, selecting and optimizing features to improve model performance

#importing packages directly on top of the program
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, KBinsDiscretizer, StandardScaler, MinMaxScaler, PolynomialFeatures

def feature_engineering(x_train, x_val, x_test):
    
    #i) feature creation - creating new features from existing features
    def create_feature(x_train, x_val):
        #a) data augmentation - augmenting (or) expanding features by creating variations (like image rotation, text paraphrasing) with modifying them
        def augment_feature(x_train, x_val):
            
            #augmenting training and validation features
            x_train, x_val = x_train, x_val
            
            #displaying augmented training and validation features
            print(x_train, x_val)
            
            print("Features are augmented successfully\n")
            return x_train, x_val
        
        #b) feature construction - constructing new features (polynomial features) by combining (or) transforming existing features without modifying them
        def construct_feature(x_train, x_val):
            
            #constructing training and validation features
            x_train, x_val = x_train, x_val
            
            #displaying constructed training and validation features
            print(x_train, x_val)
            
            print("Features are constructed successfully\n")
            return x_train, x_val
        
        x_train, x_val = augment_feature(x_train, x_val)
        x_train, x_val = construct_feature(x_train, x_val)
        
        #displaying newly created training and validation features
        print(x_train, x_val)
        
        print("Features are created successfully\n")
        return x_train, x_val
    
    #ii) feature reduction (or) extraction - reducing (or) removing redundant (or) irrelevant features (or) extracting relevant features
    def reduce_feature(x_train, x_val):
        
        #a) feature selection - selecting (or) choosing the most important features without altering them
        def select_feature(x_train, x_val):

            #selecting important training and validation features
            x_train = x_train[x_train.columns[0]]
            x_val = x_val[x_val.columns[0]]
            
            #displaying selected training and validation feature names
            print(f"Training Features:\n{x_train_name}, Validation Features:\n{x_val_name}")
            print("Features are selected successfully\n")
            return x_train, x_val
        
        #b) dimensionality reduction - reducing dimensions of features (or) transforming features into a lower-dimensional space while retaining important information
        #using algorithms like PCA, t-SNE, LDA
        def reduce_dimensions_feature(x_train, x_val):
            
            #reducing dimensions of training and validation features
            x_train, x_val = x_train, x_val
            
            #displaying reduced dimensions of training and validation features
            print(x_train, x_val)
            
            print("Dimensions of features are reduced successfully\n")
            return x_train, x_val
        
        x_train, x_val = select_feature(x_train, x_val)
        x_train, x_val = reduce_dimensions_feature(x_train, x_val)
        
        #displaying reduced training and validation features
        print(x_train, x_val)
        
        print("Features are reduced successfully\n")
        return x_train, x_val
    
    #iii) feature transformation - transforming features
    def transform_feature(x_train, x_val, x_test):
        
        #a) feature encoding (or) compression - encoding (or) compressing categorical features into numerical format (Ex: one-hot encoding, label encoding)
        def encode_feature(x_train, x_val, x_test):
            
            #using OneHotEncoder() for feature encoding to handle unknown categories
            encoder = OneHotEncoder(handle_unknown = 'ignore')
            
            #encoding training, validation and testing features using fit_transform(), transform() and transform() methods respectively
            x_train = pd.DataFrame(encoder.fit_transform(x_train).toarray())
            x_val = pd.DataFrame(encoder.transform(x_val).toarray())
            x_test = pd.DataFrame(encoder.transform(x_test).toarray())
            
            #displaying encoded training and validation features
            print(x_train, x_val)
            
            print("Features are encoded successfully\n")
            return x_train, x_val, x_test
        
        #b) feature binning - grouping continuous data into discrete bins (groups) (Ex: age groups 20-30, 30-40)
        def bin_feature(x_train, x_val, x_test):
            
            #using KBinsDiscretizer() for feature binning
            binner = KBinsDiscretizer(n_bins = 5, encode = 'ordinal', strategy = 'uniform')
            
            #binning training, validation and testing features using fit_transform(), transform() and transform() methods respectively
            x_train = pd.DataFrame(binner.fit_transform(x_train))
            x_val = pd.DataFrame(binner.transform(x_val))
            x_test = pd.DataFrame(binner.transform(x_test))
            
            #displaying binned training and validation features
            print(x_train, x_val)
            
            print("Features are binned successfully\n")
            return x_train, x_val, x_test
        
        #c) feature scaling (standardization) (z-score normalization) - scaling features to have 0 mean and unit variance
        def scale_feature(x_train, x_val, x_test):
                        
            #using StandardScaler() for feature scaling
            scaler = StandardScaler()
            
            #scaling training, validation and testing features using fit_transform() and transform() methods respectively
            x_train = pd.DataFrame(scaler.fit_transform(x_train))
            x_val = pd.DataFrame(scaler.transform(x_val))
            x_test = pd.DataFrame(scaler.transform(x_test))
            
            #displaying scaled training and validation features
            print(x_train, x_val)
            
            print("Features are scaled successfully\n")
            return x_train, x_val, x_test
        
        #d) feature normalization (minmax scaling) - normalizing feature to a fixed (particular) range of values (Ex: [0,1] (or) [-1,1])
        def normalize_feature(x_train, x_val, x_test):
                        
            #using MinMaxScaler() for feature normalization
            scaler = MinMaxScaler()
            
            #normalizing training and validation features using fit_transform() and transform() methods respectively
            x_train = pd.DataFrame(scaler.fit_transform(x_train))
            x_val = pd.DataFrame(scaler.transform(x_val))
            x_test = pd.DataFrame(scaler.transform(x_test))
            
            #displaying normalized training and validation features
            print(x_train, x_val)
            
            print("Features are normalized successfully\n")
            return x_train, x_val, x_test
        
        #x_train, x_val, x_test = encode_feature(x_train, x_val, x_test)
        #x_train, x_val, x_test = bin_feature(x_train, x_val, x_test)
        x_train, x_val, x_test = scale_feature(x_train, x_val, x_test)
        x_train, x_val, x_test = normalize_feature(x_train, x_val, x_test)
        
        #displaying transformed training and validation features
        print(x_train, x_val)
        
        print("Features are transformed successfully\n")
        return x_train, x_val, x_test
    
    #x_train, x_val = create_feature(x_train, x_val)
    #x_train, x_val = reduce_feature(x_train, x_val)
    x_train, x_val, x_test = transform_feature(x_train, x_val, x_test)
    
    #displaying engineered training and validation features
    print(x_train, x_val)
    
    print("Features are engineered successfully\n")
    return x_train, x_val, x_test
