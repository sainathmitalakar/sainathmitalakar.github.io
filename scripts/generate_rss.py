from bs4 import BeautifulSoup
from datetime import datetime
import html

# -------------- CONFIGURATION ----------------
SITE_URL = "https://sainathmitalakar.github.io"
RSS_FILE = "rss.xml"
# ---------------------------------------------

# Load index.html
with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Select all blog articles
articles = soup.select("#blog-posts article")

# Function to parse date
def parse_date(art):
    time_tag = art.find("time")
    if time_tag and 'datetime' in time_tag.attrs:
        return datetime.strptime(time_tag['datetime'], "%Y-%m-%d")
    return datetime.now()

# Sort articles newest first
articles = sorted(articles, key=parse_date, reverse=True)

items = []
for idx, art in enumerate(articles, 1):
    title_tag = art.find("h2")
    time_tag = art.find("time")
    p_tags = art.find_all("p")
    
    # Get title
    title = html.escape(title_tag.text.strip()) if title_tag else f"Blog {idx}"
    
    # Get description (first 2 paragraphs)
    description = " ".join(html.escape(p.text.strip()) for p in p_tags[:2])
    
    # Date
    date_text = time_tag['datetime'] if time_tag else datetime.now().strftime("%Y-%m-%d")
    pub_date = datetime.strptime(date_text, "%Y-%m-%d").strftime("%a, %d %b %Y %H:%M:%S +0530")
    
    # Unique slug for link and guid
    slug = "-".join(title.lower().split())
    link = f"{SITE_URL}/#blog-{slug}"
    guid = link
    
    # Build item
    items.append(f"""
    <item>
      <title>{title}</title>
      <link>{link}</link>
      <description>{description}</description>
      <pubDate>{pub_date}</pubDate>
      <guid>{guid}</guid>
    </item>
""")

# Full RSS content with self-link
rss_content = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
<title>Sainath Mitalakar Portfolio Blogs</title>
<link>{SITE_URL}</link>
<description>Latest blogs from Sainath Shivaji Mitalakar</description>
<language>en-us</language>
<atom:link href="{SITE_URL}/rss.xml" rel="self" type="application/rss+xml" />
{''.join(items)}
</channel>
</rss>
"""

# Write to rss.xml
with open(RSS_FILE, "w", encoding="utf-8") as f:
    f.write(rss_content)

print(f"RSS feed generated: {RSS_FILE}")
