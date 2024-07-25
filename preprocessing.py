import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Define the set of stop words
stop_words = set(stopwords.words('english'))

def preprocess(text):
    """
    Preprocess the text by cleaning and tokenizing.

    Parameters:
    text (str): The text to preprocess.

    Returns:
    str: The cleaned and tokenized text.
    """
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)  # Remove mentions
    text = re.sub(r'#', '', text)  # Remove hashtag symbols
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    words = word_tokenize(text)  # Tokenize the text
    words = [word.lower() for word in words if word.lower() not in stop_words]
