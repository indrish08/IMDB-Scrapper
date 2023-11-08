try:
    import request
    from bs4 import BeautifulSoup
except Exception as e:
    print(f'There are some issues while importing this package {e}')

class Title:
    def getDetails():
        url = 'https://www.imdb.com/'
