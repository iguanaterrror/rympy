import requests
from bs4 import BeautifulSoup

url = 'https://rateyourmusic.com/charts/top/album/all-time/deweight:live,archival,soundtrack/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

albums = soup.find_all('div', class_='page_charts_section_charts_item_title')
artists = soup.find_all('div', class_='page_charts_section_charts_item_artist')
ratings = soup.find_all('div', class_='page_charts_section_charts_item_details')



for album, artist, rating in zip(albums, artists, ratings):
    album_title = album.text.strip()
    artist_name = artist.text.strip()
    average_rating = rating.find('span', class_='page_charts_section_charts_item_details_average_num').text.strip()
    num_ratings = rating.find('span', class_='full').text.strip()

    print('Album:', album_title)
    print('Artist:', artist_name)
    print('Average Rating:', average_rating)
    print('Number of Ratings:', num_ratings)
    print('---')
