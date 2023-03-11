import requests


def get_player_by_id(player_id):
    url = f"https://statsapi.mlb.com/api/v1/people/{player_id}"
    response = requests.get(url)
    data = response.json()

    return data
