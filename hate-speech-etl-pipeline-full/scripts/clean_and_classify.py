import pandas as pd
import re
from textblob import TextBlob

def clean_text(t):
    t = t.lower()
    t = re.sub(r"[^a-zA-Z\s]", "", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()

def classify(t):
    polarity = TextBlob(t).sentiment.polarity
    if polarity <= -0.3:
        return "toxic"
    elif polarity >= 0.3:
        return "positive"
    return "neutral"

if __name__ == "__main__":
    df = pd.read_csv("data/raw_posts.csv")
    df["cleaned"] = df["post_text"].apply(clean_text)
    df["toxicity"] = df["cleaned"].apply(classify)
    df.to_csv("data/cleaned_posts.csv", index=False)
    print("✅ Cleaned + classified posts saved.")
