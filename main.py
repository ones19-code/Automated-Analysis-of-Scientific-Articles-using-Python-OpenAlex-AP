from fetch_articles import fetch_articles
from analyze_articles import filter_articles_by_keywords, save_to_csv
from collections import Counter

def main():
    print("="*60)
    print("Starting OpenAlex keyword analysis...\n")

    # openales urls 
    journals = {
        "Scientometrics": "https://api.openalex.org/works?filter=title_and_abstract.search:Scientometrics,type:article",
        "Quantitative Science Studies": "https://api.openalex.org/works?filter=title_and_abstract.search:Quantitative+Science+Studies,type:article",
        "Journal of Informetrics": "https://api.openalex.org/works?filter=title_and_abstract.search:Journal+of+Informetrics,type:article"
    }

    all_articles = []
    for journal_name, journal_url in journals.items():
        print(f"Collecting articles from {journal_name}...")
        articles = fetch_articles(journal_url)
        print(f"  -> Total articles collected: {len(articles)}\n")
        all_articles.extend(articles)

    print("="*60)
    print(f"Total articles retrieved (all years): {len(all_articles)}")

   
    selected = filter_articles_by_keywords(all_articles)

   
    selected_2020_plus = [a for a in selected if a.get("year") and a["year"] >= 2020]

    print(f"Articles with keywords (from 2020 onwards): {len(selected_2020_plus)} ({len(selected_2020_plus)/len(all_articles)*100:.2f}%)\n")

    # Dynamique annuelle
    if selected_2020_plus:
        year_counts = Counter(a["year"] for a in selected_2020_plus if a.get("year"))
        print("Yearly dynamics (selected articles):")
        print("-"*30)
        print(f"{'Year':<10}{'Count':<10}")
        print("-"*30)
        for year in sorted(year_counts):
            print(f"{year:<10}{year_counts[year]:<10}")
        print("-"*30)
    else:
        print("No articles with keywords from 2020 onwards.")

   
    save_to_csv(selected_2020_plus)
    print("="*60)

if __name__ == "__main__":
    main()
