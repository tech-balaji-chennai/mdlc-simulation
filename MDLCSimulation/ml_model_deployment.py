#11) ml model deployement - deploying ml model on any application (or) cloud server

#importing packages directly on top of the program
import numpy as np
import pandas as pd

class NegativeValueError(Exception):
    pass

def ml_model_deployment(model):
    
    #i) real time predictions - getting predictions on real-time
    def ml_model_predict(model):
        try:
            person_experience = float(input("Enter years of experience: "))
            if person_experience < 0.0:
                raise NegativeValueError("Experience cannot be negative. Please enter a positive float for any experience\n")
        except ValueError as e:
            print("Invalid experience. Please enter a float for any experience\n")
            return
        except NegativeValueError as e:
            print(e)
        
        #making real-time predictions on new, unseen data
        predicted_salary = model.predict(np.array([[person_experience]])) #experience = 10.0
        print(f"Predicted Salary = {predicted_salary[0]:.2f}\n")
    
    print("Model is deployed successfully\n")
    ml_model_predict(model)
