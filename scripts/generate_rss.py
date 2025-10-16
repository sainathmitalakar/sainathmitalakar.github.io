from bs4 import BeautifulSoup
from datetime import datetime
import xml.etree.ElementTree as ET

# ------------------- CONFIG -------------------
INDEX_HTML_FILE = "index.html"
RSS_FILE = "rss.xml"
SITE_URL = "https://sainathmitalakar.github.io"
FEED_TITLE = "Sainath Mitalakar Portfolio Blogs"
FEED_DESC = "Latest blogs from Sainath Shivaji Mitalakar"
FEED_LANG = "en-us"
# ----------------------------------------------

# Load and parse index.html
with open(INDEX_HTML_FILE, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

articles = soup.find_all("article")

# Create RSS structure
rss = ET.Element("rss", version="2.0")
channel = ET.SubElement(rss, "channel")
ET.SubElement(channel, "title").text = FEED_TITLE
ET.SubElement(channel, "link").text = SITE_URL
ET.SubElement(channel, "description").text = FEED_DESC
ET.SubElement(channel, "language").text = FEED_LANG

for article in articles:
    # Unique article ID
    article_id = article.get("id", "")
    if not article_id:
        continue  # skip if no id

    title_tag = article.find("h2")
    time_tag = article.find("time")
    description_tag = article.find_all("p")

    # Extract data
    title = title_tag.get_text(strip=True) if title_tag else "No Title"
    pub_date = time_tag.get("datetime") if time_tag else datetime.now().strftime("%Y-%m-%d")
    description = " ".join(p.get_text(strip=True) for p in description_tag)
    link = f"{SITE_URL}/#{article_id}"

    # Format pubDate in RFC 2822 format
    pub_date_rfc2822 = datetime.strptime(pub_date, "%Y-%m-%d").strftime("%a, %d %b %Y %H:%M:%S +0530")

    # Create RSS item
    item = ET.SubElement(channel, "item")
    ET.SubElement(item, "title").text = title
    ET.SubElement(item, "link").text = link
    ET.SubElement(item, "description").text = description
    ET.SubElement(item, "pubDate").text = pub_date_rfc2822
    ET.SubElement(item, "guid").text = link  # unique guid for each blog

# Write RSS file
tree = ET.ElementTree(rss)
tree.write(RSS_FILE, encoding="utf-8", xml_declaration=True)

print(f"RSS feed generated successfully: {RSS_FILE}")
