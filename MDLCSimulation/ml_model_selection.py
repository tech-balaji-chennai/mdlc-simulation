#7) ml model selection - selecting relevant ml model for data and creating it

#importing packages directly on top of the program
from sklearn.linear_model import LinearRegression

def ml_model_selection():
        print("Linear Regression ml model is selected and created successfully\n")
        model = LinearRegression()
        return model
