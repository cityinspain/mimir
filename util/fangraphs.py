from datetime import datetime, timedelta


def map_fangraphs_api_player(player):
    base_date = "1899-12-30"
    base_date = datetime.strptime(base_date, "%Y-%m-%d")

    minorMasterId = player.get("minorMasterId", None)
    playerName = player["playerName"]
    playerId = player.get("ID", None)
    ovrRank = player.get("Ovr_Rank", None)
    orgRank = player.get("Org_Rank", None)

    firstName = player.get("FirstName", None)
    lastName = player.get("LastName", None)

    birth_date_delta = int(player["BirthDate"])
    birth_date = base_date + timedelta(days=birth_date_delta)
    birth_date = birth_date.strftime("%Y-%m-%d")

    return {
        "minorMasterId": minorMasterId,
        "playerName": playerName,
        "firstName": firstName,
        "lastName": lastName,
        "playerId": playerId,
        "ovrRank": ovrRank,
        "orgRank": orgRank,
        "birthDate": birth_date,
    }
