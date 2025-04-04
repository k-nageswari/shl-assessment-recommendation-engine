import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = pd.read_csv("shl_catalogue.csv")
df.fillna("", inplace=True)
df["combined_text"] = df["Assessment Name"] + " " + df["Description"] + " " + df["Category"] + " " + df["Target Job Role"]

# TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df["combined_text"])

def recommend_assessments(query, top_n=5):
    query_vec = vectorizer.transform([query])
    similarity = cosine_similarity(query_vec, tfidf_matrix)
    top_indices = similarity.argsort()[0][-top_n:][::-1]
    top_scores = similarity[0][top_indices]

    results = df.iloc[top_indices].copy()
    results["Score"] = (top_scores * 100).round(2)  # Show % match
    return results[["Assessment Name", "Description", "Category", "Target Job Role", "Score"]]

