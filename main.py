import requests
from bs4 import BeautifulSoup
import csv

# Set the URL to scrape
url = 'https://www.booking.com/searchresults.en-gb.html?ss=Hurghada&ssne=Hurghada&ssne_untouched=Hurghada&efdco=1&label=gen173nr-1FCAQoggJCD3NlYXJjaF9odXJnaGFkYUgJWARoQ4gBAZgBCbgBF8gBD9gBAegBAfgBA4gCAagCA7gCsJy0nwbAAgHSAiQ3MzQwMGVhZC1hM2M3LTQ4M2UtOGE4YS03ZTM1ZWFhZjgyYzbYAgXgAgE&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-290029&dest_type=city&checkin=2023-02-17&checkout=2023-02-18&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'

# Send a request to the URL and get the page content
response = requests.get(url, headers={'user-agent': 'some agent'})
content = response.content

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(content, features="lxml")

# Find the hotel elements
hotels = soup.find_all('div', {'data-testid':"property-card"})[:10]

# Create a CSV file to save the hotel data
csv_file = open('booking.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(csv_file)

# Write the header row to the CSV file
writer.writerow(['Hotel Name', 'Rating Score', 'Rating Value', 'Number of Reviews'])

# Loop through the first 10 hotels and extract the data
for hotel in hotels[:10]:
    # Extract the hotel name
    name = hotel.find('div', {'data-testid':"title"}).text.strip ( )

    # Extract the review score
    score_elem = hotel.find('div', {'class': 'b5cd09854e d10a6220b4'})
    try:
        score = score_elem.text.strip()
    except AttributeError:
        score = ''

    # Extract the rating value
    rating_elem = hotel.find('div', {'class': 'b5cd09854e f0d4d6a2f5 e46e88563a'})
    try:
        rating_value = rating_elem.text.strip()
    except AttributeError:
        rating_value = ''

    # Extract the # of reviews
    review_elem = hotel.find('div', {'class': 'd8eab2cf7f c90c0a70d3 db63693c62'})
    try:
        review_count = review_elem.text.strip()
    except AttributeError:
        review_count = ''

    # Write the hotel data to the CSV file
    writer.writerow([name, score, rating_value, review_count])

# Close the CSV file
csv_file.close()


