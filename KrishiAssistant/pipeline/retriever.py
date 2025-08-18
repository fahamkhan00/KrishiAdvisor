
import os
import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from models.embedder import get_embedder
from pipeline.smart_mapper import generate_column_mapping


import glob
import os
import pandas as pd
from langchain.docstore.document import Document

def load_data(folder_path="data/"):
    docs = []
    files = glob.glob(os.path.join(folder_path, "*"))

    for file in files:
        print(f"📄 Loading: {file}")
        try:
            if file.endswith(".csv"):
                df = pd.read_csv(file)
            elif file.endswith(".json"):
                df = pd.read_json(file)
            elif file.endswith(".parquet"):
                df = pd.read_parquet(file)
            else:
                print(f"Skipping unsupported file: {file}")
                continue

            # Convert each row to a raw text chunk
            for _, row in df.iterrows():
                row_text = " | ".join([f"{col}: {row[col]}" for col in df.columns if pd.notna(row[col])])
                if row_text:
                    docs.append(Document(page_content=row_text.strip()))

        except Exception as e:
            print(f" Error loading {file}: {e}")

    return docs




def build_or_load_vectorstore(path="vectorstore/"):
    embedder = get_embedder()

    if os.path.exists(path):
        #print(" Loading existing vectorstore...")
        return FAISS.load_local(path, embedder,allow_dangerous_deserialization=True)

    print("🛠️ Building vectorstore...")
    documents = load_data()
    print(f" Total documents loaded: {len(documents)}")
    db = FAISS.from_documents(documents, embeddings)
    db.save_local(path)
    return db
