import sqlite3
import pandas as pd

conn = sqlite3.connect("database/posts.db")
df = pd.read_csv("data/cleaned_posts.csv")
df.to_sql("posts", conn, if_exists="replace", index=False)
conn.close()
print("✅ Loaded into SQLite database.")
