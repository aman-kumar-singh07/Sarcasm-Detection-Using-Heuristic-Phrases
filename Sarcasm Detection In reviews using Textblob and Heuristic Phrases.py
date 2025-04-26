#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install textblob')


# In[2]:


from textblob import TextBlob

text = "I love this beautiful day!"
blob = TextBlob(text)

print(blob.sentiment)



# In[4]:


import sys
get_ipython().system('{sys.executable} -m pip install textblob')


# In[5]:


from textblob import TextBlob

text = "I love this beautiful day!"
blob = TextBlob(text)
print(blob.sentiment)



# In[6]:


from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    return sentiment, polarity, subjectivity

def detect_sarcasm(text):
    negative_cues = ['not', 'never', 'barely', 'hardly', 'no', 'nothing']
    positive_cues = ['good', 'great', 'love', 'amazing', 'awesome', 'best']
    sarcasm_indicators = ['!!!', '🙄', '😒', 'lol', '...', 'wow']
    
    sarcasm_score = 0
    
    if any(word in text.lower() for word in negative_cues) and any(word in text.lower() for word in positive_cues):
        sarcasm_score += 1
        
    if any(ind in text.lower() for ind in sarcasm_indicators):
        sarcasm_score += 1

    if "food poisoning" in text.lower() or "worst" in text.lower():
        sarcasm_score += 1

    return sarcasm_score >= 2

def analyze_with_sarcasm(text):
    sentiment, polarity, subjectivity = analyze_sentiment(text)
    sarcastic = detect_sarcasm(text)
    
    if sarcastic:
        if sentiment == "Positive":
            sentiment = "Negative"
        elif sentiment == "Negative":
            sentiment = "Positive"
    
    return {
        'text': text,
        'final_sentiment': sentiment,
        'polarity': polarity,
        'subjectivity': subjectivity,
        'sarcastic': sarcastic
    }


review = "Just loved getting food poisoning. Best birthday ever!!!"
result = analyze_with_sarcasm(review)

for key, value in result.items():
    print(f"{key}: {value}")


# In[7]:


from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    return sentiment, polarity, subjectivity

def detect_sarcasm(text):
    negative_cues = ['not', 'never', 'barely', 'hardly', 'no', 'nothing']
    positive_cues = ['good', 'great', 'love', 'amazing', 'awesome', 'best']
    sarcasm_indicators = ['!!!', '🙄', '😒', 'lol', '...', 'wow']
    
    sarcasm_score = 0
    
    if any(word in text.lower() for word in negative_cues) and any(word in text.lower() for word in positive_cues):
        sarcasm_score += 1
        
    if any(ind in text.lower() for ind in sarcasm_indicators):
        sarcasm_score += 1

    if "food poisoning" in text.lower() or "worst" in text.lower():
        sarcasm_score += 1

    return sarcasm_score >= 2

def analyze_with_sarcasm(text):
    sentiment, polarity, subjectivity = analyze_sentiment(text)
    sarcastic = detect_sarcasm(text)
    
    if sarcastic:
        if sentiment == "Positive":
            sentiment = "Negative"
        elif sentiment == "Negative":
            sentiment = "Positive"
    
    return {
        'text': text,
        'final_sentiment': sentiment,
        'polarity': polarity,
        'subjectivity': subjectivity,
        'sarcastic': sarcastic
    }


review = input("Enter what review you wanna give me")
result = analyze_with_sarcasm(review)

for key, value in result.items():
    print(f"{key}: {value}")


# In[12]:


from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    return sentiment, polarity, subjectivity

def detect_sarcasm(text):
    negative_cues = ['not', 'never', 'barely', 'hardly', 'no', 'nothing']
    positive_cues = ['good', 'great', 'love', 'amazing', 'awesome', 'best']
    sarcasm_indicators = ['!!!', '🙄', '😒', 'lol', '...', 'wow']
    
    sarcasm_score = 0
    
    if any(word in text.lower() for word in negative_cues) and any(word in text.lower() for word in positive_cues):
        sarcasm_score += 1
        
    if any(ind in text.lower() for ind in sarcasm_indicators):
        sarcasm_score += 1

    if "food poisoning" in text.lower() or "worst" in text.lower():
        sarcasm_score += 1

    return sarcasm_score >= 2

def analyze_with_sarcasm(text):
    sentiment, polarity, subjectivity = analyze_sentiment(text)
    sarcastic = detect_sarcasm(text)
    
    if sarcastic:
        if sentiment == "Positive":
            sentiment = "Negative"
        elif sentiment == "Negative":
            sentiment = "Positive"
    
    return {
        'text': text,
        'final_sentiment': sentiment,
        'polarity': polarity,
        'subjectivity': subjectivity,
        'sarcastic': sarcastic
    }


review = input("Enter what review you wanna give me")
result = analyze_with_sarcasm(review)

for key, value in result.items():
    print(f"{key}: {value}")


# In[26]:


def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    return sentiment, polarity, subjectivity

def detect_sarcasm(text):

    negative_cues = ['not', 'never', 'barely', 'hardly', 'no', 'nothing', "can't", "won't"]
    positive_cues = ['good', 'great', 'love', 'amazing', 'awesome', 'best']
    sarcasm_indicators = ['!!!', '🙄', '😒', 'lol', '...', 'wow']
    
    sarcasm_score = 0
    
    # Check for both negative and positive cues in the sentence
    if any(word in text.lower() for word in negative_cues) and any(word in text.lower() for word in positive_cues):
        sarcasm_score += 1
        
    # Check for sarcasm indicators (including emojis)
    if any(ind in text.lower() for ind in sarcasm_indicators):
        sarcasm_score += 1

    # Check for common sarcastic phrases (like "can't wait")
    sarcastic_phrases = ["can't wait", "so excited", "best day ever", "just what I needed"]
    if any(phrase in text.lower() for phrase in sarcastic_phrases):
        sarcasm_score += 1

    return sarcasm_score >= 2

def analyze_with_sarcasm(text):
    sentiment, polarity, subjectivity = analyze_sentiment(text)
    sarcastic = detect_sarcasm(text)
    
    if sarcastic:
        if sentiment == "Positive":
            sentiment = "Negative"
        elif sentiment == "Negative":
            sentiment = "Positive"
    
    return {
        'text': text,
        'final_sentiment': sentiment,
        'polarity': polarity,
        'subjectivity': subjectivity,
        'sarcastic': sarcastic
    }

# Test it with your example sentence
review =  "Just loved getting food poisoning. Best birthday ever!!!"
result = analyze_with_sarcasm(review)

for key, value in result.items():
    print(f"{key}: {value}")

