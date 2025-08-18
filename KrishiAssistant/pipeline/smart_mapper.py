# pipeline/smart_mapper.py

import os
import pandas as pd
import glob

question_keywords = {"question", "query", "q", "ques", "problem", "prompt", "faq"}
answer_keywords = {"answer", "response", "a", "reply", "solution", "explanation"}

def guess_columns(columns):
    question_col = None
    answer_col = None

    for col in columns:
        col_lower = col.lower().strip()
        if not question_col and any(key in col_lower for key in question_keywords):
            question_col = col
        if not answer_col and any(key in col_lower for key in answer_keywords):
            answer_col = col

    return question_col, answer_col

def generate_column_mapping(data_dir="data/"):
    mapping = {}
    all_files = glob.glob(os.path.join(data_dir, "*"))

    for file in all_files:
        try:
            if file.endswith(".csv"):
                df = pd.read_csv(file, nrows=1)
            elif file.endswith(".json"):
                df = pd.read_json(file, nrows=1)
            elif file.endswith(".parquet"):
                df = pd.read_parquet(file, engine="pyarrow").head(1)
            else:
                continue

            q_col, a_col = guess_columns(df.columns)
            if q_col and a_col:
                mapping[file] = {"question": q_col, "answer": a_col}
                print(f" Mapped: {os.path.basename(file)} → Q: {q_col}, A: {a_col}")
            else:
                print(f"Skipped (no match): {file} → {list(df.columns)}")

        except Exception as e:
            print(f" Error reading {file}: {e}")

    return mapping
