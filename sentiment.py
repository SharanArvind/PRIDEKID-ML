import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

student_responses = [
    ("The exam was challenging but fair. I feel confident about my answers.", "positive"),
    ("I struggled a lot with this exam. It was too difficult.", "negative"),
    ("I did not do the exam well", "negative"),
    ("The exam was okay. Neither too easy nor too hard.", "neutral"),
    ("I found the exam quite easy. I finished it quickly with no major issues.", "positive"),
    ("This exam was a disaster. I couldn't understand most of the questions.", "negative"),
    ("The exam was well-structured, and I managed to answer all questions comfortably.", "positive"),
    ("I felt unprepared for this exam. The questions were too tricky.", "negative"),
    ("The exam seemed fair, but I made a few mistakes due to time pressure.", "neutral"),
    ("I am satisfied with my performance in the exam. It was challenging, but I believe I did well overall.", "positive"),
    ("I'm disappointed with my performance. The exam was harder than I expected, and I struggled to answer some questions.", "negative"),
    ("The exam went smoothly for me. I was well-prepared and managed my time effectively.", "positive"),
    ("I felt overwhelmed during the exam. The questions were too complex, and I couldn't focus properly.", "negative"),
    ("The exam was average. I didn't find it too difficult or too easy.", "neutral"),
    ("I'm pleased with my performance. The exam covered topics I studied thoroughly.", "positive"),
    ("I'm frustrated with my performance. Despite studying hard, I couldn't answer many questions.", "negative"),
    ("The exam was straightforward. I was able to answer all questions without much difficulty.", "positive"),
    ("I struggled with the exam due to lack of preparation. I regret not studying more.", "negative"),
    ("The exam was fair, but I made careless errors that affected my score.", "neutral"),
    ("I'm happy with my performance. I approached the exam with a positive mindset and it paid off.", "positive"),
    ("I'm upset about my performance. I faced unexpected challenges during the exam.", "negative"),
   
]


# Initialize Lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Preprocessing function
def preprocess_text(text):
    tokens = word_tokenize(text.lower())  # Tokenization and lowercase
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]  # Lemmatization
    tokens = [token for token in tokens if token not in stop_words]  # Remove stopwords
    return " ".join(tokens)

# Preprocess the dataset
preprocessed_responses = [(preprocess_text(response), sentiment) for response, sentiment in student_responses]

# Extract features using TF-IDF vectorization
vectorizer = TfidfVectorizer(max_features=5000)  # Limit features to avoid overfitting
X = vectorizer.fit_transform([response for response, _ in preprocessed_responses])
y = [sentiment for _, sentiment in preprocessed_responses]

# Train the classifier
classifier = MultinomialNB()
classifier.fit(X, y)

# Get input from the user
user_input = input("Enter the student response: ")

# Preprocess the user input
preprocessed_input = preprocess_text(user_input)

# Vectorize the preprocessed input
X_user = vectorizer.transform([preprocessed_input])

# Predict the sentiment
prediction = classifier.predict(X_user)

print("Predicted sentiment:", prediction[0])
