import requests

url = "https://cdn.fangraphs.com/api/prospects/board/prospects-list?statType=player&draft=2022updated&valueHeader=prospect-2022"


def get_prospect_data():
    response = requests.get(url)
    data = response.json()

    return data
