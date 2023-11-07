import requests
from bs4 import BeautifulSoup
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "IMDB Top Rated Movies"
sheet.append(['Movie Rank', 'Movie Name', 'Released Year', 'IMDB', 'URL'])

try:
    HEADERS = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get("https://www.imdb.com/chart/top/", headers=HEADERS)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, 'html.parser')
    movies = soup.find_all('div', class_="cli-children")

    with open('output.html', 'w', encoding='utf-8') as f:
        f.write(movies[0].prettify())

    for movie in movies:
        # print(movie.div.a.h3.text)
        name = movie.find('h3', class_="ipc-title__text").text
        info = movie.find_all('span', class_='cli-title-metadata-item')
        imdb = (movie.find('span', class_='ipc-rating-star').text)

        rank = name[:name.find('.')] # Rank
        name = name[name.find(" ")+1 : ] # Movie Name
        year = (info[0].text) # Year
        duration = (info[1].text) # Duration
        rating = 'Not Rated'
        if(len(info)>2):
            rating = (info[2].text) # Rating
        imdb = imdb.split("\xa0")[0] # IMDB rating out of 10
        url = f"https://www.imdb.com{movie.find('a')['href']}" # url for that movie

        # print(f"{rank} - {name} - {year} - {imdb} - {rating} -- URL : {url}")
        sheet.append([rank, name, year, imdb, url])
        # break

except Exception as e:
    print(e)

excel.save('IMDB Top 250 Movies.xlsx')