
# News Classifier

This project is a web application built using Flask that classifies news articles as either "Fake News" or "True News" using several machine learning models.

## Requirements

You can install the required packages using pip:

```bash
pip install flask pandas scikit-learn joblib
```

## Setup

### Train the Models

First, you need to train and save the models by running `train_models.py`. This script will generate the model files and the TF-IDF vectorizer.

```bash
python train_models.py
```

### Run the Flask Application

After training the models, run the Flask application using `app.py` to start the web server.

```bash
python app.py
```

By default, the Flask server will be accessible at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage

1. Open your web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).
2. Enter a news article in the text area and click the "Classify" button.
3. The application will display predictions from different models, indicating whether the news is classified as "Fake News" or "True News".

## Example

![Example Screenshot](https://via.placeholder.com/800x600.png?text=Example+Screenshot)  
*(Replace with an actual screenshot of your application)*

## Notes

- Ensure that the dataset files `Fake.csv` and `True.csv` are in the same directory as `train_models.py`.
- The models and vectorizer files (`.pkl`) must be in the same directory as `app.py` for the Flask application to function correctly.
- Modify the `index.html` file in the `templates` folder to customize the look and feel of the web interface.

## Acknowledgements

- This project uses scikit-learn for machine learning and Flask for the web framework.
- Thanks to the developers and contributors of these libraries for their valuable work.

---

Feel free to contribute to this project by submitting issues or pull requests.
```

### Explanation of Sections:

- **Requirements**: Lists the necessary packages and installation command.
- **Setup**: Provides instructions on how to train models and run the Flask application.
- **Usage**: Details how to interact with the web application.
- **Example**: Placeholder for a screenshot of the application in use.
- **Notes**: Additional details about dataset and file locations.
- **Acknowledgements**: Credits to libraries and contributors.

Replace the placeholder screenshot URL with an actual screenshot of your application if you have one.
