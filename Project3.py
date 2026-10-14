# Web Scraper for Article Title and Summary
import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return f"Failed to retrieve page (Status Code: {response.status_code})"
        
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract Title
    title = soup.find("h1").get_text(strip=True) if soup.find("h1") else "No title found"
    
    # Extract Paragraphs
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
    body_text = "\n\n".join(paragraphs[:3])  # First 3 paragraphs
    
    return f"TITLE: {title}\n\nSUMMARY/PREVIEW:\n{body_text}"