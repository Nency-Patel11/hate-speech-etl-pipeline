import os

print("\n🚀 Starting ETL Pipeline...\n")
os.system("python scripts/extract_posts.py")
os.system("python scripts/clean_and_classify.py")
os.system("python scripts/load_to_sqlite.py")
os.system("python scripts/export_final.py")
print("\n✅ ETL Pipeline Complete!")
