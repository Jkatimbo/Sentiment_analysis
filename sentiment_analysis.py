from textblob import TextBlob

def get_sentiment(text):
    """
    Determine the sentiment of a given text.

    Parameters:
    text (str): The text to analyze.

    Returns:
    str: The sentiment of the text ('positive', 'neutral', 'negative').
    """
    analysis = TextBlob(text)  # Perform sentiment analysis using TextBlob
    if analysis.sentiment.polarity > 0:
        return 'positive'  # Return 'positive' if polarity is greater than 0
    elif analysis.sentiment.polarity == 0:
        return 'neutral'  # Return 'neutral' if polarity is 0
    else:
        return 'negative'  # Return 'negative' if polarity is less than 0
