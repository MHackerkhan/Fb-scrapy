from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Function to fetch the HTML content of a webpage using Selenium
def fetch_html_selenium(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    # Scroll to the bottom of the page to load more comments
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # Wait for the page to load more comments

    html = driver.page_source
    driver.quit()
    return html

# Function to parse the HTML and extract post data
def parse_html(html):
    if not html:
        return []
    
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    posts = []

    try:
        post = soup.find('div', class_='userContentWrapper')  # Adjust the class name as per the actual webpage
        if post:
            post_data = {}
            post_data['author'] = post.find('span', class_='fwb').text if post.find('span', class_='fwb') else 'N/A'
            post_data['content'] = post.find('div', class_='userContent').text if post.find('div', class_='userContent') else 'N/A'
            post_data['timestamp'] = post.find('abbr').text if post.find('abbr') else 'N/A'
            posts.append(post_data)
    except AttributeError as e:
        print(f"Error parsing HTML: {e}")
    
    return posts

# Prompt user for input
url = input("Enter the post URL: ")

# Fetch and parse the HTML content
html_content = fetch_html_selenium(url)
if html_content:
    print("HTML content fetched successfully.")
else:
    print("Failed to fetch HTML content.")
posts = parse_html(html_content)

# Print the scraped post data
if posts:
    for post in posts:
        print(f"Author: {post['author']}")
        print(f"Content: {post['content']}")
        print(f"Timestamp: {post['timestamp']}")
        print('-' * 20)
else:
    print("No posts found or failed to parse HTML.")
