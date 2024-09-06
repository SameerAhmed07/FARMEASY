# FARMEASY
## PROJECT OVERVIEW
FARMEASY is a machine learning-based crop and fertilizer recommendation system designed to help farmers optimize their farming practices. Based on environmental inputs such as soil properties, nitrogen levels, and weather conditions, the system suggests the most suitable crop and fertilizer for a given piece of land.

The application is built using machine learning models trained on agricultural data and provides predictions via an intuitive web interface developed with Streamlit.

## Features

- Crop Recommendation: Predicts the most suitable crop based on nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall inputs.
- Fertilizer Recommendation: Provides recommendations on the best fertilizer to use based on the soil type, crop type, and nutrient levels.
- Incorporated hyperparameter limits from the TNAU Agritech Portal to enhance prediction precision.
- User-Friendly Interface: Powered by Streamlit, providing a simple and intuitive interface for farmers and users.

## DATASETS USED

This project uses two main datasets:

 - [crop_recomendation.csv](https://github.com/SameerAhmed07/FARMEASY/blob/main/crop_recommendation.csv)

 - [fertilizer Prediction .csv](https://github.com/SameerAhmed07/FARMEASY/blob/main/Fertilizer%20Prediction.csv)

## INSTALLATION

### Prerequisites
- Python 3.0
- Required Python libraries (listed in requirements.txt)

### steps

### 1.Clone the repository:

```bash
  git clone https://github.com/SameerAhmed07/FARMEASY.git
cd FARMEASY

```
### 2.Install dependencies:
```bash
  pip install -r requirements.txt

```
### 3.Place the dataset files:
- Download the datasets ([crop_recomendation.csv](https://github.com/SameerAhmed07/FARMEASY/blob/main/crop_recommendation.csv), [Fertilizer Prediction.csv](https://github.com/SameerAhmed07/FARMEASY/blob/main/Fertilizer%20Prediction.csv)).
- Place them in the root directory of the project.

### 4.Preprocess the data and train the models:
 Preprocess the data using data_preprocess.py.
 ```bash
  python data_preprocess.py
```
### 4.Train the models using model.py.
```bash
  python model.py
```
## Usage
### Crop Recommendation
- Navigate to the Crop Recommendation section.
- Input values for Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, and Rainfall.
- Click Predict Crop to get the recommended crop based on the provided inputs.
- If any values are out of the optimal range, the app will provide warnings and suggest possible corrections.
  
### Fertilizer Recommendation
- Navigate to the Fertilizer Recommendation section.
- Select the Crop Type and Soil Type from the dropdown menus.
- Input values for Nitrogen, Phosphorus, and Potassium.
- Click Predict Fertilizer to get the recommended fertilizer based on the provided inputs.
  
### Input References
- Provides a reference guide for the ranges of input values like Nitrogen, Phosphorus, Potassium, pH, Temperature, Humidity, and Rainfall.
- Helps users to understand the input ranges and their implications.
- The threshold values are taken from TNAU AGRI TECH portal.
  
### Suggestions
- Offers suggestions for optimizing input values based on agricultural best practices.
- Useful for fine-tuning inputs for better crop and fertilizer recommendations.

## Web App Pages
- Home: Introduction to EASYFARM.
- Crop Recommendation: Enter parameters to get a crop recommendation.
- Fertilizer Recommendation: Enter soil and nutrient data to get a fertilizer recommendation.
- Input References: Displays input value ranges for nitrogen, phosphorus, potassium, pH, temperature, humidity, and rainfall.
- Suggestions: Shows suggestions for optimizing input values.

## Input Thresholds
Input validation is applied to ensure values fall within acceptable ranges. For example:

- Nitrogen (N): Max 150 Kg/ha
- Phosphorus (P): Max 200 Kg/ha
- Potassium (K): Max 250 Kg/ha
- pH: Acceptable range between 6.0 and 8.5
- Temperature: Between 15°C and 35°C
- Humidity: Between 40% and 70%
- Rainfall: Between 500 mm/year and 1500 mm/year

## Technologies Used
- Python 3.0
- Streamlit: For building the web application.
- scikit-learn: For training the machine learning models.
- Pandas: For data manipulation and preprocessing.
- Joblib: For saving and loading machine learning models.
- RandomForestClassifier: For both crop and fertilizer prediction.

## Contributing
Contributions are welcome! Here's how you can help:
- Fork the repository.
- Create a new branch for your feature or bugfix.
- Commit your changes.
- Open a pull request with a detailed description.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/SameerAhmed07/FARMEASY?tab=MIT-1-ov-file) file for details.

