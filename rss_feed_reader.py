import feedparser

def print_feed_items(url):
    # Parse the feed
    data = feedparser.parse(url)

    # Check if the parsing was successful
    if data.status != 200:
        print(f"Failed to retrieve feed from {url}")
        return
    
    # Loop through the entries and print them
    for entry in data.entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
        print("-----")

# Specify the RSS feed URL here
rss_url = 'https://example.com/rss'

# Call the function to print items
print_feed_items(rss_url)