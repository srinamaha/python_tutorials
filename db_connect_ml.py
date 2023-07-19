import psycopg2
import joblib
import nltk
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer

# ... Same preprocessing and ML model training as in the previous example ...

import nltk
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample incident data and categories
incident_data = [
    ("Printer not working", "Hardware"),
    ("Software application crashed", "Software"),
    ("Email server down", "Network"),
    ("Slow response time on website", "Performance"),
    # Add more incidents and corresponding categories as needed
]

# Tokenize and preprocess incident descriptions
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    words = word_tokenize(text.lower())
    return ' '.join([w for w in words if w.isalpha() and w not in stop_words])

preprocessed_data = [(preprocess_text(desc), category) for desc, category in incident_data]

# Split data into training and testing sets
random.shuffle(preprocessed_data)
train_data = preprocessed_data[:int(0.8 * len(preprocessed_data))]
test_data = preprocessed_data[int(0.8 * len(preprocessed_data)):]

# Feature extraction using Bag-of-Words model
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform([desc for desc, _ in train_data])
X_test = vectorizer.transform([desc for desc, _ in test_data])

# Train the Naive Bayes classifier
y_train = [category for _, category in train_data]
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Function to predict category for new incident descriptions
def predict_category(incident_description):
    preprocessed_description = preprocess_text(incident_description)
    X_new = vectorizer.transform([preprocessed_description])
    return classifier.predict(X_new)[0]

# Example usage
new_incident_description = "Printer is not printing anything."
predicted_category = predict_category(new_incident_description)
print(f"Predicted category for the incident: {predicted_category}")

# ... Same preprocessing and ML model training as in the previous example ...
#####################################

# Connect to the PostgreSQL database (replace placeholders with actual connection details)
connection = psycopg2.connect(
    database="your_db_name",
    user="your_db_user",
    password="your_db_password",
    host="your_db_host",
    port="your_db_port"
)

def fetch_incident_descriptions_from_db():
    # Write SQL query to fetch incident descriptions from the database
    # Implement the actual query based on your database schema
    with connection.cursor() as cursor:
        cursor.execute("SELECT incident_description FROM incidents_table")
        incident_descriptions = cursor.fetchall()
    return [desc[0] for desc in incident_descriptions]

def update_incident_categories_in_db(incident_ids, predicted_categories):
    # Write SQL query to update the predicted categories in the database
    # Implement the actual query based on your database schema
    with connection.cursor() as cursor:
        for incident_id, category in zip(incident_ids, predicted_categories):
            cursor.execute("UPDATE incidents_table SET predicted_category = %s WHERE incident_id = %s", (category, incident_id))
        connection.commit()

# Fetch incident descriptions from the database
incident_descriptions = fetch_incident_descriptions_from_db()

# Predict incident categories using the ML model
predicted_categories = [predict_category(desc) for desc in incident_descriptions]

# Update the database with predicted incident categories
incident_ids = [incident_id for incident_id in range(1, len(incident_descriptions) + 1)]  # Replace with actual incident IDs
update_incident_categories_in_db(incident_ids, predicted_categories)

# Close the database connection
connection.close()
