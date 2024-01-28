from tensorflow import keras
from Feature_Extractor import extract_features

# Threshold value for classifying as malicious
threshold = 50.0  # Adjust this threshold as needed

# This function takes the url and returns a classification
def get_prediction(url, model_path):
    print("Loading the model...")
    model = keras.models.load_model(model_path)

    print("Extracting features from url...")
    url_features = extract_features(url)
    print(url_features)

    print("Making prediction...")
    prediction = model.predict([url_features])

    probability = prediction[0][0] * 100
    probability = round(probability, 3)
    print("There is a", probability, "% chance that the URL is malicious.")

    # Classify as malicious if probability exceeds the threshold
    if probability >= threshold:
        return "Malicious"
    else:
        return "Not Malicious"

# Example usage:
model_path = "prediction.h5"
url = "https://metumaskilogin.godaddysites.com/"
result = get_prediction(url, model_path)
print("URL is:", result)
