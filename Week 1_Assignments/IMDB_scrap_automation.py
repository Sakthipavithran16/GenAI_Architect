from playwright.sync_api import sync_playwright
import re

def scrape_imdb_top_10():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open IMDb Top 250 directly (most stable)
        page.goto("https://www.imdb.com/chart/top/", timeout=60000)

        # Wait for movie items to load
        page.wait_for_function(
            "document.querySelectorAll('li.ipc-metadata-list-summary-item').length >= 10"
        )

        movie_data = []

        for i in range(10):
            movie = page.locator("li.ipc-metadata-list-summary-item").nth(i)

            # Title
            title = movie.locator("h3").inner_text()

            # Year (robust: first 4-digit number)
            metadata_text = movie.inner_text()
            year_match = re.search(r"\b(19|20)\d{2}\b", metadata_text)
            year = year_match.group(0) if year_match else "N/A"

            # Rating
            rating = movie.locator("span.ipc-rating-star--rating").inner_text()

            movie_data.append(
                f"{i+1}. {title} ({year}) - Rating: {rating}"
            )

        # Save to text file
        with open("imdb_top_10_movies.txt", "w", encoding="utf-8") as file:
            for movie in movie_data:
                file.write(movie + "\n")

        print("✅ Scraping completed successfully")
        print("📁 Saved as imdb_top_10_movies.txt")

        browser.close()

if __name__ == "__main__":
    scrape_imdb_top_10()
