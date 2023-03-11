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

all_existing_ids_query = gql(
    """
query {
    allPlayers {
        mlbId
    }
}
""")

all_players_by_birth_date_query = gql("""
query AllPlayersByBirthDate($birthDate: Date) {
  allPlayersByBirthDate(birthDate: $birthDate) {
        mlbId
        name
        firstName
        lastName
        
    }
}
""")

update_player_with_fangraphs_info_mutation = gql("""
mutation UpdatePlayerByMlbId(
  $mlbId: String!
  $fangraphsId: String
  $fangraphsMinorMasterId: String
  $fangraphsOrgProspectRanking: Int
  $fangraphsOverallProspectRanking: Int
) {
  updatePlayerByMlbId(
    mlbId: $mlbId
    fangraphsId: $fangraphsId
    fangraphsMinorMasterId: $fangraphsMinorMasterId
    fangraphsOrgProspectRanking: $fangraphsOrgProspectRanking
    fangraphsOverallProspectRanking: $fangraphsOverallProspectRanking
  ) {
    mlbId
  }
}
""")
