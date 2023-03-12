# using MLB API, get all current teams and their rosters.
# then, update the db record for each player with their team.

import requests

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

transport = AIOHTTPTransport(url="http://localhost:4001/graphql")
client = Client(transport=transport)

# get all teams


def map_team_player(team_id, player):
    return {
        "id": player.get("person").get("id"),
        "parent_id": player.get("parentTeamId"),
        "team_id": team_id
    }


def map_team(team):
    return {
        "id": team.get("id"),
        "parent_id": team.get("parentOrgId"),
        "name": team.get("name"),
    }


def get_teams():
    url = "https://statsapi.mlb.com/api/v1/teams?sportIds=1,11,12,13,14"
    response = requests.get(url)
    data = response.json()

    return list(map(map_team, data.get("teams")))


def get_team_roster(team_id):
    url = f"https://statsapi.mlb.com/api/v1/teams/{team_id}/roster?rosterType=40Man"

    response = requests.get(url)
    data = response.json()

    # data = list(map(map_team_player, data.get("roster")))
    data = list(map(lambda x: map_team_player(team_id, x), data.get("roster")))

    return data


mutation = gql(
    """
    mutation UpdatePlayerTeamDataByMlbId(
  $mlbId: String
  $currentTeamId: String
  $parentOrgId: String
) {

  updatePlayerByMlbId(
    mlbId: $mlbId
    currentTeamId: $currentTeamId
    parentOrgId: $parentOrgId
  ) {
    mlbId
  }

}
""")


teams = get_teams()
# print(teams)

for team in teams:
    print(f"process team: {team.get('name')}")
    roster = get_team_roster(team.get("id"))

    for player in roster:

        try:
            res = client.execute(mutation, variable_values={
                "mlbId": str(player.get("id")),
                "currentTeamId": str(player.get("team_id")),
                "parentOrgId": str(player.get("parent_id")),
            })
        except Exception as e:
            print(e)
            print(player)
