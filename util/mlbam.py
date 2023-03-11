def map_player(player):
    player = player['people'][0]

    mlb_id = player['id']

    height = player.get('height', None)
    if height:
        # convert height from "feet' inches" to inches
        height = int(player.get("height", "").split(
            "'")[0]) * 12 + int(player.get("height", "").split("'")[1].split('"')[0])
    weight = player.get('weight', None)

    bat_side = player.get('batSide', {}).get('code', None)
    pitch_hand = player.get('pitchHand', {}).get('code', None)

    first_name = player.get('firstName', None)
    last_name = player.get('lastName', None)
    full_name = player.get('fullName', None)
    use_name = player.get('useName', None)

    mlb_debut_date = player.get('mlbDebutDate', None)

    mlb_debut_year = None
    mlb_debut_month = None
    mlb_debut_day = None

    if mlb_debut_date:
        mlb_debut_year = mlb_debut_date.split('-')[0]
        mlb_debut_month = mlb_debut_date.split('-')[1]
        mlb_debut_day = mlb_debut_date.split('-')[2]

    birth_date = player.get('birthDate', None)

    birth_year = None
    birth_month = None
    birth_day = None

    if birth_date:
        birth_year = birth_date.split('-')[0]
        birth_month = birth_date.split('-')[1]
        birth_day = birth_date.split('-')[2]

    birth_city = player.get('birthCity', None)
    birth_state = player.get('birthStateProvince', None)
    birth_country = player.get('birthCountry', None)

    primary_position = player.get(
        'primaryPosition', {}).get("abbreviation", None)

    return {
        'mlb_id': mlb_id,
        'name': full_name,
        'first_name': first_name,
        'last_name': last_name,
        'use_name': use_name,
        'primary_position': primary_position,
        'height': height,
        'weight': weight,
        'bat_side': bat_side,
        'pitch_hand': pitch_hand,
        'mlb_debut_year': mlb_debut_year,
        'mlb_debut_month': mlb_debut_month,
        'mlb_debut_day': mlb_debut_day,
        'birth_year': birth_year,
        'birth_month': birth_month,
        'birth_day': birth_day,
        'birth_city': birth_city,
        'birth_state_province': birth_state,
        'birth_country': birth_country,
    }
