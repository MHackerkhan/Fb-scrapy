from facebook_scraper import get_posts

# Prompt user for input
post_url = input("Enter the post URL: ")

# Extract the post ID from the URL
post_id = post_url.split('/')[-2]

# Fetch the post data
for post in get_posts(post_urls=[post_url]):
    print(f"Author: {post['username']}")
    print(f"Content: {post['text']}")
    print(f"Timestamp: {post['time']}")
    print('-' * 20)
