import feedparser 

# Use a pipeline as a high-level helper
from transformers import pipeline

ticker = 'META'
keyword = ''

pipe = pipeline("text-classification", model="ProsusAI/finbert")


rss_url = 'https://finance.yahoo.com/rss/headline?s={}'