import instaloader
import csv

# Initialize Instaloader
L = instaloader.Instaloader()

# Replace 'profile_username' with the Instagram profile you want to scrape
profile_username = 'sparklenigeria'

# Load the profile
profile = instaloader.Profile.from_username(L.context, profile_username)

# Create a list to store the post URLs
post_urls = []

# Iterate through the profile's posts and extract URLs
for post in profile.get_posts():
    post_urls.append(f"https://www.instagram.com/p/{post.shortcode}/")

# Define the CSV filename
csv_filename = 'instagram_posts.csv'

# Write the URLs to a CSV file
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Post URLs'])
    csv_writer.writerows([[url] for url in post_urls])

print(f'{len(post_urls)} post URLs scraped and saved to {csv_filename}')
