import requests
from bs4 import BeautifulSoup

# URL of the news website (You can change this)
url = "https://www.bbc.com/news"

# Step 1: Fetch HTML content
response = requests.get(url)

if response.status_code == 200:
    html = response.text

    # Step 2: Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Extract headlines (many news sites use <h2> tags)
    headlines = soup.find_all("h2")

    # Store extracted text
    extracted_headlines = []

    for h in headlines:
        text = h.get_text(strip=True)
        if text:
            extracted_headlines.append(text)

    # Step 3: Save headlines to a text file
    with open("news_headlines.txt", "w", encoding="utf-8") as f:
        for line in extracted_headlines:
            f.write(line + "\n")

    print("✅ Headlines scraped successfully!")
    print("Saved to: news_headlines.txt")

else:
    print("❌ Failed to retrieve webpage. Status code:", response.status_code)
