import nltk
import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Download required NLP data
nltk.download('stopwords')
nltk.download('wordnet')


# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    """
    Cleans and prepares text for chatbot processing
    """

    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Split sentence into words
    words = text.split()

    # Remove common words
    stop_words = set(stopwords.words("english"))

    words = [
        word for word in words 
        if word not in stop_words
    ]

    # Convert words to base form
    words = [
        lemmatizer.lemmatize(word)
        for word in words
    ]

    return " ".join(words)