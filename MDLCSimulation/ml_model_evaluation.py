#10) ml model evaluation - evaluating ml model's performance and improving it

#importing packages directly on top of the program
from sklearn.metrics import r2_score, mean_squared_error

def ml_model_evaluation(final_model, x_test, y_test):
    
    #i) ml model testing - testing final ml model prediction on test set      
    def test_final_model(final_model, x_test, y_test):
        y_test_pred = final_model.predict(x_test)
        print(f"Predicted Salary:\n{y_test_pred}\n")
        print(f"Actual Salary:\n{y_test}\n")
        print("Final model predicted successfully\n")
        print("Model is tested successfully\n")
        return y_test_pred
    
    #ii) performance metrics calculation of final ml model - calculating performance metrics of final model prediction to check its performance
    #performance metrics are r2, mse, rmse, etc.
    def calculate_final_model_performance(y_test, y_test_pred):
        r2_test = r2_score(y_test, y_test_pred)
        mse_test = mean_squared_error(y_test, y_test_pred)
        print(f"R2 score = {r2_test*100:.4f}%")
        print(f"MSE = {mse_test*100:.4f}%")
        print("Final Model is tested successfully\n")
        
        #b.1) performance of final ml model
        if r2_test >= 0.99:
            print("Model's performance: perfect")
        elif r2_test > 0.90:
            print("Model's performance: outstanding")
        elif r2_test == 0.90:
            print("Model's performance: excellent")
        elif r2_test > 0.80:
            print("Model's performance: very strong")
        elif r2_test == 0.80:
            print("Model's performance: strong")
        elif r2_test > 0.50: #above average (or) superpar
            print("Model's performance: moderate")
        elif r2_test == 0.50: #at average (or) par
            print("Model's performance: average")
        elif r2_test > 0.20: #below average (or) subpar
            print("Model's performance: fair")
        elif r2_test == 0.20:
            print("Model's performance: weak")
        elif r2_test > 0.10:
            print("Model's performance: very weak")
        elif r2_test == 0.10:
            print("Model's performance: terrible")
        elif r2_test > 0.01:
            print("Model's performance: awful")
        elif r2_test == 0.01:
            print("Model's performance: imperfect")
        else:
            print("Model's performance: Useless")
    
    y_test_pred = test_final_model(final_model, x_test, y_test)
    calculate_final_model_performance(y_test, y_test_pred)
    print("Model is evaluated successfully\n")
    
    return final_model
