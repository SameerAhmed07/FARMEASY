# train_models.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import joblib
from data_preprocess import preprocess_data

def train_crop_recommendation_model(crop_data):
    # Features and target for crop recommendation
    X = crop_data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    y = crop_data['label']

    # Define the RandomForestClassifier model
    model = RandomForestClassifier(random_state=42)

    # Hyperparameter tuning
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
    grid_search.fit(X, y)

    return grid_search.best_estimator_

def train_fertilizer_recommendation_model(fertilizer_data):
    # Features and target for fertilizer recommendation
    X = fertilizer_data[['Soil Type', 'Crop Type', 'Nitrogen', 'Phosphorous', 'Potassium']]
    y = fertilizer_data['Fertilizer Name']

    # Define the RandomForestClassifier model
    model = RandomForestClassifier(random_state=42)

    # Hyperparameter tuning
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
    grid_search.fit(X, y)

    return grid_search.best_estimator_

if __name__ == "__main__":
    # Preprocess data
    crop_data, fertilizer_data, le_crop, le_soil = preprocess_data()

    # Train models
    crop_model = train_crop_recommendation_model(crop_data)
    fertilizer_model = train_fertilizer_recommendation_model(fertilizer_data)

    # Save the models
    joblib.dump(crop_model, 'crop_model.pkl')
    joblib.dump(fertilizer_model, 'fertilizer_model.pkl')

    # Save LabelEncoders for later use
    joblib.dump(le_crop, 'le_crop.pkl')
    joblib.dump(le_soil, 'le_soil.pkl')
