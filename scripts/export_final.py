import pandas as pd

df = pd.read_csv("data/cleaned_posts.csv")
df.to_csv("output/final_output.csv", index=False)
print("✅ Final CSV saved to output/final_output.csv")
