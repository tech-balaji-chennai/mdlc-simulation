#8) ml model training - training ml model

#importing packages directly on top of the program


def ml_model_training(model, x_train, y_train):
    model.fit(x_train, y_train)
    print("Model is trained successfully\n")
    return model
