import requests
from bs4 import BeautifulSoup

# Function to fetch the HTML content of a webpage
def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

# Function to parse the HTML and extract post data
def parse_html(html):
    if not html:
        return []
    soup = BeautifulSoup(html, 'html.parser')
    posts = []
    try:
        for post in soup.find_all('div', class_='post-class'):  # Adjust the class name as per the actual webpage
            post_data = {}
            post_data['author'] = post.find('span', class_='author-class').text  # Adjust the class name as per the actual webpage
            post_data['content'] = post.find('div', class_='content-class').text  # Adjust the class name as per the actual webpage
            post_data['timestamp'] = post.find('span', class_='timestamp-class').text  # Adjust the class name as per the actual webpage
            posts.append(post_data)
    except AttributeError as e:
        print(f"Error parsing HTML: {e}")
    return posts

# Prompt user for input
url = input("Enter the post URL: ")

# Fetch and parse the HTML content
html_content = fetch_html(url)
posts = parse_html(html_content)

# Print the scraped post data
for post in posts:
    print(f"Author: {post['author']}")
    print(f"Content: {post['content']}")
    print(f"Timestamp: {post['timestamp']}")
    print('-' * 20)
