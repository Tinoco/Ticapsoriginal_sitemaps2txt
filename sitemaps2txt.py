# TQDM PROGRESS BAR
from tqdm import tqdm

# IDENTIFY LARGE XML FILE
import advertools as adv

# REQUEST TO GET RESPONSES
import requests

# INDEXING YOUR LARGE SITEMAPS
sitemap = adv.sitemap_to_df("https://ticapsoriginal.com/static/sitemaps1.xml")

# TYPE CASTING URL TO LIST
urls = sitemap["loc"].to_list()

# CREATE SITEMAPS TXT FILE
sitemapstxt = open("sitemaps.txt", "w")

# WALK ON ALL URLS
for item in tqdm(urls):
    sitemapstxt.write(item+"\n")
