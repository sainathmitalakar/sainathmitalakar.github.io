from bs4 import BeautifulSoup
from datetime import datetime
import html

SITE_URL = "https://sainathmitalakar.github.io"
RSS_FILE = "rss.xml"

# Open index.html
with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find all blog articles
articles = soup.select("#blog-posts article")

# Sort articles by date (newest first)
def parse_date(art):
    time_tag = art.find("time")
    if time_tag and 'datetime' in time_tag.attrs:
        return datetime.strptime(time_tag['datetime'], "%Y-%m-%d")
    return datetime.now()

articles = sorted(articles, key=parse_date, reverse=True)

items = []
for art in articles:
    title_tag = art.find("h2")
    time_tag = art.find("time")
    p_tags = art.find_all("p")
    
    title = html.escape(title_tag.text.strip()) if title_tag else "Untitled Blog"
    date_text = time_tag['datetime'] if time_tag else datetime.now().strftime("%Y-%m-%d")
    description = " ".join(html.escape(p.text.strip()) for p in p_tags[:2])  # first 2 paragraphs
    link = f"{SITE_URL}/#blog-section"
    pub_date = datetime.strptime(date_text, "%Y-%m-%d").strftime("%a, %d %b %Y %H:%M:%S +0530")
    
    items.append(f"""
    <item>
      <title>{title}</title>
      <link>{link}</link>
      <description>{description}</description>
      <pubDate>{pub_date}</pubDate>
      <guid>{link}</guid>
    </item>
""")

rss_content = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
<title>Sainath Mitalakar Portfolio Blogs</title>
<link>{SITE_URL}</link>
<description>Latest blogs from Sainath Shivaji Mitalakar</description>
<language>en-us</language>
{''.join(items)}
</channel>
</rss>
"""

with open(RSS_FILE, "w", encoding="utf-8") as f:
    f.write(rss_content)

print(f"RSS feed generated: {RSS_FILE}")
