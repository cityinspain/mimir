
from get.chadwick import get_register_df
from util.chadwick import process_register_df

from get.mlbam import get_player_by_id
from util.mlbam import map_player

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

from queries import create_player_mutation

import progressbar

transport = AIOHTTPTransport(url="http://localhost:4001/graphql")
client = Client(transport=transport)


def download_registers():
    df = get_register_df()
    df = process_register_df(df)

    return df


df = download_registers()


with_mlb_ids = df.loc[df['mlb_id'].str.len() > 0]

progressbar_max = len(with_mlb_ids)
bar = progressbar.ProgressBar(max_value=progressbar_max)

for index, row in with_mlb_ids.iterrows():
    mlb_player = get_player_by_id(row['mlb_id'])

    try:
        player = map_player(mlb_player)
    except:
        continue

    new_row = {
        **row,
        **player
    }

    date = new_row.get("birth_date")
    if date:
        # convert datetime.date to ISO string
        new_row["birth_date"] = date.isoformat()

    params = {
        "mlbId": str(new_row.get("mlb_id")),
        "name": new_row.get("name", None),
        "firstName": new_row.get("first_name", None),
        "lastName": new_row.get("last_name", None),
        "useName": new_row.get("use_name", None),
        "birthDate": new_row.get("birth_date", None),
        "birthCity": new_row.get("birth_city", None),
        "birthStateProvince": new_row.get("birth_state_province", None),
        "birthCountry": new_row.get("birth_country", None),
        "height": new_row.get("height", None),
        "weight": new_row.get("weight", None),
        "retroId": new_row.get("retro_id", None),
        "bbrefId": new_row.get("bbref_id", None),
        "bbrefMinorsId": new_row.get("bbref_minors_id", None),
    }

    # remove None key/value pairs
    params = {k: v for k, v in params.items() if v is not None}
    params = {k: v for k, v in params.items() if v != ""}

    bar.update(index)

    try:
        result = client.execute(create_player_mutation, variable_values=params)

    except Exception as e:
        continue
