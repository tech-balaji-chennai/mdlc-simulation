#9) ml model tuning - tuning ml model by hyperparameter tuning and model selection

#importing packages directly on top of the program
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error

def ml_model_tuning(current_model, x_val, y_val, max_iterations=3): #setting max_iterations to 3 to stop after 3 retries
    
    #hyperparameter tuning - tuning hyperparameters of current model (or) optimizing model
    def hyperparameter_tuning(model, x_val, y_val):
        if current_model is None:
            return None
        
        # Remove 'positive' as it might cause issues
        param_grid = {'fit_intercept': [True, False]}
        grid_search = GridSearchCV(estimator = current_model, param_grid = param_grid, cv=min(5, len(x_val)), scoring='r2', error_score='raise')
        
        try:
            grid_search.fit(x_val, y_val)
        except Exception as e:
            print(f"Error during hyperparameter tuning: {e}")
            return None
        
        print(grid_search.best_params_)
        return grid_search
    
    def model_selection(grid_search):
        if grid_search is None:
            return None
        selected_model = grid_search.best_estimator_
        return selected_model

    def validate_selected_model(selected_model, x_val, y_val):
        if selected_model is None:
            return None
        y_val_pred = selected_model.predict(x_val)
        print(f"Predicted Salary:\n{y_val_pred}\n")
        print(f"Actual Salary:\n{y_val}\n")
        print("Selected model predicted successfully\n")
        print("Model is validated successfully\n")
        return y_val_pred
    
    def calculate_selected_model_performance(selected_model, y_val, y_val_pred, iteration):
        if selected_model is None or y_val_pred is None:
            return False, None

        try:
            r2_val = r2_score(y_val, y_val_pred)
            mse_val = mean_squared_error(y_val, y_val_pred)
            print(f"R2 score = {r2_val * 100:.4f}%")
            print(f"MSE = {mse_val * 100:.4f}%")
            print("Performance metrics of selected model are calculated successfully\n")
            
            if r2_val < 0.90 and iteration < max_iterations:
                print("Model is not up to the level\nRetuning...\n")
                return False, None  #Indicates that retuning is needed
            return True, selected_model  #Indicates success

        except Exception as e:
            print(f"Error during performance calculation: {e}")
            return False, None
    
    for i in range(max_iterations):
        grid_search = hyperparameter_tuning(current_model, x_val, y_val)
        if grid_search is None:
            print("Hyperparameter tuning failed. Stopping...")
            break

        selected_model = model_selection(grid_search)
        if selected_model is None:
            print("Model selection failed. Stopping...")
            break
        
        y_val_pred = validate_selected_model(selected_model, x_val, y_val)
        if y_val_pred is None:
             print("Model validation failed. Stopping...")
             break

        is_good, selected_model = calculate_selected_model_performance(selected_model, y_val, y_val_pred, i)
        if is_good:
            return selected_model
    
    return current_model
