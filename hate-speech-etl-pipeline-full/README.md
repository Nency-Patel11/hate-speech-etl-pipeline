# Hate-Speech ETL Pipeline (Python + NLP)

A complete **end-to-end ETL (Extract → Transform → Load) pipeline** that collects social media posts, cleans the text, classifies toxicity using NLP, stores the results in a SQLite database, and exports a final CSV for further analysis.

This project is designed for students or aspiring **Data Engineers / NLP practitioners** to showcase skills in Python, NLP, ETL pipelines, and database management.

---

## 🚀 Features

- **Extract**: Collects posts from social media (placeholder Reddit/Twitter posts).
- **Transform**: Cleans text by removing special characters, links, and extra spaces.
- **Classify Toxicity**: Uses `TextBlob` sentiment analysis to classify posts as `toxic`, `neutral`, or `positive`.
- **Load**: Stores cleaned and classified data into a **SQLite database**.
- **Export**: Generates a final CSV report for easy analysis.
- **Modular Design**: Separate scripts for each ETL step, making it **easy to extend** or replace with real APIs.

---

## 📁 Project Structure

hate-speech-etl-pipeline-full/
│
├─ data/ # Raw and cleaned CSV files
├─ scripts/ # Python scripts for each ETL step
├─ database/ # SQLite database storage
├─ output/ # Final CSV output
└─ README.md # Project documentation

yaml
Copy code

---

## ⚙️ How to Run

1. Clone or download the repository.
2. Navigate into the project folder:

```bash
cd hate-speech-etl-pipeline-full
Install required Python packages:

bash
Copy code
pip install pandas textblob requests beautifulsoup4
Download TextBlob corpora:

bash
Copy code
python -m textblob.download_corpora
Run the ETL pipeline:

bash
Copy code
python scripts/run_pipeline.py
Check the final output:

bash
Copy code
output/final_output.csv

##🛠 Technology Stack
Python: Core programming language

TextBlob: NLP sentiment analysis

Pandas: Data manipulation

SQLite: Database storage

CSV: Data export for easy analysis

##💡 Potential Extensions
Replace placeholder data with real Reddit or Twitter API data.

Improve toxicity classification using transformer-based models (BERT, RoBERTa).

Integrate with cloud storage like AWS S3 or Google Cloud for scalability.

Add visualizations or dashboards for interactive reporting.
