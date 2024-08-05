# News Classifier

This project is a web application built using Flask that classifies news articles as either "Fake News" or "True News" using several machine learning models. The models are trained on a dataset of news articles and are able to make predictions based on the provided input.

## Project Structure

- `train_models.py`: Script to train and save the machine learning models and vectorizer.
- `app.py`: Flask application script that loads the trained models and serves the web interface.
- `templates/index.html`: HTML template for the user interface.
- `LR_model.pkl`: Saved Logistic Regression model.
- `DT_model.pkl`: Saved Decision Tree model.
- `GB_model.pkl`: Saved Gradient Boosting model.
- `RF_model.pkl`: Saved Random Forest model.
- `vectorizer.pkl`: Saved TF-IDF Vectorizer.

## Requirements

- Python 3.12 or higher
- Flask
- pandas
- scikit-learn
- joblib

You can install the required packages using pip:

pip install flask pandas scikit-learn joblib

Setup
Train the Models:

First, you need to train and save the models by running train_models.py. This script will generate the model files and the TF-IDF vectorizer.
python train_models.py

Run the Flask Application:

After training the models, run the Flask application using app.py to start the web server.
python app.py

By default, the Flask server will be accessible at http://127.0.0.1:5000.

Usage
Open your web browser and navigate to http://127.0.0.1:5000.
Enter a news article in the text area and click the "Classify" button.
The application will display predictions from different models, indicating whether the news is classified as "Fake News" or "True News".
Example
 (Replace with an actual screenshot of your application)

Notes
Ensure that the dataset files Fake.csv and True.csv are in the same directory as train_models.py.
The models and vectorizer files (.pkl) must be in the same directory as app.py for the Flask application to function correctly.
Modify the index.html file in the templates folder to customize the look and feel of the web interface.

Acknowledgements
This project uses scikit-learn for machine learning and Flask for the web framework.
Thanks to the developers and contributors of these libraries for their valuable work.
