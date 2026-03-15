import re
from datetime import datetime
from dateutil import parser
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def classify_message(message):
    
    # Deadline detection
    try:
        date = parser.parse(message, fuzzy=True)
        hours = (date - datetime.now()).total_seconds() / 3600
        breakpoint()

        if hours >= 24:
            return "deadline", "blue"
        elif hours >= 12:
            return "deadline", "yellow"
        elif hours < 2:
            return "deadline", "orange"
    except:
        pass

    #  Number detection
    numbers = re.findall(r'\d+', message)

    if numbers:
        num = int(numbers[0]) % 100

        if num == 0:
            return "number", "white"
        elif num <= 50:
            return "number", "grey"
        else:
            return "number", "black"
        
    # Sentiment detection
    score = analyzer.polarity_scores(message)['compound']

    if score <  -0.6:
        return "sentiment", "red"
    elif score < -0.2:
        return "sentiment", "lightcoral"
    elif score < 0.2:
        return "sentiment", "orange"
    else:
        return "sentiment", "green"
