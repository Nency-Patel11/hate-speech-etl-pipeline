import pandas as pd

def extract_posts():
    # Placeholder extractor
    data = [
        "I love this product!",
        "This is terrible and stupid.",
        "Amazing experience!",
        "You are dumb."
    ]
    df = pd.DataFrame({"post_text": data})
    df.to_csv("data/raw_posts.csv", index=False)
    print("✅ Extracted posts to data/raw_posts.csv")

if __name__ == "__main__":
    extract_posts()
