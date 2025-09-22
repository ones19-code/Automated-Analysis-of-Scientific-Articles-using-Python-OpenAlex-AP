import requests
import time


EMAIL = "otalbi@constructor.university"

def fetch_articles(journal_url, max_pages=5):
    """Fetch articles from OpenAlex API given the journal search URL."""
    all_articles = []

    headers = {
        "User-Agent": f"PythonOpenAlexApp ({EMAIL})"
    }

    for page in range(1, max_pages + 1):
        url = f"{journal_url}&page={page}"
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                works = data.get("results", [])
                for work in works:
                    all_articles.append({
                        "id": work.get("id"),
                        "title": work.get("title"),
                        "abstract": work.get("abstract"),
                        "year": work.get("publication_year"),
                        "doi": work.get("doi")
                    })
            else:
                print(f"Error fetching data from {journal_url}: HTTP {response.status_code}")
        except Exception as e:
            print(f"Exception occurred: {e}")
        time.sleep(1)  # éviter de spammer l'API

    return all_articles
