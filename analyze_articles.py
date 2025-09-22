import csv
from collections import Counter

keywords = [
    "machine learning", "deep learning", "neural networks", "large language model",
    "LLM", "transformer", "attention mechanism", "transfer learning",
    "reinforcement learning", "RL", "supervised learning", "unsupervised learning",
    
]

def filter_articles_by_keywords(articles, start_year=2020):
    """Filtrer les articles selon les mots-clés et l'année."""
    selected = []
    for article in articles:
        year = article.get("year")
        if not year or year < start_year:
            continue
        text = (article.get("title") or "") + " " + (article.get("abstract") or "")
        if any(keyword.lower() in text.lower() for keyword in keywords):
            selected.append(article)
    return selected

def save_to_csv(articles, filename="data/selected_articles.csv"):
    fieldnames = ["id", "title", "abstract", "year", "doi"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(articles)
    print(f"CSV saved successfully at {filename}")

def yearly_dynamics(articles):
    """Calculer la répartition par année."""
    counter = Counter(a.get("year") for a in articles if a.get("year"))
    print("\nYearly dynamics (selected articles):")
    for year in sorted(counter):
        print(f"  {year}: {counter[year]} articles")
