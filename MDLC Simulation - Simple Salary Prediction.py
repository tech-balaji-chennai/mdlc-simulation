#MDLC (Model Development Life Cycle) Simulation

#importing packages directly on top of the program
from MDLCSimulation import *

#main function - execution starts here
if __name__ == '__main__':
    
    #Initializing variables that are needed during steps 3 to 11 to empty
    data_name, data, x_train, x_val, x_test, y_train, y_val, y_test, model = None, None, None, None, None, None, None, None, None
    ml_lifecycle = "\nMDLC (Model Development Life Cycle) - Steps:\n1) Problem Definition\n2) Design\n3) Data Collection\n4) Data Preprocessing\n" \
                   "5) Exploratory Data Analysis (EDA)\n6) Feature Engineering\n7) ML Model Selection\n8) ML Model Training\n9) ML Model Tuning\n" \
                   "10) ML Model Evaluation\n11) ML Model Deployment\n12) ML Model Monitoring And Maintenance\n13) Exit\n\n"
    
    #controlling MDLC while loop execution based on user input
    is_running = True
    
    while is_running:
        try:
            #getting choice of MDLC process as user input
            choice = int(input(f"{ml_lifecycle}Enter your choice: "))
            print()
            if not isinstance(choice, int):
                raise ValueError()
            match choice:
                case 1:
                    problem_statement = ''''''\
                    '''Problem Definition:\n    - Salary differs according to the job profile of the person.\n''' \
                    '''    - But, generally, it is the working experience that determines the salary.\n''' \
                    '''    1) Define business objectives: Predict salary based on experience.\n''' \
                    '''    2) Analyze business context: Used for hiring, budgeting, or market analysis.\n''' \
                    '''    3) Analyze stakeholder needs: HR, recruiters, or employees need accurate salary estimates.\n''' \
                    '''    4) Identify desired outcome: Estimate salary for given experience.\n''' \
                    '''    5) Determine task scope: Simple Linear Regression with one feature (experience).\n''' \
                    '''    6) Identify target: Salary (continuous variable).\n''' \
                    '''    7) Identify features: Experience (years of work).\n''' \
                    '''    8) Identify success metrics: – MAE, MSE, or R² for model accuracy.\n'''
                    problem_definition(problem_statement)
                case 2:
                    design_solution()
                case 3:
                    data_collection()
                case 4:
                    data_name, data, (x_train, x_val, x_test, y_train, y_val, y_test) = data_preprocessing()
                    if data is None:
                        print("Failed to load data. Kindly check the file path and format (Process 4)\n")
                        continue
                case 5:
                    if data is not None:
                        EDA(data)
                    else:
                        print("Kindly 1st load data (Process 4)\n")
                case 6:
                    if x_train is not None and x_val is not None and x_test is not None:
                        x_train, x_val, x_test = feature_engineering(x_train, x_val, x_test)
                    else:
                        print("Kindly 1st preprocess data (Process 4)\n")
                case 7:
                    model = ml_model_selection()
                case 8:
                    if x_train is not None and y_train is not None and model is not None:
                        model = ml_model_training(model, x_train, y_train)
                    else:
                        print("Kindly 1st preprocess data and select a model (Processes 4 and 7)\n")
                case 9:
                    if model is not None and x_val is not None and y_val is not None:
                        model = ml_model_tuning(model, x_val, y_val, max_iterations=3)
                    else:
                        print("Kindly 1st preprocess data and train a model (Processes 4 and 8)\n")
                case 10:
                    if model is not None and x_test is not None and y_test is not None:
                        model = ml_model_evaluation(model, x_test, y_test)
                    else:
                        print("Kindly 1st preprocess data and train and tune a model (Processes 4, 8 and 9)\n")
                case 11:
                    if model is not None:
                        ml_model_deployment(model)
                    else:
                        print("Kindly 1st train and tune a model (Processes 8 and 9)\n")
                case 12:
                    ml_model_monitoring_maintenance()
                case 13:
                    print("Exiting from mdlc\n")
                    break
                case _:
                    print("No process is executed...\n")
        
        except ValueError as e:
            print("\nInvalid choice. Please enter an integer for any choice\n")
            continue
        
        while True:
            try:
                #MDLC while loop execution is controlled based on user input
                user_input = input('Do you wish to continue MDLC (yes or no)? ').lower()
                if user_input == 'no':
                    is_running = False
                elif user_input == 'yes':
                    pass
                else:
                    raise ValueError("\nInvalid input. Please enter either yes or no\n")
                break
            except ValueError as e:
                print(e)
