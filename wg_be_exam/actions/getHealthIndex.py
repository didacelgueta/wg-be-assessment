import requests


class GetHealthIndex:
    @staticmethod
    def handle(url: str, base_year: int) -> int:
        res = requests.get(url)

        json_res = res.json()['facts']

        for value in range(len(json_res)-1, 0, -1):
            if str(base_year) in json_res[value]['Base year']:
                return round(json_res[value]['Health index'], 2)
