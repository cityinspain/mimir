from gql import gql

create_player_mutation = gql(
    """
mutation Mutation(
  $name: String
  $mlbId: String
  $birthDate: Date
  $firstName: String
  $lastName: String
  $fullName: String
  $birthCity: String
  $birthCountry: String
  $primaryPosition: String
  $birthStateProvince: String
  $height: Int
  $weight: Int
  $useName: String
  $retroId: String
  $fangraphsId: String
  $fangraphsMinorMasterId: String
  $bbrefId: String
  $bbrefMinorsId: String
) {
  createPlayer(
    name: $name
    mlbId: $mlbId
    birthDate: $birthDate
    firstName: $firstName
    lastName: $lastName
    fullName: $fullName
    birthCity: $birthCity
    birthCountry: $birthCountry
    primaryPosition: $primaryPosition
    birthStateProvince: $birthStateProvince
    height: $height
    weight: $weight
    useName: $useName
    retroId: $retroId
    fangraphsId: $fangraphsId
    fangraphsMinorMasterId: $fangraphsMinorMasterId
    bbrefId: $bbrefId
    bbrefMinorsId: $bbrefMinorsId
  ) {
    mlbId
  }
}

"""
)


def get_create_player_mutation(player):
    params = {
        "mlb_id": player.get("mlb_id"),
        "birth_city": player.get("birth_city"),
        "birth_state_province": player.get("birth_state_province"),
        "birth_country": player.get("birth_country"),
        "birth_date": player.get("birth_date"),
        "mlbId": player.get("mlb_id"),
        "name": player.get("name"),
        "firstName": player.get("first_name"),
        "lastName": player.get("last_name"),
        "birthDate": player.get("birth_date"),
        "birthCity": player.get("birth_city"),
        "birthStateProvince": player.get("birth_state_province"),
        "birthCountry": player.get("birth_country"),
        "height": player.get("height"),
        "weight": player.get("weight"),
    }
