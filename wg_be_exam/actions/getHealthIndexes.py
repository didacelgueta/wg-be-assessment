import requests
from bs4 import BeautifulSoup


class GetHealthIndexes:
    @staticmethod
    def handle(url: str) -> list:
        res = requests.get(url)

        soup = BeautifulSoup(res.text, 'html.parser')

        indexes = []
        for td in soup.find_all('td'):
            indexes.append(td.string)

        return indexes
