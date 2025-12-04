

import pandas as pd
import re
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
from flask import Flask, render_template, request
import os
df = pd.read_csv("my_qna_dataset.csv")  # Make sure this file exists

def clean_text(text):
    if isinstance(text, str):
        text = re.sub(r'[^A-Za-z0-9\s]', '', text)  # remove symbols
        text = text.lower().strip()
    else:
        text = ''
    return text

df['Question'] = df['Question'].apply(clean_text)
df['Answer'] = df['Answer'].apply(clean_text)

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
question_embeddings = model.encode(df['Question'].tolist())

d = question_embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(np.array(question_embeddings))

faiss.write_index(index, "qna_faiss.index")

def retrieve_answers(query, model, index, df, k=5):
    query_vec = model.encode([clean_text(query)])
    distances, indices = index.search(query_vec, k)
    
    results = []
    for i in range(k):
        results.append({
            "Answer": df['Answer'].iloc[indices[0][i]],
            "Distance": distances[0][i]
        })
    return results

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    answers = []
    if request.method == "POST":
        query = request.form['query']
        answers = retrieve_answers(query, model, index, df, k=5)
    return render_template("index.html", answers=answers)

if __name__ == "__main__":

    if not os.path.exists("templates"):
        os.makedirs("templates")

    if not os.path.exists("templates/index.html"):
        with open("templates/index.html", "w") as f:
            f.write("""
<!DOCTYPE html>
<html>
<head>
    <title>QnA Bot</title>
</head>
<body>
    <h1>My QnA Bot</h1>
    <form method="POST">
        <input type="text" name="query" placeholder="Ask a question..." required>
        <input type="submit" value="Ask">
    </form>
    <h2>Answers:</h2>
    {% for item in answers %}
        <p><strong>{{ loop.index }}.</strong> {{ item['Answer'] }} (Distance: {{ item['Distance'] }})</p>
    {% endfor %}
</body>
</html>
""")
    app.run(debug=True)
